---
tag: F1CGWAW74E
kind: definition
name: Stalk
msc: [54B40, 14F06]
defines: JTAKAPTT8H
uses: [TB6TM6R4MD, 0CQHFPGJ45, 02BH3MCBQB, VZXF7RNFKS, MZ02BKPHJA, 0G8VEZ3WTK]
sources:
  - url: https://en.wikipedia.org/wiki/Stalk_(sheaf)
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]], let $\mathcal F$ be a presheaf or a [[sheaf|TB6TM6R4MD]] of sets on $X$, and let $x \in X$.
Consider pairs $(U, s)$ where $U$ is an [[open set|02BH3MCBQB]] containing $x$ and $s \in \mathcal F(U)$.
Two pairs $(U, s)$ and $(V, t)$ are equivalent if there is an open set $W$ with $x \in W \subseteq U \cap V$ and $s|_W = t|_W$.
The *stalk* of $\mathcal F$ at $x$ is the set $\mathcal F_x$ of equivalence classes.
The class of $(U, s)$ is the *germ* of $s$ at $x$, written $s_x$.

## Remarks

The relation is an [[equivalence relation|0G8VEZ3WTK]]: for transitivity, intersect the two open sets $W$.
In the language of categories, $\mathcal F_x$ is the direct limit of the sets $\mathcal F(U)$ over the open neighbourhoods $U$ of $x$, ordered by reverse inclusion.
If $\mathcal F$ is a sheaf of abelian groups or of rings, then each stalk is an abelian group or a ring, with $s_x + t_x = (s|_W + t|_W)_x$ for $W$ a common neighbourhood.

Example: for the sheaf of continuous real functions on $\R$, the stalk at $0$ is the ring of [[germs|VZXF7RNFKS]] of continuous functions at $0$.
It is a [[local ring|MZ02BKPHJA]]: the germs with $f(0) \ne 0$ are units, since $1/f$ is continuous near $0$, and the other germs form the unique maximal ideal.

Example: for the sheaf of holomorphic functions on $\C$, the stalk at $0$ is the ring of power series $\sum a_n z^n$ with positive radius of convergence.

Non-example: a germ is not a function value.
The functions $0$ and $x \mapsto \max(x, 0)$ have the same value at $0$, but they have different germs at $0$, since they differ on every interval around $0$.

For a sheaf, a section $s \in \mathcal F(U)$ is determined by its germs $s_x$ for $x \in U$, by the locality condition.
