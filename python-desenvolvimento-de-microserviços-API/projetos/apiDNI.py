import aiohttp
import asyncio
import json
# from PyQt5.QtWidgets import QLabel, QLineEdit, QDialog, QApplication, QTreeWidget, QTreeWidgetItem, QPushButton
# from ConnDB import ConnectDB

# conn = ConnectDB()


def ApiRequest():
    try:
        async def main():
            async with aiohttp.ClientSession() as session:
                data = {
                    "tipo": "produtos",
                    "filtro": "timestampupdate",
                    "data": "20230610205959"
                }

                url = 'http://192.168.1.240:84/RetrofitExample/public/consulta?cnpj=07744784000101'
                async with session.post(url, auth=aiohttp.BasicAuth('dniautocom', '1234'), json=data) as resp:
                    response = await resp.text()
                    array = json.loads(response)
                    for item in array:
                        # conn.conecta()
                        query = """
                        REPLACE INTO estoque (
                            ID, DATACAD, CODIGO, etiqueta, CODVINCULO, QTDEVINCULO, TEMPOREP, PESOLIQ, SNBAIXA,
                            UN, DESCRICAO, QTDE, MIN, ULTVEND, ULTCOMPRA, PRECOREP, ULTPRECO, PRECOMEDIO, PRECOVENDA,
                            PRECODOLAR, PRECOATACADO, IPI, ICMS, CLFISCAL, PROCEDENCI, pesaveis, DATAPROMOCAO,
                            DATAPROMOCAO2, PROMOCAO, SUBCAT2, CONTAGEM, TRIBUT, CONTROLE, VALDIAS, QTDEMB,
                            PIS, COFINS, CST, CODIGOINTERNO, VINCULOINTERNO, ATUALIZACAOINTERNA, CARTAOLOJA,
                            ICMSNORMAL, QTDEANT, SITUACAO, NATREC, ECSTPIS, ETRIBUTCOFINS, STRIBUTCOFINS,
                            ECSTCOFINS, TIPO_IVA, CFOP, CSOSN, CSTPIS, CSTCOFINS, ORIGEMCST, SBC, Comissao,
                            Oferta, ALCOOLICO, PROMOCAO_QTDE, PROMOCAO_ATIVO, CLASSIFICADO, CEST, ORIGEMMERC,
                            PRECOVENDA3, PRECO2AD, PLU, MARGEMTABELA, PROMOCAOLEVE, PROMOCAOPAGUE, PROMOCAOTIPO,
                            promocaoDataAtivacao, promocaoDataDesativacao, unEmb, ultprecomedio, promocaoDataFidelidade1,
                            promocaoDataFidelidade2, pmz, PESOBRUTO, PESOLIQUIDO, ORIGEMCAD, promocaoDataLeve1,
                            promocaoDataLeve2, GRUPOFISCAL, CESTABASICA, TIMESTAMPUPDATE
                        )
                        VALUES (
                            %(ID)s, %(DATACAD)s, %(CODIGO)s, %(etiqueta)s, %(CODVINCULO)s, %(QTDEVINCULO)s, %(TEMPOREP)s,
                            %(PESOLIQ)s, %(SNBAIXA)s, %(UN)s, %(DESCRICAO)s, %(QTDE)s, %(MIN)s, %(ULTVEND)s, %(ULTCOMPRA)s,
                            %(PRECOREP)s, %(ULTPRECO)s, %(PRECOMEDIO)s, %(PRECOVENDA)s, %(PRECODOLAR)s, %(PRECOATACADO)s,
                            %(IPI)s, %(ICMS)s, %(CLFISCAL)s, %(PROCEDENCI)s, %(pesaveis)s, %(DATAPROMOCAO)s,
                            %(DATAPROMOCAO2)s, %(PROMOCAO)s, %(SUBCAT2)s, %(CONTAGEM)s, %(TRIBUT)s, %(CONTROLE)s,
                            %(VALDIAS)s, %(QTDEMB)s, %(PIS)s, %(COFINS)s, %(CST)s, %(CODIGOINTERNO)s,
                            %(VINCULOINTERNO)s, %(ATUALIZACAOINTERNA)s, %(CARTAOLOJA)s, %(ICMSNORMAL)s, %(QTDEANT)s,
                            %(SITUACAO)s, %(NATREC)s, %(ECSTPIS)s, %(ETRIBUTCOFINS)s, %(STRIBUTCOFINS)s, %(ECSTCOFINS)s,
                            %(TIPO_IVA)s, %(CFOP)s, %(CSOSN)s, %(CSTPIS)s, %(CSTCOFINS)s, %(ORIGEMCST)s, %(SBC)s,
                            %(Comissao)s, %(Oferta)s, %(ALCOOLICO)s, %(PROMOCAO_QTDE)s, %(PROMOCAO_ATIVO)s, %(CLASSIFICADO)s,
                            %(CEST)s, %(ORIGEMMERC)s, %(PRECOVENDA3)s, %(PRECO2AD)s, %(PLU)s, %(MARGEMTABELA)s,
                            %(PROMOCAOLEVE)s, %(PROMOCAOPAGUE)s, %(PROMOCAOTIPO)s, %(promocaoDataAtivacao)s,
                            %(promocaoDataDesativacao)s, %(unEmb)s, %(ultprecomedio)s, %(promocaoDataFidelidade1)s,
                            %(promocaoDataFidelidade2)s, %(pmz)s, %(PESOBRUTO)s, %(PESOLIQUIDO)s, %(ORIGEMCAD)s,
                            %(promocaoDataLeve1)s, %(promocaoDataLeve2)s, %(GRUPOFISCAL)s, %(CESTABASICA)s, %(TIMESTAMPUPDATE)s
                        )
                        """
                        # conn.execute(query, item)

        asyncio.run(main())
    except Exception:
        pass