#include <iostream>
#include <string>
using namespace std;
 
// Function to remove adjacent duplicates characters from a string
void removeDuplicates(string &S) {
    char prev = '\0';
    for (auto it = S.begin(); it != S.end(); it++) {
        if (prev == *it) {
            S.erase(it);
            it--;
        }
        else {
            prev = *it;
        }
    }
}
 
int main() {
    string S = "AAABBCDDD";
    removeDuplicates(S);
    cout << S << endl;
 
    return 0;
}
