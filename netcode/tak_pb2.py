# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tak.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ttak.proto\x12\x03tak\"%\n\rGameParameter\x12\x14\n\x0c\x62oard_length\x18\x01 \x01(\r\",\n\x0bPlaceAction\x12\x1d\n\x05piece\x18\x01 \x01(\x0e\x32\x0e.tak.PieceType\">\n\nMoveAction\x12!\n\tdirection\x18\x01 \x01(\x0e\x32\x0e.tak.Direction\x12\r\n\x05\x64rops\x18\x02 \x03(\r\"n\n\x08GameTurn\x12\t\n\x01x\x18\x01 \x01(\r\x12\t\n\x01y\x18\x02 \x01(\r\x12!\n\x05place\x18\x03 \x01(\x0b\x32\x10.tak.PlaceActionH\x00\x12\x1f\n\x04move\x18\x04 \x01(\x0b\x32\x0f.tak.MoveActionH\x00\x42\x08\n\x06\x41\x63tion\"B\n\x05Piece\x12\x1c\n\x04type\x18\x01 \x01(\x0e\x32\x0e.tak.PieceType\x12\x1b\n\x13second_player_owned\x18\x02 \x01(\x08\"\"\n\x04Pile\x12\x1a\n\x06pieces\x18\x01 \x03(\x0b\x32\n.tak.Piece\"r\n\tGameState\x12\x14\n\x0c\x62oard_length\x18\x01 \x01(\r\x12\x18\n\x10remaining_stones\x18\x02 \x03(\r\x12\x1b\n\x13remaining_capstones\x18\x03 \x03(\r\x12\x18\n\x05\x62oard\x18\x04 \x03(\x0b\x32\t.tak.Pile*5\n\tDirection\x12\t\n\x05NORTH\x10\x00\x12\x08\n\x04\x45\x41ST\x10\x01\x12\t\n\x05SOUTH\x10\x02\x12\x08\n\x04WEST\x10\x03*=\n\tPieceType\x12\x0e\n\nFLAT_STONE\x10\x00\x12\x12\n\x0eSTANDING_STONE\x10\x01\x12\x0c\n\x08\x43\x41PSTONE\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tak_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_DIRECTION']._serialized_start=499
  _globals['_DIRECTION']._serialized_end=552
  _globals['_PIECETYPE']._serialized_start=554
  _globals['_PIECETYPE']._serialized_end=615
  _globals['_GAMEPARAMETER']._serialized_start=18
  _globals['_GAMEPARAMETER']._serialized_end=55
  _globals['_PLACEACTION']._serialized_start=57
  _globals['_PLACEACTION']._serialized_end=101
  _globals['_MOVEACTION']._serialized_start=103
  _globals['_MOVEACTION']._serialized_end=165
  _globals['_GAMETURN']._serialized_start=167
  _globals['_GAMETURN']._serialized_end=277
  _globals['_PIECE']._serialized_start=279
  _globals['_PIECE']._serialized_end=345
  _globals['_PILE']._serialized_start=347
  _globals['_PILE']._serialized_end=381
  _globals['_GAMESTATE']._serialized_start=383
  _globals['_GAMESTATE']._serialized_end=497
# @@protoc_insertion_point(module_scope)