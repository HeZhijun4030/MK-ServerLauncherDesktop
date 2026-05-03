/**
* @file   cms_utils.hpp
 * @brief  CMS Cross-platform C++ utility toolkit Header only
 * @author HeZhijun4030
 * @date   2026-05-03
 */
#ifndef CMS_UTILS_HPP
#define CMS_UTILS_HPP

#include <iostream>
#include <limits>
#include <string>

namespace cms
{

    namespace terminal
    {
        /**
         * @brief Clear terminal screen in Linux or Windows
         */
        inline void ClearScreen()
        {
#if defined(_WIN32) || defined(_WIN64)
            system("cls");
#else
            system("clear");
#endif
        }
    }

    namespace io
    {
        /**
         * @brief Clear input when error was happened
         */
        inline void ClearInput()
        {std::cin.clear();std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');} //ClearInput

        /**
        * @brief Safely reads user input with EOF detection
        * @tparam T      Target data type
        * @param Prompt  Prompt message to display
        * @return T      Valid input value
        * @throws std::runtime_error If input stream reaches EOF
        *
        * @note  Performs type validation and extra character detection
        * @warning Does NOT support std::string type
        * @see ClearInput()
        */
        template <typename T>
        T SafeInput(const std::string& Prompt)
        {
            T Result;
            while (true)
            {
                std::cout << Prompt;if (std::cin.eof())throw std::runtime_error("Input stream closed unexpectedly");
                if (std::cin >> Result)
                {
                    int next = std::cin.peek();if (next != '\n' && next != EOF){std::cout << "Extra characters detected, please try again" << std::endl;ClearInput();continue;}return Result;
                }
                std::cout << "Input type error, please try again" << std::endl;ClearInput();

            }
        }//SafeInput
    }
} // namespace cms

#endif // CMS_UTILS_HPP
