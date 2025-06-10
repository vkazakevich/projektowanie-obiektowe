import Fluent
import Vapor

func routes(_ app: Application) throws {
    app.get { req throws in
        return req.redirect(to: "/products")
    }

    try app.register(collection: ProductController())
    try app.register(collection: CategoryController())
    try app.register(collection: PostController())
}
