import Fluent
import Leaf
import Vapor

struct ProductController: RouteCollection {
    func boot(routes: any RoutesBuilder) throws {
        let products = routes.grouped("products")

        products.get(use: self.index)
        products.post(use: self.store)

        products.get("create", use: self.create)

        products.group(":productID") { product in
            product.get(use: self.show)

            product.get("edit", use: self.edit)
            product.post("delete", use: self.delete)
            product.post("put", use: self.update)
        }
    }

    @Sendable
    func index(req: Request) throws -> EventLoopFuture<View> {
        Product.query(on: req.db).all().flatMap { products in
            return req.view.render("products/index", ["products": products])
        }
    }

    @Sendable
    func show(req: Request) throws -> EventLoopFuture<View> {
        Product.find(req.parameters.get("productID"), on: req.db)
            .unwrap(or: Abort(.notFound))
            .flatMap { product in
                return req.view.render("products/show", ["product": product])
            }
    }

    @Sendable
    func create(req: Request) throws -> EventLoopFuture<View> {
        return req.view.render("products/create")
    }

    @Sendable
    func store(req: Request) async throws -> Response {
        let product = try req.content.decode(ProductDTO.self).toModel()
        try await product.save(on: req.db)

        return req.redirect(to: "/products")
    }

    @Sendable
    func edit(req: Request) throws -> EventLoopFuture<View> {
        Product.find(req.parameters.get("productID"), on: req.db)
            .unwrap(or: Abort(.notFound))
            .flatMap { product in
                return req.view.render("products/edit", ["product": product])
            }
    }

    @Sendable
    func update(req: Request) async throws -> Response {
        guard let product = try await Product.find(req.parameters.get("productID"), on: req.db)
        else {
            throw Abort(.notFound)
        }

        let productDto = try req.content.decode(ProductDTO.self)

        product.title = productDto.title
        product.price = productDto.price
        product.quantity = productDto.quantity

        try await product.update(on: req.db)

        return req.redirect(to: "/products")
    }

    @Sendable
    func delete(req: Request) async throws -> Response {
        guard let product = try await Product.find(req.parameters.get("productID"), on: req.db)
        else {
            throw Abort(.notFound)
        }

        try await product.delete(on: req.db)

        return req.redirect(to: "/products")
    }
}
