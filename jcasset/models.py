from sqlalchemy import Column, Integer, String, ForeignKey
from app import Base
from sqlalchemy.orm import relationship
from passlib.apps import custom_app_context as pwd_context


class Servers(Base):
    __tablename__ = 'Servers'
    sno = Column(String(20),  ForeignKey("Server_DESC.sno"), primary_key=True,)
    name = Column(String(30), unique=False)
    vendor = Column(String(30), unique=False)
    rackno = Column(String(30), unique=False)
    runits = Column(String(30), unique=False)
    mgmt_ip = Column(String(16), unique=True)
    env = Column(String(16), unique=True)
    status = Column(String(200), default="None")
    ServerDR = relationship('Server_DESC', backref='Server_DESC.sno', primaryjoin='Servers.sno==Server_DESC.sno', lazy='joined')
    def __init__(self, sno=None, name=None, vendor=None, rackno=None, runits=None, mgmt_ip=None, env=None):
        self.sno = sno
        self.name = name
        self.vendor = vendor
        self.rackno = rackno
        self.runits = runits
        self.mgmt_ip = mgmt_ip
        self.env = env
    def __repr__(self):
        return '<Servers %r>' % self.sno

class Server_DESC(Base):
    __tablename__ = 'Server_DESC'

    sno = Column(String(20),primary_key=True)
    type = Column(String(30))
    hostname = Column(String(30))
    role = Column(String(30))
    owner = Column(String(30))
    data_ip =  Column(String(16))
    gateway =  Column(String(16))
    netmask =  Column(String(16))
    interface =  Column(String(16))
    def __init__(self,sno=None, type=None, hostname=None, role=None, owner=None, data_ip=None, gateway=None, netmask=None, interface=None):
        self.sno = sno
        self.type = type
        self.hostname = hostname
        self.role = role
        self.owner = owner
        self.data_ip = data_ip
        self.gateway = gateway
        self.netmask = netmask
        self.interface = interface
    def __repr__(self):
        return "<Server_DESC: %r>"%self.sno

class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    username = Column(String(30))
    password_hash = Column(String(50))

    def __init__(self, username, password):
        self.username = username
        self.password_hash = password

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def __repr__(self):
        return "<Username: %r>" %self.username


class Os_Users(Base):
    __tablename__ = 'Os_Users'
    id = Column(Integer, primary_key=True)
    username = Column(String(30))
    password = Column(String(50))
    ssh_key  = Column(String(500))

    def __init__(self, username, password, ssh_key):
        self.username = username
        self.password = password
        self.ssh_key = ssh_key
    def __repr__(self):
        return "<Server_DESC: %r>"%self.id

class Environment(Base):
    __tablename__ = 'Environment'
    id = Column(Integer, primary_key=True)
    env = Column(String(30))
    dns = Column(String(50))
    proxy  = Column(String(22))
    subnets  = Column(String(25))

    def __init__(self, env, dns, proxy, subnets):
        self.env = env
        self.dns = dns
        self.proxy = proxy
        self.subnets = subnets
    def __repr__(self):
        return "<Environment: %r>"%self.id



