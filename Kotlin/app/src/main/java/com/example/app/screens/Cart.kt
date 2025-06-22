package com.example.app.screens

import android.util.Log
import android.widget.Toast
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.example.app.models.Cart
import com.example.app.providers.RealmProvider
import io.realm.kotlin.ext.query
import kotlinx.coroutines.flow.map
import com.stripe.android.paymentsheet.PaymentSheet
import com.stripe.android.paymentsheet.PaymentSheetResult
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.setValue
import androidx.compose.ui.platform.LocalContext
import com.github.kittinunf.fuel.core.extensions.jsonBody
import com.github.kittinunf.fuel.httpPost
import com.github.kittinunf.fuel.json.responseJson
import com.stripe.android.PaymentConfiguration
import com.github.kittinunf.result.Result

const val BACKEND_URL = "http://10.0.2.2:4242"

@Composable
fun CartScreen() {
    val realm = RealmProvider.realm

    val cartItemsState = realm.query<Cart>()
        .asFlow()
        .map { it.list }
        .collectAsState(initial = emptyList())

    val cartItems = cartItemsState.value

    val totalAmount = cartItems.sumOf { it.product!!.price * it.amount }

    val context = LocalContext.current

    val onPaymentSheetResult: (PaymentSheetResult) -> Unit = { result ->
        when (result) {
            is PaymentSheetResult.Canceled -> {
                Log.d("StripeDebug", "Canceled")
            }

            is PaymentSheetResult.Failed -> {
                Log.d("StripeDebug", "Error: ${result.error}")
                Toast.makeText(context, "Payment failed!", Toast.LENGTH_SHORT).show()
            }

            is PaymentSheetResult.Completed -> {
                realm.writeBlocking {
                    val query = this.query<Cart>()
                    delete(query)
                }

                Log.d("StripeDebug", "Completed")
                Toast.makeText(context, "Success!", Toast.LENGTH_SHORT).show()
            }
        }
    }

    val paymentSheet = remember { PaymentSheet.Builder(onPaymentSheetResult) }.build()

    var customerConfig by remember { mutableStateOf<PaymentSheet.CustomerConfiguration?>(null) }
    var paymentIntentClientSecret by remember { mutableStateOf<String?>(null) }


    LaunchedEffect(totalAmount) {
        if (totalAmount > 0) {
            "$BACKEND_URL/payment-sheet".httpPost()
                .jsonBody("{ \"amount\" : \"$totalAmount\" }").responseJson { _, _, result ->
                    if (result is Result.Success) {
                        val responseJson = result.get().obj()
                        paymentIntentClientSecret = responseJson.getString("paymentIntent")
                        customerConfig = PaymentSheet.CustomerConfiguration(
                            id = responseJson.getString("customer"),
                            ephemeralKeySecret = responseJson.getString("ephemeralKey")
                        )
                        val publishableKey = responseJson.getString("publishableKey")
                        PaymentConfiguration.init(context, publishableKey)
                    }
                }
        }
    }

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

            if (cartItems.count() > 0) {
                Text("Total: $" + totalAmount)

                Button(
                    onClick = {
                        val currentConfig = customerConfig
                        val currentClientSecret = paymentIntentClientSecret

                        if (currentConfig != null && currentClientSecret != null) {
                            presentPaymentSheet(paymentSheet, currentConfig, currentClientSecret)
                        }
                    }
                ) {
                    Text("Checkout")
                }
            }
        }
    }
}

fun presentPaymentSheet(
    paymentSheet: PaymentSheet,
    customerConfig: PaymentSheet.CustomerConfiguration,
    paymentIntentClientSecret: String
) {
    paymentSheet.presentWithPaymentIntent(
        paymentIntentClientSecret,
        PaymentSheet.Configuration.Builder(merchantDisplayName = "My merchant name")
            .customer(customerConfig)
            .build()
    )
}

@Preview(showBackground = true)
@Composable
fun CartScreenPreview() {
    CartScreen()
}