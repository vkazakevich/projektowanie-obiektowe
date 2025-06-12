import Fluent
import Vapor

struct PostDTO: Content {
    var id: UUID?
    var title: String
    var content: String
    var author: String

    func toModel() -> Post {
        let model = Post()

        model.id = self.id
        model.title = self.title
        model.content = self.content
        model.author = self.author

        return model
    }
}
