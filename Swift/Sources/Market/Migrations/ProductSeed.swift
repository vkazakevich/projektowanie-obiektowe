import Fluent

struct ProductSeed: AsyncMigration {
    func prepare(on database: any Database) async throws {
        guard
            let category = try await Category.query(on: database)
                .filter(\.$name == "Apple")
                .first(),
            let categoryID = category.id
        else {
            return
        }

        let products = [
            Product(title: "Macbook Air M1", price: 299, quantity: 10, categoryID: categoryID),
            Product(title: "Macbook Air M3", price: 399, quantity: 10, categoryID: categoryID),
            Product(title: "iPhone 15 PRO", price: 199, quantity: 10, categoryID: categoryID),
        ]

        try await products.create(on: database)
    }

    func revert(on database: any Database) async throws {
        try await Product.query(on: database).delete()
    }
}
