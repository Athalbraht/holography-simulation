#include <iostream>
#include "test.h"
#include "complex.h"
#include <cmath>
#include "fft2.h"

using namespace std;

int main()
{
	Complex *c = new Complex(1,(LD)M_PI);
	cout<<M_PI<<endl;
	cout<<c->imag()<<endl;
	LD *arr = new LD[10];
	int s[2]={5,5};
	for(int i=0; i<10; i++)
	{
		arr[i] = (LD)i;
	}
	
	vector<Complex*> result;
	result = fft2(arr, s);
	cout<<result[1]->module<<endl;
	for(int j=0; j<10;j++)
	{
		cout<<"mod->"<<result[j]->module<<endl;
		cout<<"ang->"<<result[j]->phi<<endl;
	}
	delete [] arr;

	return 0;
}
