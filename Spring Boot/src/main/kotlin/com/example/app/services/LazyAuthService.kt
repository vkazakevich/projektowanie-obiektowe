package org.example.app.services

import org.springframework.stereotype.Service

@Service
class LazyAuthService {
    var authorized: Boolean = false

    companion object {
        const val MOCK_USERNAME = "admin"
        const val MOCK_PASSWORD = "password"

        val instance: LazyAuthService by lazy { LazyAuthService() }
    }

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
