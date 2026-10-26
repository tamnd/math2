---
tag: 0H8Q4MANBD
kind: statement
role: lemma
name: Every finite tree with at least two vertices has a leaf
msc: [05C05]
uses: [0T0F6CCS9W, 0MJ0JS72DZ]
sources:
  - url: https://en.wikipedia.org/wiki/Tree_(graph_theory)
    locator: Properties
---

## Statement

Let $T$ be a finite [[tree|0MJ0JS72DZ]] with at least two vertices.
Then $T$ has a vertex of [[degree|0T0F6CCS9W]] $1$.

## Remarks

In fact $T$ has at least two leaves: the two ends of a longest path are leaves.
Proof idea: take a longest path $v_0, \dots, v_k$. A neighbour of $v_k$ other than $v_{k-1}$ would extend the path or close a cycle, so $\deg(v_k) = 1$.
The lemma is the base of induction proofs on trees, as in the proof that [[a tree on n vertices has n − 1 edges|0VSNHTHK8T]].

## Explanations

### L1 human

A finite tree with at least one edge always has an end point.
Walk along the tree as far as you can without going back. You stop at a vertex with only one edge.
