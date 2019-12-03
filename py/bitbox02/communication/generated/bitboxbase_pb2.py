# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bitboxbase.proto

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
  name='bitboxbase.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x10\x62itboxbase.proto\"\x96\x03\n\x1a\x42itBoxBaseHeartbeatRequest\x12\x39\n\nstate_code\x18\x01 \x01(\x0e\x32%.BitBoxBaseHeartbeatRequest.StateCode\x12\x45\n\x10\x64\x65scription_code\x18\x02 \x01(\x0e\x32+.BitBoxBaseHeartbeatRequest.DescriptionCode\":\n\tStateCode\x12\x08\n\x04IDLE\x10\x00\x12\x0b\n\x07WORKING\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x12\t\n\x05\x45RROR\x10\x03\"\xb9\x01\n\x0f\x44\x65scriptionCode\x12\t\n\x05\x45MPTY\x10\x00\x12\x16\n\x12INITIAL_BLOCK_SYNC\x10\x01\x12\x13\n\x0f\x44OWNLOAD_UPDATE\x10\x02\x12\x15\n\x11OUT_OF_DISK_SPACE\x10\x03\x12\x0f\n\x0bREDIS_ERROR\x10\x04\x12\n\n\x06REBOOT\x10\x05\x12\x0c\n\x08SHUTDOWN\x10\x06\x12\x11\n\rUPDATE_FAILED\x10\x07\x12\x19\n\x15NO_NETWORK_CONNECTION\x10\x08\".\n\x1f\x42itBoxBaseConfirmPairingRequest\x12\x0b\n\x03msg\x18\x01 \x01(\x0c\"\x9c\x03\n\x1a\x42itBoxBaseSetConfigRequest\x12\x42\n\x0fstatus_led_mode\x18\x01 \x01(\x0e\x32).BitBoxBaseSetConfigRequest.StatusLedMode\x12H\n\x12status_screen_mode\x18\x02 \x01(\x0e\x32,.BitBoxBaseSetConfigRequest.StatusScreenMode\x12\x0c\n\x02ip\x18\x03 \x01(\x0cH\x00\x12\x10\n\x08hostname\x18\x04 \x01(\t\"Y\n\rStatusLedMode\x12\x0e\n\nLED_ALWAYS\x10\x00\x12\x12\n\x0eLED_ON_WORKING\x10\x01\x12\x12\n\x0eLED_ON_WARNING\x10\x02\x12\x10\n\x0cLED_ON_ERROR\x10\x03\"h\n\x10StatusScreenMode\x12\x11\n\rSCREEN_ALWAYS\x10\x00\x12\x15\n\x11SCREEN_ON_WORKING\x10\x01\x12\x15\n\x11SCREEN_ON_WARNING\x10\x02\x12\x13\n\x0fSCREEN_ON_ERROR\x10\x03\x42\x0b\n\tip_option\"2\n\x1e\x42itBoxBaseDisplayStatusRequest\x12\x10\n\x08\x64uration\x18\x01 \x01(\r\"\xfb\x01\n\x11\x42itBoxBaseRequest\x12\x30\n\theartbeat\x18\x01 \x01(\x0b\x32\x1b.BitBoxBaseHeartbeatRequestH\x00\x12\x31\n\nset_config\x18\x02 \x01(\x0b\x32\x1b.BitBoxBaseSetConfigRequestH\x00\x12;\n\x0f\x63onfirm_pairing\x18\x03 \x01(\x0b\x32 .BitBoxBaseConfirmPairingRequestH\x00\x12\x39\n\x0e\x64isplay_status\x18\x04 \x01(\x0b\x32\x1f.BitBoxBaseDisplayStatusRequestH\x00\x42\t\n\x07requestb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_BITBOXBASEHEARTBEATREQUEST_STATECODE = _descriptor.EnumDescriptor(
  name='StateCode',
  full_name='BitBoxBaseHeartbeatRequest.StateCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IDLE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WORKING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WARNING', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=181,
  serialized_end=239,
)
_sym_db.RegisterEnumDescriptor(_BITBOXBASEHEARTBEATREQUEST_STATECODE)

_BITBOXBASEHEARTBEATREQUEST_DESCRIPTIONCODE = _descriptor.EnumDescriptor(
  name='DescriptionCode',
  full_name='BitBoxBaseHeartbeatRequest.DescriptionCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EMPTY', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INITIAL_BLOCK_SYNC', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOWNLOAD_UPDATE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OUT_OF_DISK_SPACE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REDIS_ERROR', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REBOOT', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHUTDOWN', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_FAILED', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_NETWORK_CONNECTION', index=8, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=242,
  serialized_end=427,
)
_sym_db.RegisterEnumDescriptor(_BITBOXBASEHEARTBEATREQUEST_DESCRIPTIONCODE)

_BITBOXBASESETCONFIGREQUEST_STATUSLEDMODE = _descriptor.EnumDescriptor(
  name='StatusLedMode',
  full_name='BitBoxBaseSetConfigRequest.StatusLedMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LED_ALWAYS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LED_ON_WORKING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LED_ON_WARNING', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LED_ON_ERROR', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=682,
  serialized_end=771,
)
_sym_db.RegisterEnumDescriptor(_BITBOXBASESETCONFIGREQUEST_STATUSLEDMODE)

_BITBOXBASESETCONFIGREQUEST_STATUSSCREENMODE = _descriptor.EnumDescriptor(
  name='StatusScreenMode',
  full_name='BitBoxBaseSetConfigRequest.StatusScreenMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SCREEN_ALWAYS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCREEN_ON_WORKING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCREEN_ON_WARNING', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCREEN_ON_ERROR', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=773,
  serialized_end=877,
)
_sym_db.RegisterEnumDescriptor(_BITBOXBASESETCONFIGREQUEST_STATUSSCREENMODE)


_BITBOXBASEHEARTBEATREQUEST = _descriptor.Descriptor(
  name='BitBoxBaseHeartbeatRequest',
  full_name='BitBoxBaseHeartbeatRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state_code', full_name='BitBoxBaseHeartbeatRequest.state_code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description_code', full_name='BitBoxBaseHeartbeatRequest.description_code', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BITBOXBASEHEARTBEATREQUEST_STATECODE,
    _BITBOXBASEHEARTBEATREQUEST_DESCRIPTIONCODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=427,
)


_BITBOXBASECONFIRMPAIRINGREQUEST = _descriptor.Descriptor(
  name='BitBoxBaseConfirmPairingRequest',
  full_name='BitBoxBaseConfirmPairingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='BitBoxBaseConfirmPairingRequest.msg', index=0,
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
  serialized_start=429,
  serialized_end=475,
)


_BITBOXBASESETCONFIGREQUEST = _descriptor.Descriptor(
  name='BitBoxBaseSetConfigRequest',
  full_name='BitBoxBaseSetConfigRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status_led_mode', full_name='BitBoxBaseSetConfigRequest.status_led_mode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status_screen_mode', full_name='BitBoxBaseSetConfigRequest.status_screen_mode', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ip', full_name='BitBoxBaseSetConfigRequest.ip', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hostname', full_name='BitBoxBaseSetConfigRequest.hostname', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BITBOXBASESETCONFIGREQUEST_STATUSLEDMODE,
    _BITBOXBASESETCONFIGREQUEST_STATUSSCREENMODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='ip_option', full_name='BitBoxBaseSetConfigRequest.ip_option',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=478,
  serialized_end=890,
)


_BITBOXBASEDISPLAYSTATUSREQUEST = _descriptor.Descriptor(
  name='BitBoxBaseDisplayStatusRequest',
  full_name='BitBoxBaseDisplayStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='duration', full_name='BitBoxBaseDisplayStatusRequest.duration', index=0,
      number=1, type=13, cpp_type=3, label=1,
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
  serialized_start=892,
  serialized_end=942,
)


_BITBOXBASEREQUEST = _descriptor.Descriptor(
  name='BitBoxBaseRequest',
  full_name='BitBoxBaseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='heartbeat', full_name='BitBoxBaseRequest.heartbeat', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='set_config', full_name='BitBoxBaseRequest.set_config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='confirm_pairing', full_name='BitBoxBaseRequest.confirm_pairing', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='display_status', full_name='BitBoxBaseRequest.display_status', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='request', full_name='BitBoxBaseRequest.request',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=945,
  serialized_end=1196,
)

_BITBOXBASEHEARTBEATREQUEST.fields_by_name['state_code'].enum_type = _BITBOXBASEHEARTBEATREQUEST_STATECODE
_BITBOXBASEHEARTBEATREQUEST.fields_by_name['description_code'].enum_type = _BITBOXBASEHEARTBEATREQUEST_DESCRIPTIONCODE
_BITBOXBASEHEARTBEATREQUEST_STATECODE.containing_type = _BITBOXBASEHEARTBEATREQUEST
_BITBOXBASEHEARTBEATREQUEST_DESCRIPTIONCODE.containing_type = _BITBOXBASEHEARTBEATREQUEST
_BITBOXBASESETCONFIGREQUEST.fields_by_name['status_led_mode'].enum_type = _BITBOXBASESETCONFIGREQUEST_STATUSLEDMODE
_BITBOXBASESETCONFIGREQUEST.fields_by_name['status_screen_mode'].enum_type = _BITBOXBASESETCONFIGREQUEST_STATUSSCREENMODE
_BITBOXBASESETCONFIGREQUEST_STATUSLEDMODE.containing_type = _BITBOXBASESETCONFIGREQUEST
_BITBOXBASESETCONFIGREQUEST_STATUSSCREENMODE.containing_type = _BITBOXBASESETCONFIGREQUEST
_BITBOXBASESETCONFIGREQUEST.oneofs_by_name['ip_option'].fields.append(
  _BITBOXBASESETCONFIGREQUEST.fields_by_name['ip'])
_BITBOXBASESETCONFIGREQUEST.fields_by_name['ip'].containing_oneof = _BITBOXBASESETCONFIGREQUEST.oneofs_by_name['ip_option']
_BITBOXBASEREQUEST.fields_by_name['heartbeat'].message_type = _BITBOXBASEHEARTBEATREQUEST
_BITBOXBASEREQUEST.fields_by_name['set_config'].message_type = _BITBOXBASESETCONFIGREQUEST
_BITBOXBASEREQUEST.fields_by_name['confirm_pairing'].message_type = _BITBOXBASECONFIRMPAIRINGREQUEST
_BITBOXBASEREQUEST.fields_by_name['display_status'].message_type = _BITBOXBASEDISPLAYSTATUSREQUEST
_BITBOXBASEREQUEST.oneofs_by_name['request'].fields.append(
  _BITBOXBASEREQUEST.fields_by_name['heartbeat'])
_BITBOXBASEREQUEST.fields_by_name['heartbeat'].containing_oneof = _BITBOXBASEREQUEST.oneofs_by_name['request']
_BITBOXBASEREQUEST.oneofs_by_name['request'].fields.append(
  _BITBOXBASEREQUEST.fields_by_name['set_config'])
_BITBOXBASEREQUEST.fields_by_name['set_config'].containing_oneof = _BITBOXBASEREQUEST.oneofs_by_name['request']
_BITBOXBASEREQUEST.oneofs_by_name['request'].fields.append(
  _BITBOXBASEREQUEST.fields_by_name['confirm_pairing'])
_BITBOXBASEREQUEST.fields_by_name['confirm_pairing'].containing_oneof = _BITBOXBASEREQUEST.oneofs_by_name['request']
_BITBOXBASEREQUEST.oneofs_by_name['request'].fields.append(
  _BITBOXBASEREQUEST.fields_by_name['display_status'])
_BITBOXBASEREQUEST.fields_by_name['display_status'].containing_oneof = _BITBOXBASEREQUEST.oneofs_by_name['request']
DESCRIPTOR.message_types_by_name['BitBoxBaseHeartbeatRequest'] = _BITBOXBASEHEARTBEATREQUEST
DESCRIPTOR.message_types_by_name['BitBoxBaseConfirmPairingRequest'] = _BITBOXBASECONFIRMPAIRINGREQUEST
DESCRIPTOR.message_types_by_name['BitBoxBaseSetConfigRequest'] = _BITBOXBASESETCONFIGREQUEST
DESCRIPTOR.message_types_by_name['BitBoxBaseDisplayStatusRequest'] = _BITBOXBASEDISPLAYSTATUSREQUEST
DESCRIPTOR.message_types_by_name['BitBoxBaseRequest'] = _BITBOXBASEREQUEST

BitBoxBaseHeartbeatRequest = _reflection.GeneratedProtocolMessageType('BitBoxBaseHeartbeatRequest', (_message.Message,), dict(
  DESCRIPTOR = _BITBOXBASEHEARTBEATREQUEST,
  __module__ = 'bitboxbase_pb2'
  # @@protoc_insertion_point(class_scope:BitBoxBaseHeartbeatRequest)
  ))
_sym_db.RegisterMessage(BitBoxBaseHeartbeatRequest)

BitBoxBaseConfirmPairingRequest = _reflection.GeneratedProtocolMessageType('BitBoxBaseConfirmPairingRequest', (_message.Message,), dict(
  DESCRIPTOR = _BITBOXBASECONFIRMPAIRINGREQUEST,
  __module__ = 'bitboxbase_pb2'
  # @@protoc_insertion_point(class_scope:BitBoxBaseConfirmPairingRequest)
  ))
_sym_db.RegisterMessage(BitBoxBaseConfirmPairingRequest)

BitBoxBaseSetConfigRequest = _reflection.GeneratedProtocolMessageType('BitBoxBaseSetConfigRequest', (_message.Message,), dict(
  DESCRIPTOR = _BITBOXBASESETCONFIGREQUEST,
  __module__ = 'bitboxbase_pb2'
  # @@protoc_insertion_point(class_scope:BitBoxBaseSetConfigRequest)
  ))
_sym_db.RegisterMessage(BitBoxBaseSetConfigRequest)

BitBoxBaseDisplayStatusRequest = _reflection.GeneratedProtocolMessageType('BitBoxBaseDisplayStatusRequest', (_message.Message,), dict(
  DESCRIPTOR = _BITBOXBASEDISPLAYSTATUSREQUEST,
  __module__ = 'bitboxbase_pb2'
  # @@protoc_insertion_point(class_scope:BitBoxBaseDisplayStatusRequest)
  ))
_sym_db.RegisterMessage(BitBoxBaseDisplayStatusRequest)

BitBoxBaseRequest = _reflection.GeneratedProtocolMessageType('BitBoxBaseRequest', (_message.Message,), dict(
  DESCRIPTOR = _BITBOXBASEREQUEST,
  __module__ = 'bitboxbase_pb2'
  # @@protoc_insertion_point(class_scope:BitBoxBaseRequest)
  ))
_sym_db.RegisterMessage(BitBoxBaseRequest)


# @@protoc_insertion_point(module_scope)
