---
tag: 7G7CSM2NZ9
kind: statement
role: theorem
name: Kodaira embedding theorem
msc: [32Q40, 32J25]
uses: [JSGWAN2RJV, QAC7BYK9KX, J45KWFHENP, ZT9A6JK8QF]
about: [J45KWFHENP, JSGWAN2RJV]
sources:
  - url: https://en.wikipedia.org/wiki/Kodaira_embedding_theorem
same_as:
  wikidata: Q6425088
  wikipedia: Kodaira embedding theorem
---

## Statement

Let $X$ be a compact [[complex manifold|JSGWAN2RJV]] and let $L$ be a [[holomorphic line bundle|QAC7BYK9KX]] on $X$.
Suppose that $L$ is [[positive|J45KWFHENP]]: it has a Hermitian metric whose Chern curvature form $\frac{i}{2\pi}\Theta$ is a positive $(1,1)$-form.
Then there is an integer $k_0$ with the following property.
For every $k \ge k_0$, the holomorphic sections of $L^{\otimes k}$ define a holomorphic embedding of $X$ into a complex [[projective space|ZT9A6JK8QF]] $\mathbb{CP}^N$.
In particular, $X$ is projective.

## Remarks

Proof idea: choose a basis $s_0, \ldots, s_N$ of the space of holomorphic sections of $L^{\otimes k}$ and consider $x \mapsto [s_0(x) : \cdots : s_N(x)]$.
This is an embedding as soon as the sections separate points and tangent vectors.
To get sections with prescribed values at one or two points, one blows up these points.
Then the [[Kodaira vanishing theorem|NY77DQ2AX8]] on the blow-up kills the obstruction in $H^1$; for large $k$ the needed positivity holds.

Equivalent form: a compact complex manifold is projective if and only if it has a [[Kähler|X60JG9AEQJ]] form $\omega$ with a rational cohomology class.
Rational means that $[\omega]$ lies in the image of $H^2(X; \Q)$; after scaling, one may take it integral.
Such $X$ are called Hodge manifolds.
Then $L$ is the line bundle with first Chern class $[\omega]$.
By [[Chow's theorem|6EFEG5VJEF]], $X$ is then the zero set of homogeneous polynomials in $\mathbb{CP}^N$.

Example: on $\mathbb{CP}^n$ the hyperplane bundle $\mathcal{O}(1)$ is positive, with the Fubini–Study metric, and already $k = 1$ gives the identity embedding.

The positivity hypothesis cannot be dropped.
A generic complex torus $\C^2 / \Lambda$ is Kähler, but its Kähler classes are not rational.
It has no positive line bundle and it is not projective; it even has no nonconstant meromorphic functions.

## Explanations

### L1 human

The theorem gives a test for when a compact complex manifold can be described by polynomial equations in projective space.
The test is the existence of a line bundle with positive curvature.
If there is one, high powers of it have enough holomorphic sections to serve as projective coordinates and to embed the manifold.

### L2 human

The theorem is the bridge between complex differential geometry and algebraic geometry: a curvature condition implies an algebraic conclusion.
Combined with the theory of Kähler manifolds it says that projective manifolds are exactly the compact Kähler manifolds with an integral Kähler class.
A positive line bundle is thus [[ample|RRK8P6TXG2]], and the converse also holds.
It shows, for instance, that every compact Riemann surface is a projective algebraic curve.
Via the Riemann bilinear relations, it also tells which complex tori are abelian varieties.
