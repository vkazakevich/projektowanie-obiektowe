package com.example.app.models

import kotlinx.serialization.Serializable

@Serializable
data class Product(val name: String, val category: Category, val price: Int)

val products = mutableListOf<Product>()