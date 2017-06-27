#include <iostream>
#include <vector>

using namespace std;

class Simulation
{
  public:
  int dim, resolution, n_net;
  double f, len, dt, time, a_time, c=3e8; 
  vector<double>net;
  
  Simulation(int, int,double, double, double, double);
  void fill();
  double source(double, double);
  void reference_beam();
  void object_beam();
  void save();
  

};

