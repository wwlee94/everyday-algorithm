public class Parent { 
    public int age = 55; 
    public String name = "황인수"; 
    
    public void print(int age, String name){
        this.age = age;
        this.name = name;
        System.out.println("Child method :" + age);
        System.out.println("Child method :" + name);
    }
}
