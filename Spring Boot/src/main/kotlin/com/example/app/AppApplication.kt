package org.example.app

import org.example.app.models.Task
import org.example.app.models.tasks
import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication class AppApplication

fun main(args: Array<String>) {
    for (i in 1..5) tasks.add(Task(i.toLong(), "Task ${i}", false))

    runApplication<AppApplication>(*args)
}
