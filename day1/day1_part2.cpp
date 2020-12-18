// --- Day 1: Report Repair ---
// Daniel Lesniewicz, 250996
// https://adventofcode.com/2020/day/1

#include <iostream>
#include <fstream>

int data [1000];

int main( ){
    std::fstream myfile("\inputDay1.txt", std::ios_base::in);

    int line;
    int counter = 0; //ilosc wczytanych liczb
    long result = 0;
    
    while (myfile >> line){
        data[counter] = line;
        ++counter;     
    }
    
    // sprawdzanie warunku poprzez przejrzenie wszystkich kombinacji i obliczenie iloczynu
    for (int i = 0; i < counter; i++){	
		for (int j = i + 1; j < counter; j++){
			for (int k = j + 1; k < counter; k++){
				int sum = data[i] + data[j] + data[k];
				
				if(sum == 2020){	
					std::cout << "(number1, number2, number3)= (" << data[i]<<", " << data[j] <<", " << data[k]<< ")" << std::endl;
					result = data[i] * data[j] * data[k];
				}
			}
		}
	}
    std::cout<<"result (number1 * number2 * number3) = " << result << std::endl;
    return 0;
}