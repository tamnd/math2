---
tag: TPGYWSS528
kind: concept
name: Capacitated minimum spanning tree
aliases: [algorithms-for-finding-capacitated-minimum-spanning-trees, cmst]
sources:
  - wikipedia: en:23015254@r1270867004
    locator: Capacitated minimum spanning tree
    note: adopted
    mention: wikipedia://en/23015254
    sections: [Summary]
same_as:
  wikidata: Q5034477
  wikipedia: Capacitated minimum spanning tree
inventory: [PTZ3FAPH9Z]
---

## Summary

**Capacitated minimum spanning tree** is a minimal cost spanning tree of a [[graph|00C0BR7D7H]] that has a designated root node $r$ and satisfies the capacity constraint $c$. The capacity constraint ensures that all subtrees (maximal subgraphs connected to the root by a single edge) incident on the root node $r$ have no more than $c$ nodes. If the tree nodes have weights, then the capacity constraint may be interpreted as follows: the sum of weights in any subtree should be no greater than $c$. The edges connecting the subgraphs to the root node are called *gates*. Finding the optimal solution is NP-hard.
