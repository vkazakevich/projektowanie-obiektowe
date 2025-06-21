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
import androidx.compose.runtime.collectAsState
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.example.app.models.Cart
import com.example.app.models.Product
import com.example.app.providers.RealmProvider
import io.realm.kotlin.ext.query
import kotlinx.coroutines.flow.map

@Composable
fun ProductsScreen() {
    val realm = RealmProvider.realm
    val products = realm.query<Product>().find()

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

            product.category?.let {
                Text("Category: " + it.name)
            }

            Text("$" + product.price.toString())

            AddToCartButton(product)
        }
    }
}

@Composable
fun AddToCartButton(product: Product) {
    val realm = RealmProvider.realm

    val cartItemState = realm.query<Cart>("product._id = $0", product._id)
            .first()
            .asFlow()
            .map { it?.obj }
            .collectAsState(initial = null)

    val cartItem = cartItemState.value

    if (cartItem != null) {
        Text("In cart: " + cartItem.amount)
    }

    Button(
        onClick = {
            realm.writeBlocking {
                if (cartItem != null) {
                    findLatest(cartItem)?.let { it.amount++ }
                } else {
                    copyToRealm(Cart().apply {
                        this.product = findLatest(product)
                        amount = 1
                    })
                }
            }
        }) { Text("Add to cart") }

    if (cartItem != null) {
        Button(
            onClick = {
                realm.writeBlocking {
                    val latestCartItem = findLatest(cartItem)

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

@Preview(showBackground = true)
@Composable
fun ProductsScreenPreview() {
    ProductsScreen()
}
