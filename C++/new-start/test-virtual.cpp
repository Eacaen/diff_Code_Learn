    #include<iostream>
    using namespace std;
    class A{
    public:
      virtual void fun1(){cout<<"in A's fun1"<<endl;}
      void fun2(){cout<<"in A's fun2"<<endl;}
    };
    class B:public A{
    public:
    void fun1(){cout<<"in B's fun1"<<endl;}
    void fun2(){cout<<"in B's fun2"<<endl;}
    };
    int main()
    {
       B b;
    // a.fun();
    //b.fun();
    A* pa=&b;
    pa->fun1();
    pa->fun2();
    
    b.fun1();
    b.fun2();

    }
