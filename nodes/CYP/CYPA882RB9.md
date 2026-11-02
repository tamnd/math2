---
tag: CYPA882RB9
kind: object
name: Grassmannian
msc: [14M15]
instance_of: [A4H4CZ2V35]
uses: [A4H4CZ2V35, ZT9A6JK8QF, 00YC1D652K, 0MDMZ965VE, 36X2WTHYCB, RF8WD9TSE7]
sources:
  - url: https://en.wikipedia.org/wiki/Grassmannian
same_as:
  wikidata: Q129638
  wikipedia: Grassmannian
---

## Description

Let $F$ be a field and let $0 \le r \le n$ be integers.
The *Grassmannian* $\operatorname{Gr}(r, n)$ is the set of $r$-dimensional [[linear subspaces|00YC1D652K]] of $F^n$.

The Plücker embedding makes it a subset of a [[projective space|ZT9A6JK8QF]].
Let $\bigwedge^r F^n$ be the $r$-th exterior power, a part of the [[exterior algebra|0MDMZ965VE]], of dimension $\binom{n}{r}$.
A subspace $W$ with basis $w_1, \dots, w_r$ is sent to
$$W \mapsto [w_1 \wedge \cdots \wedge w_r] \in \mathbb{P}\left(\bigwedge\nolimits^r F^n\right) \cong \mathbb{P}^{\binom{n}{r} - 1}.$$
A change of basis multiplies $w_1 \wedge \cdots \wedge w_r$ by the determinant of the change of basis matrix, so the point is well defined.
The map is injective, since $W = \set{v \in F^n : v \wedge w_1 \wedge \cdots \wedge w_r = 0}$.
The coordinates of the image are the Plücker coordinates $p_I$, the $r \times r$ minors of the $r \times n$ matrix with rows $w_1, \dots, w_r$.

## Remarks

When $F$ is algebraically closed, the image is the zero set of quadratic equations, the Plücker relations, and it is a [[projective variety|A4H4CZ2V35]] of [[dimension|36X2WTHYCB]] $r(n - r)$.

For $r = 1$, $\operatorname{Gr}(1, n) = \mathbb{P}^{n-1}$.
For $r = 2$ and $n = 4$, the Grassmannian of lines in $\mathbb{P}^3$ is the quadric hypersurface
$$p_{12} p_{34} - p_{13} p_{24} + p_{14} p_{23} = 0$$
in $\mathbb{P}^5$, of dimension $4 = 2 \cdot (4 - 2)$.

Over $\R$ or $\C$, Grassmannians are also compact manifolds, and infinite Grassmannians are [[classifying spaces for vector bundles|RF8WD9TSE7]].

## Explanations

### L1 human

The Grassmannian is a space whose points are planes, or more generally subspaces of a fixed dimension, inside a bigger space.
The lines through the origin of $F^n$ form projective space, so the Grassmannian generalises projective space.
To give it coordinates, take a basis of the subspace, write it as the rows of a matrix, and record all the maximal minors of that matrix.
Changing the basis multiplies all minors by the same number, so the minors give a well-defined point of projective space.
