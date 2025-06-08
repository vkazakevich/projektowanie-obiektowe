import Fluent
import Leaf
import Vapor

struct CategoryController: RouteCollection {
    static let cacheKey = "categories"

    func boot(routes: any RoutesBuilder) throws {
        let categories = routes.grouped("categories")

        categories.get(use: self.index)
        categories.post(use: self.store)

        categories.get("create", use: self.create)

        categories.group(":categoryID") { category in
            category.get(use: self.show)

            category.get("edit", use: self.edit)
            category.post("delete", use: self.delete)
            category.post("put", use: self.update)
        }
    }

    @Sendable
    func index(req: Request) async throws -> View {
        if let categories = try await req.redis.get(
            .init(CategoryController.cacheKey), asJSON: [Category].self)
        {
            return try await req.view.render("categories/index", ["categories": categories])
        }

        let categories = try await Category.query(on: req.db).all()

        try await req.redis.set(.init(CategoryController.cacheKey), toJSON: categories)
        _ = req.redis.expire(.init(CategoryController.cacheKey), after: .seconds(30))

        return try await req.view.render("categories/index", ["categories": categories])
    }

    @Sendable
    func show(req: Request) throws -> EventLoopFuture<View> {
        Category.find(req.parameters.get("categoryID"), on: req.db)
            .unwrap(or: Abort(.notFound))
            .flatMap { category in
                return req.view.render("categories/show", ["category": category])
            }
    }

    @Sendable
    func create(req: Request) throws -> EventLoopFuture<View> {
        return req.view.render("categories/create")
    }

    @Sendable
    func store(req: Request) async throws -> Response {
        let category = try req.content.decode(CategoryDTO.self).toModel()
        try await category.save(on: req.db)

        _ = req.redis.delete(.init(CategoryController.cacheKey))

        return req.redirect(to: "/categories")
    }

    @Sendable
    func edit(req: Request) throws -> EventLoopFuture<View> {
        Category.find(req.parameters.get("categoryID"), on: req.db)
            .unwrap(or: Abort(.notFound))
            .flatMap { category in
                return req.view.render("categories/edit", ["category": category])
            }
    }

    @Sendable
    func update(req: Request) async throws -> Response {
        guard let category = try await Category.find(req.parameters.get("categoryID"), on: req.db)
        else {
            throw Abort(.notFound)
        }

        let CategoryDTO = try req.content.decode(CategoryDTO.self)

        category.name = CategoryDTO.name

        try await category.update(on: req.db)

        _ = req.redis.delete(.init(CategoryController.cacheKey))

        return req.redirect(to: "/categories")
    }

    @Sendable
    func delete(req: Request) async throws -> Response {
        guard let category = try await Category.find(req.parameters.get("categoryID"), on: req.db)
        else {
            throw Abort(.notFound)
        }

        try await category.delete(on: req.db)
        
        _ = req.redis.delete(.init(CategoryController.cacheKey))

        return req.redirect(to: "/categories")
    }
}
