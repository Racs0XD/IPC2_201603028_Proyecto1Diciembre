#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------- Clases --------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------- Artista --------------------------------------------------------
class NodeArtista:
    def __init__(self,artista):
        self.artistaA = artista 
        self.albumA = ListaDobleAlbum()  
        
#------------------------------------------------------- Album --------------------------------------------------------
class NodeAlbum:
    def __init__(self,album,imagen):
        self.albumB = album
        self.imagenB = imagen
        self.cancionB = ListaDobleCancion()
#------------------------------------------------------- Cancion --------------------------------------------------------
class NodeCancion:
    def __init__(self,nombre, ruta):
        self.nombreC = nombre
        self.rutaC = ruta

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------- Listas --------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------ Artista --------------------------------------------------------
class ListaDobleArtista:    
    def __init__(self):
        self.inicioArtista = None
        self.finalArtista = None                    
    
    def listarArtista(self, artista):  
        nuevoArtista = NodeArtista(artista)
        if self.inicioArtista is None:            
            self.inicioArtista = nuevoArtista
            self.finalArtista = self.inicioArtista
        else:            
            n = self.finalArtista  
            n.siguiente= nuevoArtista
            self.finalArtista = n.siguiente
            self.finalArtista.anterior = n
    
    def mostrarArtista(self):
            n = self.inicioArtista
            while n is not None:                
                yield n
                n = n.siguiente

                
#------------------------------------------------------- Album --------------------------------------------------------
class ListaDobleAlbum:
    def __init__(self):
        self.inicioAlbum = None    
        self.finalAlbum = None 
        
    def listarAlbum(self,album):        
        nuevoAlbum = NodeAlbum(album)     
        if self.inicioAlbum is None:            
            self.inicioAlbum = nuevoAlbum
            self.finalAlbum = self.inicioAlbum
        else:            
            m = self.finalAlbum  
            m.siguiente= nuevoAlbum
            self.finalAlbum = m.siguiente
            self.finalAlbum.anterior = m

    def mostrarAlbum(self):
            m = self.inicioAlbum
            while m is not None:   
                yield m
                m = m.siguiente    
#------------------------------------------------------- Cancion --------------------------------------------------------
class ListaDobleCancion:
    def __init__(self):
        self.inicioCancion = None 
        self.finalCancion = None    

    def listarCancion(self,cancion):        
        nuevaCancion = NodeAlbum(cancion)
         
        if self.inicioCancion is None:            
            self.inicioCancion = nuevaCancion
            self.finalCancion = self.inicioCancion
        else:            
            o = self.finalCancion  
            o.siguiente = nuevaCancion
            self.finalCancion = o.siguiente
            self.finalCancion.anterior = o

    def mostrarCancion(self):
            o = self.inicioCancion
            while o is not None:                  
                yield o
                o = o.siguiente
    


