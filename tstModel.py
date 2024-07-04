from database.DAO import DAO
from model.model import Model
myLinee = DAO.getAllLinee()
mymodel = Model()
mymodel.buildGraph()
print(f"The graph has {mymodel.getNumNodes()} nodes and {mymodel.getNumEdges()} edges.")
