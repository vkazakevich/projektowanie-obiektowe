package org.example.app.services

import org.springframework.stereotype.Service

@Service
object AuthService {
    var authorized: Boolean = false

    const val MOCK_USERNAME = "admin"
    const val MOCK_PASSWORD = "password"

    fun login(username: String, password: String): Boolean {
        authorized = false
        
        if (MOCK_USERNAME != username) return false
        if (MOCK_PASSWORD != password) return false

        authorized = true
        return authorized
    }

    fun check(): Boolean {
        return authorized
    }
}
