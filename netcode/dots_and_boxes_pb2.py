# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dots-and-boxes.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x64ots-and-boxes.proto\x12\x03\x64\x61\x62\"Y\n\rGameParameter\x12\"\n\x1anumber_of_vertical_columns\x18\x01 \x01(\r\x12$\n\x1cnumber_of_horizontal_columns\x18\x02 \x01(\r\"G\n\x08GameTurn\x12\x10\n\x08vertical\x18\x01 \x01(\x08\x12\x15\n\rtarget_column\x18\x02 \x01(\r\x12\x12\n\ntarget_gap\x18\x03 \x01(\r\"s\n\tGameState\x12\x18\n\x10vertical_columns\x18\x01 \x01(\r\x12\x1a\n\x12horizontal_columns\x18\x02 \x01(\r\x12\x16\n\x0evertical_lines\x18\x03 \x01(\x0c\x12\x18\n\x10horizontal_lines\x18\x04 \x01(\x0c\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dots_and_boxes_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GAMEPARAMETER']._serialized_start=29
  _globals['_GAMEPARAMETER']._serialized_end=118
  _globals['_GAMETURN']._serialized_start=120
  _globals['_GAMETURN']._serialized_end=191
  _globals['_GAMESTATE']._serialized_start=193
  _globals['_GAMESTATE']._serialized_end=308
# @@protoc_insertion_point(module_scope)
