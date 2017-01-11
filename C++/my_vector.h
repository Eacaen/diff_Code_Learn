#ifndef   MY_VECTOR_H
#define  MY_VECTOR_H

#include <my_vertor.h>
#include <iostream>
#include "..\fibonacci\Fib.h"
using namespace std;
typedef int Rank;

#define DEFAULT_CAPACITY 3

template <typename T>
class Vector
{
protected:
	Rank _size;
	int _capacity;
	T *_elem;
	copyfrom(T const* A, Rank lo,Rank hi);
public:
	VectorVector(int c =DEFAULT_CAPACITY,int s = 0, T v =0)
	{
		_elem =new T[_capacity = c];
		for(_size = 0 ; _size < s; _elem[_size++] = v) ;
	}
	Vector(T const* A , Rank lo , Rank hi)
	{
		copyfrom(A,lo,hi);
	}//
	Vector(T const* A , Rank n)
	{
		copyfrom(A,0,n);
	}
	Vector(Vector<T> const& V , Rank lo , Rank hi)
	{
		copyfrom(v._elem,lo,hi);
	}
	Vector(Vector<T> const& V)
	{
		copyfrom(v._elem,0,v._size);
	}

	~Vector()
	{
		delete []_elem;
	}
/**************************************************

**************************************************/
	T& operator[](Rank r)const;
	Vector<T> & operator=(Vector<T> const&);
	T& Vector<T>::operator[](Rank r)const;
	Rank Vector<T>::insert(Rank r, T const& e);
	void Vector<T>::expand();
	Rank Vector<T>::find(T const& e , Rank lo,Rank hi)const;
	int Vector<T>::remove(Rank lo , Rank hi);
	int Vector<T>::remove(Rank r);
	int Vector<T>::deduplicate();

	void traverse(void (*) (T&));
	template<typename VST>void traverse(VST& );

}

template<typename T>
void Vector<T>::copyfrom(T const* A, Rank lo,Rank hi)
{
	_elem = new T[_capacity = 2*(hi - lo)];
	_size = 0;
	while(lo < hi)
	{
		_elem[_size++] = A[lo++];
	}
}

template<typename T>
Vector<T>& Vector<T>::operator=(Vector<T> const& V)
{
	if(_elem)delete [] _elem;
	copyfrom(V._elem , 0 , V._size);
	return *this;
}

template<typename T>
void Vector<T>::expand()
{
	if(_size < _capacity)return;
	if(_capacity < DEFAULT_CAPACITY) _capacity = DEFAULT_CAPACITY;
	T* oldElem = _elem;
	_elem = new T[_capacity<<=1];
	for(int i = 0 ; i < _size ; i++)
		_elem[i] = oldElem[i];
	delete []oldElem;
}

template<typename T>
T& Vector<T>::operator[](Rank r)const
{
	return _elem[r];
}

template<typename T>
void permute(Vector<T>& v)
{
	for( int i = v._size() ; i > 0 ; i--)
		swap(v[i - 1], v[rand() % i]);
}

template<typename T>
Rank Vector<T>::find(T const& e , Rank lo,Rank hi)const
{
	while((lo < hi -- ) && (e != _elem[hi]));
	return hi;
}

template<typename T>
Rank Vector<T>::insert(Rank r, T const& e)
{
	expand();
	for( int i = _size ; i > r ; i--)_elem[i] = _elem[i - 1];
	_elem[r] = e;
	_size++;
	return r;
}
template<typename T>
int Vector<T>::remove(Rank lo , Rank hi)
{
	if( lo == hi)return 0;
	while(hi < _size)_elem[lo++] = _elem[hi++];
	_size -=(hi - lo);
	shrink();
	return hi - ho;
}
template<typename T>
int Vector<T>::remove(Rank r)
{
	T e = _elem[r];
	remove(r,r+1);
	return e;
}
template<typename T>
int Vector<T>::deduplicate()
{
	int oidSize = _size;
	Rank i = 1;
	while(i < _size)
		(find(_elem[i] , 0 , i) < 0 )?i++ : remove(i);
	return oldElem - _size;
}
template<typename T>
void Vector<T>::traverse(void (*visit)(T&))
{
	for(int i = 0 ; i < _size ; i++)
		visit(_elem[i]);
}
template<typename T>
template<typename VST>
void Vector<T>::traverse(VST& visit)
{
	for(int i = 0; i < _size ; i++)
		visit(_elem[i]);
}

template<typename T>
struct Increase
{
	virtual void operator()(T& e)
	{
		e++;
	}
};
template<typename T>
void Increase(Vector<T> & v)
{
	v.traverse(Increase<T>());
}
/******************************************************

******************************************************/
template<typename T>
int Vector<T>::uniquify_slow()
{
	int oldSize = _size;
	int i = 0;
	while(i < _size -1)
		(_elem[i] == _elem[i+1]) ? remove(i+1) : i++;
	return oldSize - _size;
}

template<typename T>
int Vector<T>::uniquify()
{
	Rank i =0 , j = 0;
	while(++j < _size)
		if(_elem[i] != _elem[j])
			_elem[++i] = _elem[j];
	_size = ++i;
	return j - i;
}

template<typename T>
static Rank binSearch_show(T* A , T const& e, Rank lo ,Rank hi)
{
	while(lo < hi)
	{
		Rank mi = (lo + hi) >>1;
		if(e < A[mi]) hi = mi;
		else 
			if(e > A[mi]) lo = mi+1;
		else
			return mi;
	}
	return -1;
}

template<typename T>
static Rank binSearch(T* A , T const& e, Rank lo ,Rank hi)
{
	while(hi - lo > 1)
	{
		Rank mi = (lo + hi)>>1;
		(e < A[mi]) ? hi = mi : lo = mi;
	}
	return (e == A[lo] ) ? lo : -1;

}

template<typename T>
static Rank fibSearch(T* A , T const& e, Rank lo ,Rank hi)
{
	Fib fib(hi - lo);
	while(lo < hi)
	{
		while(hi - lo < fib.get()) fib.prev();
		Rank mi = lo + fib.get() - 1;
		if(e < A[mi]) hi = mi;
		else 
			if(e > A[mi]) lo = mi+1;
		else
			return mi;
	}
	return -1;
}
template<typename T>
void Vector<T>::bubbleSort(Rank lo , Rank hi)
{
	while(!bubble(lo,hi--));
}

template<typename T>
bool Vector<T>::bubble(Rank lo , Rank hi)
{
	bool sorted  = true;
	while(++lo < hi)
		if(_elem[lo - 1] > _elem[lo])
		{
			sorted = false;
			swap(_elem[lo - 1] , _elem[lo]);
		}
	return sorted;
}

template<typename T>
void Vector<T>::mergeSort(Rank lo , Rank hi)
{
	if(hi - lo < 2)return;
	int  mi = (lo + hi) >> 1;
	mergeSort(lo , mi);
	mergeSort(mi , hi);
	merge(lo , mi , hi);
}

template<typename T>
void Vector<T>::merge(Rank lo , Rank mi , Rank hi)
{
	T* A = _elem + lo;
	int lb = mi - lo;
	T* B = new T[lb];
	for( Rank i = 0 ; i < lb ; B[i] = A[i++]);
	int lc = hi - mi;
	T* C = _elem + mi;
	for(Rank i = 0 , j = 0 , k = 0 ; (j < lb) || (k < lc) ;)
	{
		if( (j < lb) && ( !( k < lc) || (B[j] <= C[k]) ) ) A[i++] = B[j++];
		if( (k < lc) && (!( k < lb) || (C[k] <  B[j] ) ) )  A[i++] = C[k++];
	}
	delete [] B;
}

#endif
