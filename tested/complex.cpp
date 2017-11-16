#include "complex.h"
#include <cmath>

Complex::Complex(LD module=0., LD phi=0.)
{
	this->module = module;
	this->phi = phi;
}

LD Complex::real()
{
	this->a = this->module * cos(phi);
	return this->a;
}

LD Complex::imag()
{
	this->b = this->module * sin(phi);
	return this->b;
}

