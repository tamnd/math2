---
tag: CQ4C1WKMF6
kind: definition
name: Combinatorial design
msc: [05B05, 05B30]
defines: PAJTMQ604P
uses: [070R982G4B, 4JCSS2Z1BA]
sources:
  - url: https://en.wikipedia.org/wiki/Combinatorial_design
---

## Definition

Let $t, v, k, \lambda$ be positive integers with $t \le k \le v$.
Let $X$ be a [[finite set|070R982G4B]], whose elements are called points.
Let $\mathcal{B}$ be a finite family of subsets of $X$, called blocks, with repetitions allowed.
The pair $(X, \mathcal{B})$ is a *$t$-$(v, k, \lambda)$ design* if:

1. $\abs{X} = v$.
2. Every block has exactly $k$ points.
3. Every subset of $X$ with $t$ points is contained in exactly $\lambda$ blocks.

A *combinatorial design* in the usual sense is a $t$-design of this kind.
More broadly, the term covers any finite set with a family of subsets that satisfies a prescribed balance condition of this sort.

## Remarks

A $2$-$(v, k, \lambda)$ design is a balanced incomplete [[block design|4JCSS2Z1BA]], and a $t$-$(v, k, 1)$ design is a [[Steiner system|7BPSC4T4M3]] $S(t, k, v)$.
Counting gives the number of blocks: $\abs{\mathcal{B}} = \lambda \binom{v}{t} / \binom{k}{t}$.

Example: $X = \set{1, \dots, 7}$ with blocks $\set{1,2,4}$, $\set{2,3,5}$, $\set{3,4,6}$, $\set{4,5,7}$, $\set{5,6,1}$, $\set{6,7,2}$, $\set{7,1,3}$ is a $2$-$(7, 3, 1)$ design, the Fano plane.
The blocks are the translates of $\set{1, 2, 4}$ modulo $7$, whose pairwise differences $\pm 1, \pm 2, \pm 3$ cover each nonzero residue exactly once, so every pair of points lies in exactly one block.

Non-example: $X = \set{1, 2, 3, 4}$ with blocks $\set{1, 2}$ and $\set{3, 4}$ is not a $2$-$(4, 2, 1)$ design, because the pair $\set{1, 3}$ lies in no block.
