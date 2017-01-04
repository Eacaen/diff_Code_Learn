//***********************************************************
//TIME:14/10/2016
//COPY From:清华 邓俊辉 《数据结构C++》 Edition3
//***********************************************************
#include "graph.h"
#include "Vector.h"

template<typename Tv>
struct Vertex
{
	Tv data;
	int inDegree,outDegree;
	VStatus status;//from graph.h
	int dTime,fTime;
	int parent;
	int prioroty;
	Vertex(Tv const& d = (Tv)0):data(d),inDegree(0),outDegree(0),status(UNDISCOVERED),
								dTime(-1),fTime(-1),parent(-1),prioroty(INT_MAX){}
};

template<typename Te>
struct Edge
{
	Te data;
	int weight;
	Estatus status;
	Edge(Te const& d, int w):data(d),weight(w),status(UNDISCOVERED){}
};

template<typename Tv,typename Te>
class GraphMatrix : public Graph<Tv,Te>
{
private:
	Vector<Vertex<Tv>> V;
	Vector<Vector<Edge<Te>*>> E;
public:
	GraphMatrix(){n = e = 0};
	~GraphMatrix()
	{
		for(int j = 0 ; j < n; j++)
			for(int k = 0;k < n; k++)
				delete E[j][k];
	}

//顶点的基本操作：
	virtual Tv& vertex(int i){return V[i].data;}
	virtual int firstNbr(int i){return nextNbr(i,n);}
	virtual int nextNbr(int i, int j)
	{
		while( (-1<j)&& (!exists(i,--j)));
		return j;
	}
	virtual VStatus& status(int i){return V[i].status;}

//顶点的动态操作
	virtual int insert(Tv const& vertex)//插入顶点，返回编号
	{
		for(int j = 0 ; j < n; j++)E[j].insert(NULL)++;
		n++;
		E.insert(Vector<Edge<Te>*>(n,n,(Edge<Te>*)NULL));
		return V.insert(Vertex<Tv>(vertex));//向量类的操作
	}

	virtual Tv remove(int i)
	{
		for(int j = 0; j < n; j++)
		{
			if(exists(i,j)){delete E[i][j]; V[j].inDegree--;}
		}
		E.remove(i);
		n--;
		for(int j = 0; j < n; j++)
		{
			if(exists(j,i)){delete E[j][i]; V.[i].outDegree--;}
		}
		Tv Vbak = vertex(i);
		V.remove(i);
		return Vbak;
//边的确认操作
		virtual bool exists(int i,int j)
		{
			return (0<=i)&&(i<n)&&(0<=j)&&(i<n)&&(E[i][j] != NULL);
		}

		virtual Estatus& status(int i,int j){return E[i][j]->status;}
		virtual Te& edge(int i,int j){return E[i][j]->data;}
		virtual int& weight(int i,int j){return E[i][j]->weight;}
//边的动态操作
		virtual void insert(Te const& edge, int w,int i,int j)
		{
			if(exists(i,j))return;//ensure the edge is not exist 
			E[i][j] = new Edge<Te>(edge,w);
			e++;
			V[i].outDegree++;
			V[i].inDegree++;
		}
		virtual Te remove(int i,int j)
		{
			Te eBak = edge(i,j);
			delete E[i][j];
			E[i][j] = NULL;
			e--;
			V[i].outDegree--;
			V[i].inDegree--;
			return eBak;		
		}

	}
};