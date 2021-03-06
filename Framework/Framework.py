from Framework.BaseTextObject import TextObject
from Framework.Item import Item
from Framework.Tag import Tag
from Framework.Commands import Command
from Framework.Exceptions import ClassInvalid


class Framework:

    def __init__(self,controller):
        self._controller = controller
        self._idplayer = "player"

    def getplayer(self):
        return self._controller.player

    def addcls(self, idx, cls):
        if issubclass(cls, Command):
            self._controller.factory.addnewclass(idx, cls)
        elif issubclass(cls, Tag):
            self._controller.factory.addnewtag(idx, cls)
        else:
            ClassInvalid()

    def addplayerstatus(self, idx, idstatus, valuestatus):
        if idx.lower() == self._idplayer:
            self._controller.player.setstatus(idstatus,valuestatus)

    def setstatus(self, textobject, idx, valuestatus):
        textobject.setstatus(idx,valuestatus)

    def getstatus(self,idx,idstatus):
        return idx.getstatus(idstatus)

    def getlocal(self, title):
        return self._controller.getlocal(title)

#Itens manipulations  ------------------------------------------------------------------
    def playerhas(self, idx):
        return self._controller.hasitem(idx)

    def createitem(self,name,description, statusdic=None):
        item = Item(name,description)
        if statusdic:
            for k, v in statusdic.items():
                item.addstatus(k, v)
        return item

    def additemplayer(self,name,description,statusdic=None):
        self._controller.additem(self.createitem(name,description,statusdic))

    def removeitemplayer(self, idx):
        self._controller.removeitem(idx)
#Itens manipulations  ------------------------------------------------------------------

    def createtextobject(self,name,description, statusdic=None):
        obj = TextObject(name,description)
        for k, v in statusdic.items():
            obj.setstatus( k, v)
        return obj

    def addlocal(self, local, idx, object):
        if isinstance(object, TextObject):
            local.setstatus( idx, object)
        else:
            self._controller.addcommand(local, idx, object)

    def gettextobject(self, local, idx):
        return local.getstatus(idx)