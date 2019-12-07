#include <bits/stdc++.h>
#include <cmath> 
#include <ctype.h>

using namespace std;

void showMatrix(string s, int rows, int cols){
    int len= s.length();
    int pos = 0; 
    for(int i = 0; i < rows; i++){
        for(int j = 0; j < cols; j++){
            if(pos<len){
                cout << s[pos++] << " ";
            }         

        }
        cout << endl;
    }
}
string removeSpaces(string str)  
{ 
    str.erase(remove(str.begin(), str.end(), ' '), str.end()); 
    return str; 
} 
  
string removeExtra(string str)  
{ 
    str.erase(remove(str.begin(), str.end(), '-'), str.end()); 
    return str; 
} 
// Complete the encryption function below.
string encryption(string s) {
string str = removeSpaces(s);
int len = str.length();
int rows = floor(sqrt(len));
int cols= ceil(sqrt(len));
while(rows*cols<len){rows++;}
cout << "len = " << len << "min = " << rows << " max = " <<  cols << endl;
char matrix[rows][cols];

int pos = 0;
for(int i = 0; i < rows; i++){
    for(int j = 0; j < cols; j++){
    if(pos<len){
       cout << " inserting " << str[pos] << " at " << i << ":" << j << endl;
        matrix[i][j] = str[pos++];
       
        }
    else{
        
        matrix[i][j] = '-'; 
    }
    }
}
showMatrix(str,rows,cols);
string final = "";
pos = 0;

for(int i = 0; i < cols; i++){
    for(int j = 0; j < rows; j++){
            final+=matrix[j][i];
    }
    final+=" ";
}
final = removeExtra(final);
cout << "final: " << final << endl;
return final; 


}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = encryption(s);

    fout << result << "\n";

    fout.close();

    return 0;
}

