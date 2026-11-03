---
tag: J9HJT3XRFM
kind: definition
name: Tanner graph
msc: [94B05, 94B35]
defines: GTDMNAMPD9
uses: [Y4JB44WWFG, 0ZVQKTRKVQ, 0ZXZ82FTX2]
sources:
  - url: https://en.wikipedia.org/wiki/Tanner_graph
---

## Definition

Let $\F_q$ be a [[finite field|0ZXZ82FTX2]] and let $H = (h_{ij})$ be an $m \times n$ matrix over $\F_q$, a [[parity-check matrix|Y4JB44WWFG]] of the code $C = \set{x \in \F_q^n : H x^T = 0}$.
The *Tanner graph* of $H$ is the [[bipartite graph|0ZVQKTRKVQ]] with vertex set $\set{v_1, \dots, v_n} \cup \set{c_1, \dots, c_m}$ and an edge between $v_j$ and $c_i$ exactly when $h_{ij} \ne 0$.
The $v_j$ are the *variable nodes* and the $c_i$ are the *check nodes*.

## Remarks

A word $x \in \F_q^n$ lies in $C$ if and only if, for each check node $c_i$, the sum $\sum_j h_{ij} x_j$ over its neighbours $v_j$ is $0$.
The degree of $v_j$ is the number of nonzero entries in column $j$, and the degree of $c_i$ is the number of nonzero entries in row $i$.
The graph depends on $H$, not only on $C$: two parity-check matrices of one code can give different Tanner graphs.

Example: the $[7, 4, 3]$ binary [[Hamming code|D68NF1S2NW]] with
$$H = \begin{pmatrix} 1 & 0 & 1 & 0 & 1 & 0 & 1 \\ 0 & 1 & 1 & 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 1 & 1 & 1 & 1 \end{pmatrix}$$
has a Tanner graph with $7$ variable nodes, $3$ check nodes of degree $4$ and $12$ edges.
The node $v_7$ has degree $3$, and $v_3, v_5, v_6$ have degree $2$.

Non-example: a graph with an edge between two variable nodes is not a Tanner graph, since edges only join a variable node to a check node.
