package com.example.app.models

import io.realm.kotlin.types.RealmObject
import io.realm.kotlin.types.annotations.PrimaryKey
import org.mongodb.kbson.ObjectId

class Product : RealmObject {
    @PrimaryKey
    var _id: ObjectId = ObjectId()
    var name: String = ""
    var price: Double = 0.0
    var category: Category? = null
}
