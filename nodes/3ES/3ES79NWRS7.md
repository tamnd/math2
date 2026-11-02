---
tag: 3ES79NWRS7
kind: statement
role: theorem
name: Vector fields on spheres
msc: [57R25, 55R25]
uses: [T62369RFH6, WY6K3P4YCG]
about: [T62369RFH6, WY6K3P4YCG]
sources:
  - url: https://en.wikipedia.org/wiki/Vector_fields_on_spheres
same_as:
  wikidata: Q7917824
  wikipedia: Vector fields on spheres
---

## Statement

Let $n \ge 1$ and write $n = 2^{4a + b} m$ with $m$ odd, $a \ge 0$ and $0 \le b \le 3$.
Let $\rho(n) = 2^b + 8a$, the Radon–Hurwitz number of $n$.
Then the largest number of continuous tangent vector fields on the [[sphere|T62369RFH6]] $S^{n-1}$ that are linearly independent at every point is $\rho(n) - 1$.

## Remarks

The lower bound is a construction from Radon and Hurwitz: $\rho(n) - 1$ linear maps $A_i$ of $\R^n$ such that the fields $x \mapsto A_i x$ on $S^{n-1}$ are pointwise independent.
These maps come from modules over Clifford algebras.
The upper bound was proved by J. F. Adams in 1962 using topological K-theory and Adams operations on real projective spaces.

Example: for $n$ odd, $\rho(n) = 1$, so an even-dimensional sphere $S^{n-1}$ has no nowhere-zero vector field; this is the [[hairy ball theorem|Z49RAKVCWG]].
For $n = 4$, $\rho(4) = 4$, and $S^3$ has $3$ independent fields, given by multiplication by the quaternions $i$, $j$ and $k$.
For $n = 16 = 2^{4}$, $a = 1$ and $b = 0$, so $\rho(16) = 9$ and $S^{15}$ has $8$ independent fields but not $9$.

As a consequence, the [[tangent bundle|WY6K3P4YCG]] of $S^{n-1}$ is trivial, that is, $S^{n-1}$ is parallelizable, exactly when $\rho(n) = n$, which happens for $n = 1, 2, 4, 8$: the spheres $S^0$, $S^1$, $S^3$ and $S^7$.

## Explanations

### L1 human

A vector field on a sphere attaches an arrow tangent to the sphere at each point, varying continuously.
One can ask how many such fields one can choose so that at every point the arrows point in genuinely different directions.
The answer depends on how often $2$ divides $n$, in a precise pattern with period $8$.
For the ordinary sphere in space the answer is zero: every field vanishes somewhere.

### L2 human

The problem is equivalent to asking for sections of the Stiefel bundle $V_{k+1}(\R^n) \to S^{n-1}$.
Adams' proof of the upper bound works with real projective spaces and computes their real K-theory $\widetilde{KO}(\R P^m)$ together with the Adams operations on it.
The theorem is closely related to the Hopf invariant one problem and to the classification of normed division algebras over $\R$, which also singles out the dimensions $1, 2, 4, 8$.
