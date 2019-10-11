# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DealService.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import CommonResult_pb2 as CommonResult__pb2
import Datetime_pb2 as Datetime__pb2
import Empty_pb2 as Empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='DealService.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11\x44\x65\x61lService.proto\x1a\x12\x43ommonResult.proto\x1a\x0e\x44\x61tetime.proto\x1a\x0b\x45mpty.proto\"+\n\x0eInquiryRequest\x12\x19\n\x07inquiry\x18\x01 \x01(\x0b\x32\x08.Inquiry\"(\n\rAccuseRequest\x12\x17\n\x06\x61\x63\x63use\x18\x01 \x01(\x0b\x32\x07.Accuse\"N\n\x07Inquiry\x12\r\n\x05title\x18\x01 \x01(\t\x12\x10\n\x08\x63ontents\x18\x02 \x01(\t\x12\"\n\x08\x63\x61tegory\x18\x03 \x01(\x0e\x32\x10.InquiryCategory\"Q\n\x06\x41\x63\x63use\x12\x12\n\nmission_id\x18\x01 \x01(\x05\x12\x10\n\x08\x63ontents\x18\x02 \x01(\t\x12!\n\x08\x63\x61tegory\x18\x03 \x01(\x0e\x32\x0f.AccuseCategory\"r\n\x11InquiryWithAnswer\x12\x19\n\x07inquiry\x18\x01 \x01(\x0b\x32\x08.Inquiry\x12\x13\n\x0bis_complete\x18\x02 \x01(\x08\x12\x1d\n\ncreated_at\x18\x03 \x01(\x0b\x32\t.Datetime\x12\x0e\n\x06\x61nswer\x18\x04 \x01(\t\"0\n\x0fInquiryResponse\x12\x1d\n\x06result\x18\x01 \x01(\x0b\x32\r.CommonResult\"]\n\x15LookUpInquiryResponse\x12\x1d\n\x06result\x18\x01 \x01(\x0b\x32\r.CommonResult\x12%\n\tinquiries\x18\x02 \x03(\x0b\x32\x12.InquiryWithAnswer\"/\n\x0e\x41\x63\x63useResponse\x12\x1d\n\x06result\x18\x01 \x01(\x0b\x32\r.CommonResult*f\n\x0fInquiryCategory\x12\x1c\n\x18UNKNOWN_INQUIRY_CATEGORY\x10\x00\x12\t\n\x05POINT\x10\x01\x12\x0b\n\x07PROJECT\x10\x02\x12\x0c\n\x08REGISTER\x10\x03\x12\x0f\n\x0b\x45TC_INQUIRY\x10\x04*g\n\x0e\x41\x63\x63useCategory\x12\x1b\n\x17UNKNOWN_ACCUSE_CATEGORY\x10\x00\x12\n\n\x06INSULT\x10\x01\x12\x11\n\rADVERTISEMENT\x10\x02\x12\t\n\x05\x41\x44ULT\x10\x03\x12\x0e\n\nETC_ACCUSE\x10\x04\x32\x97\x01\n\x0b\x44\x65\x61lService\x12,\n\x07Inquiry\x12\x0f.InquiryRequest\x1a\x10.InquiryResponse\x12/\n\rLookUpInquiry\x12\x06.Empty\x1a\x16.LookUpInquiryResponse\x12)\n\x06\x41\x63\x63use\x12\x0e.AccuseRequest\x1a\x0f.AccuseResponseb\x06proto3')
  ,
  dependencies=[CommonResult__pb2.DESCRIPTOR,Datetime__pb2.DESCRIPTOR,Empty__pb2.DESCRIPTOR,])

_INQUIRYCATEGORY = _descriptor.EnumDescriptor(
  name='InquiryCategory',
  full_name='InquiryCategory',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_INQUIRY_CATEGORY', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POINT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROJECT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGISTER', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ETC_INQUIRY', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=630,
  serialized_end=732,
)
_sym_db.RegisterEnumDescriptor(_INQUIRYCATEGORY)

InquiryCategory = enum_type_wrapper.EnumTypeWrapper(_INQUIRYCATEGORY)
_ACCUSECATEGORY = _descriptor.EnumDescriptor(
  name='AccuseCategory',
  full_name='AccuseCategory',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_ACCUSE_CATEGORY', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INSULT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADVERTISEMENT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADULT', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ETC_ACCUSE', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=734,
  serialized_end=837,
)
_sym_db.RegisterEnumDescriptor(_ACCUSECATEGORY)

AccuseCategory = enum_type_wrapper.EnumTypeWrapper(_ACCUSECATEGORY)
UNKNOWN_INQUIRY_CATEGORY = 0
POINT = 1
PROJECT = 2
REGISTER = 3
ETC_INQUIRY = 4
UNKNOWN_ACCUSE_CATEGORY = 0
INSULT = 1
ADVERTISEMENT = 2
ADULT = 3
ETC_ACCUSE = 4



_INQUIRYREQUEST = _descriptor.Descriptor(
  name='InquiryRequest',
  full_name='InquiryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inquiry', full_name='InquiryRequest.inquiry', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=113,
)


_ACCUSEREQUEST = _descriptor.Descriptor(
  name='AccuseRequest',
  full_name='AccuseRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='accuse', full_name='AccuseRequest.accuse', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=155,
)


_INQUIRY = _descriptor.Descriptor(
  name='Inquiry',
  full_name='Inquiry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='Inquiry.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contents', full_name='Inquiry.contents', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='Inquiry.category', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=157,
  serialized_end=235,
)


_ACCUSE = _descriptor.Descriptor(
  name='Accuse',
  full_name='Accuse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mission_id', full_name='Accuse.mission_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contents', full_name='Accuse.contents', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='Accuse.category', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=237,
  serialized_end=318,
)


_INQUIRYWITHANSWER = _descriptor.Descriptor(
  name='InquiryWithAnswer',
  full_name='InquiryWithAnswer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inquiry', full_name='InquiryWithAnswer.inquiry', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_complete', full_name='InquiryWithAnswer.is_complete', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='InquiryWithAnswer.created_at', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='answer', full_name='InquiryWithAnswer.answer', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=320,
  serialized_end=434,
)


_INQUIRYRESPONSE = _descriptor.Descriptor(
  name='InquiryResponse',
  full_name='InquiryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='InquiryResponse.result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=436,
  serialized_end=484,
)


_LOOKUPINQUIRYRESPONSE = _descriptor.Descriptor(
  name='LookUpInquiryResponse',
  full_name='LookUpInquiryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='LookUpInquiryResponse.result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inquiries', full_name='LookUpInquiryResponse.inquiries', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=486,
  serialized_end=579,
)


_ACCUSERESPONSE = _descriptor.Descriptor(
  name='AccuseResponse',
  full_name='AccuseResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='AccuseResponse.result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=581,
  serialized_end=628,
)

_INQUIRYREQUEST.fields_by_name['inquiry'].message_type = _INQUIRY
_ACCUSEREQUEST.fields_by_name['accuse'].message_type = _ACCUSE
_INQUIRY.fields_by_name['category'].enum_type = _INQUIRYCATEGORY
_ACCUSE.fields_by_name['category'].enum_type = _ACCUSECATEGORY
_INQUIRYWITHANSWER.fields_by_name['inquiry'].message_type = _INQUIRY
_INQUIRYWITHANSWER.fields_by_name['created_at'].message_type = Datetime__pb2._DATETIME
_INQUIRYRESPONSE.fields_by_name['result'].message_type = CommonResult__pb2._COMMONRESULT
_LOOKUPINQUIRYRESPONSE.fields_by_name['result'].message_type = CommonResult__pb2._COMMONRESULT
_LOOKUPINQUIRYRESPONSE.fields_by_name['inquiries'].message_type = _INQUIRYWITHANSWER
_ACCUSERESPONSE.fields_by_name['result'].message_type = CommonResult__pb2._COMMONRESULT
DESCRIPTOR.message_types_by_name['InquiryRequest'] = _INQUIRYREQUEST
DESCRIPTOR.message_types_by_name['AccuseRequest'] = _ACCUSEREQUEST
DESCRIPTOR.message_types_by_name['Inquiry'] = _INQUIRY
DESCRIPTOR.message_types_by_name['Accuse'] = _ACCUSE
DESCRIPTOR.message_types_by_name['InquiryWithAnswer'] = _INQUIRYWITHANSWER
DESCRIPTOR.message_types_by_name['InquiryResponse'] = _INQUIRYRESPONSE
DESCRIPTOR.message_types_by_name['LookUpInquiryResponse'] = _LOOKUPINQUIRYRESPONSE
DESCRIPTOR.message_types_by_name['AccuseResponse'] = _ACCUSERESPONSE
DESCRIPTOR.enum_types_by_name['InquiryCategory'] = _INQUIRYCATEGORY
DESCRIPTOR.enum_types_by_name['AccuseCategory'] = _ACCUSECATEGORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InquiryRequest = _reflection.GeneratedProtocolMessageType('InquiryRequest', (_message.Message,), {
  'DESCRIPTOR' : _INQUIRYREQUEST,
  '__module__' : 'DealService_pb2'
  # @@protoc_insertion_point(class_scope:InquiryRequest)
  })
_sym_db.RegisterMessage(InquiryRequest)

AccuseRequest = _reflection.GeneratedProtocolMessageType('AccuseRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCUSEREQUEST,
  '__module__' : 'DealService_pb2'
  # @@protoc_insertion_point(class_scope:AccuseRequest)
  })
_sym_db.RegisterMessage(AccuseRequest)

Inquiry = _reflection.GeneratedProtocolMessageType('Inquiry', (_message.Message,), {
  'DESCRIPTOR' : _INQUIRY,
  '__module__' : 'DealService_pb2'
  # @@protoc_insertion_point(class_scope:Inquiry)
  })
_sym_db.RegisterMessage(Inquiry)

Accuse = _reflection.GeneratedProtocolMessageType('Accuse', (_message.Message,), {
  'DESCRIPTOR' : _ACCUSE,
  '__module__' : 'DealService_pb2'
  # @@protoc_insertion_point(class_scope:Accuse)
  })
_sym_db.RegisterMessage(Accuse)

InquiryWithAnswer = _reflection.GeneratedProtocolMessageType('InquiryWithAnswer', (_message.Message,), {
  'DESCRIPTOR' : _INQUIRYWITHANSWER,
  '__module__' : 'DealService_pb2'
  # @@protoc_insertion_point(class_scope:InquiryWithAnswer)
  })
_sym_db.RegisterMessage(InquiryWithAnswer)

InquiryResponse = _reflection.GeneratedProtocolMessageType('InquiryResponse', (_message.Message,), {
  'DESCRIPTOR' : _INQUIRYRESPONSE,
  '__module__' : 'DealService_pb2'
  # @@protoc_insertion_point(class_scope:InquiryResponse)
  })
_sym_db.RegisterMessage(InquiryResponse)

LookUpInquiryResponse = _reflection.GeneratedProtocolMessageType('LookUpInquiryResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOOKUPINQUIRYRESPONSE,
  '__module__' : 'DealService_pb2'
  # @@protoc_insertion_point(class_scope:LookUpInquiryResponse)
  })
_sym_db.RegisterMessage(LookUpInquiryResponse)

AccuseResponse = _reflection.GeneratedProtocolMessageType('AccuseResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCUSERESPONSE,
  '__module__' : 'DealService_pb2'
  # @@protoc_insertion_point(class_scope:AccuseResponse)
  })
_sym_db.RegisterMessage(AccuseResponse)



_DEALSERVICE = _descriptor.ServiceDescriptor(
  name='DealService',
  full_name='DealService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=840,
  serialized_end=991,
  methods=[
  _descriptor.MethodDescriptor(
    name='Inquiry',
    full_name='DealService.Inquiry',
    index=0,
    containing_service=None,
    input_type=_INQUIRYREQUEST,
    output_type=_INQUIRYRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='LookUpInquiry',
    full_name='DealService.LookUpInquiry',
    index=1,
    containing_service=None,
    input_type=Empty__pb2._EMPTY,
    output_type=_LOOKUPINQUIRYRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Accuse',
    full_name='DealService.Accuse',
    index=2,
    containing_service=None,
    input_type=_ACCUSEREQUEST,
    output_type=_ACCUSERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DEALSERVICE)

DESCRIPTOR.services_by_name['DealService'] = _DEALSERVICE

# @@protoc_insertion_point(module_scope)
