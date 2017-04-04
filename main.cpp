//model prediction

#include "svm.h"
#include <string.h>

#include <Windows.h>
#include <sstream>
#include<time.h>
#include <string>
#include<iostream>
#include <vector>
#include <fstream>
#include <winsock.h>   
#include <mysql.h>  
using namespace std;  
 
      
#pragma comment(lib, "ws2_32.lib")  
#pragma comment(lib, "libmysql.lib")  

using namespace std;

svm_parameter param;

std::vector<std::string> split(std::string str,std::string cha) 
{   
	int size = (int) str.size();
    std::string::size_type pos;
    std::vector<std::string> result;
   // str=str+cha;  
    
    for(int i=0; i<size; i++)
    {
        pos=str.find(cha,i);
        if(pos<size)
        {
            std::string s=str.substr(i,pos-i);
            result.push_back(s);
            i = pos+cha.size() - 1;
        }
    }
    return result;
}

int CountLines(char *filename)//count the line of file
{
ifstream ReadFile;
int n=0;
string temp;
ReadFile.open(filename,ios::in);//ios::in ��ʾ��ֻ���ķ�ʽ��ȡ�ļ�
if(ReadFile.fail())//�ļ���ʧ��:����0
{
   return 0;
}
else//�ļ�����,�����ļ�����
{
   while(getline(ReadFile,temp))
   {
    n++;
   }
   return n;
}
ReadFile.close();
}



int main(){
	string sqlstr;  
	double   tmpValue;   
	ifstream file;
    int LINES,i=0,j=0;
	vector<vector<string>> data ;
	vector<int> result ;
	
	LINES=CountLines("TestingData_Weight.txt");
	ifstream myfile1 ("TestingData_Weight.txt");
    string line1;
    

	 
	for (i = 0; i < LINES; i++ )  //LINE ����������
           {
              data.push_back ( vector<string>() );  
			 
            }
	while (getline(myfile1, line1) ) 
		{  
		   
			 vector<string> tmp;
			 tmp = split(line1, "\t");
			 if (line1!="")
			 {
			  for (i=0;i<=15;i++)    // 0: tweeter_id
         	  { 
		         data[j].push_back(tmp[i]);	
				 
			 	//= split(line1, "\t");    
			  }	
			 
			  j++;
			  if (j==LINES)  break;
			 }

        }

    myfile1.close();
	//init_param();
	//svm_problem prob;
	//prob.l = 4; //������
//	prob.y = new double[prob.l];
	double d;
	//int probfeature = 2; //��������ά��

//	if(param.gamma == 0) param.gamma = 0.5; 
	svm_model *model = svm_load_model("modle.txt");

	svm_node xnode[15];

	for (i=0;i<LINES;i++)  // LINES = testing data number
	{
      for (j=0;j<15;j++)    // 15 features
	  {
	     xnode[j].index = j+1;
		 tmpValue=atof(const_cast<const char *>(data[i][j+1].c_str()));  
		 xnode[j].value= atof(const_cast<const char *>(data[i][j+1].c_str())); 
	  }
	  xnode[15].index = -1;	  // -1 means end
	  d = svm_predict(model, xnode);
	  result.push_back(d);
	  cout<<d<<" "<<endl;
	}


//  ******************    Mysql operation  ^^ *******************

	    MYSQL mydata;  
      
        //��ʼ�����ݿ�  
        if (0 == mysql_library_init(0, NULL, NULL)) {  
            cout << "mysql_library_init() succeed" << endl;  
        } else {  
            cout << "mysql_library_init() failed" << endl;  
            return -1;  
        }  
      
 
      
        //��ʼ�����ݽṹ  
        if (NULL != mysql_init(&mydata)) {  
            cout << "mysql_init() succeed" << endl;  
        } else {  
            cout << "mysql_init() failed" << endl;  
            return -1;  
        }  
      
 
      
        //���������ݿ�֮ǰ�����ö��������ѡ��  
        //�������õ�ѡ��ܶ࣬���������ַ����������޷���������  
    /*    if (0 == mysql_options(&mydata, MYSQL_SET_CHARSET_NAME, "gbk")) {  
            cout << "mysql_options() succeed" << endl;  
        } else {  
            cout << "mysql_options() failed" << endl;  
            return -1;  
        }  */
      
    
      
        //�������ݿ�  
        if (NULL  
            != mysql_real_connect(&mydata, "localhost", "root", "root", "hma2014",  
            3306, NULL, 0))  
            //����ĵ�ַ���û��������룬�˿ڿ��Ը����Լ����ص��������  
        {  
            cout << "mysql_real_connect() succeed" << endl;  
        } else {  
            cout << "mysql_real_connect() failed" << endl;  
            return -1;  
        }  

		
			char  tmp[1];
			string tmpstr,timestr;
			int length; 
		for (i=0;i<LINES;i++)
		{
		   time_t seconds;
           seconds = time(NULL);
           tm * timeinfo;
           timeinfo = localtime(&seconds);
           timestr= asctime(timeinfo) ;
             char c[8];
            itoa(result[i],c,16);
			//length = sprintf(tmp, "%05X", result[i]); 
			tmpstr=c;
			sqlstr =  
			"insert into Basketball_ratio (tweet_id,inType,inserttime) values ('"+data[i][0]+"','"+tmpstr+ "','"+timestr+"');";  
			if (0 == mysql_query(&mydata, sqlstr.c_str())) {  
			//cout << "mysql_query() insert data succeed" << endl;  
			} else {  
			cout << "mysql_query() insert data failed" << endl;  
			mysql_close(&mydata);  
			return -1;  
			}  
		}
      
	 system("pause");  
}


string int2str(int &i) {
  string s;
  stringstream ss(s);
   ss << i;
 
  return ss.str();
 }