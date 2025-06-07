import Fluent

import struct Foundation.UUID

/// Property wrappers interact poorly with `Sendable` checking, causing a warning for the `@ID` property
/// It is recommended you write your model with sendability checking on and then suppress the warning
/// afterwards with `@unchecked Sendable`.
final class Product: Model, @unchecked Sendable {
    static let schema = "products"

    @ID(key: .id)
    var id: UUID?

    @Field(key: "title")
    var title: String

    @Field(key: "price")
    var price: Double

    @Field(key: "quantity")
    var quantity: Int

    @Parent(key: "category_id")
    var category: Category

    init() {}

    init(id: UUID? = nil, title: String, price: Double, quantity: Int, categoryID: UUID) {
        self.id = id
        self.title = title
        self.price = price
        self.quantity = quantity
        $category.id = categoryID
    }

    func toDTO() -> ProductDTO {
        .init(
            id: self.id,
            title: self.title,
            price: self.price,
            quantity: self.quantity,
            categoryID: self.$category.id
        )
    }
}
