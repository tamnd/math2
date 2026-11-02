---
tag: 4BEWKR0EG7
kind: statement
role: theorem
name: Mostow rigidity theorem
msc: [53C24, "22E40", 57K32]
uses: [7CBT4SM83Y, 1X42JAA349, S1XK3HXHFX, 08MG7H8JW5, 02HPP5VCZH]
about: [S1XK3HXHFX]
sources:
  - url: https://en.wikipedia.org/wiki/Mostow_rigidity_theorem
same_as:
  wikidata: Q3984063
  wikipedia: Mostow rigidity theorem
---

## Statement

Let $n \ge 3$, and let $M$ and $N$ be closed connected hyperbolic $n$-manifolds.
That is, they are compact connected [[Riemannian manifolds|7CBT4SM83Y]] without boundary, complete, with constant [[sectional curvature|1X42JAA349]] $-1$.
Let $\phi \colon \pi_1(M) \to \pi_1(N)$ be an [[isomorphism|08MG7H8JW5]] of [[fundamental groups|S1XK3HXHFX]].
Then there is a unique [[isometry|02HPP5VCZH]] $f \colon M \to N$ that induces $\phi$, up to the choice of base points.

## Remarks

Here is the idea of Mostow's proof.
A homotopy equivalence $M \to N$ inducing $\phi$ lifts to a quasi-isometry of the universal covers, both equal to hyperbolic space $\mathbb{H}^n$.
This quasi-isometry extends to a quasiconformal homeomorphism of the sphere at infinity $S^{n-1}$, equivariant for the two actions of $\pi_1$.
Ergodicity of the action of $\pi_1(M)$ on $S^{n-1}$ forces this map to be conformal, so it comes from an isometry of $\mathbb{H}^n$.

Consequence: the volume of a closed hyperbolic manifold of dimension at least $3$ depends only on its fundamental group.
So the volume is a topological invariant.

The hypothesis $n \ge 3$ is necessary.
For a closed orientable surface of genus $g \ge 2$, the hyperbolic metrics, up to isometries isotopic to the identity, form the Teichmüller space of real dimension $6g - 6$.
Its quotient by the mapping class group still has positive dimension, so two hyperbolic surfaces of genus $g$ need not be isometric.

The theorem extends to complete hyperbolic manifolds of finite volume, by work of Marden for $n = 3$ and of Prasad in general.

## Explanations

### L1 human

A hyperbolic manifold is a space that looks everywhere like the hyperbolic plane or its higher-dimensional analogues.
The fundamental group records how loops in the space can be deformed.
In dimension $3$ and higher, Mostow proved that this purely topological information determines the whole geometry.
So the shape and the size of such a manifold cannot be changed without changing its topology.

### L2 human

In the language of Lie groups, the theorem says the following.
Two cocompact lattices in $\mathrm{SO}(n, 1)$, $n \ge 3$, that are isomorphic as abstract groups are conjugate in the isometry group of $\mathbb{H}^n$.
Mostow extended it to irreducible cocompact lattices in semisimple Lie groups not locally isomorphic to $\mathrm{SL}_2(\R)$.
In higher rank, the [[Margulis superrigidity theorem|DSKV65NHZZ]] gives a much stronger form.
By contrast, surfaces have flexible moduli, which leads to Teichmüller theory.
