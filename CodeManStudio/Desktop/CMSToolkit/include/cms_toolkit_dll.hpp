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

            // TODO(Hzj) Ease in/out more curve
            enum Curve {
                Linear,
                QuadIn
            };

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

    /*
     清屏void
    */
    namespace terminal
    {
        CMS_API void ClearScreen();
    }

    namespace io
    {
        /*
        用来处理输入异常清空
        */
        CMS_API void ClearInput();

        /*
        参数:
        std::string 提示信息 -> T
        */
        template <typename T>
        T SafeInput(const std::string& Prompt)
        {
            T Resault;
            while (true)
            {
                if (std::cin >> Resault){if (std::cin.peek() != '\n'){std::cout << "More unknow chars , plz try again" << std::endl;ClearInput();continue;}return Resault;}
                std::cout << "Input Error , plz try again" << std::endl;
                ClearInput();
            }
        } //SafeInput
    }
} // namespace cms

#endif // CMS_UTILS_DLL_HPP
