package org.example.app.controller

import org.example.app.models.tasks
import org.springframework.http.HttpStatus
import org.springframework.web.bind.annotation.*
import org.springframework.web.server.ResponseStatusException

@RestController
@RequestMapping("/api/tasks")
class TaskController {

    @GetMapping fun index() = tasks

    @GetMapping("/{id}")
    fun getTaskById(@PathVariable id: Long) =
            tasks.find { it.ID.equals(id) }
                    ?: throw ResponseStatusException(HttpStatus.NOT_FOUND, "Task not found")
}
