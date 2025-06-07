import Fluent
import FluentSQLiteDriver
import Leaf
import NIOSSL
import Vapor
import Redis

// configures your application
public func configure(_ app: Application) async throws {
    // uncomment to serve files from /Public folder
    // app.middleware.use(FileMiddleware(publicDirectory: app.directory.publicDirectory))

    app.redis.configuration = try RedisConfiguration(hostname: "localhost")

    app.databases.use(DatabaseConfigurationFactory.sqlite(.file("db.sqlite")), as: .sqlite)

    app.migrations.add(CreateCategory())
    app.migrations.add(CategorySeed())

    app.migrations.add(CreateProduct())

    app.views.use(.leaf)

    // register routes
    try routes(app)
}
