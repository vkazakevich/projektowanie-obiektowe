package com.example.app.screens

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Card
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.example.app.models.Category
import com.example.app.models.Product

@Composable
fun ProductsScreen() {
    val categories = listOf(
        Category("Apple"),
        Category("Asus"),
        Category("Lenovo"),
    )

    val products = listOf(
        Product(name = "Macbook Air M1", category = categories[0], price = 199),
        Product(name = "Macbook Air M2", category = categories[0], price = 299),
        Product(name = "Macbook Air M3", category = categories[0], price = 399),
    )

    productList(products)
}

@Composable
fun productList(products: List<Product>) {
    Row {
        Column {
            products.forEach { product ->
                productRow(product)
            }
        }
    }
}

@Composable
fun productRow(
    product: Product
) {
    Card(modifier = Modifier.fillMaxWidth().padding(8.dp)) {
        Column(
            modifier = Modifier.padding(8.dp),
            verticalArrangement = Arrangement.Center
        ) {
            Text(product.name)
            Text(product.category.name)
            Text("$" + product.price.toString())
        }
    }
}

@Preview(showBackground = true)
@Composable
fun ProductsScreenPreview() {
    ProductsScreen()
}