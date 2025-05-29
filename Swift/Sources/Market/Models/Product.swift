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

    init() { }

    init(id: UUID? = nil, title: String, price: Double, quantity: Int) {
        self.id = id
        self.title = title
        self.price = price
        self.quantity = quantity
    }
    
    func toDTO() -> ProductDTO {
        .init(
            id: self.id,
            title: self.$title.value,
            price: self.$price.value,
            quantity: self.$quantity.value
        )
    }
}
