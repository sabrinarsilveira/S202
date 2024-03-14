from database import Database
from helper.writeAJson import writeAJson

class ProductAnalyzer:
    def __init__(self, database: Database):
        self.database = database

    def vendastotaldia(self):

        result = self.database.collection.aggregate([

            {"$unwind": "$produtos"},
            {"$group": {"_id": "$data_compra", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
    
])
        writeAJson(result, "Vendas total por dia")


    def produtomaisvendido(self):
        
        result = self.database.collection.aggregate([

            {"$unwind": "$produtos"},
            {"$group": {"_id": {"compra_id": "$_id", "produto_descricao": "$produtos.descricao"},"total_vendido": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total_vendido": -1}},
])
        
        writeAJson(result, "Produto mais vendido em todas as compras")


    def clientemaisgastou(self):

        result = self.database.collection.aggregate([

             {"$unwind": "$produtos"},
             {"$group": {
                "_id": {"cliente_id": "$cliente_id", "data_compra": "$data_compra"},
                "total_gasto": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}
            }},
            {"$limit": 1},


])
        
        writeAJson(result, "Cliente que mais gastou em uma unica compra")
    

    def produtosmaisde1(self):

        result = self.database.collection.aggregate([
        
             {"$unwind": "$produtos"},
             {"$match": {"produtos.quantidade": {"$gt": 1}}},
             {"$group": {
                "_id": "$produtos.descricao",
                "quantidade_total_vendida": {"$sum": "$produtos.quantidade"}
            }},

])
        
        writeAJson(result, "Produtos que venderam mais de 1")

       


    

db = Database("mercado", "compras")
mercado = ProductAnalyzer(db)


mercado.vendastotaldia()

mercado.produtomaisvendido()

mercado.clientemaisgastou()

mercado.produtosmaisde1()
