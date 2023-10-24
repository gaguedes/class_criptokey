import cryptocode
import base64


class dadosCriptografia:
    def __init__(self,valor,tipo):
        self.valor = valor
        self.tipo = tipo


class criptografia(dadosCriptografia):
    def __int__(self,valor,tipo):
        dadosCriptografia.__init__(self,valor,tipo)

    def encryptDecript(self):
        if self.tipo == 'criptografar':
            criptografia = cryptocode.encrypt(self.valor, "8bZ*Yj6JST8dZxPb%^npNCj^Rvh9MIxfiP1W1TKik&Iy5xmWq%")
            criptografiaBytes = criptografia.encode("ascii")
            criptografiaBase64Bytes = base64.b64encode(criptografiaBytes)
            criptografiaBase64String = criptografiaBase64Bytes.decode("ascii")
            return criptografiaBase64String

        elif self.tipo == 'descriptografar':
            valorBase64 = self.valor
            valorBase64Bytes = valorBase64.encode("ascii")

            valorBase64BytesStringBytes = base64.b64decode(valorBase64Bytes)
            retornoBase64 = valorBase64BytesStringBytes.decode("ascii")
            valorDescriptografado = cryptocode.decrypt(retornoBase64, "8bZ*Yj6JST8dZxPb%^npNCj^Rvh9MIxfiP1W1TKik&Iy5xmWq%")
            return valorDescriptografado

        else:
            return False
