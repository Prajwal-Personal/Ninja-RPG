class Tilemap:
    def __init__(self,tileSize = 16):
        self.tileSize = tileSize
        self.tileMap = {}
        self.offGrid = []

        for i in range(10):
            self.tileMap[str(3+i)+";10"] = {
                "type" : "grass",
                "variant" : 1,
                "position" : (3+i,10)
            }
            self.tileMap["10;" + str(5+i)] = {
                "type" : "stone",
                "variant" : 1,
                "position" : (10,5+i)
            } 