#include <stdio.h>
#include <iostream>
#include <math.h>
#include <cmath>
#include <vector>
using namespace std;
int main(){
   int n;//n de casos
    cin >> n;

    int h = 0; //Altura
    int dis = 0; //Distancia
    long l = 0; //longitud tirolina

    for (int i = 0;i < n;i++){
        
        cin >> h;
        cin >> dis;
           
            l = (sqrt(pow(h, 2) + pow(dis, 2)));   
        
        cout << l << endl;
        
    }
}