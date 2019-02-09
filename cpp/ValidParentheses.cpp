/*

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

The brackets must close in the correct order, 
"()" and "()[]{}" are all valid but "(]" and "([)]" are not.

*/

#include <iostream> 
#include <string>
#include <stack>

using namespace std;

bool isValid(string s){
    stack<char> myStack;
    int i = 0;
    while (i != s.length()){
        char c = s[i];
        if (c != ')' && c != '}' && c != ']'){
            myStack.push(c); // Push element into stack if ({[
        }else{
            if (myStack.size() == 0)
                return false; // No element in stack -> false
            char pre = myStack.top(); // Top element in stack
            switch(c){
                case ')':
                    if (pre == '(') myStack.pop();
                    else return false;
                    break;
                case '}':
                    if (pre == '{') myStack.pop();
                    else return false;
                    break;
                case ']':
                    if (pre == '[') myStack.pop();
                    else return false;
                    break;
                // If the first element in stack corresponds to c
                // Pop element from stack (this pair vanish)
                // If not a suitable pair return false 
                // (one pair false -> all false)
            }
        }
        i++;
    }
    if (myStack.size() == 0) return true;
    else return false;
    // If no element remains after comparison
    // It means every open character corresponds to a closed character
}


int main(){
    string str;
    while (true){
        cout << "Input: ";
        cin >> str;
        if(isValid(str)){
            cout << "Valid input\n";
        }else{
            cout << "Invalid input\n";
        }
    }
    return 0;
}
