---
tag: PXXEWA9V2S
kind: statement
role: theorem
name: Koecher–Vinberg theorem
msc: [17C36, 17C20, 52A20]
uses: [N184N4TVZ2, NZMXY4WTZX, 0QVNCJXRY3]
about: [NZMXY4WTZX, N184N4TVZ2]
sources:
  - url: https://en.wikipedia.org/wiki/Koecher%E2%80%93Vinberg_theorem
same_as:
  wikidata: Q6425525
  wikipedia: Koecher–Vinberg theorem
---

## Statement

Let $V$ be a finite-dimensional real vector space.

1. Let $V$ carry the structure of a [[Euclidean Jordan algebra|N184N4TVZ2]], with an [[inner product|0QVNCJXRY3]] $\ip{\cdot}{\cdot}$ such that $\ip{xy}{z} = \ip{y}{xz}$ for all $x, y, z \in V$. Then the interior $\Omega$ of the set of squares $\set{x^2 : x \in V}$ is a [[symmetric cone|NZMXY4WTZX]] in $V$ for this inner product.
2. Conversely, let $V$ carry an inner product and let $\Omega \subseteq V$ be a symmetric cone. Then there is a Jordan product on $V$ that makes $V$ a Euclidean Jordan algebra whose interior of the set of squares is $\Omega$.

## Remarks

For the first part, one shows that $\Omega$ is the set of $x$ whose spectral values are all positive.
Then one shows that the quadratic representations $P(a) = 2L(a)^2 - L(a^2)$ for $a \in \Omega$ preserve $\Omega$ and act transitively on it.
For the converse, one fixes a point $e \in \Omega$ and builds the Jordan product from the derivatives at $e$ of the characteristic function of the cone; $e$ becomes the unit.
Example: take the Jordan algebra of real symmetric $n \times n$ matrices with $A \circ B = \tfrac12(AB + BA)$ and $\ip{A}{B} = \tr(AB)$.
There the squares are the positive semidefinite matrices, and the symmetric cone is the cone of positive definite matrices.
The classification of simple Euclidean Jordan algebras gives five families of irreducible symmetric cones.
They are the Lorentz cones, the cones of positive definite Hermitian matrices over $\R$, $\C$ and the quaternions, and one $27$-dimensional cone.
That cone consists of the positive definite $3 \times 3$ Hermitian octonion matrices.

## Explanations

### L1 human

The theorem says that two different-looking objects are the same thing.
A symmetric cone is a geometric object: a cone that is its own dual and looks the same at every point.
A Euclidean Jordan algebra is an algebraic object: a commutative product with a positivity property.
Every such algebra gives a symmetric cone, the interior of its squares, and every symmetric cone comes from such an algebra.

### L2 human

The correspondence lets one translate questions about cones into algebra.
Eigenvalues, traces and determinants of a Euclidean Jordan algebra give barrier functions and spectral decompositions on the cone, which is the basis of interior point methods for symmetric cone programming.
Together with the Jordan–von Neumann–Wigner classification it gives the full list of symmetric cones as products of five irreducible types.
Every symmetric cone is in particular a homogeneous cone, but there are homogeneous cones that are not self-dual, and Vinberg studied those as well.
