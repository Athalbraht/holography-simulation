#include "../include/functions.h"
#include <math.h>
#include <iostream>
#include <fstream>

using namespace std;

Simulation::Simulation(int dim, int res, double f, double dt, double len, double time)
{
	this->dim = dim;
	this->resolution = res;
	this->f = f;
	this->len = len;
	this->dt = dt;
	this->time = time;
	this->a_time = time/dt;
	this->n_net = pow(res,2);
	fill();

}

void Simulation::fill()
{
	for(int i=0; i<n_net; i++)
	{
		net.push_back(0.);
	}
}

double Simulation::source(double t, double x)
{
	return cos(2*3.14*f*(t - x/c));
}

void Simulation::reference_beam(double tt)
{
	for(int i=0; i<resolution; i++)
	{
		for(int j=0; j<resolution; j++)
		{
			net[i + j*resolution] = source(tt/f, len+ 1.*sin(3.14/2)*c/f);
	//		cout<<net[i+j*resolution]<<" ";
		}
	//	cout<<endl;
	}
}


void Simulation::object_beam(double tt)
{
	for(int i=0; i<resolution; i++)
	{
		for(int j=resolution-1; j>=0; j--)
		{	
			double R = 0.5*resolution*c/f; 
			double x = R-R*sin(acos((c/f*resolution/2 - j*c/f)/R));
			//cout<<x<<endl;
			net[i + j*resolution] += source(tt/f,x);
			//cout<<net[i+j*resolution]<<" ";
		}
		//cout<<endl;
	}
}

void Simulation::save()
{
	fstream file;
	file.open("test.data", ios::app);
	file<<n_net<<endl;
	for(int i=0; i<n_net; i++)
	{
		file<<net[i]<<" ";
	}
	file.close();
}

void Simulation::start(int n)
{
	fill();
	double t = 0.;
	for(int i=0;i<n;i++)
	{
		t += dt;
		reference_beam(t);
		object_beam(t);
		save();
	}
}
