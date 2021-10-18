from bktree import BKTree
from redblacktree import RedBlackTree
from project import QueryProcessor, Dataset
from ranker import Ranker
from metrics import levenshtein_distance_DP
from datetime import datetime
import random

print(datetime.now().time())
# Process data
Qp = QueryProcessor()
dataset = Dataset("Brooklyn_Public_Library_Catalog.csv", Qp)
dataset.load()
print('Loading Complete: ')
print(datetime.now().time())

# Build RBtree
RBtree = RedBlackTree()
for token, id_ in dataset.get_token_bookids():
    RBtree.insert(token, id_)
print('RBtree has been build with '+str(RBtree._count)+' nodes:')
print(datetime.now().time())

# Build BKtree
BKtree = BKTree(levenshtein_distance_DP)
for word in dataset.get_dictionary():
    BKtree.insert(word.lower())
 
print('BKtree has been build with '+str(BKtree._count)+' nodes:')
print(datetime.now().time())

# Build Ranker
Ranker = Ranker(dataset, Qp, RBtree, BKtree)

# Test ranker
ev1 = Ranker.evaluate('12 angry men (Motion picture)";"12 angry men [videorecording] / United Artists   story and screenplay, Reginald Rose   producers, Henry Fonda, Reginald Rose   director, Sidney Lumet.')
ev2 = Ranker.evaluate('Sketches and studies in Italy and Greece.')
ev3 = Ranker.evaluate('Symposium on high-voltage cable insulation, presented under the joint sponsorship of the Insulated Conductors Committee of the American Institute of Electrical Engineers and Committee D-27 on Electrical Insulating Liquids and Gases of the American Society for Testing and Materials, New York, N. Y., November 18, 1959.')
ev4 = Ranker.evaluate('test')
ev5 = Ranker.evaluate('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua')

print('Testing ranker: \n')
print(ev1)
print('\n')
print(ev2)
print('\n')
print(ev3)
print('\n')
print(ev4)
print('\n')
print(ev5)
