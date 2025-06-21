package com.example.app.models

import io.realm.kotlin.types.RealmObject
import io.realm.kotlin.types.annotations.PrimaryKey
import org.mongodb.kbson.ObjectId

class Cart : RealmObject {
    @PrimaryKey
    var _id: ObjectId = ObjectId()
    var product: Product? = null
    var amount: Int = 0
}