#include <iostream>
#include <vector>
using namespace std;


class A{
public:
int operator()(int x){return x;}
};

class Func{
public:
    int operator() (int a, int b)
    {
        cout<<a<<'+'<<b<<'='<<a+b<<endl;
        return a;
    }
};
int addFunc(int a, int b, Func& func)
{
    func(a,b);
    return a;
}

class FuncT{
public:
    template<typename T>
    T operator() (T t1, T t2)
    {
        cout<<t1<<'+'<<t2<<'='<<t1+t2<<endl;
        return t1;
    }
};

template <typename T>
T addFuncT(T t1, T t2, FuncT& funct)
{
    funct(t1,t2);
    return t1;
}

struct increase
{
    template<typename T>
    int operator()(T& e)
    {
        cout<<9*e<<endl;
        return e;
    }
};
template <typename T>
T increaseFuncT(T t1, increase& aaa)
{
    aaa(t1);
    return t1;
}

template<typename T, typename VST>
void traverse(T ,VST&  );
int main()
{
    /*
    int a[] = {0,1,2,3,4,5,6,7,8};
    int i =2;
     cout<<i++<<endl;
    cout<<a[i]<<endl;
     cout<<i<<endl;
        cout<<a[i++]<<endl;

        A a;
        cout<<a(5);

    Func func;
    addFunc(1,3,func);

    FuncT funct;
    addFuncT(2,4,funct);
    addFuncT(1.4,2.3,funct);


    increase aaa;
    traverse(0.333,aaa);  */
    int i =1 , j=4;

    cout<<((i+j)>>1)<<endl;
    cout << "Hello world!" << endl;
    return 0;
}

template<typename T,typename VST>
void traverse(T num,VST& funame)
{
    cout<<"increaseFuncT "<<endl;
    increaseFuncT(num ,funame);
}
