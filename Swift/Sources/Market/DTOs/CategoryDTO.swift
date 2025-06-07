import Fluent
import Vapor

struct CategoryDTO: Content {
    var id: UUID?
    var name: String

    func toModel() -> Category {
        let model: Category = Category()

        model.id = self.id
        model.name = self.name

        return model
    }
}
