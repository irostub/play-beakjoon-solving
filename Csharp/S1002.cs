using System;

class S1002{
    class Person{
        private int x_pos;
        private int y_pos;
        private int target_distance;
        public Person(){
            this.x_pos = 0;
            this.y_pos = 0;
            this.target_distance = 0;
        }

        public int get_x_pos(){
            return x_pos;
        }
        public int get_y_pos(){
            return y_pos;
        }
        public int get_target_distance(){
            return target_distance;
        }
        public void set_all(int x, int y, int dist){
            x_pos = x;
            y_pos = y;
            target_distance = dist;
        }
    }
    public static void Main(){
        Person p1 = new Person(), p2 = new Person();
        int loopControl = int.Parse(Console.ReadLine());

        while(loopControl-->0)
        {
            string[] input = Console.ReadLine().Split();
            int[] datas = Array.ConvertAll<string, int>(input, int.Parse);
            p1.set_all(datas[0],datas[1],datas[2]);
            p2.set_all(datas[3],datas[4],datas[5]);
            double distance = Math.Sqrt(Math.Pow(p2.get_x_pos()-p1.get_x_pos(),2)+Math.Pow(p2.get_y_pos()-p1.get_y_pos(),2));
            int r_sum = p2.get_target_distance() + p1.get_target_distance();
            int r_sub = Math.Abs(p2.get_target_distance() - p1.get_target_distance());
            
            if(distance == 0)
            {
                if(p1.get_target_distance() == p2.get_target_distance())
                {
                    Console.WriteLine("-1");
                }
                else
                {
                    Console.WriteLine("0");
                }
            }
            else if(distance == r_sum || distance == r_sub)
            {
                Console.WriteLine("1");
            }
            else if(distance < r_sum && distance > r_sub)
            {
                Console.WriteLine("2");
            }
            else if(distance > r_sum || distance < r_sub)
            {
                Console.WriteLine("0");
            }
        }
    }
}