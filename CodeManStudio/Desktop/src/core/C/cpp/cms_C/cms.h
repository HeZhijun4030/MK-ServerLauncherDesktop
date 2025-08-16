#pragma once
#ifndef CMS_H
#define CMS_H

#
#include <pybind11/pybind11.h>


#include <WinSock2.h>
#include <stdio.h>
#include <stdlib.h>
#include <pybind11/stl.h>  
#include <stdexcept>
#include <ws2tcpip.h> 

#pragma comment(lib, "ws2_32.lib")
namespace py = pybind11;
#endif // CMS_H