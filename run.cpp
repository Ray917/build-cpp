#include<iostream>
#include<windows.h>
#include<string>
#include<cstring>
#include<fstream>
#include<cassert>
#include<ctime>
using namespace std;
string a="";
string temp="",temp2="";
char b[2048]={0};
SYSTEMTIME StOld;
SYSTEMTIME StNow;
void TimeDifference(SYSTEMTIME StOld,SYSTEMTIME StNow){
	WORD wMinute;
	WORD wSecond;
	WORD wMilliseconds;
	if(StNow.wMilliseconds<StOld.wMilliseconds){
		StNow.wSecond--;
		StNow.wMilliseconds+=1000;
		wMilliseconds=StNow.wMilliseconds-StOld.wMilliseconds;
	}
	else wMilliseconds=StNow.wMilliseconds-StOld.wMilliseconds;
	if(StNow.wSecond<StOld.wSecond){
		StNow.wMinute--;
		StNow.wSecond+=60;
		wSecond=StNow.wSecond-StOld.wSecond;
	}
	else wSecond=StNow.wSecond-StOld.wSecond;
	if(StNow.wMinute<StOld.wMinute){
		StNow.wMinute+=60;
		wMinute=StNow.wMinute-StOld.wMinute;
	}
	else wMinute=StNow.wMinute-StOld.wMinute;
	if(wMinute!=0)printf("%d",wMinute*60);
	printf("%d",wSecond);
	printf(".%d",wMilliseconds);
}
string readTxt(string file){
    ifstream infile; 
    infile.open(file.data()); 
    assert(infile.is_open());
    string s;
    getline(infile,s);
    infile.close();
    return s;
}
int main(int argc,char *argv[]){
    system("title Build-C++ Compile and Running Process");
    system("cls");
    if(argc!=2){return 0;}
    a+="g++.exe ";
    a+=char(34);
    temp=argv[1];
    a+=temp;
    a+=char(34);
    a+=" -o ";
    a+=char(34);
    for(int i=temp.size()-1;i>=0;i--){
        if(temp[i]=='.'){
            temp2=temp.substr(0,i);
            break;
        }
    }
    a+=temp2;
    a+=".exe";
    a+=char(34);
    a+=readTxt(".\\setting.txt");
    for(int i=0;i<a.size();i++){
        b[i]=a[i];
    }
    system(b);
    a=char(34)+temp2+".exe"+char(34);
    memset(b,0,sizeof(b));
    for(int i=0;i<a.size();i++){
        b[i]=a[i];
    }
    GetLocalTime(&StOld);
    system(b);
    GetLocalTime(&StNow);
    cout<<"\n--------------------------------"<<endl;
	cout<<"Process exited after ";
    TimeDifference(StOld,StNow);
	cout<<" seconds with return value 0"<<endl;
	system("pause");
    return 0;
}