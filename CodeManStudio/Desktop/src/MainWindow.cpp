/**
 * @file MainWindow.cpp
 * @brief MK-ServerLauncher 桌面版主窗口实现文件
 * @author CodeManStudio
 * @version 1.0.0
 * @date 2026-02-28
 *
 * @details
 * 实现了 MainWindow 类的所有成员函数
 * 包括窗口初始化、日志设置和资源清理等功能
*/

#include "ui_client_UI.h"  
#include "MainWindow.hpp"
#include <QVBoxLayout>
#include <QWidget>
#include <QDebug>

namespace CMS {
    /**
     * @brief 构造函数实现
     *
     * 初始化主窗口，包括：
     * 调用基类 QMainWindow 构造函数
     * 创建 UI 对象（由 Qt Designer 生成）
     * 初始化日志器
     * 设置窗口属性
     * 加载 UI 布局
     * 应用深色主题样式
     *
     * @param parent 父窗口指针，默认为 nullptr
     * @param logger spdlog 日志器指针
     *
     * @note 日志器必须在构造函数中初始化，否则无法记录早期日志
     * @see ~MainWindow() 析构函数负责清理资源
     */
MainWindow::MainWindow(QWidget* parent, std::shared_ptr<spdlog::logger> logger)
        : QMainWindow(parent),ui(new Ui::Form),logger_(logger)
{
        logger_->info("MainWindow Created");
        setWindowTitle("MK-ServerLauncher Desktop");resize(300, 200);ui->setupUi(this);qApp->setStyleSheet(CMS::DARK_STYLESHEET);
        
        //TODO(Hzj) : Actually idk what to do
}

MainWindow::~MainWindow()
{
        logger_->info("Application destoyed success");
        delete ui;
}
} // namespace CMS