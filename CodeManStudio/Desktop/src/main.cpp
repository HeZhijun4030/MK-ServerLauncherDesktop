/**
 * @file main.cpp
 * @brief MK-ServerLauncher 桌面版主程序入口
 * @author CodeManStudio
 * @version ?
 * @date 2026-2-28
 *
 * @details
 * 该文件是应用程序的入口点，负责初始化Qt环境、
 * 设置日志系统和创建主窗口。
 */

#include <QApplication>
#include <QLabel>
#include "MainWindow.hpp"
#include "spdlog/sinks/stdout_color_sinks.h"

/**
 * @brief 应用程序入口点
 *
 * 初始化Qt应用程序，设置日志系统，创建并显示主窗口
 * 这是MK-ServerLauncher桌面版的启动入口
 */
int main(int argc, char* argv[])
{
    //初始化Qt应用程序
    QApplication app(argc, argv);

    //使用spdlog的彩色控制台输出，日志器名称为"main"
    auto MainLogger = spdlog::stdout_color_mt("main");

    app.setApplicationName("MK-ServerLauncher Desktop");
    app.setOrganizationName("MuVerse / CodeManStudio");
    app.setApplicationVersion("1.0.0");

    //创建主窗口实例，传入日志器
    //父窗口为nullptr，表示这是一个顶级窗口
    CMS::MainWindow window(nullptr, MainLogger);
    window.show();
    
    MainLogger->info("Window showed");

    return app.exec();
}