package org.example.app.services

object AuthService {
    var authorized: Boolean = false

    fun login(): Boolean {
        authorized = true
        return authorized
    }

    fun check(): Boolean {
        return authorized
    }
}
