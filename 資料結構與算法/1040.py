#include <iostream>
#include <string>
using namespace std;

int main() {
    string str;
    cin >> str;
    int N;
    cin >> N;
    for (int i = 0; i < N; i++) {
        int num;
        cin >> num;
        cout << num;
        if (i != N - 1) {
            cout << str;
        }
    }
    cout << endl;
    return 0;
}
