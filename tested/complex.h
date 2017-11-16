typedef long double LD;

class Complex
{
	public:
		LD a, b, module, phi;

		Complex(LD, LD);
		LD real();
		LD imag();
};
