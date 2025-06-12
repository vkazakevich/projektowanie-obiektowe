import Fluent

struct PostSeed: AsyncMigration {
    func prepare(on database: any Database) async throws {
        let content =
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer imperdiet at tortor nec ultricies. Ut a lectus quis nibh dapibus semper. Praesent sagittis in neque in vulputate. In malesuada arcu vitae molestie gravida. Sed vestibulum sem tortor, eu consectetur sapien condimentum nec. Donec imperdiet, metus at sollicitudin vulputate, ligula mauris suscipit nibh, ut dictum nisi felis sodales urna. Vestibulum elementum, elit eget auctor faucibus, risus tellus porta tortor, quis consequat justo tellus in metus. Pellentesque sagittis, dolor in bibendum egestas, nisl arcu pretium mauris, sed fringilla eros odio ac ex. Aliquam commodo bibendum tortor, tristique suscipit sapien finibus quis. Nam blandit semper lacinia."

        let posts = [
            Post(title: "Hello world!", content: content, author: "Admin"),
            Post(title: "Hello again!", content: "Just some blog post", author: "Admin"),
        ]

        try await posts.create(on: database)
    }

    func revert(on database: any Database) async throws {
        try await Post.query(on: database).delete()
    }
}
