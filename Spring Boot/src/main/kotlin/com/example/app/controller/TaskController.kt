package org.example.app.controller

import org.example.app.models.Task
import org.example.app.services.AuthService
import org.example.app.services.LazyAuthService
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.http.HttpStatus
import org.springframework.web.bind.annotation.*
import org.springframework.web.server.ResponseStatusException

@RestController
@RequestMapping("/api/tasks")
class TaskController @Autowired constructor(private val authService: LazyAuthService) {

    val tasks =
            listOf(
                    Task(ID = 1, Name = "Task 1", IsDone = false),
                    Task(ID = 2, Name = "Task 2", IsDone = false),
                    Task(ID = 3, Name = "Task 3", IsDone = true),
            )

    @GetMapping
    fun index(): List<Task> {
        if (!authService.check()) {
            throw ResponseStatusException(HttpStatus.UNAUTHORIZED, "Authorization Required")
        }

        return tasks
    }

    @GetMapping("/{id}")
    fun getTaskById(@PathVariable id: Long): Task {
        if (!authService.check()) {
            throw ResponseStatusException(HttpStatus.UNAUTHORIZED, "Authorization Required")
        }

        return tasks.find { it.ID.equals(id) }
                ?: throw ResponseStatusException(HttpStatus.NOT_FOUND, "Task not found")
    }
}
