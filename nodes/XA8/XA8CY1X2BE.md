---
tag: XA8CY1X2BE
kind: definition
name: Matrix Lie group
msc: ["22E15", "22E60"]
defines: 36KSZ7GA5S
uses: [0FCHE902D7, 0X1JXT47GA, 0ZCK8DQYN1, 3NJGY8QSTE, 020M04FN1H]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_group
---

## Definition

Let $n \ge 1$ and let $GL_n(\C)$ be the [[general linear group|0FCHE902D7]] of invertible complex $n \times n$ matrices, with the topology of $\C^{n^2}$.
A *matrix Lie group* is a [[subgroup|0X1JXT47GA]] $G$ of $GL_n(\C)$ that is a [[closed subset|0ZCK8DQYN1]] of $GL_n(\C)$.
That is, if $A_k \in G$ and $A_k \to A$ entrywise with $A \in GL_n(\C)$, then $A \in G$.

## Remarks

Example: $SL_n(\R) = \set{A \in GL_n(\C) : A \text{ real}, \det A = 1}$ is a subgroup, and it is closed because the entries being real and $\det$ being $1$ are conditions preserved under limits, as $\det$ is continuous.

Non-example: let $\alpha$ be irrational and $G = \set{\operatorname{diag}(e^{it}, e^{i\alpha t}) : t \in \R}$.
It is a subgroup of $GL_2(\C)$, but it is not closed: its closure is the set of all $\operatorname{diag}(e^{i\theta}, e^{i\varphi})$, which contains $\operatorname{diag}(1, -1) \notin G$.

The condition is closedness in $GL_n(\C)$, not in the space of all matrices: $GL_n(\C)$ itself is a matrix Lie group.
Closed subgroups of $GL_n(\R)$ are matrix Lie groups too.
By the [[closed subgroup theorem|3NJGY8QSTE]], a matrix Lie group is an embedded Lie subgroup of $GL_n(\C)$.
Its Lie algebra is $\mathfrak{g} = \set{X \in M_n(\C) : e^{tX} \in G \text{ for all } t \in \R}$, with the [[matrix exponential|020M04FN1H]] and the bracket $[X, Y] = XY - YX$.
