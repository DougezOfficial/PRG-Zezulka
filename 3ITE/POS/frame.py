import re

class PDU:

    def __init__(self, payload):
        if type(self) is PDU:
            raise TypeError("Nelze vytvořit instanci abstr. třídy PDU")
        self._payload = payload

    def getPayload(self):
        return self._payload
    
    def setPayload(self, val):
        self._payload = val 

    def isValid(self):
        raise NotImplementedError("Podtřída musí mít isValid()")

class EthFrame(PDU):
    def __init__(self, dmac, smac, type_id, payload, fcs=None):

        super().__init__(payload)

        if not self.isValidMac(dmac) or not self.isValidMac(smac):
            raise ValueError("Neplatný formát MAC")

        self._dmac = dmac
        self._smac = smac
        self._type = type_id

        if fcs is None:
            self._fcs = self.calculateFcs()
        else:
            self._fcs = fcs

    @staticmethod
    def isValidMac(mac):
        vzor = r"^([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}$"
        return bool(re.match(vzor, mac))

    def getDmac(self):
        return self._dmac

    def setDmac(self, val):
        if self.isValidMac(val):
            self._dmac = val
            self.recalculateFcs()

    def getSmac(self):
        return self._smac

    def setSmac(self, val):
        if self.isValidMac(val):
            self._smac = val
            self.recalculateFcs()

    def getType(self):
        return self._type

    def setType(self, val):
        self._type = val
        self.recalculateFcs()

    def setPayload(self, val):
        super().setPayload(val)
        self.recalculateFcs()       

    def getFcs(self):
        return self._fcs

    def calculateFcs(self):
        raw_string = f"{self._dmac}{self._smac}{self._type}{self.getPayload()}"
        return sum(ord(c) for c in raw_string)
    
    def recalculateFcs(self):
        self._fcs = self.calculateFcs()
    
    def isValid(self):
        return self._fcs == self.calculateFcs()
    
    def corruptData(self):
        self._payload = "Chyba přenosu"
        self._fcs = -1

    def __str__(self):
        return f"[EthFrame] SRC: {self._smac} DST: {self._dmac} DATA: {self.getPayload()}"

frame = EthFrame("00:11:22:AA:BB:CC", "AA:BB:CC:00:11:22", 0x0800, "testmsg")
print(f"vytvořený rámec: Validní: {frame.isValid()}")

frame.setPayload("Nova data")
print(f"po změně dat. Validní: {frame.isValid()}")

frame.corruptData()
print(f"po zničení dat. Validní: {frame.isValid()}")