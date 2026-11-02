---
tag: XK1KDMCW4K
kind: definition
name: Abelian algebra
msc: [08A30, 08B10]
defines: EHASX3TBRQ
uses: [N9M2N27END, 6DSWPHSWQW]
sources:
  - url: https://en.wikipedia.org/wiki/Universal_algebra
---

## Definition

Let $A$ be an algebra.
The algebra $A$ is *abelian* if the following holds.
For every $n \ge 1$, every $(n+1)$-ary [[term operation|N9M2N27END]] $t$ of $A$, all elements $a, b \in A$ and all tuples $\bar{c}, \bar{d} \in A^n$:
$$t(a, \bar{c}) = t(a, \bar{d}) \implies t(b, \bar{c}) = t(b, \bar{d}).$$

## Remarks

In the language of [[commutator theory|6DSWPHSWQW]], $A$ is abelian if and only if $[1_A, 1_A] = 0_A$, where $1_A$ and $0_A$ are the largest and the least congruences of $A$.
Example: every module $M$ over a ring $R$ is abelian.
Each term operation has the form $t(x, \bar{y}) = r x + s_1 y_1 + \cdots + s_n y_n$ with $r, s_i \in R$.
So $t(a, \bar{c}) = t(a, \bar{d})$ means $\sum_i s_i c_i = \sum_i s_i d_i$, and this gives $t(b, \bar{c}) = t(b, \bar{d})$ for every $b$.
Non-example: a lattice $L$ with elements $0 < 1$ is not abelian.
Take $t(x, y) = x \wedge y$, $a = 0$, $c = 0$ and $d = 1$: then $t(0, 0) = 0 = t(0, 1)$, but $t(1, 0) = 0 \ne 1 = t(1, 1)$.
A group is abelian in this sense exactly when it is commutative.

## Explanations

### L1 human

An algebra is abelian when the effect of changing some inputs of a term operation never depends on the value of another input.
