
import Fluent
import Vapor

import struct Foundation.UUID

final class Post: Model, @unchecked Sendable {
    static let schema = "posts"

    @ID(key: .id)
    var id: UUID?

    @Field(key: "title")
    var title: String

    @Field(key: "content")
    var content: String

    @Field(key: "author")
    var author: String

    @Timestamp(key: "created_at", on: .create)
    var createdAt: Date?

    @Timestamp(key: "updated_at", on: .update)
    var updatedAt: Date?

    init() {}

    init(id: UUID? = nil, title: String, content: String, author: String) {
        self.id = id
        self.title = title
        self.content = content
        self.author = author
    }

    func toDTO() -> PostDTO {
        .init(
            id: self.id,
            title: self.title,
            content: self.content,
            author: self.author,
        )
    }
}
