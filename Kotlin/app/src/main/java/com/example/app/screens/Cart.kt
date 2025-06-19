package com.example.app.screens

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.example.app.models.Category
import com.example.app.models.cartItems
import com.example.app.models.categories
import com.example.app.models.products

@Composable
fun CartScreen() {
    Row {
        Column {
            if (cartItems.count() == 0) {
                Text("Cart is empty")
            }

            cartItems.forEach { item ->
                Card(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(8.dp)
                ) {
                    Column(modifier = Modifier.padding(8.dp)) {
                        val product = products.find { it.id == item.productID }

                        if (product != null) {
                            Text("Product: " + product.name)
                            Text("Quantity: " + item.amount.value)
                            Text("Price: $" + (product.price * item.amount.value))

                            Button(
                                onClick = {
                                    if (item.amount.value <= 1) {
                                        cartItems.remove(item)
                                    } else {
                                        item.amount.value--
                                    }
                                }) { Text("Remove from cart") }
                        }
                    }
                }
            }
        }
    }
}

@Preview(showBackground = true)
@Composable
fun CartScreenPreview() {
    CartScreen()
}