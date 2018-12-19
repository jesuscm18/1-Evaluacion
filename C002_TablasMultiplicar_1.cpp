#include<iostream>
using namespace std;
int main(){
    int numero;
    int i;
    char salir;
    cout<<"Que tabala quieres que te haga (del 1 al 10)? ";
    cin>>numero;
    for(i=1;i<=10;i++){
        cout<<i;
        cout<<" x ";
        cout<<numero;
        cout<<" = ";
        cout<<i*numero;
        cout<<"\n";
        }
    cout<<"Toca cualquier tecla para salir";
    cin>>salir;
    return 0;
}
