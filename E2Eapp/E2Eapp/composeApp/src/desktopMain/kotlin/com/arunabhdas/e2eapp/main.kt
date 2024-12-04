package com.arunabhdas.e2eapp

import androidx.compose.ui.window.Window
import androidx.compose.ui.window.application

fun main() = application {
    Window(
        onCloseRequest = ::exitApplication,
        title = "E2Eapp",
    ) {
        App()
    }
}