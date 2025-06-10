import Fluent
import Leaf
import Vapor

struct PostController: RouteCollection {
    static let cacheKey = "posts"

    func boot(routes: any RoutesBuilder) throws {
        let posts = routes.grouped("posts")

        posts.get(use: self.index)
        posts.post(use: self.store)

        posts.get("create", use: self.create)

        posts.group(":postID") { post in
            post.get(use: self.show)

            post.get("edit", use: self.edit)
            post.post("delete", use: self.delete)
            post.post("put", use: self.update)
        }
    }

    @Sendable
    func index(req: Request) async throws -> View {
        if let posts: [Post] = try await req.redis.get(
            .init(PostController.cacheKey), asJSON: [Post].self)
        {
            return try await req.view.render("posts/index", ["posts": posts])
        }

        let posts = try await Post.query(on: req.db).all()

        try await req.redis.set(.init(PostController.cacheKey), toJSON: posts)
        _ = req.redis.expire(.init(PostController.cacheKey), after: .seconds(30))

        return try await req.view.render("posts/index", ["posts": posts])
    }

    @Sendable
    func show(req: Request) throws -> EventLoopFuture<View> {
        Post.find(req.parameters.get("postID"), on: req.db)
            .unwrap(or: Abort(.notFound))
            .flatMap { post in
                return req.view.render("posts/show", ["post": post])
            }
    }

    @Sendable
    func create(req: Request) throws -> EventLoopFuture<View> {
        return req.view.render("posts/create")
    }

    @Sendable
    func store(req: Request) async throws -> Response {
        let post = try req.content.decode(PostDTO.self).toModel()
        try await post.save(on: req.db)

        _ = req.redis.delete(.init(PostController.cacheKey))

        return req.redirect(to: "/posts")
    }

    @Sendable
    func edit(req: Request) throws -> EventLoopFuture<View> {
        Post.find(req.parameters.get("postID"), on: req.db)
            .unwrap(or: Abort(.notFound))
            .flatMap { post in
                return req.view.render("posts/edit", ["post": post])
            }
    }

    @Sendable
    func update(req: Request) async throws -> Response {
        guard let post = try await Post.find(req.parameters.get("postID"), on: req.db)
        else {
            throw Abort(.notFound)
        }

        let PostDTO = try req.content.decode(PostDTO.self)

        post.title = PostDTO.title
        post.content = PostDTO.content
        post.author = PostDTO.author

        try await post.update(on: req.db)

        _ = req.redis.delete(.init(PostController.cacheKey))

        return req.redirect(to: "/posts")
    }

    @Sendable
    func delete(req: Request) async throws -> Response {
        guard let post = try await Post.find(req.parameters.get("postID"), on: req.db)
        else {
            throw Abort(.notFound)
        }

        try await post.delete(on: req.db)

        _ = req.redis.delete(.init(PostController.cacheKey))

        return req.redirect(to: "/posts")
    }
}
