package com.example.app.models

import kotlinx.serialization.Serializable
import java.util.UUID

@Serializable
data class Product(val id: String = UUID.randomUUID().toString(), val name: String, val category: Category, val price: Int)

val products = mutableListOf<Product>()