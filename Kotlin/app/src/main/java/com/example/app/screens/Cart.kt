package com.example.app.screens

import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.example.app.models.Cart
import com.example.app.providers.RealmProvider
import io.realm.kotlin.ext.query
import kotlinx.coroutines.flow.map

@Composable
fun CartScreen() {
    val realm = RealmProvider.realm

    val cartItemsState = realm.query<Cart>()
        .asFlow()
        .map { it.list }
        .collectAsState(initial = emptyList())

    val cartItems = cartItemsState.value

    Row {
        Column {
            if (cartItems.count() == 0) {
                Text("Cart is empty")
            }

            cartItems.forEach { item ->
                item.product?.let { product ->
                    Card(
                        modifier = Modifier
                            .fillMaxWidth()
                            .padding(8.dp)
                    ) {
                        Column(modifier = Modifier.padding(8.dp)) {
                            Text("Product: " + product.name)
                            Text("Quantity: " + item.amount)
                            Text("Price: $" + (product.price * item.amount))

                            Button(
                                onClick = {
                                    realm.writeBlocking {
                                        val latestCartItem = findLatest(item)

                                        if (latestCartItem != null) {
                                            if (latestCartItem.amount <= 1) {
                                                delete(latestCartItem)
                                            } else {
                                                latestCartItem.amount--
                                            }
                                        }
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