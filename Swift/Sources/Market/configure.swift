import Fluent
import FluentSQLiteDriver
import Leaf
import NIOSSL
import Redis
import Vapor

// configures your application
public func configure(_ app: Application) async throws {
    // uncomment to serve files from /Public folder
    // app.middleware.use(FileMiddleware(publicDirectory: app.directory.publicDirectory))

    if let redisURL = Environment.get("REDIS_URL") {
        var config = TLSConfiguration.makeClientConfiguration()
        config.certificateVerification = .none

        app.redis.configuration = try RedisConfiguration(url: redisURL, tlsConfiguration: config)
    } else {
        app.redis.configuration = try RedisConfiguration(hostname: "localhost")
    }

    app.databases.use(DatabaseConfigurationFactory.sqlite(.file("db.sqlite")), as: .sqlite)

    app.migrations.add(CreateCategory())
    app.migrations.add(CategorySeed())

    app.migrations.add(CreateProduct())
    app.migrations.add(ProductSeed())

    app.migrations.add(CreatePost())
    app.migrations.add(PostSeed())

    app.views.use(.leaf)

    try await app.autoMigrate()

    try routes(app)
}
