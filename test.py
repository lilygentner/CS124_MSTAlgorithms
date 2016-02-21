import pandas as pd

from Graph import *
from Prim import *
from minPQ import *


n_to_test = [2**n for n in range(15,17)]

def tr_len(S):
	x = sum([r[1] for r in S])
	return x


nGraph_tests = []
for n in n_to_test:
	results = [prim(nGraph(n)) for _ in range(4)]
	lengths = [tree_len(r) for r in results]
	nGraph_tests.append(np.mean(lengths))

results_df = pd.DataFrame(nGraph_tests, index = n_to_test)
print results_df


for d in range(2,5):
	d_test = []
	for n in n_to_test:
		results = [prim(uGraph(n, d)) for _ in range(4)]
		lengths = [tree_len(r) for r in results]
		d_test.append(np.mean(lengths))
	col_name = "uGraph_"+str(d)
	results_df[col_name] = d_test


print results_df


results_df.to_csv('MST2.csv')


