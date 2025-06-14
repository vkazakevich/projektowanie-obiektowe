package com.example.app.models

import kotlinx.serialization.Serializable

@Serializable
data class Category(val name: String)

val categories = mutableListOf<Category>()