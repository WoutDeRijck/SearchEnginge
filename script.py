# Group 43; Tuytte Victor; De Rijck Wout

from bktree import BKTree
from redblacktree import RedBlackTree
from project import QueryProcessor, Dataset
from ranker import Ranker
from metrics import levenshtein_distance_DP

# Process data
Qp = QueryProcessor()
dataset = Dataset("Brooklyn_Public_Library_Catalog.csv", Qp)
dataset.load()

# Build RBtree
RB_tree = RedBlackTree()
for token, id_ in dataset.get_token_bookids():
    RB_tree.insert(token, id_)

# Build BKtree
BK_tree = BKTree(levenshtein_distance_DP)
for word in dataset.get_dictionary():
    BK_tree.insert(word.lower())

# Build Ranker
Ranker = Ranker(dataset, Qp, RB_tree, BK_tree)

