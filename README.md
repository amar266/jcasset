JCASSET-API
===================

 Restful APIs framework for DataCenter Asset Management powered by Flask-restful.
JCASSET API comes with some tools for exposing your Assets Information
via a RESTful API.

Each RestFul APIs exposed supports the following:

    /Server – GET Request for all servers invemtory
    API Example : curl -i - u <username:password>http://localhost:5000/Server
    
    /Server/<Server Serial Number> - Get,PUT,DELETE Request for specific server inventory
    Api Example : 
    curl -i -u <username:password> http://localhost:5000/Server/<Server Serial Number>
    curl -i -u <username:password> http://localhost:5000/Server/<Server Serial Number> -H "Content-Type:application/json" -d '{"name":"<New Name>", "vendor":"<New Vendor Name>"}' -X PUT
    curl http://localhost:5000/Server/<Server Serial Number> -X DELETE
    
    /Server/<Server Serial Number> - POST Request with following data 
    {"name":"ProLiant Servers","vendor":"HP","rackno":"<rack number>","runits":"<location in the rack>","mgmt_ip":"<ILO IP>","type":"<Server Type>","hostname":"<Server Hostname>","role":"<Server Role>","owner":"<Owner of the server>","data_ip":"<Data IP of the Server>"}
    API Example:
    curl -i -u <username:password> http://localhost:5000/Server/SGH437NXA3G -H "Content-Type:application/json" -X POST -d ' {"name":"ProLiant Servers","vendor":"HP","rackno":"<rack number>","runits":"<location in the rack>","mgmt_ip":"<ILO IP>","type":"<Server Type>","hostname":"<Server Hostname>","role":"<Server Role>","owner":"<Owner of the server>","data_ip":"<Data IP of the Server>"}'
    
    


Coding Conventions
------------------

This project is PEP8 compilant and please refer to these sources for the Coding
Conventions : http://www.python.org/dev/peps/pep-0008/




The initial Author is Amar Krishna <amar266@gmail.com>
