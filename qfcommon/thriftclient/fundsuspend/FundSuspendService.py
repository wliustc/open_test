#
# Autogenerated by Thrift Compiler (0.9.1)
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
  def ping(self):
    pass

  def gen_suspend_records(self, txcurrcd, hand_type, src):
    """
    Parameters:
     - txcurrcd
     - hand_type
     - src
    """
    pass

  def add_suspend_records(self, txcurrcd, hand_type, userids):
    """
    Parameters:
     - txcurrcd
     - hand_type
     - userids
    """
    pass

  def audit_suspend_records(self, batid, hand_state):
    """
    Parameters:
     - batid
     - hand_state
    """
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def ping(self):
    self.send_ping()
    return self.recv_ping()

  def send_ping(self):
    self._oprot.writeMessageBegin('ping', TMessageType.CALL, self._seqid)
    args = ping_args()
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_ping(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = ping_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "ping failed: unknown result");

  def gen_suspend_records(self, txcurrcd, hand_type, src):
    """
    Parameters:
     - txcurrcd
     - hand_type
     - src
    """
    self.send_gen_suspend_records(txcurrcd, hand_type, src)

  def send_gen_suspend_records(self, txcurrcd, hand_type, src):
    self._oprot.writeMessageBegin('gen_suspend_records', TMessageType.CALL, self._seqid)
    args = gen_suspend_records_args()
    args.txcurrcd = txcurrcd
    args.hand_type = hand_type
    args.src = src
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()
  def add_suspend_records(self, txcurrcd, hand_type, userids):
    """
    Parameters:
     - txcurrcd
     - hand_type
     - userids
    """
    self.send_add_suspend_records(txcurrcd, hand_type, userids)

  def send_add_suspend_records(self, txcurrcd, hand_type, userids):
    self._oprot.writeMessageBegin('add_suspend_records', TMessageType.CALL, self._seqid)
    args = add_suspend_records_args()
    args.txcurrcd = txcurrcd
    args.hand_type = hand_type
    args.userids = userids
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()
  def audit_suspend_records(self, batid, hand_state):
    """
    Parameters:
     - batid
     - hand_state
    """
    self.send_audit_suspend_records(batid, hand_state)
    return self.recv_audit_suspend_records()

  def send_audit_suspend_records(self, batid, hand_state):
    self._oprot.writeMessageBegin('audit_suspend_records', TMessageType.CALL, self._seqid)
    args = audit_suspend_records_args()
    args.batid = batid
    args.hand_state = hand_state
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_audit_suspend_records(self):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = audit_suspend_records_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "audit_suspend_records failed: unknown result");


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["ping"] = Processor.process_ping
    self._processMap["gen_suspend_records"] = Processor.process_gen_suspend_records
    self._processMap["add_suspend_records"] = Processor.process_add_suspend_records
    self._processMap["audit_suspend_records"] = Processor.process_audit_suspend_records

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

  def process_ping(self, seqid, iprot, oprot):
    args = ping_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = ping_result()
    result.success = self._handler.ping()
    oprot.writeMessageBegin("ping", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_gen_suspend_records(self, seqid, iprot, oprot):
    args = gen_suspend_records_args()
    args.read(iprot)
    iprot.readMessageEnd()
    self._handler.gen_suspend_records(args.txcurrcd, args.hand_type, args.src)
    return

  def process_add_suspend_records(self, seqid, iprot, oprot):
    args = add_suspend_records_args()
    args.read(iprot)
    iprot.readMessageEnd()
    self._handler.add_suspend_records(args.txcurrcd, args.hand_type, args.userids)
    return

  def process_audit_suspend_records(self, seqid, iprot, oprot):
    args = audit_suspend_records_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = audit_suspend_records_result()
    result.success = self._handler.audit_suspend_records(args.batid, args.hand_state)
    oprot.writeMessageBegin("audit_suspend_records", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class ping_args:

  thrift_spec = (
  )

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ping_args')
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

class ping_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (FundSuspendReturn, FundSuspendReturn.thrift_spec), None, ), # 0
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
        if ftype == TType.STRUCT:
          self.success = FundSuspendReturn()
          self.success.read(iprot)
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
    oprot.writeStructBegin('ping_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
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

class gen_suspend_records_args:
  """
  Attributes:
   - txcurrcd
   - hand_type
   - src
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'txcurrcd', None, None, ), # 1
    (2, TType.I16, 'hand_type', None, None, ), # 2
    (3, TType.I16, 'src', None, None, ), # 3
  )

  def __init__(self, txcurrcd=None, hand_type=None, src=None,):
    self.txcurrcd = txcurrcd
    self.hand_type = hand_type
    self.src = src

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
          self.txcurrcd = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I16:
          self.hand_type = iprot.readI16();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I16:
          self.src = iprot.readI16();
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
    oprot.writeStructBegin('gen_suspend_records_args')
    if self.txcurrcd is not None:
      oprot.writeFieldBegin('txcurrcd', TType.STRING, 1)
      oprot.writeString(self.txcurrcd)
      oprot.writeFieldEnd()
    if self.hand_type is not None:
      oprot.writeFieldBegin('hand_type', TType.I16, 2)
      oprot.writeI16(self.hand_type)
      oprot.writeFieldEnd()
    if self.src is not None:
      oprot.writeFieldBegin('src', TType.I16, 3)
      oprot.writeI16(self.src)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.txcurrcd is None:
      raise TProtocol.TProtocolException(message='Required field txcurrcd is unset!')
    if self.hand_type is None:
      raise TProtocol.TProtocolException(message='Required field hand_type is unset!')
    if self.src is None:
      raise TProtocol.TProtocolException(message='Required field src is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class add_suspend_records_args:
  """
  Attributes:
   - txcurrcd
   - hand_type
   - userids
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'txcurrcd', None, None, ), # 1
    (2, TType.I16, 'hand_type', None, None, ), # 2
    (3, TType.STRING, 'userids', None, None, ), # 3
  )

  def __init__(self, txcurrcd=None, hand_type=None, userids=None,):
    self.txcurrcd = txcurrcd
    self.hand_type = hand_type
    self.userids = userids

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
          self.txcurrcd = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I16:
          self.hand_type = iprot.readI16();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.userids = iprot.readString();
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
    oprot.writeStructBegin('add_suspend_records_args')
    if self.txcurrcd is not None:
      oprot.writeFieldBegin('txcurrcd', TType.STRING, 1)
      oprot.writeString(self.txcurrcd)
      oprot.writeFieldEnd()
    if self.hand_type is not None:
      oprot.writeFieldBegin('hand_type', TType.I16, 2)
      oprot.writeI16(self.hand_type)
      oprot.writeFieldEnd()
    if self.userids is not None:
      oprot.writeFieldBegin('userids', TType.STRING, 3)
      oprot.writeString(self.userids)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.txcurrcd is None:
      raise TProtocol.TProtocolException(message='Required field txcurrcd is unset!')
    if self.hand_type is None:
      raise TProtocol.TProtocolException(message='Required field hand_type is unset!')
    if self.userids is None:
      raise TProtocol.TProtocolException(message='Required field userids is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class audit_suspend_records_args:
  """
  Attributes:
   - batid
   - hand_state
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'batid', None, None, ), # 1
    (2, TType.I16, 'hand_state', None, None, ), # 2
  )

  def __init__(self, batid=None, hand_state=None,):
    self.batid = batid
    self.hand_state = hand_state

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
        if ftype == TType.I64:
          self.batid = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I16:
          self.hand_state = iprot.readI16();
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
    oprot.writeStructBegin('audit_suspend_records_args')
    if self.batid is not None:
      oprot.writeFieldBegin('batid', TType.I64, 1)
      oprot.writeI64(self.batid)
      oprot.writeFieldEnd()
    if self.hand_state is not None:
      oprot.writeFieldBegin('hand_state', TType.I16, 2)
      oprot.writeI16(self.hand_state)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.batid is None:
      raise TProtocol.TProtocolException(message='Required field batid is unset!')
    if self.hand_state is None:
      raise TProtocol.TProtocolException(message='Required field hand_state is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class audit_suspend_records_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRUCT, 'success', (FundSuspendReturn, FundSuspendReturn.thrift_spec), None, ), # 0
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
        if ftype == TType.STRUCT:
          self.success = FundSuspendReturn()
          self.success.read(iprot)
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
    oprot.writeStructBegin('audit_suspend_records_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.STRUCT, 0)
      self.success.write(oprot)
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
