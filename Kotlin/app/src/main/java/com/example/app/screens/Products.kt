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
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.example.app.models.Cart
import com.example.app.models.Product
import com.example.app.models.cartItems
import com.example.app.models.products

@Composable
fun ProductsScreen() {
    productList(products)
}

@Composable
fun productList(products: List<Product>) {
    Row {
        Column {
            products.forEach { product -> productRow(product) }
        }
    }
}

@Composable
fun productRow(product: Product) {
    Card(
        modifier = Modifier
            .fillMaxWidth()
            .padding(8.dp)
    ) {
        Column(modifier = Modifier.padding(8.dp), verticalArrangement = Arrangement.Center) {
            Text(product.name)
            Text(product.category.name)
            Text("$" + product.price.toString())

            AddToCartButton(product)
        }
    }
}

@Composable
fun AddToCartButton(product: Product) {
    val existItem = cartItems.find { it.productID == product.id }

    if (existItem != null) {
        Text("In cart: " + existItem.amount.value)
    }

    Button(
        onClick = {
            if (existItem != null) {
                existItem.amount.value++
            } else {
                cartItems.add(Cart(product.id))
            }
        }) { Text("Add to cart") }

    if (existItem != null) {
        Button(
            onClick = {
                if (existItem.amount.value <= 1) {
                    cartItems.remove(existItem)
                } else {
                    existItem.amount.value--
                }
            }) { Text("Remove from cart") }
    }
}

@Preview(showBackground = true)
@Composable
fun ProductsScreenPreview() {
    ProductsScreen()
}
