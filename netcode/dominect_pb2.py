# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dominect.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x64ominect.proto\x12\x03\x64om\":\n\rGameParameter\x12\x13\n\x0b\x62oard_width\x18\x01 \x01(\r\x12\x14\n\x0c\x62oard_height\x18\x02 \x01(\r\":\n\x08GameTurn\x12\n\n\x02x1\x18\x01 \x01(\r\x12\n\n\x02y1\x18\x02 \x01(\r\x12\n\n\x02x2\x18\x03 \x01(\r\x12\n\n\x02y2\x18\x04 \x01(\r\"J\n\tGameState\x12\x13\n\x0b\x62oard_width\x18\x01 \x01(\r\x12\x14\n\x0c\x62oard_height\x18\x02 \x01(\r\x12\x12\n\nboard_data\x18\x03 \x01(\x0c\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dominect_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GAMEPARAMETER']._serialized_start=23
  _globals['_GAMEPARAMETER']._serialized_end=81
  _globals['_GAMETURN']._serialized_start=83
  _globals['_GAMETURN']._serialized_end=141
  _globals['_GAMESTATE']._serialized_start=143
  _globals['_GAMESTATE']._serialized_end=217
# @@protoc_insertion_point(module_scope)
