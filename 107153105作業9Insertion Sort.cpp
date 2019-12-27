#include <iostream>

using namespace std;


void soft(int m_array [], int length){
 cout << "排序前:";
 for(int i=0; i<length; i++){
  if(i == (length-1)){
   cout << m_array[i] << endl; 
  }else{
   cout << m_array[i] << ", ";
  }
 }

 for(int i=1; i<length; i++){
  int temp = m_array[i];
  int j = i-1;

  while(j>=0 && m_array[j]>temp){
   m_array[j+1] = m_array[j];
   j--;
  }
  m_array[j+1] = temp;
 }

 cout << "排序後:";
 for(int i=0; i<length; i++){
  if(i == (length-1)){
   cout << m_array[i] << endl; 
  }else{
   cout << m_array[i] << ", ";
  }
 }
}



int main(){

 int A[] = {8,11,99,1,4,558,41,71,81,99,5};
 int length = sizeof(A)/sizeof(int);
 soft(A, length);

 system("pause");
 return 1;
}

