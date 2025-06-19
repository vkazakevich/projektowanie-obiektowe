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
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.example.app.models.Category
import com.example.app.models.Product

@Composable
fun CategoriesScreen() {
    val categories = listOf(
        Category("Apple"),
        Category("Asus"),
        Category("Lenovo"),
    )

    categoryList(categories)
}

@Composable
fun categoryList(categories: List<Category>) {
    Row {
        Column {
            categories.forEach { category ->
                Card (modifier = Modifier.fillMaxWidth().padding(8.dp)){
                    Column {
                        Text(category.name, modifier = Modifier.padding(8.dp))
                    }
                }
            }
        }
    }
}

@Preview(showBackground = true)
@Composable
fun CategoriesScreenPreview() {
    CategoriesScreen()
}