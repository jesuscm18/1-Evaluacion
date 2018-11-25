#include<iostream>
//Clasificador par o impar
using namespace std;
int main(){
    char salir;
    int i;
    int n_maximo;
       cout<<"Desde que numero desea contar? ";
       cin>>i;
       cout<<"Hasta que numero desea contar? ";
       cin>>n_maximo;
       for(i;i<=n_maximo;i++){
       if(i%2==0){
                 cout<<i;
                 cout<<" es Par";
                 cout<<"\n";}
       else{
            cout<<i;
            cout<<" es Impar";
            cout<<"\n";}
            }
    cout<<"Toca cualquier tecla para salir";
    cin>>salir;
    return 0;
}
