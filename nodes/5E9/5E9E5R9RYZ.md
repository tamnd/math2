---
tag: 5E9E5R9RYZ
kind: example
name: Brieskorn manifold
msc: [32S55, 57R60, 32S25]
instance_of: [C831AN3RFM]
uses: [VTGYEES3VS, 1ZE51P7GRQ, 6WYEMXSHD9, NHERCK7C43]
sources:
  - url: https://en.wikipedia.org/wiki/Brieskorn_manifold
same_as:
  wikidata: Q4967112
  wikipedia: Brieskorn manifold
---

## Example

Let $n \ge 1$ and let $a_0, \dots, a_n \ge 2$ be integers.
The *Brieskorn manifold* is
$$\Sigma(a_0, \dots, a_n) = \set{z \in \C^{n+1} : z_0^{a_0} + z_1^{a_1} + \cdots + z_n^{a_n} = 0} \cap S^{2n+1},$$
where $S^{2n+1}$ is the unit sphere in $\C^{n+1}$.
It is the [[link|C831AN3RFM]] at $0$ of the hypersurface $f^{-1}(0)$, where $f = z_0^{a_0} + \cdots + z_n^{a_n}$.

Check: the partial derivatives of $f$ are $a_j z_j^{a_j - 1}$, which vanish together only at $z = 0$.
So $f$ has an [[isolated singularity|VTGYEES3VS]] at $0$ and $f^{-1}(0)$ is smooth away from $0$.
Since $f$ is weighted homogeneous, the sphere of radius $1$ gives the same link as any small sphere.
So $\Sigma(a_0, \dots, a_n)$ is a smooth closed manifold of dimension $2n - 1$.
The [[Milnor number|1ZE51P7GRQ]] of $f$ is $(a_0 - 1)(a_1 - 1) \cdots (a_n - 1)$, because the monomials $z_0^{b_0} \cdots z_n^{b_n}$ with $0 \le b_j \le a_j - 2$ form a basis of the local algebra.

## Remarks

$\Sigma(2, 3, 5)$ is the [[Poincaré homology sphere|NHERCK7C43]], a $3$-manifold with the homology of $S^3$ but a nontrivial fundamental group of order $120$.
For $n = 1$, $\Sigma(p, q)$ is the torus link of type $(p, q)$ in $S^3$, a knot when $p$ and $q$ are coprime.
Brieskorn showed that the $7$-manifolds $\Sigma(6k - 1, 3, 2, 2, 2)$ for $k = 1, \dots, 28$ are homeomorphic to $S^7$ and realize the $28$ oriented diffeomorphism classes of [[exotic spheres|6WYEMXSHD9]] of dimension $7$.

## Explanations

### L1 human

Brieskorn manifolds come from the simplest polynomials one can write: sums of powers of the variables.
Cut the zero set of such a polynomial with the unit sphere, and the result is a smooth manifold.
Changing the exponents changes the manifold in a computable way.
Some choices give spheres that are equal to the usual sphere as topological spaces but not as smooth manifolds.
