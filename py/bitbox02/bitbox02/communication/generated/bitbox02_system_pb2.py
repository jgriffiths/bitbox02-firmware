# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bitbox02_system.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='bitbox02_system.proto',
  package='shiftcrypto.bitbox02',
  syntax='proto3',
  serialized_pb=_b('\n\x15\x62itbox02_system.proto\x12\x14shiftcrypto.bitbox02\"\x14\n\x12\x43heckSDCardRequest\"\'\n\x13\x43heckSDCardResponse\x12\x10\n\x08inserted\x18\x01 \x01(\x08\"\x13\n\x11\x44\x65viceInfoRequest\"\x95\x01\n\x12\x44\x65viceInfoResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0binitialized\x18\x02 \x01(\x08\x12\x0f\n\x07version\x18\x03 \x01(\t\x12#\n\x1bmnemonic_passphrase_enabled\x18\x04 \x01(\x08\x12&\n\x1emonotonic_increments_remaining\x18\x05 \x01(\r\"\x9b\x01\n\x19InsertRemoveSDCardRequest\x12L\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32<.shiftcrypto.bitbox02.InsertRemoveSDCardRequest.SDCardAction\"0\n\x0cSDCardAction\x12\x0f\n\x0bREMOVE_CARD\x10\x00\x12\x0f\n\x0bINSERT_CARD\x10\x01\"\x0e\n\x0cResetRequest\",\n\x18SetDeviceLanguageRequest\x12\x10\n\x08language\x18\x01 \x01(\t\"$\n\x14SetDeviceNameRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"%\n\x12SetPasswordRequest\x12\x0f\n\x07\x65ntropy\x18\x01 \x01(\x0c\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_INSERTREMOVESDCARDREQUEST_SDCARDACTION = _descriptor.EnumDescriptor(
  name='SDCardAction',
  full_name='shiftcrypto.bitbox02.InsertRemoveSDCardRequest.SDCardAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REMOVE_CARD', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INSERT_CARD', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=391,
  serialized_end=439,
)
_sym_db.RegisterEnumDescriptor(_INSERTREMOVESDCARDREQUEST_SDCARDACTION)


_CHECKSDCARDREQUEST = _descriptor.Descriptor(
  name='CheckSDCardRequest',
  full_name='shiftcrypto.bitbox02.CheckSDCardRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=67,
)


_CHECKSDCARDRESPONSE = _descriptor.Descriptor(
  name='CheckSDCardResponse',
  full_name='shiftcrypto.bitbox02.CheckSDCardResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inserted', full_name='shiftcrypto.bitbox02.CheckSDCardResponse.inserted', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=108,
)


_DEVICEINFOREQUEST = _descriptor.Descriptor(
  name='DeviceInfoRequest',
  full_name='shiftcrypto.bitbox02.DeviceInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=129,
)


_DEVICEINFORESPONSE = _descriptor.Descriptor(
  name='DeviceInfoResponse',
  full_name='shiftcrypto.bitbox02.DeviceInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='shiftcrypto.bitbox02.DeviceInfoResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='initialized', full_name='shiftcrypto.bitbox02.DeviceInfoResponse.initialized', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='shiftcrypto.bitbox02.DeviceInfoResponse.version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mnemonic_passphrase_enabled', full_name='shiftcrypto.bitbox02.DeviceInfoResponse.mnemonic_passphrase_enabled', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='monotonic_increments_remaining', full_name='shiftcrypto.bitbox02.DeviceInfoResponse.monotonic_increments_remaining', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=281,
)


_INSERTREMOVESDCARDREQUEST = _descriptor.Descriptor(
  name='InsertRemoveSDCardRequest',
  full_name='shiftcrypto.bitbox02.InsertRemoveSDCardRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='shiftcrypto.bitbox02.InsertRemoveSDCardRequest.action', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _INSERTREMOVESDCARDREQUEST_SDCARDACTION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=284,
  serialized_end=439,
)


_RESETREQUEST = _descriptor.Descriptor(
  name='ResetRequest',
  full_name='shiftcrypto.bitbox02.ResetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=441,
  serialized_end=455,
)


_SETDEVICELANGUAGEREQUEST = _descriptor.Descriptor(
  name='SetDeviceLanguageRequest',
  full_name='shiftcrypto.bitbox02.SetDeviceLanguageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='language', full_name='shiftcrypto.bitbox02.SetDeviceLanguageRequest.language', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=457,
  serialized_end=501,
)


_SETDEVICENAMEREQUEST = _descriptor.Descriptor(
  name='SetDeviceNameRequest',
  full_name='shiftcrypto.bitbox02.SetDeviceNameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='shiftcrypto.bitbox02.SetDeviceNameRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=503,
  serialized_end=539,
)


_SETPASSWORDREQUEST = _descriptor.Descriptor(
  name='SetPasswordRequest',
  full_name='shiftcrypto.bitbox02.SetPasswordRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entropy', full_name='shiftcrypto.bitbox02.SetPasswordRequest.entropy', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=541,
  serialized_end=578,
)

_INSERTREMOVESDCARDREQUEST.fields_by_name['action'].enum_type = _INSERTREMOVESDCARDREQUEST_SDCARDACTION
_INSERTREMOVESDCARDREQUEST_SDCARDACTION.containing_type = _INSERTREMOVESDCARDREQUEST
DESCRIPTOR.message_types_by_name['CheckSDCardRequest'] = _CHECKSDCARDREQUEST
DESCRIPTOR.message_types_by_name['CheckSDCardResponse'] = _CHECKSDCARDRESPONSE
DESCRIPTOR.message_types_by_name['DeviceInfoRequest'] = _DEVICEINFOREQUEST
DESCRIPTOR.message_types_by_name['DeviceInfoResponse'] = _DEVICEINFORESPONSE
DESCRIPTOR.message_types_by_name['InsertRemoveSDCardRequest'] = _INSERTREMOVESDCARDREQUEST
DESCRIPTOR.message_types_by_name['ResetRequest'] = _RESETREQUEST
DESCRIPTOR.message_types_by_name['SetDeviceLanguageRequest'] = _SETDEVICELANGUAGEREQUEST
DESCRIPTOR.message_types_by_name['SetDeviceNameRequest'] = _SETDEVICENAMEREQUEST
DESCRIPTOR.message_types_by_name['SetPasswordRequest'] = _SETPASSWORDREQUEST

CheckSDCardRequest = _reflection.GeneratedProtocolMessageType('CheckSDCardRequest', (_message.Message,), dict(
  DESCRIPTOR = _CHECKSDCARDREQUEST,
  __module__ = 'bitbox02_system_pb2'
  # @@protoc_insertion_point(class_scope:shiftcrypto.bitbox02.CheckSDCardRequest)
  ))
_sym_db.RegisterMessage(CheckSDCardRequest)

CheckSDCardResponse = _reflection.GeneratedProtocolMessageType('CheckSDCardResponse', (_message.Message,), dict(
  DESCRIPTOR = _CHECKSDCARDRESPONSE,
  __module__ = 'bitbox02_system_pb2'
  # @@protoc_insertion_point(class_scope:shiftcrypto.bitbox02.CheckSDCardResponse)
  ))
_sym_db.RegisterMessage(CheckSDCardResponse)

DeviceInfoRequest = _reflection.GeneratedProtocolMessageType('DeviceInfoRequest', (_message.Message,), dict(
  DESCRIPTOR = _DEVICEINFOREQUEST,
  __module__ = 'bitbox02_system_pb2'
  # @@protoc_insertion_point(class_scope:shiftcrypto.bitbox02.DeviceInfoRequest)
  ))
_sym_db.RegisterMessage(DeviceInfoRequest)

DeviceInfoResponse = _reflection.GeneratedProtocolMessageType('DeviceInfoResponse', (_message.Message,), dict(
  DESCRIPTOR = _DEVICEINFORESPONSE,
  __module__ = 'bitbox02_system_pb2'
  # @@protoc_insertion_point(class_scope:shiftcrypto.bitbox02.DeviceInfoResponse)
  ))
_sym_db.RegisterMessage(DeviceInfoResponse)

InsertRemoveSDCardRequest = _reflection.GeneratedProtocolMessageType('InsertRemoveSDCardRequest', (_message.Message,), dict(
  DESCRIPTOR = _INSERTREMOVESDCARDREQUEST,
  __module__ = 'bitbox02_system_pb2'
  # @@protoc_insertion_point(class_scope:shiftcrypto.bitbox02.InsertRemoveSDCardRequest)
  ))
_sym_db.RegisterMessage(InsertRemoveSDCardRequest)

ResetRequest = _reflection.GeneratedProtocolMessageType('ResetRequest', (_message.Message,), dict(
  DESCRIPTOR = _RESETREQUEST,
  __module__ = 'bitbox02_system_pb2'
  # @@protoc_insertion_point(class_scope:shiftcrypto.bitbox02.ResetRequest)
  ))
_sym_db.RegisterMessage(ResetRequest)

SetDeviceLanguageRequest = _reflection.GeneratedProtocolMessageType('SetDeviceLanguageRequest', (_message.Message,), dict(
  DESCRIPTOR = _SETDEVICELANGUAGEREQUEST,
  __module__ = 'bitbox02_system_pb2'
  # @@protoc_insertion_point(class_scope:shiftcrypto.bitbox02.SetDeviceLanguageRequest)
  ))
_sym_db.RegisterMessage(SetDeviceLanguageRequest)

SetDeviceNameRequest = _reflection.GeneratedProtocolMessageType('SetDeviceNameRequest', (_message.Message,), dict(
  DESCRIPTOR = _SETDEVICENAMEREQUEST,
  __module__ = 'bitbox02_system_pb2'
  # @@protoc_insertion_point(class_scope:shiftcrypto.bitbox02.SetDeviceNameRequest)
  ))
_sym_db.RegisterMessage(SetDeviceNameRequest)

SetPasswordRequest = _reflection.GeneratedProtocolMessageType('SetPasswordRequest', (_message.Message,), dict(
  DESCRIPTOR = _SETPASSWORDREQUEST,
  __module__ = 'bitbox02_system_pb2'
  # @@protoc_insertion_point(class_scope:shiftcrypto.bitbox02.SetPasswordRequest)
  ))
_sym_db.RegisterMessage(SetPasswordRequest)


# @@protoc_insertion_point(module_scope)
