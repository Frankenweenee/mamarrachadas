
class Carro:
    def __init__(self, request): 
        self.request=request
        self.session=request.session
        carro=self.session.get('carro')
        if not carro: # si no hay pedido...
            carro=self.session['carro']={} #lo creamos como un diccionario vacio
        self.carro=carro
        

    def agregar(self, articulo):
        if(str(articulo.id)not in self.carro.keys()):
            self.carro[articulo.id]={
                "id_articulo":articulo.id,
                "articulo":articulo.articulo,
                "precio":str(articulo.precio),
                "cantidad":1,
            }
        else:
            for key, value in self.carro.items():
                if key == str(articulo.id):
                    value["cantidad"] = value["cantidad"]+1
                    value["precio"] = float(value["precio"])+articulo.precio
                    break
        self.guardar_pedido()

    def guardar_pedido(self):
        self.session["carro"]=self.carro
        self.session.modified=True
    
    def eliminar_articulo(self,articulo):
        articulo.id=str(articulo.id)
        if articulo.id in self.carro:
            del self.carro[articulo.id]
            self.guardar_pedido()

    def restar_articulo(self, articulo):
        for key, value in self.carro.items():
            if key == str(articulo.id):
                value["cantidad"] = value["cantidad"]-1
                value["precio"] = float(value["precio"])-articulo.precio
                if value["cantidad"]<1:
                    self.eliminar_articulo(articulo)
                break
        self.guardar_pedido()
    
    def limpiar_pedido(self):
        self.session["pedido"]={}
        self.session.modified = True
