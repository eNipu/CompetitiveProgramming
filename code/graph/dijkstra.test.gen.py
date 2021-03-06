# This file was *autogenerated* from the file dijkstra_fast.test.gen.sage.
from sage.all_cmdline import *   # import sage library
_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_4 = Integer(4); _sage_const_8 = Integer(8); _sage_const_0p2 = RealNumber('0.2'); _sage_const_10 = Integer(10); _sage_const_0p4 = RealNumber('0.4'); _sage_const_0p6 = RealNumber('0.6'); _sage_const_0p9 = RealNumber('0.9'); _sage_const_0p8 = RealNumber('0.8'); _sage_const_300 = Integer(300); _sage_const_0p01 = RealNumber('0.01'); _sage_const_19 = Integer(19); _sage_const_400 = Integer(400)
gs = []

gs += [
       digraphs.RandomDirectedGNP(_sage_const_10 , _sage_const_0p2 ),
       digraphs.RandomDirectedGNP(_sage_const_300 , _sage_const_0p01 ),
       digraphs.RandomDirectedGNP(_sage_const_300 , _sage_const_0p2 ),
       digraphs.RandomDirectedGNP(_sage_const_300 , _sage_const_0p4 ),
       digraphs.RandomDirectedGNP(_sage_const_300 , _sage_const_0p6 ),
       digraphs.RandomDirectedGNP(_sage_const_300 , _sage_const_0p8 ),
       digraphs.RandomDirectedGNP(_sage_const_300 , _sage_const_0p9 ),
]

gs += list(digraphs(_sage_const_1 ))
gs += list(digraphs(_sage_const_2 ))
gs += list(digraphs(_sage_const_3 ))
gs += list(digraphs(_sage_const_4 ))

gs = [
        digraphs.Circuit(_sage_const_3 ),
        digraphs.Circuit(_sage_const_10 ),
        digraphs.Circulant(_sage_const_10 , [_sage_const_2 ]),
        digraphs.Circulant(_sage_const_400 , [_sage_const_2 , _sage_const_8 , _sage_const_19 ]),
        digraphs.Path(_sage_const_1 ),
        digraphs.Path(_sage_const_10 ),
        digraphs.Path(_sage_const_300 ),
        digraphs.RandomDirectedGN(_sage_const_10 ),
        digraphs.RandomDirectedGN(_sage_const_300 ),
        digraphs.RandomDirectedGNC(_sage_const_10 ),
        digraphs.RandomDirectedGNC(_sage_const_300 ),
        digraphs.Tournament(_sage_const_10 ),
        digraphs.Tournament(_sage_const_300 ),
]

print(len(gs))
for g in gs:
    print("%d %d" % (len(g.vertices()), len(g.edges())))
    for (u,v) in g.edge_iterator(labels=None):
        w = randint(_sage_const_0 , _sage_const_300 )
        g.set_edge_label(u,v,w)
        print("%d %d %d" % (u, v, w))
    for u,d in sorted(g.shortest_path_all_pairs(by_weight=True)[_sage_const_0 ].items()):
        print ' '.join([ str(p) if p != Infinity else '-1' for v,p in sorted(d.items()) ])
