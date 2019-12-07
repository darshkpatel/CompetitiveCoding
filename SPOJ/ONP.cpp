#include<iostream>
#include<string>
#include<vector>
using namespace std;
vector<int> stack;

int get_priority(char x){
    switch (x)
    {
        case '(': return 6;
        case '^': return 5;
        case '$': return 5;
        case '*': return 4;
        case '/': return 4;
        case '+': return 3;
        case '-': return 3;
    }
}

void postfix(string x){
    for(int i=0;i<x.length();i++){
        if(isalnum(x[i])){
            cout << x[i];
        }
        else
        {
            if(x[i]=='(' || stack.size()==0){
                stack.push_back(x[i]);
            }
            else
            {
                if(x[i]==')'){
                    while(stack.back()!='('){
                        cout << stack.back();stack.pop_back();
                    }
                    
                }
                else if(get_priority(x[i])>get_priority(stack.back())){
                    stack.push_back(x[i]);
                }
                else{
                    while(get_priority(stack.back())>=get_priority(x[i])){
                        cout << stack.back();stack.pop_back();
                    }
                    stack.push_back(x[i]);
                }
            }
            
        }
        
    }
}

int main(){
    int cases;
    cin >> cases;
    for(int i=0;i<cases;i++){
        string expression;
        cin >> expression;
        postfix(expression);
        cout << '\n';
    }
    return 0;
}