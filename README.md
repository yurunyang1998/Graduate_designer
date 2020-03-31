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
