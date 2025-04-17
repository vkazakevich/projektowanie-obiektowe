package org.example.app.models

data class Task(val ID: Long, val Name: String, val IsDone: Boolean)

val tasks = mutableListOf<Task>()