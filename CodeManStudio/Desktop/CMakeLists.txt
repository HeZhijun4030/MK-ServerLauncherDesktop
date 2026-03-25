cmake_minimum_required(VERSION 3.16)
project(CMS)

set(CMSUTILS_DIR "${CMAKE_CURRENT_SOURCE_DIR}/CMSToolkit")

add_library(CMSUtils SHARED IMPORTED)

set_target_properties(CMSUtils PROPERTIES

        IMPORTED_LOCATION_RELEASE     "${CMSUTILS_DIR}/bin/CMSToolkit.dll"
        IMPORTED_IMPLIB_RELEASE       "${CMSUTILS_DIR}/lib/CMSToolkit.lib"


        IMPORTED_LOCATION_DEBUG       "${CMSUTILS_DIR}/bin/CMSToolkitd.dll"
        IMPORTED_IMPLIB_DEBUG         "${CMSUTILS_DIR}/lib/CMSToolkitd.lib"


        INTERFACE_INCLUDE_DIRECTORIES "${CMSUTILS_DIR}/include"
)



set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)
find_package(spdlog REQUIRED CONFIG)
find_package(Qt6 REQUIRED COMPONENTS Core Widgets WebSockets)
set(CMAKE_AUTOUIC_SEARCH_PATHS ${CMAKE_CURRENT_SOURCE_DIR})
qt6_add_executable(${PROJECT_NAME}
        src/main.cpp
        src/MainWindow.cpp
        src/MainWindow.hpp
        Client.ui
        src/WebSocketManager.hpp
        src/WebSocketManager.cpp
        Dark/darkstyle.qrc
        client_Res.qrc
)

target_link_libraries(${PROJECT_NAME} PRIVATE
        Qt6::Core
        Qt6::Widgets
        Qt6::WebSockets
        spdlog::spdlog
        CMSUtils
)

target_include_directories(${PROJECT_NAME} PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src

        ${CMAKE_CURRENT_SOURCE_DIR}/include
)