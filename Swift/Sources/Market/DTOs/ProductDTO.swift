import Fluent
import Vapor

struct ProductDTO: Content {
    var id: UUID?
    var title: String?
    var price: Double?
    var quantity: Int?
    
    func toModel() -> Product {
        let model = Product()
        
        model.id = self.id

        if let title = self.title {
            model.title = title
        }
        if let quantity = self.quantity {
            model.quantity = quantity
        }

        if let price = self.price {
            model.price = price
        }

        return model
    }
}
