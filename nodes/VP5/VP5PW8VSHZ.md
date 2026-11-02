---
tag: VP5PW8VSHZ
kind: object
name: Moduli space of instantons
msc: [58D27, 53C07, 57R57]
instance_of: [FJZRW9P0K3]
uses: [YWBTGC7MFA, 888SJ2508Y, 707DEWCCFX, 8H58Q6YJCH, 8E37E74XVP, PAD37GKDPD, FJZRW9P0K3]
sources:
  - url: https://en.wikipedia.org/wiki/Instanton
---

## Description

Let $X$ be a compact oriented Riemannian [[4-manifold|8H58Q6YJCH]] and $P \to X$ a [[principal|8E37E74XVP]] $SU(2)$-bundle with second [[Chern class|PAD37GKDPD]] $c_2(P) = k$.
The *moduli space of instantons* on $P$ is
$$\mathcal{M}_k = \set{A : A \text{ a connection on } P, \ F_A^+ = 0} / \mathcal{G}(P),$$
the set of anti-self-dual connections, the [[instantons|YWBTGC7MFA]], modulo the [[gauge group|707DEWCCFX]].
It is a subset of the [[space of connections modulo gauge|888SJ2508Y]].

## Remarks

The linearisation of the equation $F_A^+ = 0$, together with the Coulomb gauge condition, is an elliptic operator.
Its index, computed by the Atiyah–Singer index theorem, gives the expected dimension
$$\dim \mathcal{M}_k = 8k - 3(1 - b_1(X) + b^+(X)).$$
Here $b_1$ is the first Betti number and $b^+$ the dimension of a maximal positive subspace for the intersection form.
Near an irreducible instanton $A$ at which this linearised operator is surjective, $\mathcal{M}_k$ is a smooth manifold of this dimension.
For $X = S^4$ with its round metric and $k = 1$, the formula gives $8 - 3 = 5$.
Indeed $\mathcal{M}_1$ is a $5$-dimensional manifold, diffeomorphic to an open $5$-ball, and each of its instantons is determined by a centre in $S^4$ and a scale.


The moduli space is not compact in general: instantons can concentrate at points, and Uhlenbeck's compactness theorem describes the limits.
Donaldson used these moduli spaces to prove his theorem on definite intersection forms of smooth $4$-manifolds and to define new invariants.

## Explanations

### L1 human

Instantons are the most efficient twisted connections on a bundle over a four-dimensional space.
Counting them only up to gauge transformations, which do not change the geometry, gives the moduli space.
It is a finite-dimensional space even though connections form an infinite-dimensional space, because the instanton equation is elliptic.
Its shape carries information about the smooth structure of the underlying four-manifold.
