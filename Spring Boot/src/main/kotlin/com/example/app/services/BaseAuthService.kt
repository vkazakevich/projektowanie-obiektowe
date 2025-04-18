package org.example.app.services

import org.example.app.models.User

abstract class BaseAuthService {
    var currentUser: User? = null

    val users = listOf(User("admin", "password"))

    fun login(username: String, password: String): Boolean {
        currentUser = null

        val user = users.find { it.Username.lowercase().equals(username.lowercase()) }

        if (user == null) return check()
        if (user.Password != password) return check()

        currentUser = user

        return check()
    }

    fun check(): Boolean {
        return currentUser != null
    }
}