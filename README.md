# WebServicesLabs
Web Services module labs (the module covers SOAP and REST APIs) 

### Lab 1 [SOAP]:
The implementation is done using `JAX-WS` following the Youtube tutorial `Introducing SOAP and JAX-WS`

[![Introducing SOAP and JAX-WS](https://github.com/theJaxon/WebServicesLabs/blob/master/etc/Lab%201/Video.jpg)](https://www.youtube.com/watch?v=fE1pVSiXNkU)

JAX-WS stands for Java Api for XML based Web Services, it will generate the `WSDL` for us.

### Steps:
- 2 projects were created, one representing `Server` and the other representing the `Client`
- a simple `Employee` class was written so that upon request through client using id, it returns the name of the employee
- The main FXMLcontroller `ServerController` uses the Endpoint.publish method in its initialize method.

--- 

### Lab 2 [REST]:
The implementation was done using python, flask and sqllite

