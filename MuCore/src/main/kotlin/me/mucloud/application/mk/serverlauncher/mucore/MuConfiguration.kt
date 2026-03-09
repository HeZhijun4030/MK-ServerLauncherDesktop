package me.mucloud.application.mk.serverlauncher.mucore

import com.electronwill.nightconfig.core.file.FileConfig
import java.io.File
import java.nio.charset.StandardCharsets

class MuConfiguration{

    private val configFile = File("config.yml")
    private val configBase: FileConfig = FileConfig.builder(configFile)
        .charset(StandardCharsets.UTF_8)
        .defaultResource("/config.yml")
        .autoreload().sync()
        .build()

    var version: Int
    var serverFolder: String
    var logFolder: String
    var muCorePort: Int
    var systemMonitorInterval: Int

    init{
        configBase.load()

        version = configBase.getInt("ConfigVersion")
        serverFolder = configBase.get("ServerFolderPath")
        logFolder = configBase.get("LogFolderPath")
        muCorePort = configBase.getInt("MuCorePort")
        systemMonitorInterval = configBase.getInt("SystemMonitorInterval")

        verifyFolders()
    }

    private fun verifyFolders(){
        if(!getServerFolder().exists()) getServerFolder().mkdirs()
        if(!getLogFolder().exists()) getLogFolder().mkdirs()
    }

    fun getServerFolder(): File = File(serverFolder).absoluteFile
    fun getLogFolder(): File = File(logFolder).absoluteFile

    fun save(){
        configBase.save()
    }
}