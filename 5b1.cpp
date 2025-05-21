#include <iostream>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        string s;
        getline(cin, s);
        long long final_result_of_output = 0, totalU = 0, uBeforeLastW = 0;
        for (char c : s) {
            if (c == 'w') uBeforeLastW = totalU;
            else if (c == 'u') {
                final_result_of_output += uBeforeLastW;
                totalU++;
            }
        }
        cout << final_result_of_output << '\n';
    }
    return 0;
}
