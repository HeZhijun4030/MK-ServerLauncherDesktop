/**
 * @file   cms_toolkit_dll.cpp
 * @brief  CMS Cross-platform C++ utility toolkit dll head
 * @author HeZhijun4030
 * @date   2026-05-03
 */
#ifndef CMS_UTILS_DLL_HPP
#define CMS_UTILS_DLL_HPP

#define CMS_Ver "0.0.1"

#ifdef _WIN32
#ifdef CMS_EXPORTS
#define CMS_API __declspec(dllexport)
#else
#define CMS_API __declspec(dllimport)
#endif
#else
#define CMS_API
#endif

#include <iostream>
#include <limits>
#include <string>
#include <chrono>

namespace cms
{
    CMS_API void Init();


    namespace tween
    {
        class CMS_API BaseTween
        {
        public:
            enum Eas{In,Out};
            // TODO(Hzj) Ease in/out more curve
            enum Curve {Linear,QuadIn,Qurd};

            explicit BaseTween(const float& st = 0,const float& fi = 0,const float& du = 0,const Curve& cu=Curve::Linear);

            //void start(const float& st,const float& fi,const float& du,const Curve& cu);
            void Start();
            float Update();
            void BindToTarget(float& Target);
            void ApplyToUpdate();
            bool GetIsRunning() const;
        private:
            static float GetCurrentTimeMs();
            float ApplyCurve(const float& t) const;
            float StartValue;
            float FinalValue;
            float Duration;
            Curve CurCurve;
            bool IsRunning;

            float StartTime;

            float* BindTarget;

            //TODO 熔断
            bool Finished;
        };

    }


    namespace terminal
    {
        /**
         * @brief Clear terminal screen in Linux or Windows
         */
        CMS_API void ClearScreen();
    }

    namespace io
    {
        /**
         * @brief Clear input when error was happened
         */
        CMS_API void ClearInput();

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

#endif // CMS_UTILS_DLL_HPP
