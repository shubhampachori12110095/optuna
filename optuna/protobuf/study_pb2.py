# flake8: noqa
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: study.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import pruners_pb2 as pruners__pb2
import samplers_pb2 as samplers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='study.proto',
  package='optuna.study',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0bstudy.proto\x12\x0coptuna.study\x1a\rpruners.proto\x1a\x0esamplers.proto\"\xb8\x01\n\x12\x43reateStudyOptions\x12\x12\n\nstudy_name\x18\x01 \x01(\t\x12)\n\x07sampler\x18\x02 \x01(\x0b\x32\x18.optuna.samplers.Sampler\x12&\n\x06pruner\x18\x03 \x01(\x0b\x32\x16.optuna.pruners.Pruner\x12\x0f\n\x07storage\x18\x04 \x01(\t\x12*\n\tdirection\x18\x05 \x01(\x0e\x32\x17.optuna.study.Direction\"$\n\rStudyInstance\x12\x13\n\x0binstance_id\x18\x01 \x01(\x04*\'\n\tDirection\x12\x0c\n\x08MINIMIZE\x10\x00\x12\x0c\n\x08MAXIMIZE\x10\x01\x32R\n\x05Study\x12I\n\x06\x63reate\x12 .optuna.study.CreateStudyOptions\x1a\x1b.optuna.study.StudyInstance\"\x00\x62\x06proto3')
  ,
  dependencies=[pruners__pb2.DESCRIPTOR,samplers__pb2.DESCRIPTOR,])

_DIRECTION = _descriptor.EnumDescriptor(
  name='Direction',
  full_name='optuna.study.Direction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MINIMIZE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAXIMIZE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=285,
  serialized_end=324,
)
_sym_db.RegisterEnumDescriptor(_DIRECTION)

Direction = enum_type_wrapper.EnumTypeWrapper(_DIRECTION)
MINIMIZE = 0
MAXIMIZE = 1



_CREATESTUDYOPTIONS = _descriptor.Descriptor(
  name='CreateStudyOptions',
  full_name='optuna.study.CreateStudyOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='study_name', full_name='optuna.study.CreateStudyOptions.study_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sampler', full_name='optuna.study.CreateStudyOptions.sampler', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pruner', full_name='optuna.study.CreateStudyOptions.pruner', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='storage', full_name='optuna.study.CreateStudyOptions.storage', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='direction', full_name='optuna.study.CreateStudyOptions.direction', index=4,
      number=5, type=14, cpp_type=8, label=1,
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
  serialized_start=61,
  serialized_end=245,
)


_STUDYINSTANCE = _descriptor.Descriptor(
  name='StudyInstance',
  full_name='optuna.study.StudyInstance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_id', full_name='optuna.study.StudyInstance.instance_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
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
  serialized_start=247,
  serialized_end=283,
)

_CREATESTUDYOPTIONS.fields_by_name['sampler'].message_type = samplers__pb2._SAMPLER
_CREATESTUDYOPTIONS.fields_by_name['pruner'].message_type = pruners__pb2._PRUNER
_CREATESTUDYOPTIONS.fields_by_name['direction'].enum_type = _DIRECTION
DESCRIPTOR.message_types_by_name['CreateStudyOptions'] = _CREATESTUDYOPTIONS
DESCRIPTOR.message_types_by_name['StudyInstance'] = _STUDYINSTANCE
DESCRIPTOR.enum_types_by_name['Direction'] = _DIRECTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateStudyOptions = _reflection.GeneratedProtocolMessageType('CreateStudyOptions', (_message.Message,), dict(
  DESCRIPTOR = _CREATESTUDYOPTIONS,
  __module__ = 'study_pb2'
  # @@protoc_insertion_point(class_scope:optuna.study.CreateStudyOptions)
  ))
_sym_db.RegisterMessage(CreateStudyOptions)

StudyInstance = _reflection.GeneratedProtocolMessageType('StudyInstance', (_message.Message,), dict(
  DESCRIPTOR = _STUDYINSTANCE,
  __module__ = 'study_pb2'
  # @@protoc_insertion_point(class_scope:optuna.study.StudyInstance)
  ))
_sym_db.RegisterMessage(StudyInstance)



_STUDY = _descriptor.ServiceDescriptor(
  name='Study',
  full_name='optuna.study.Study',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=326,
  serialized_end=408,
  methods=[
  _descriptor.MethodDescriptor(
    name='create',
    full_name='optuna.study.Study.create',
    index=0,
    containing_service=None,
    input_type=_CREATESTUDYOPTIONS,
    output_type=_STUDYINSTANCE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_STUDY)

DESCRIPTOR.services_by_name['Study'] = _STUDY

# @@protoc_insertion_point(module_scope)