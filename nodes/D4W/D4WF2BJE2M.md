---
tag: D4WF2BJE2M
kind: example
name: Iwasawa manifold
msc: [32J18, 32Q55, 53C55]
instance_of: [JSGWAN2RJV]
uses: [ZZYCV5EX9J, 0K5W69AC0J, BTYF5Y5PFY, 43NRBE72C6, X60JG9AEQJ, 0ZV14XRNF0]
sources:
  - url: https://en.wikipedia.org/wiki/Iwasawa_manifold
same_as:
  wikidata: Q6100709
  wikipedia: Iwasawa manifold
---

## Example

Let $G$ be the complex [[Heisenberg group|ZZYCV5EX9J]] of matrices
$$\begin{pmatrix} 1 & x & z \\ 0 & 1 & y \\ 0 & 0 & 1 \end{pmatrix}, \qquad x, y, z \in \C,$$
a complex Lie group isomorphic to $\C^3$ as a complex manifold.
Let $\Gamma \subset G$ be the subgroup of matrices with $x, y, z$ in the [[Gaussian integers|0K5W69AC0J]] $\Z[i]$.
The *Iwasawa manifold* is the quotient $X = \Gamma \backslash G$ of $G$ by the left action of $\Gamma$.
It is a compact [[complex manifold|JSGWAN2RJV]] of dimension $3$: $\Gamma$ is a discrete cocompact subgroup, a [[lattice|BTYF5Y5PFY]] of $G$, and acts freely by holomorphic maps.

Check that $X$ is not [[Kähler|X60JG9AEQJ]].
Left multiplication by the matrix with entries $(a, b, c)$ sends $(x, y, z)$ to $(x + a, \, y + b, \, z + a y + c)$.
So the holomorphic $1$-forms $dx$, $dy$ and $\theta = dz - x\, dy$ are invariant: $d(z + ay + c) - (x + a)\, d(y + b) = dz - x\, dy$.
They descend to holomorphic $1$-forms on $X$.
But $d\theta = -dx \wedge dy \ne 0$, so $\theta$ is not [[closed|0ZV14XRNF0]].
On a compact Kähler manifold every holomorphic form is closed, so $X$ is not Kähler.

## Remarks

$X$ is a [[nilmanifold|43NRBE72C6]] and a fibre bundle over the complex torus $\C^2 / \Z[i]^2$, via $(x, y, z) \mapsto (x, y)$, with fibre the elliptic curve $\C / \Z[i]$.
Its holomorphic tangent bundle is trivial, spanned by the left-invariant vector fields dual to $dx, dy, \theta$, so $X$ is a compact complex parallelizable manifold.
Its first Betti number is $4$, an even number, so non-Kählerness is not visible from $b_1$ here.

## Explanations

### L1 human

The Iwasawa manifold is made from $3 \times 3$ upper triangular complex matrices with ones on the diagonal.
Two matrices count as the same when they differ by one with Gaussian integer entries.
It is a compact complex manifold of dimension $3$ with three independent holomorphic vector fields at each point.
It has a holomorphic $1$-form whose derivative is not zero, which cannot happen on a compact Kähler manifold.
So it is a basic example of a compact complex manifold that is not Kähler, even though its Betti numbers look normal.
