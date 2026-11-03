---
tag: GXYN4CQF0Y
kind: definition
name: Maximum parsimony
msc: [92B10, 92D15]
defines: 59450K6JK8
uses: [5624H8KWKK]
sources:
  - url: https://en.wikipedia.org/wiki/Maximum_parsimony
---

## Definition

Let $X$ be a finite set of taxa and $C$ a finite set of states.
A *character* is a map $\chi \colon X \to C$.
Let $T$ be an unrooted [[phylogenetic tree|5624H8KWKK]] on $X$ with vertex set $V$ and edge set $E$, and identify each leaf with its taxon.

1. An *extension* of $\chi$ to $T$ is a map $\bar\chi \colon V \to C$ that agrees with $\chi$ on the leaves.
2. The *parsimony score* of $\chi$ on $T$ is $l(\chi, T) = \min_{\bar\chi} \abs{\set{\set{u, v} \in E : \bar\chi(u) \ne \bar\chi(v)}}$, the minimum over all extensions.
3. For a sequence of characters $\chi_1, \dots, \chi_m$, the parsimony score of $T$ is $l(T) = \sum_{k=1}^m l(\chi_k, T)$.

A *maximum parsimony tree* is a phylogenetic tree on $X$ that minimises $l(T)$; maximum parsimony is the method that outputs such trees.

## Remarks

Example: let $X = \set{a, b, c, d}$ and $\chi = (0, 0, 1, 1)$ on $(a, b, c, d)$.
On the binary tree $ab|cd$, which joins $a, b$ to one internal vertex $u$ and $c, d$ to another vertex $v$, the extension with $\bar\chi(u) = 0$, $\bar\chi(v) = 1$ has one change, so $l = 1$.
On the tree $ac|bd$ each internal vertex is adjacent to leaves with different states, so every extension has at least two changes, and $l = 2$.
Non-example: counting changes for one fixed extension, such as the one with all internal states $0$, is not the parsimony score, since clause 2 takes the minimum over extensions.
For a fixed tree $l(\chi, T)$ is computed in linear time by the Fitch algorithm for binary trees or the Sankoff algorithm with weights; minimising over all trees is NP-hard.
