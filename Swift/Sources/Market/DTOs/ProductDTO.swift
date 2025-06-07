import Fluent
import Vapor

struct ProductDTO: Content {
    var id: UUID?
    var title: String
    var price: Double
    var quantity: Int
    var categoryID: UUID

    func toModel() -> Product {
        let model = Product()

        model.id = self.id

        model.title = self.title
        model.quantity = self.quantity
        model.price = self.price
        model.$category.id = self.categoryID

        return model
    }
}
