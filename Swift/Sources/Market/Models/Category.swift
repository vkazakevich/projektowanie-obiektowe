import Fluent

import struct Foundation.UUID

final class Category: Model, @unchecked Sendable {
    static let schema = "categories"

    @ID(key: .id)
    var id: UUID?

    @Field(key: "name")
    var name: String

    init() {}

    init(id: UUID? = nil, name: String) {
        self.id = id
        self.name = name
    }

    func toDTO() -> CategoryDTO {
        .init(
            id: self.id,
            name: self.name
        )
    }
}
