---
tag: 6YDMMN6M9R
kind: definition
name: Barrelled space
msc: [46A08]
defines: ZE6DXEJB8H
uses: [B6GY2KJMWW, 0ZCK8DQYN1, 02AS45T3H9, 2TDSHJJYS4, NM1BCK3ZX9, 0ZCY0Z80B6]
sources:
  - url: https://en.wikipedia.org/wiki/Barrelled_space
---

## Definition

Let $\mathbb{K}$ be $\R$ or $\C$, and let $E$ be a Hausdorff [[locally convex space|B6GY2KJMWW]] over $\mathbb{K}$.
A *barrel* in $E$ is a subset $T \subseteq E$ that is [[closed|0ZCK8DQYN1]], [[convex|02AS45T3H9]], [[balanced|2TDSHJJYS4]] and [[absorbing|NM1BCK3ZX9]].
$E$ is *barrelled* if every barrel in $E$ is a [[neighbourhood|0ZCY0Z80B6]] of $0$.

## Remarks

Some authors define barrelled spaces among all topological vector spaces, with the same condition.
Example: every Banach space $E$ is barrelled.
If $T$ is a barrel, then $E = \bigcup_{n \ge 1} nT$ since $T$ is absorbing.
By the Baire category theorem some $nT$, hence $T$, has an interior point.
Convexity and balance then give that $T$ contains a ball around $0$.
The same argument shows that every Fréchet space is barrelled.
Non-example: let $c_{00}$ be the space of finitely supported real sequences with the norm $\norm{x} = \sup_n \abs{x_n}$, and let $T = \set{x : \abs{x_n} \le 1/n \text{ for all } n}$.
$T$ is a barrel, but it is not a neighbourhood of $0$: for each $\varepsilon > 0$ the vector $\varepsilon e_n$ has norm $\varepsilon$ and lies outside $T$ once $n > 1 / \varepsilon$.
In a barrelled space, every family of continuous linear maps into a locally convex space that is bounded at each point is equicontinuous.
