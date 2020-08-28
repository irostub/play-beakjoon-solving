using System;

class S1000
{
    public static void Main()
    {
        string input = Console.ReadLine();
        int a = int.Parse(input.Split()[0]);
        int b = int.Parse(input.Split()[1]);
        Console.WriteLine(a + b);
    }
}