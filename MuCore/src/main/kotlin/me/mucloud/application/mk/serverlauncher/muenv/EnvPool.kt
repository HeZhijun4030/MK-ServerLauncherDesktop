package me.mucloud.application.mk.serverlauncher.muenv

import com.google.gson.GsonBuilder
import com.google.gson.reflect.TypeToken
import me.mucloud.application.mk.serverlauncher.muenv.EnvPool.envFile
import me.mucloud.application.mk.serverlauncher.muenv.EnvPool.jEnvs
import java.io.File
import java.io.FileWriter
import java.nio.charset.StandardCharsets

/**
 *  # Environment Pool
 *
 *  Supported to Install/Import/Delete MuEnvironment
 *
 *  @since VoidLand V1 | DEV.1
 *  @author Mu_Cloud
 */
object EnvPool {

    private val gson = GsonBuilder()
        .setPrettyPrinting()
        .registerTypeAdapter(JavaEnvironment::class.java, JavaEnvironmentAdapter)
        .create()

    private val jEnvs: MutableList<JavaEnvironment> = mutableListOf() // In-Memory storage
    private val envFile: File = File("env.json") // Persistent storage file
    private val envFileWriter: FileWriter
    
    init {
        if(!envFile.exists()) {
            envFile.createNewFile()
        }
        envFileWriter = FileWriter(envFile, StandardCharsets.UTF_8)
        if (!scanLocalJavaEnv()) {
            envFileWriter.write("[]")
            envFileWriter.flush()
        }
    }

    /**
     * # Local Java Environment Scanner
     *
     * Scan the System Java Installation as JavaEnvironment named "SysEnv"
     *
     * *For now, it will only scan the "JAVA_HOME" system environment to locate the Java Installation in System*
     *
     * This Function Implementation may change Frequently
     */
    private fun scanLocalJavaEnv(): Boolean{
        val sysEnvPath = System.getenv("JAVA_HOME") ?: return false
        regEnv(JavaEnvironment("SysEnv", sysEnvPath))
        return true
    }

    /**
     * Scan JavaEnvironment from env.json in MK-ServerLauncher Installation Folder
     *
     * @return List of JavaEnvironment, element deserialized by JavaEnvironmentAdapter
     */
    fun scanEnv() {
        if(envFile.exists()){
            gson.fromJson<List<JavaEnvironment>>(
                envFile.readText(StandardCharsets.UTF_8),
                object : TypeToken<List<JavaEnvironment>>(){}.type
            ).forEach{ e ->
                jEnvs.add(e)
            }
        }
    }

    /**
     * Write [jEnvs] Object to [envFile] by JavaEnvironmentAdapter
     */
    fun save(){
        if(envFile.exists()){
            envFileWriter.write(gson.toJson(jEnvs, object : TypeToken<List<JavaEnvironment>>(){}.type))
            envFileWriter.flush()
        }
    }

    fun getEnv(name: String) = jEnvs.find { it.name == name }

    fun delEnv(envName: String): Boolean{
        return jEnvs.removeIf { it.name == envName }.also{ save() }
    }

    fun regEnv(env: JavaEnvironment){
        val target = jEnvs.find { it.name == env.name || it.getExecFolder() == env.getExecFolder() }
        if (target == null){
            jEnvs.add(env)
            save()
        }
    }

    fun getEnvList(): List<JavaEnvironment> = jEnvs

}