---
tag: 2KKXVKFN16
kind: example
name: Invasion percolation
msc: [82B43, 60K35]
illustrates: [BH7YPXCYDK]
uses: [BH7YPXCYDK, MP8VSZK19A, ZAKCAS4GC7, 0JW7KT6PQW, FVJ624HTV0]
sources:
  - url: https://en.wikipedia.org/wiki/Invasion_percolation
same_as:
  wikidata: Q24902133
  wikipedia: Invasion percolation
---

## Example

Let $G = (V, E)$ be an infinite connected graph with finite degrees, and let $o \in V$.
Give each edge $e$ an independent weight $U(e)$, uniform on $[0, 1]$; almost surely all weights are distinct.
*Invasion percolation* from $o$ builds clusters $I_0 \subset I_1 \subset \cdots$.
Start with $I_0 = \set{o}$.
Given $I_n$, choose the edge of smallest weight among the edges with exactly one endpoint in $I_n$.
Let $I_{n+1}$ be $I_n$ together with the other endpoint of that edge.
The *invasion cluster* is $I_\infty = \bigcup_n I_n$.

Check on $G = \Z$ with $o = 0$ and weights $U(\set{-2, -1}) = 0.2$, $U(\set{-1, 0}) = 0.7$, $U(\set{0, 1}) = 0.4$, $U(\set{1, 2}) = 0.9$.
Step 1 compares $0.7$ and $0.4$ and adds the vertex $1$.
Step 2 compares $0.7$ and $0.9$ and adds $-1$.
Step 3 compares $0.2$ and $0.9$ and adds $-2$.
After crossing the high weight $0.7$, the invasion at once uses the low weight $0.2$ behind it.

## Remarks

The rule is the same as Prim's algorithm for a [[minimum spanning tree|0JW7KT6PQW]], run on an infinite graph from $o$; see [[Prim's algorithm|ZAKCAS4GC7]].
For $p \in [0, 1]$, the edges with $U(e) \le p$ form [[bond percolation|BH7YPXCYDK]] with parameter $p$, so the model couples all values of $p$ at once.
Let $d \ge 2$, and let $p$ be above the [[percolation threshold|MP8VSZK19A]] $p_c$ of $\Z^d$.
On $\Z^d$ the invasion eventually reaches the infinite cluster of edges with weight at most $p$.
From then on it never accepts an edge of weight larger than $p$.
So the invasion finds the critical value by itself, without any parameter being tuned, and its cluster looks like a large critical percolation cluster.
This makes it a standard example of [[self-organized criticality|FVJ624HTV0]].

## Explanations

### L1 human

Water is pushed slowly into a porous rock filled with oil.
At each moment it enters the one pore next to it that is easiest to enter.
The pores have random resistances, given by the weights.
The water does not need any outside parameter, yet the shape it fills has the fractal look of percolation exactly at its threshold.
