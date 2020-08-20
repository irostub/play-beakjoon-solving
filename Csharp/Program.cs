using System;

namespace Csharp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("ready");
            S1001.Main();
        }
        //Main 진입점 다수 일 때 dotnet 으로 실행하는 경우 옵션,
        //dotnet run Csharp.csproj /p:StartupObject=Csharp.Program
    }
}
