# Graduate_designer
A tool to convert dicom and rt structure to nrrd
## Dependence
PyQt5
pandas
pydicom

## How to use
### usage 1  提取指定rt
Firstly, You should click "菜单"，then click "set root folder" , which means choose a base directory of your CT dataset .
For example ,My file structure is that  
```
                                    --HMR->|-- data001 ->|-- PETSTR   
                                           |-- data002   |-- PET  
                                           ....          |-- CT_CTSTR  
                                           |-- data040   |-- CTSTR -->|  rtstructure.dcm  
                                                         |-- CT    -->|  000000.dcm  
                                                                      |  000001.dcm  
                                                                      |  000002.dcm  
                                                                      |  000003.dcm  
                                                                      |  ..........  
                                                                      |  000120.dcm  
```                                                                 
So I should choose HMR  as my base dir in "set root folder"  
Then  you should click "set rt structure" to choose a rt structure file . Please make sure that other rtstructure files which in other data folders have the same directory structure as that you chosed .  
In my example ,I should /HMR/data001/CTSTR/rtstructure.dcm  
  
Thirdly , please click "choose excel file"  to set a label table . The excel file indicates each rt to each data.  
In the excel , the first column means the data number ,like data001 .And the second means the GTV area ,all other GTV areas will be removed  from the rt structure ,except this.  
Finally , click the "提取指定rt"  to start work, it perhaps need some time to deal with all job, please be patient.  
A file named  newrtfile.dcm will be saved in the same directory as the rtstructure.dcm that you chosed.  
### usage 2 将rt structure转化为nrrd  
Before we start, please install a third party program named ["plastimatch"](http://www.plastimatch.org/)  and set its path by click "设置plastimatch" .  
Please set  plastimatch path as /Plastimatch/bin/plastimatch.exe  
Then click “将rt structure 转化为nrrd" ,it will convert all newrtfile.dcm to newrtfile.nrrd under the same folder  

### usage 3 将CT数据转化为nrrd  
Clicking "将CT数据转为nrrd” will convert all CT series data to a nrrd file.  
It will ask you to choose a CT folder , In my example ,I should choose  /HMR/data001/CT .Than the program will convert all CT data in other folders ,like data002, to a nrrd file and saved it under the CT data path which you chosed. 


