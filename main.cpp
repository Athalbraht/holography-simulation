#include "functions.h"

using namespace std;

int dim=2, resolution=100;
double tt = 0;

int main(int argc, char *argv[])
{

  Simulation *sim = new Simulation(2, 900, 1e10, 1.1,1,1);
  //sim->fill();
  //sim->reference_beam();
  //sim->object_beam();
  //sim->save();
  sim->start(10);

  return 0;
}
