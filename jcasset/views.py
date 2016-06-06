from flask import Flask, request, jsonify
from flask_restful import Resource, reqparse
from app import db_session
from auth import auth
from models import Servers, Server_DESC
from string import Template
import os, sys
import subprocess

class Server(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, help='Name for the Server')
    parser.add_argument('vendor', type=str, help='Vendor Name')
    parser.add_argument('rackno', type=str, help='Rack Number')
    parser.add_argument('runits', type=str, help='Position in rack')
    parser.add_argument('mgmt_ip', type=str, help='ILO IP of the Server')
    parser.add_argument('env', type=str, help='Server Environment')
    parser.add_argument('type', type=str, help='Type of Server')
    parser.add_argument('hostname', type=str, help='Hostname of Server')
    parser.add_argument('role', type=str, help='Role Of Server')
    parser.add_argument('owner', type=str, help='Owner of Server')
    parser.add_argument('data_ip', type=str, help='Data Ip of Server')
    parser.add_argument('gateway', type=str, help='Gateway of Server')
    parser.add_argument('netmask', type=str, help='Netmask of Server')
    parser.add_argument('interface', type=str, help='Active Interface of Server')

    @auth.login_required
    def get(self, serial_no=None):

        if serial_no == None:
            tasks = Servers.query.join(Server_DESC).all()

        else:
            tasks = Servers.query.join(Server_DESC).filter_by(sno=serial_no).all()

        output = []
        for task in tasks:

            row = {}
            for field in Servers.__table__.c:
                row[str(field.name)] = getattr(task, field.name, None)
            for field in Server_DESC.__table__.c:
                row[str(field.name)] = getattr(task.ServerDR, field.name, None)
            output.append(row)
        return jsonify(Server=output)

    @auth.login_required
    def post(self,serial_no):
        data = request.json
        args = self.parser.parse_args()
        Ser = Servers(serial_no, args["name"], args["vendor"], args["rackno"], args["runits"], args["mgmt_ip"], args["env"])
        Ser_desc = Server_DESC(serial_no,args["type"], args["hostname"], args["role"], args["owner"],args["data_ip"], args["gateway"], args["netmask"], args["interface"])
        db_session.add(Ser)
        db_session.add(Ser_desc)
        db_session.commit()
        return data

    @auth.login_required
    def put(self, serial_no):
        data = request.json
        Servers.query.filter_by(sno=serial_no).update(data)
        db_session.commit()
        return data

    @auth.login_required
    def delete(self,serial_no):
        Servers.query.filter_by(sno=serial_no).delete()
        Server_DESC.query.filter_by(sno=serial_no).delete()
        db_session.commit()
        return "Deleted %s" %serial_no

class Spawn(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, help='Name for the Server')
    @auth.login_required
    def get(self, serial_no=None):

        tasks = Servers.query.join(Server_DESC).filter_by(sno=serial_no).all()

        output = []
        for task in tasks:

            row = {}
            for field in Servers.__table__.c:
                row[str(field.name)] = getattr(task, field.name, None)
            for field in Server_DESC.__table__.c:
                row[str(field.name)] = getattr(task.ServerDR, field.name, None)
            output.append(row)
        iso = self.create_iso(serial_no)
        return jsonify(Server=output)
  
    def post_usr(self,usr):
        #usr = self.usr
        post = ""
        for i in usr:
            username = i["username"]
            password = i["password"]
            key = i["key"]
            data_usr = {'username':username, 'password':password,'key':key}
            fileus = open("./jcasset/templates/usr.txt")
            src = Template ( fileus.read() )
            post_val = src.substitute(data_usr)
            post = post + post_val
            fileus.close()

        return post
 
    def create_ks(self,serial_no):
         tasks = Servers.query.join(Server_DESC).filter_by(sno=serial_no).all()
         for task in tasks:
             ip = getattr(task.ServerDR, "data_ip", None)
             netmask = getattr(task.ServerDR, "netmask", None)
             gateway = getattr(task.ServerDR, "gateway", None)
             interface = getattr(task.ServerDR, "interface", None)
             hostname = getattr(task.ServerDR, "hostname", None)
         #cwd = os.getcwd()
         ksfile = open("./jcasset/templates/ks.cfg")
         src = Template( ksfile.read() )
         usr = usr = [{'username':'vpc_team', 'password':'teststag', 'key':"sdna,msbd,nabsdbasbd,amsnbd,bf,sdn v,nsbdv,nsbv,ns"}, {'username':'amar', 'password':'teststag', 'key':"sdna,msbd,nabsdbasbd,amsnbd,bf,sdn v,nsbdv,nsbv,ns"}] 
         post = self.post_usr(usr)
         d = { 'ip':ip, 'netmask':netmask, 'gateway':gateway, 'nameserver':'10.140.218.59', 'proxy':'10.140.218.59', 'port':'3128','post':post, 'hostname':hostname, 'interface':interface}
         result = src.substitute(d)
         ksfile.close()
         nfile = open("/tmp/amar.txt", 'w+')
         nfile.write(result)
         nfile.close()

    def create_iso(self, serial_no):
        #create directory for temporary use
        #generate a random name
        dirname = "/tmp/dfsdfsdfsd"  
        os.mkdir(dirname)
        #Copy iso data to the directory
        try:
            subprocess.call(["cp", "-rT", "/home/ubuntu/iso_temp/",dirname])
        except:
            print "Command failed"
        os.chdir(dirname)
        #create ks file 
        #ks = self.create_ks(serial_no)        
        try:
            subprocess.call(["mkisofs", "-D", "-r", "-V", "ATTENDLESS_UBUNTU", "-cache-inodes", "-J", "-l", "-b", "isolinux/isolinux.bin", "-c", "isolinux/boot.cat", "-no-emul-boot", "-boot-load-size", "4", "-boot-info-table", "-o", "/var/www/html/iso/autoinstall5.iso", dirname])
        except:
           print "ISO Creation Failed"
        #Remove tmp dir
        #os.rmdir(dirname)







        







