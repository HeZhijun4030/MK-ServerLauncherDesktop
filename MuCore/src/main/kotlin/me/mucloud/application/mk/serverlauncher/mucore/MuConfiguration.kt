package me.mucloud.application.mk.serverlauncher.mucore

import java.io.File

class MuConfiguration{

    private val ServerFolder = File("servers")
    private val LogFolder = File("logs")

    init{
        initFolders()
    }

    private fun initFolders(){
        if(!getServerFolder().exists()) getServerFolder().mkdirs()
        if(!getLogFolder().exists()) getLogFolder().mkdirs()
    }

    fun getServerFolder(): File = ServerFolder
    fun getLogFolder(): File = LogFolder
}