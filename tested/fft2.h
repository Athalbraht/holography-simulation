#include <complex.h>
#include <cmath>
#include <vector>

vector<Complex*> fft2(LD  *array, int *shape )
{
	int n = shape[0]*shape[1];
	vector<Complex*>fft(n, new Complex(0, 0));

	for(int i=0; i<shape[0]; i++)
	{
		for(int j=0; j<shape[1]; j++)
		{
			 for(int ii=0; ii<shape[0]; ii++)
			 {
			 	for(int jj=0; jj<shape[1]; jj++)
				{
					fft[j+i*shape[1]]->module = array[jj+ii*shape[1]];
					fft[j+i*shape[1]]->phi = 2.*(LD)M_PI *(-(LD)(j*jj)/shape[1] - (LD)(i*ii)/(LD)shape[0]);

				}
			 }
		}
	}
	return fft;
}	
