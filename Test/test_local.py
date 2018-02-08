from unittest import TestCase
from Framework.Constants import COMMAND_NOT_EXECUTABLE,COMMAND_GO,DIRECTION_NOT_PERMITED,DIRECTION_NOT_VALID
from Framework.Controller import Controller
from Framework.Exceptions import DirectionNotFoundException,LocalAlreadyImplementException
from Framework.Local import Local
from Framework.Actor import Player
from Framework.World import World

__author__ = 'Thadeu Jose'


class TestLocal(TestCase):
  def setUp(self):
    self.controller = Controller(World(),Player())
    self.local = Local('Teste','Teste',self.controller)
    self.local1 = Local('Teste1','Teste',self.controller)
    self.local.addLocal('North',self.local1)

  def test_addLocal_DirectionNotFoundException(self):
    with self.assertRaises(DirectionNotFoundException):
      self.local.addLocal("AS",self.local1)

  def test_addLocal_LocalAlreadyImplementException(self):
    with self.assertRaises(LocalAlreadyImplementException):
      self.local.addLocal("North",self.local1)

  def test_addLocal_sucessful(self):
    self.assertEqual(self.local1.getLocal('South'),self.local)

  def test_getLocal_DIRECTION_NOT_VALID(self):
    self.assertEqual(self.local.getLocal('As'),DIRECTION_NOT_VALID)

  def test_getLocal_DIRECTION_NOT_PERMITED(self):
    self.assertEqual(self.local.getLocal('South'),DIRECTION_NOT_PERMITED)

  def test_getLocal_sucessful(self):
    self.assertEqual(self.local.getLocal('North'),self.local1)

  def test_exec_COMMAND_NOT_EXECUTABLE(self):
    self.assertEqual(self.local.execute('QualquerCoisa', 'QualquerCoisa'), COMMAND_NOT_EXECUTABLE)

  def test_exec_sucessful(self):
    self.assertEqual(self.local.execute(COMMAND_GO, ['North']), 'Teste1\nTeste')

