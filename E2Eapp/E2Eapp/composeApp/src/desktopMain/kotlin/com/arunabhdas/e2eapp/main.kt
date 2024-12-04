package com.arunabhdas.e2eapp

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material.Button
import androidx.compose.material.Text
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.compose.ui.window.Window
import androidx.compose.ui.window.WindowState
import androidx.compose.ui.window.application

fun main() = application {
    var secondWindowOpened by remember { mutableStateOf(true) }
    Window(
        onCloseRequest = ::exitApplication,
        title = "E2Eapp",
    ) {
        App()
        if (secondWindowOpened) {
            Window(
                onCloseRequest = { secondWindowOpened = false },
                title = "Settings",
                state = WindowState(width = 300.dp, height = 600.dp),
                resizable = false
            ) {
                Column(
                    modifier = Modifier.fillMaxSize(),
                    verticalArrangement = Arrangement.Center,
                    horizontalAlignment = Alignment.CenterHorizontally
                ) {
                    Button(onClick = {}) {
                        Text("Settings")
                    }
                }
            }
        }
    }
}