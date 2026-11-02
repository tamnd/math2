---
tag: AP4A0GX0V2
kind: statement
role: theorem
name: Eells–Sampson theorem
msc: ["58E20", 53C43, 35K55]
uses: [7CBT4SM83Y, 1X42JAA349, KZJYG9DS3M, MD99PYBCE6, 9YA6S6HD9V]
about: [KZJYG9DS3M, MD99PYBCE6]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_map
---

## Statement

Let $(M, g)$ and $(N, h)$ be compact [[Riemannian manifolds|7CBT4SM83Y]] without boundary, and assume that $N$ has nonpositive [[sectional curvature|1X42JAA349]].
Let $u_0 \colon M \to N$ be a smooth map.
Then the [[harmonic map heat flow|MD99PYBCE6]] with initial map $u_0$ has a smooth solution $u$ on $M \times [0, \infty)$.
There is a sequence $t_k \to \infty$ such that $u(\cdot, t_k)$ converges smoothly to a [[harmonic map|KZJYG9DS3M]] $u_\infty \colon M \to N$, and $u_\infty$ is [[homotopic|9YA6S6HD9V]] to $u_0$.
In particular, every continuous map from $M$ to $N$ is homotopic to a harmonic map.

## Remarks

The key estimate is a Bochner formula for the energy density $e = \frac{1}{2} \abs{du}^2$ along the flow: $(\partial_t - \Delta_g) e \le C e$, where $C$ depends on a lower bound for the Ricci curvature of $M$.
The curvature term of $N$ enters with a sign that helps because the sectional curvature of $N$ is nonpositive.
Together with the decrease of the energy, this gives uniform bounds on $e$, hence on all derivatives by parabolic regularity, so the flow cannot blow up.
Since $\int_0^\infty \int_M \abs{\tau(u)}^2 \, dV_g \, dt \le E(u_0)$, the tension tends to zero along a sequence of times, and compactness gives the harmonic limit.

Example: for $M = S^1$ with its standard metric, harmonic maps are closed geodesics parametrized proportionally to arc length, or constant maps.
So the theorem shows that every free homotopy class of loops in a compact manifold of nonpositive curvature contains a closed geodesic or a constant loop.

The curvature hypothesis cannot be dropped: Eells and Wood showed that, for any metrics, there is no harmonic map of degree $\pm 1$ from a $2$-torus to a $2$-sphere.

## Explanations

### L1 human

Take a map into a space that is curved like a saddle everywhere.
The theorem says that it can be relaxed, by continuously lowering its energy, into a harmonic map, the best possible map in its class.
The relaxing process is a heat flow for maps.
Nonpositive curvature of the target prevents the map from tearing or concentrating energy at a point.

### L2 human

This was the first general existence theorem for harmonic maps, and it introduced the heat flow method into geometry.
Hartman later showed that the whole flow converges, not only a sequence, and proved uniqueness results for harmonic maps in a homotopy class under negative curvature.
Without the curvature condition, the flow can form singularities in finite or infinite time, and two-dimensional domains show bubbling of harmonic spheres.
Harmonic maps from this theorem are a basic tool in rigidity theory, for example in proofs of Mostow-type rigidity and in non-abelian Hodge theory.
