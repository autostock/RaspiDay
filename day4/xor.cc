#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct {int depth; int layer[10]; double weight[30];} NN;
const double e=2.718281828459045, temperature=0.08;
#define	sigmoid(x) (1.0/(1.0+pow(e, -x/temperature)))

double* evaluate(NN &net, double cell[]) {
	int Weight=0, Out=0;

	for (int level = 1; level < net.depth; level++) {
		int In = Out;
		Out += net.layer[level-1];		
		for (int j = 0; j < net.layer[level]; j++) {
			double s = net.weight[Weight++]; // bias
			for (int i = 0; i < net.layer[level-1]; i++) s += net.weight[Weight++] * cell[In+i];
			cell[Out+j] = sigmoid(s);
		}
	}
	return &cell[Out] ;
};

void xorNN(int a, int b) {
	static NN net={3, /*layer*/ {2,2,1},
		{/*inner1 node2 bias=*/-0.3, /*w0=*/+0.7, /*w1=*/-0.7,
		 /*inner1 node3 bias=*/-0.4, /*w0=*/-0.6, /*w1=*/+0.5,
		 /*outer2 node4 bias=*/-0.5, /*w2=*/+1.1, /*w3=*/+1.5,}};
	double cell[2+2+1]={a,b};
	printf("%d xor %d -> %d\n", a, b, evaluate(net, cell)[0]<0.5?0:1 );
}

int main(int argc, char* argv[]) {
	xorNN(0,0);
	xorNN(0,1);
	xorNN(1,0);
	xorNN(1,1);
}
