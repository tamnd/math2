---
tag: TGZATGBHTH
kind: definition
name: Block design
msc: [05B05]
defines: 4JCSS2Z1BA
uses: [0BBTH3YSZA, 05Q6G4EH2G]
sources:
  - url: https://en.wikipedia.org/wiki/Block_design
---

## Definition

Let $t, v, k, \lambda$ be positive integers with $t \le k < v$.
A $t$-$(v, k, \lambda)$ design is a pair $(X, \mathcal{B})$ such that:

1. $X$ is a [[finite set|0BBTH3YSZA]] with $v$ elements, called points.
2. $\mathcal{B}$ is a finite [[family|05Q6G4EH2G]] of subsets of $X$, called blocks, each with exactly $k$ elements.
3. Each subset of $X$ with exactly $t$ elements is contained in exactly $\lambda$ blocks.

A balanced incomplete block design, or $2$-design, is a $2$-$(v, k, \lambda)$ design.

## Remarks

The family $\mathcal{B}$ may contain a block more than once.
The design is simple if it has no repeated block.
In a $2$-$(v, k, \lambda)$ design with $b$ blocks, each point lies in the same number $r$ of blocks, and $bk = vr$ and $r(k - 1) = \lambda (v - 1)$.
Example: let $X = \set{1, \dots, 7}$ and let the blocks be $\set{1,2,3}$, $\set{1,4,5}$, $\set{1,6,7}$, $\set{2,4,6}$, $\set{2,5,7}$, $\set{3,4,7}$, $\set{3,5,6}$.
Each of the $21$ pairs of points lies in exactly one of these blocks, so this is a $2$-$(7, 3, 1)$ design, the [[Fano plane|QQ8GW1ASZM]].
Here each point lies in $r = 3$ blocks, and $b = 7$.
Non-example: on $X = \set{1, 2, 3, 4}$ the blocks $\set{1,2,3}$ and $\set{1,2,4}$ do not form a $2$-design, because the pair $\set{1,2}$ lies in two blocks and the pair $\set{3,4}$ lies in none.
A $t$-$(v, k, 1)$ design is a [[Steiner system|7BPSC4T4M3]] $S(t, k, v)$.
