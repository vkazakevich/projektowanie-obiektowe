package com.example.app.providers

import com.example.app.models.Cart
import com.example.app.models.Category
import com.example.app.models.Product
import io.realm.kotlin.Realm
import io.realm.kotlin.RealmConfiguration

object RealmProvider {
    private val config: RealmConfiguration by lazy {
        RealmConfiguration
            .Builder(schema = setOf(
                Product::class,
                Category::class,
                Cart::class
            ))
            .deleteRealmIfMigrationNeeded()
            .build()
    }

    val realm: Realm by lazy {
        Realm.Companion.open(config)
    }
}