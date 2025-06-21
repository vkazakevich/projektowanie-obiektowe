package com.example.app.utils

import com.example.app.models.Category
import com.example.app.models.Product
import com.example.app.providers.RealmProvider

object Seeds {
    fun fill() {
        val realm = RealmProvider.realm

        realm.writeBlocking {
            deleteAll()
        }

        realm.writeBlocking {
            val seedsData = mapOf(
                "Mobile phones" to listOf("iPhone", "Samsung", "Xiaomi"),
                "Game consoles" to listOf("PlayStation 5", "Xbox", "Nintendo Switch"),
                "Laptops" to listOf("Macbook", "HP", "Lenovo", "Acer")
            )

            seedsData.forEach { (categoryName, productNames) ->
                val category = copyToRealm(Category().apply {
                    name = categoryName
                })

                productNames.forEach { productName ->
                    val product = Product().apply {
                        name = productName
                        price = (100..500).random().toDouble()
                        this.category = category
                    }

                    copyToRealm(product)
                }
            }
        }
    }
}