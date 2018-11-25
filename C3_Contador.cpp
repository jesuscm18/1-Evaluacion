#include<iostream>
int main() {
    //este programa cuenta hasta 10
    int i;
    char salir;
    //los for son un poco distintos
    //i++ es igual a i=i+1
    for(i=1;i<=10;i++){
        std::cout<<i;
        std::cout<<"\n";
        }
    std::cout<<"Toca cualquier tecla para salir";
    std::cin>>salir;
    return 0;
}
