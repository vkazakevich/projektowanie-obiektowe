import Fluent
import Leaf
import Vapor

struct ProductController: RouteCollection {
    static let cacheKey = "products"

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
    func index(req: Request) async throws -> View {
        if let products = try await req.redis.get(.init(ProductController.cacheKey), asJSON: [Product].self) {
            return try await req.view.render("products/index", ["products": products])
        }

        let products = try await Product.query(on: req.db).with(\.$category).all()

        try await req.redis.set(.init(ProductController.cacheKey), toJSON: products)
        _ = req.redis.expire(.init(ProductController.cacheKey), after: .seconds(30))

        return try await req.view.render("products/index", ["products": products])
    }

    @Sendable
    func show(req: Request) async throws -> View {
        guard let product = try await Product.find(req.parameters.get("productID"), on: req.db)
        else {
            throw Abort(.notFound)
        }

        _ = try await product.$category.get(on: req.db)

        return try await req.view.render("products/show", ["product": product])
    }

    @Sendable
    func create(req: Request) async throws -> View {
        let categories = try await Category.query(on: req.db).all()
        return try await req.view.render("products/create", ["categories": categories])
    }

    @Sendable
    func store(req: Request) async throws -> Response {
        let product = try req.content.decode(ProductDTO.self).toModel()
        try await product.save(on: req.db)

        return req.redirect(to: "/products")
    }

    @Sendable
    func edit(req: Request) async throws -> View {
        guard let product = try await Product.find(req.parameters.get("productID"), on: req.db)
        else {
            throw Abort(.notFound)
        }

        let categories = try await Category.query(on: req.db).all()

        struct EditProductContext: Encodable {
            var product: Product
            var categories: [Category]
        }

        return try await req.view.render(
            "products/edit", EditProductContext(product: product, categories: categories))
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
        product.$category.id = productDto.categoryID

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
