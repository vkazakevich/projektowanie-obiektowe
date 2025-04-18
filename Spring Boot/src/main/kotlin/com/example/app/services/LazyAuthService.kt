package org.example.app.services

import org.springframework.stereotype.Service

@Service
class LazyAuthService : BaseAuthService() {
    companion object {
        val instance: LazyAuthService by lazy { LazyAuthService() }
    }
}
