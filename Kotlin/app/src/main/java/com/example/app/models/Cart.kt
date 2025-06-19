package com.example.app.models

import androidx.compose.runtime.mutableStateListOf
import androidx.compose.runtime.MutableState
import androidx.compose.runtime.mutableStateOf
import kotlinx.serialization.Serializable

@Serializable
data class Cart(val productID: String, val amount: MutableState<Int> = mutableStateOf(1))

val cartItems = mutableStateListOf<Cart>()