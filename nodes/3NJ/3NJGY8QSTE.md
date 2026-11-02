---
tag: 3NJGY8QSTE
kind: statement
role: theorem
name: Closed subgroup theorem
msc: ["22E15", "22E60"]
uses: [7JBRGCVJRB, 0X1JXT47GA, 0ZCK8DQYN1, NM8XCPS1Q3, H3QX1ZFC8K]
about: [NM8XCPS1Q3]
sources:
  - url: https://en.wikipedia.org/wiki/Closed-subgroup_theorem
same_as:
  wikidata: Q18206032
  wikipedia: Closed-subgroup theorem
---

## Statement

Let $G$ be a [[Lie group|7JBRGCVJRB]] with Lie algebra $\mathfrak{g}$ and [[exponential map|H3QX1ZFC8K]] $\exp$.
Let $H$ be a [[subgroup|0X1JXT47GA]] of $G$ that is a [[closed subset|0ZCK8DQYN1]] of $G$.
Then $H$ is an embedded submanifold of $G$, and with this smooth structure $H$ is an embedded [[Lie subgroup|NM8XCPS1Q3]] of $G$.
Its Lie algebra is
$$\mathfrak{h} = \set{X \in \mathfrak{g} : \exp(tX) \in H \text{ for all } t \in \R}.$$

## Remarks

The proof first shows that $\mathfrak{h}$ is a linear subspace, using the limits $\exp(X + Y) = \lim_n (\exp(X/n)\exp(Y/n))^n$ and closedness of $H$.
Then one chooses a complement $\mathfrak{m}$ of $\mathfrak{h}$ in $\mathfrak{g}$ and shows that $(Y, X) \mapsto \exp(Y)\exp(X)$ on $\mathfrak{m} \times \mathfrak{h}$ is a chart near $e$ in which $H$ is the slice $Y = 0$.
The key point is that $H$ has no elements of the form $\exp(Y)$ with small nonzero $Y \in \mathfrak{m}$; otherwise a limit argument gives a nonzero element of $\mathfrak{h} \cap \mathfrak{m}$.
Example: $SO(n) = \set{A \in GL_n(\R) : A^T A = I, \det A = 1}$ is closed, so it is a Lie group; its Lie algebra is the space of skew-symmetric matrices.
The closedness hypothesis is necessary: the image of $t \mapsto (e^{it}, e^{i\sqrt2 t})$ in the torus $S^1 \times S^1$ is a subgroup that is dense and not closed, and it is not an embedded submanifold.

## Explanations

### L1 human

To check that a group of matrices is a Lie group, one would normally need to build charts and check smoothness.
This theorem removes the work: any subgroup of a Lie group that is closed as a set is automatically a smooth submanifold and a Lie group.
So all the usual groups cut out by equations, such as orthogonal, unitary and symplectic groups, are Lie groups at once.

### L2 human

The theorem is often stated for matrix groups and attributed to von Neumann in that case and to Élie Cartan in general.
A typical use: the stabiliser $H$ of a point under a smooth action is closed, hence a Lie subgroup.
Then the quotient $G / H$ is a manifold, a homogeneous space.
The formula for $\mathfrak{h}$ is the practical way to compute Lie algebras: for $SL_n(\R)$ it gives the matrices of trace $0$, because $\det e^{tX} = e^{t \tr X}$.
It also gives Cartan's theorem that a continuous homomorphism of Lie groups is smooth, by applying it to the graph.
