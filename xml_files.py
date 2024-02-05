import os
import xml.etree.cElementTree as Et
from datetime import date

class Read_xml():
    def __init__(self, directory) -> None:
        self.directory = directory

    def all_files(self):
            
            return   [ os.path.join(self.directory, arq)for arq in os.listdir(self.directory)
            if arq.lower().endswith(".xml")]
            
            
        

    def nfe_data(self, xml):
        root = Et.parse(xml).getroot()
        nsNFE = {"ns": "http://www.portalfiscal.inf.br/nfe"}
        NFe = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:nNF", nsNFE))
        serie = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:serie", nsNFE))
        data_emissao = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:ide/ns:dhEmi", nsNFE))
        chave = self.check_none(root.find("./ns:protNFe/ns:infProt/ns:chNFe", nsNFE))
        cnpj_emitente = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:CNPJ", nsNFE))
        nome_emitente = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:emit/ns:xNome", nsNFE))
        cnpj_emitente = self.format_cnpj(cnpj_emitente)
        valorNFe = self.check_none(root.find("./ns:NFe/ns:infNFe/ns:total/ns:ICMSTot/ns:vNF", nsNFE))
        data_importacao = date.today()
        data_importacao = data_importacao.strftime('%d/%m/%y')
        data_saida = ""
        usuario = ''

        itemNota = 1
        notas = []

        for item in root.findall("./ns:NFe/ns:infNFe/ns:det", nsNFE):
            cod = self.check_none(item.find("./ns:prod/ns:cProd",nsNFE))
            qntd = self.check_none(item.find("./ns:prod/ns:qCom",nsNFE))
            descicao = self.check_none(item.find("./ns:prod/ns:xProd",nsNFE))
            unidade_medida = self.check_none(item.find("./ns:prod/ns:uCom",nsNFE))
            valorProd = self.check_none(item.find("./ns:prod/ns:vProd",nsNFE))

            dados = [NFe, serie, data_emissao, chave, cnpj_emitente, nome_emitente,
                     valorNFe,itemNota, cod, qntd, descicao, unidade_medida, valorProd,
                     data_importacao, usuario, data_saida]
            
            notas.append(dados)
            itemNota +=1
            return notas


    def check_none(self, var):
        if var == None:
            return ""
        else:
            try:
                return var.text.replace('.',',')
            except:
                return var.text

    def format_cnpj(self, cnpj):
        try:

            cnpj = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
            return cnpj
        
        except:
            return ""
        
if __name__ == "__main__":
    
    xml =  Read_xml('projeto python\\xml_files') 
    all = xml.all_files()

    for i in all:
        result = xml.nfe_data(i)

     