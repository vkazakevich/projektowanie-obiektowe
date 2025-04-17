package org.example.app.controller

import org.example.app.models.Task
import org.example.app.models.tasks
import org.example.app.services.AuthService
import org.springframework.http.HttpStatus
import org.springframework.web.bind.annotation.*
import org.springframework.web.server.ResponseStatusException

@RestController
@RequestMapping("/api/tasks")
class TaskController {

    @GetMapping
    fun index(): MutableList<Task> {
        check_auth()

        return tasks
    }

    @GetMapping("/{id}")
    fun getTaskById(@PathVariable id: Long): Task {
        check_auth()

        return tasks.find { it.ID.equals(id) }
                ?: throw ResponseStatusException(HttpStatus.NOT_FOUND, "Task not found")
    }

    fun check_auth() {
        if (!AuthService.check()) {
            throw ResponseStatusException(HttpStatus.UNAUTHORIZED, "Authorization Required")
        }
    }
}
