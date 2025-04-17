package org.example.app.controller

import org.example.app.services.AuthService
import org.springframework.web.bind.annotation.*

@RestController
@RequestMapping("/api/auth")
class AuthController {

    @PostMapping("/login")
    fun login(
            @RequestParam("username") username: String,
            @RequestParam("password") password: String
    ) = mapOf("status" to AuthService.login(username, password))
}
