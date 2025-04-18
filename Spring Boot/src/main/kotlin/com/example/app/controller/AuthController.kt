package org.example.app.controller

import org.example.app.services.AuthService
import org.example.app.services.LazyAuthService
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.web.bind.annotation.*

@RestController
@RequestMapping("/api/auth")
class AuthController @Autowired constructor(private val authService: LazyAuthService) {

    @PostMapping("/login")
    fun login(
            @RequestParam("username") username: String,
            @RequestParam("password") password: String
    ) = mapOf("status" to authService.login(username, password))
}
