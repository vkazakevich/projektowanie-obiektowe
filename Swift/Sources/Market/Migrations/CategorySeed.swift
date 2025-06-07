import Fluent

struct CategorySeed: AsyncMigration {
    func prepare(on database: any Database) async throws {
        let categories = [
            Category(name: "Apple"),
            Category(name: "Asus"),
            Category(name: "Acer"),
        ]

        try await categories.create(on: database)
    }

    func revert(on database: any Database) async throws {
        try await Category.query(on: database).delete()
    }
}
