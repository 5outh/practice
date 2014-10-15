#include <vector>
#include <map>
#include <iostream>
#include <algorithm>

int coin_vals[8] = {1, 2, 5, 10, 20, 50, 100, 200}; 
// int coin_vals[3] = {1, 2, 3};
std::map<int, long> coinsums;

int sum(std::vector<long> xs) {
    long s = 0;
    for(long x : xs) {
        s += x;
    }
    return s;
}

long num_combos(int x) {
    if(x == 0) {
        return 1;
    }
    if(x < 0) {
        return 0;
    }
    
    try {
        // If a value exists in the table, return it
        return coinsums.at(x);
    } catch(std::exception e) {

        // Value not found in table
        std::vector<long> subts;
        
        for(int val : coin_vals) {
            long v = num_combos(x - val);
            subts.push_back(v);
        }

        coinsums[x] = sum(subts);
        
        return coinsums[x];
    }

}

int main(int argc, char const *argv[])
{
    int init_val = 200;
    std::cout << num_combos(init_val) << "\n";
    return 0;
}
