#
# Autogenerated by Thrift Compiler (0.9.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface:
  def createVirtualNetwork(self, protocol, controllerAddress, controllerPort, networkAddress, mask):
    """
    Parameters:
     - protocol
     - controllerAddress
     - controllerPort
     - networkAddress
     - mask
    """
    pass

  def createVirtualSwitch(self, tenantId, dpids):
    """
    Parameters:
     - tenantId
     - dpids
    """
    pass

  def createHost(self, tenantId, dpid, portNumber, mac):
    """
    Parameters:
     - tenantId
     - dpid
     - portNumber
     - mac
    """
    pass

  def createVirtualLink(self, tenantId, pathString):
    """
    Parameters:
     - tenantId
     - pathString
    """
    pass

  def startNetwork(self, tenantId):
    """
    Parameters:
     - tenantId
    """
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def createVirtualNetwork(self, protocol, controllerAddress, controllerPort, networkAddress, mask):
    """
    Parameters:
     - protocol
     - controllerAddress
     - controllerPort
     - networkAddress
     - mask
    """
    self.send_createVirtualNetwork(protocol, controllerAddress, controllerPort, networkAddress, mask)
    return self.recv_createVirtualNetwork()

  def send_createVirtualNetwork(self, protocol, controllerAddress, controllerPort, networkAddress, mask):
    self._oprot.writeMessageBegin('createVirtualNetwork', TMessageType.CALL, self._seqid)
    args = createVirtualNetwork_args()
    args.protocol = protocol
    args.controllerAddress = controllerAddress
    args.controllerPort = controllerPort
    args.networkAddress = networkAddress
    args.mask = mask
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_createVirtualNetwork(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = createVirtualNetwork_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "createVirtualNetwork failed: unknown result");

  def createVirtualSwitch(self, tenantId, dpids):
    """
    Parameters:
     - tenantId
     - dpids
    """
    self.send_createVirtualSwitch(tenantId, dpids)
    return self.recv_createVirtualSwitch()

  def send_createVirtualSwitch(self, tenantId, dpids):
    self._oprot.writeMessageBegin('createVirtualSwitch', TMessageType.CALL, self._seqid)
    args = createVirtualSwitch_args()
    args.tenantId = tenantId
    args.dpids = dpids
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_createVirtualSwitch(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = createVirtualSwitch_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "createVirtualSwitch failed: unknown result");

  def createHost(self, tenantId, dpid, portNumber, mac):
    """
    Parameters:
     - tenantId
     - dpid
     - portNumber
     - mac
    """
    self.send_createHost(tenantId, dpid, portNumber, mac)
    return self.recv_createHost()

  def send_createHost(self, tenantId, dpid, portNumber, mac):
    self._oprot.writeMessageBegin('createHost', TMessageType.CALL, self._seqid)
    args = createHost_args()
    args.tenantId = tenantId
    args.dpid = dpid
    args.portNumber = portNumber
    args.mac = mac
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_createHost(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = createHost_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "createHost failed: unknown result");

  def createVirtualLink(self, tenantId, pathString):
    """
    Parameters:
     - tenantId
     - pathString
    """
    self.send_createVirtualLink(tenantId, pathString)
    return self.recv_createVirtualLink()

  def send_createVirtualLink(self, tenantId, pathString):
    self._oprot.writeMessageBegin('createVirtualLink', TMessageType.CALL, self._seqid)
    args = createVirtualLink_args()
    args.tenantId = tenantId
    args.pathString = pathString
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_createVirtualLink(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = createVirtualLink_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "createVirtualLink failed: unknown result");

  def startNetwork(self, tenantId):
    """
    Parameters:
     - tenantId
    """
    self.send_startNetwork(tenantId)
    return self.recv_startNetwork()

  def send_startNetwork(self, tenantId):
    self._oprot.writeMessageBegin('startNetwork', TMessageType.CALL, self._seqid)
    args = startNetwork_args()
    args.tenantId = tenantId
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_startNetwork(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = startNetwork_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "startNetwork failed: unknown result");


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["createVirtualNetwork"] = Processor.process_createVirtualNetwork
    self._processMap["createVirtualSwitch"] = Processor.process_createVirtualSwitch
    self._processMap["createHost"] = Processor.process_createHost
    self._processMap["createVirtualLink"] = Processor.process_createVirtualLink
    self._processMap["startNetwork"] = Processor.process_startNetwork

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_createVirtualNetwork(self, seqid, iprot, oprot):
    args = createVirtualNetwork_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = createVirtualNetwork_result()
    result.success = self._handler.createVirtualNetwork(args.protocol, args.controllerAddress, args.controllerPort, args.networkAddress, args.mask)
    oprot.writeMessageBegin("createVirtualNetwork", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_createVirtualSwitch(self, seqid, iprot, oprot):
    args = createVirtualSwitch_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = createVirtualSwitch_result()
    result.success = self._handler.createVirtualSwitch(args.tenantId, args.dpids)
    oprot.writeMessageBegin("createVirtualSwitch", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_createHost(self, seqid, iprot, oprot):
    args = createHost_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = createHost_result()
    result.success = self._handler.createHost(args.tenantId, args.dpid, args.portNumber, args.mac)
    oprot.writeMessageBegin("createHost", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_createVirtualLink(self, seqid, iprot, oprot):
    args = createVirtualLink_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = createVirtualLink_result()
    result.success = self._handler.createVirtualLink(args.tenantId, args.pathString)
    oprot.writeMessageBegin("createVirtualLink", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_startNetwork(self, seqid, iprot, oprot):
    args = startNetwork_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = startNetwork_result()
    result.success = self._handler.startNetwork(args.tenantId)
    oprot.writeMessageBegin("startNetwork", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class createVirtualNetwork_args:
  """
  Attributes:
   - protocol
   - controllerAddress
   - controllerPort
   - networkAddress
   - mask
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'protocol', None, None, ), # 1
    (2, TType.STRING, 'controllerAddress', None, None, ), # 2
    (3, TType.I16, 'controllerPort', None, None, ), # 3
    (4, TType.STRING, 'networkAddress', None, None, ), # 4
    (5, TType.I16, 'mask', None, None, ), # 5
  )

  def __init__(self, protocol=None, controllerAddress=None, controllerPort=None, networkAddress=None, mask=None,):
    self.protocol = protocol
    self.controllerAddress = controllerAddress
    self.controllerPort = controllerPort
    self.networkAddress = networkAddress
    self.mask = mask

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.protocol = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.controllerAddress = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I16:
          self.controllerPort = iprot.readI16();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.networkAddress = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I16:
          self.mask = iprot.readI16();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('createVirtualNetwork_args')
    if self.protocol is not None:
      oprot.writeFieldBegin('protocol', TType.STRING, 1)
      oprot.writeString(self.protocol)
      oprot.writeFieldEnd()
    if self.controllerAddress is not None:
      oprot.writeFieldBegin('controllerAddress', TType.STRING, 2)
      oprot.writeString(self.controllerAddress)
      oprot.writeFieldEnd()
    if self.controllerPort is not None:
      oprot.writeFieldBegin('controllerPort', TType.I16, 3)
      oprot.writeI16(self.controllerPort)
      oprot.writeFieldEnd()
    if self.networkAddress is not None:
      oprot.writeFieldBegin('networkAddress', TType.STRING, 4)
      oprot.writeString(self.networkAddress)
      oprot.writeFieldEnd()
    if self.mask is not None:
      oprot.writeFieldBegin('mask', TType.I16, 5)
      oprot.writeI16(self.mask)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class createVirtualNetwork_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.I32, 'success', None, None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.I32:
          self.success = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('createVirtualNetwork_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.I32, 0)
      oprot.writeI32(self.success)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class createVirtualSwitch_args:
  """
  Attributes:
   - tenantId
   - dpids
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'tenantId', None, None, ), # 1
    (2, TType.LIST, 'dpids', (TType.STRING,None), None, ), # 2
  )

  def __init__(self, tenantId=None, dpids=None,):
    self.tenantId = tenantId
    self.dpids = dpids

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.tenantId = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.dpids = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = iprot.readString();
            self.dpids.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('createVirtualSwitch_args')
    if self.tenantId is not None:
      oprot.writeFieldBegin('tenantId', TType.I32, 1)
      oprot.writeI32(self.tenantId)
      oprot.writeFieldEnd()
    if self.dpids is not None:
      oprot.writeFieldBegin('dpids', TType.LIST, 2)
      oprot.writeListBegin(TType.STRING, len(self.dpids))
      for iter6 in self.dpids:
        oprot.writeString(iter6)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class createVirtualSwitch_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.I64, 'success', None, None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.I64:
          self.success = iprot.readI64();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('createVirtualSwitch_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.I64, 0)
      oprot.writeI64(self.success)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class createHost_args:
  """
  Attributes:
   - tenantId
   - dpid
   - portNumber
   - mac
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'tenantId', None, None, ), # 1
    (2, TType.STRING, 'dpid', None, None, ), # 2
    (3, TType.I16, 'portNumber', None, None, ), # 3
    (4, TType.STRING, 'mac', None, None, ), # 4
  )

  def __init__(self, tenantId=None, dpid=None, portNumber=None, mac=None,):
    self.tenantId = tenantId
    self.dpid = dpid
    self.portNumber = portNumber
    self.mac = mac

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.tenantId = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.dpid = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I16:
          self.portNumber = iprot.readI16();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.mac = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('createHost_args')
    if self.tenantId is not None:
      oprot.writeFieldBegin('tenantId', TType.I32, 1)
      oprot.writeI32(self.tenantId)
      oprot.writeFieldEnd()
    if self.dpid is not None:
      oprot.writeFieldBegin('dpid', TType.STRING, 2)
      oprot.writeString(self.dpid)
      oprot.writeFieldEnd()
    if self.portNumber is not None:
      oprot.writeFieldBegin('portNumber', TType.I16, 3)
      oprot.writeI16(self.portNumber)
      oprot.writeFieldEnd()
    if self.mac is not None:
      oprot.writeFieldBegin('mac', TType.STRING, 4)
      oprot.writeString(self.mac)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class createHost_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.I32, 'success', None, None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.I32:
          self.success = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('createHost_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.I32, 0)
      oprot.writeI32(self.success)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class createVirtualLink_args:
  """
  Attributes:
   - tenantId
   - pathString
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'tenantId', None, None, ), # 1
    (2, TType.STRING, 'pathString', None, None, ), # 2
  )

  def __init__(self, tenantId=None, pathString=None,):
    self.tenantId = tenantId
    self.pathString = pathString

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.tenantId = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.pathString = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('createVirtualLink_args')
    if self.tenantId is not None:
      oprot.writeFieldBegin('tenantId', TType.I32, 1)
      oprot.writeI32(self.tenantId)
      oprot.writeFieldEnd()
    if self.pathString is not None:
      oprot.writeFieldBegin('pathString', TType.STRING, 2)
      oprot.writeString(self.pathString)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class createVirtualLink_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.I32, 'success', None, None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.I32:
          self.success = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('createVirtualLink_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.I32, 0)
      oprot.writeI32(self.success)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class startNetwork_args:
  """
  Attributes:
   - tenantId
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'tenantId', None, None, ), # 1
  )

  def __init__(self, tenantId=None,):
    self.tenantId = tenantId

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.tenantId = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('startNetwork_args')
    if self.tenantId is not None:
      oprot.writeFieldBegin('tenantId', TType.I32, 1)
      oprot.writeI32(self.tenantId)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class startNetwork_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.BOOL, 'success', None, None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.BOOL:
          self.success = iprot.readBool();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('startNetwork_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.BOOL, 0)
      oprot.writeBool(self.success)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
