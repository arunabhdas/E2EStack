package com.arunabhdas.e2eapp

interface Platform {
    val name: String
}

expect fun getPlatform(): Platform