package org.example.app.controller

import org.example.app.models.Task
import org.example.app.models.tasks
import org.example.app.services.AuthService
import org.springframework.http.HttpStatus
import org.springframework.web.bind.annotation.*
import org.springframework.web.server.ResponseStatusException

@RestController
@RequestMapping("/api/auth")
class AuthController {

    @PostMapping("/login")
    fun login() = mapOf("status" to AuthService.login())
}
