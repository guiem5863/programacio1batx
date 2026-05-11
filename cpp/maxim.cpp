#include <stdio.h>
#include <iostream>
#include <math.h>
#include <cmath>
#include <vector>
using namespace std;
int main(){
   int n;//n de casos
   cin >> n;

    for (int i = 0;i < n;i++){
 
        int a; //nombre de nombres
        int max = -(10*10*10*10*10*10) -1; //on posarem el maxim
        int sum = 0;//vegades que surt el maxim
        
        cin >> a;   //legim el nombre de vegades A
        vector<long long int> v(a);//on posam els nombres participants
         
        //legim totes les dades:
        for (int y = 0;y < a;y++){
            cin >> v[y];
            
        
        }  
        
        for (int y = 0;y < a;y++){
            //hem de veure si hi ha un nou maxim
            if(max<v[y]){
                sum = 0;
                max = v[y];
            }
           if(v[y] == max){
               sum++;
               
               } 
            //if()
            //hem de veure si es igual al maxim i sumar un nombre a sum
        }
        cout << max << " " << sum << endl;
     
    }
}