---
tag: TCF1PXZ5YN
kind: definition
name: Upper nilradical
msc: [16N40]
defines: 3G2JQEYBEK
uses: [0894J980RK, 0DDA6CY7GJ, NZ1G9WRWFB]
sources:
  - url: https://en.wikipedia.org/wiki/Nilradical_of_a_ring
---

## Definition

Let $R$ be a [[ring|0894J980RK]].
The *upper nilradical* $\operatorname{Nil}^*(R)$ of $R$ is the sum of all [[nil ideals|NZ1G9WRWFB]] of $R$.
These are the [[two-sided ideals|0DDA6CY7GJ]] $I$ of $R$ such that every element of $I$ is nilpotent.

## Remarks

The sum of two nil ideals $I$ and $I'$ is nil, since $(I + I')/I' \cong I/(I \cap I')$ is nil and $I'$ is nil.
Hence $\operatorname{Nil}^*(R)$ is itself a nil ideal, and it is the largest nil ideal of $R$.
Example: in $\Z/12\Z$ the nil ideals are $0$ and $6\Z/12\Z$, so $\operatorname{Nil}^*(\Z/12\Z) = \set{0, 6}$.
Non-example: in $M_2(\Q)$ the element $e_{12}$ is nilpotent but does not lie in $\operatorname{Nil}^*(M_2(\Q))$.
Indeed the only ideals of $M_2(\Q)$ are $0$ and the whole ring, which contains $1$, so $\operatorname{Nil}^*(M_2(\Q)) = 0$.
In general $\operatorname{Nil}_*(R) \subseteq \operatorname{L}(R) \subseteq \operatorname{Nil}^*(R)$, where $\operatorname{Nil}_*$ is the [[prime radical|WF117EJ2HF]] and $\operatorname{L}$ the [[Levitzki radical|9DD8M9R868]], and both inclusions can be strict.
For a commutative ring the upper nilradical is the [[nilradical|QQDN6EYQNJ]].
