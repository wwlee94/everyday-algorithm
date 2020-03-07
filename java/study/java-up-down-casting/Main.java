public class Main 
{
    public static void main(String[] args)
    {
    	Parent p = new Child();
    	Child c = (Child)p;

    	p.print(0, "김진영");
    	System.out.println("자식의 나이1 : "+ p.age);
    	System.out.println("자식의 이름1 : "+ p.name);

        c.print();
        System.out.println("자식의 나이2 : "+ c.age);
    	System.out.println("자식의 이름2 : "+ c.name);
    }
}