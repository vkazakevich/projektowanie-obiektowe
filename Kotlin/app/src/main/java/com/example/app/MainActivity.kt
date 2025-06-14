package com.example.app

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Card
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.example.app.models.Category
import com.example.app.models.Product
import com.example.app.ui.theme.AppTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            AppTheme {
                Scaffold(modifier = Modifier.fillMaxSize()) { innerPadding ->
                    Row (modifier = Modifier.padding(innerPadding)) {
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

                        ProductList(products)
                        CategoryList(categories)
                    }
                }
            }
        }
    }
}

@Composable
fun ProductList(products: List<Product>) {
    Row {
        Text("Products", color = Color.Blue)

        Column {
            products.forEach { product ->
                ProductRow(product)
            }
        }
    }
}

@Composable
fun CategoryList(categories: List<Category>) {
    Row {
        Text("Categories", color = Color.Blue)

        Column {
            categories.forEach { category ->
                Card {
                    Column {
                        Text(category.name)
                    }
                }
            }
        }
    }
}

@Composable
fun ProductRow(
    product: Product
) {
    Card(modifier = Modifier.padding(8.dp)) {
        Column (
            modifier = Modifier.padding(8.dp),
            verticalArrangement = Arrangement.Center
        ) {
            Text(product.name)
            Text(product.category.name)
            Text("$" + product.price.toString())
        }
    }
}