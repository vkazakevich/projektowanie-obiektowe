package com.example.app

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.runtime.Composable
import androidx.compose.ui.tooling.preview.Preview
import androidx.navigation.compose.rememberNavController
import com.example.app.screens.ProductsScreen
import com.example.app.ui.theme.AppTheme
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.navigation.NavController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import com.example.app.screens.CartScreen
import com.example.app.screens.CategoriesScreen
import com.example.app.utils.Seeds

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        Seeds.fill()

        setContent {
            Main()
        }
    }
}

@Composable
fun Main() {
    AppTheme {
        Scaffold(modifier = Modifier.fillMaxSize()) { innerPadding ->
            Row(modifier = Modifier.padding(innerPadding)) {
                val navController = rememberNavController()

                Column(Modifier.padding(8.dp)) {
                    NavBar(navController = navController)
                    NavHost(navController, startDestination = NavRoutes.Products.route) {
                        composable(NavRoutes.Products.route) { ProductsScreen() }
                        composable(NavRoutes.Categories.route) { CategoriesScreen() }
                        composable(NavRoutes.Cart.route) { CartScreen() }
                    }
                }
            }
        }
    }
}

@Composable
fun NavBar(navController: NavController) {
    Row(
        Modifier
            .fillMaxWidth()
            .padding(bottom = 8.dp)
    ) {
        Text(
            "Products",
            Modifier
                .weight(0.33f)
                .clickable { navController.navigate(NavRoutes.Products.route) },
            fontSize = 22.sp,
            color = Color(0xFF6650a4)
        )
        Text(
            "Categories",
            Modifier
                .weight(0.33f)
                .clickable { navController.navigate(NavRoutes.Categories.route) },
            fontSize = 22.sp,
            color = Color(0xFF6650a4)
        )
        Text(
            "Cart",
            Modifier
                .weight(0.33f)
                .clickable { navController.navigate(NavRoutes.Cart.route) },
            fontSize = 22.sp,
            color = Color(0xFF6650a4)
        )
    }
}

sealed class NavRoutes(val route: String) {
    object Products : NavRoutes("products")
    object Categories : NavRoutes("categories")
    object Cart : NavRoutes("cart")
}

@Preview(showBackground = true)
@Composable
fun MainPreview() {
    Main()
}