---
tag: KTFG1S2SMG
kind: statement
role: theorem
name: Milnor fibration theorem
msc: [32S55, 32S05, 57R45]
uses: [507C34W0ZT, P9CM4GQ2T0, CX4M8K61AB, C831AN3RFM]
about: [VTGYEES3VS, C831AN3RFM]
sources:
  - url: https://en.wikipedia.org/wiki/Milnor_map
same_as:
  wikidata: Q6860249
  wikipedia: Milnor map
---

## Statement

Let $f \colon U \to \C$ be a [[holomorphic function|507C34W0ZT]] on an open neighbourhood $U$ of $0$ in $\C^{n+1}$, with $f(0) = 0$ and $f$ not identically zero.
For $\varepsilon > 0$, let $S_\varepsilon$ be the [[sphere|P9CM4GQ2T0]] of radius $\varepsilon$ about $0$ and let $K_\varepsilon = S_\varepsilon \cap f^{-1}(0)$, the [[link|C831AN3RFM]] of $f^{-1}(0)$ at $0$.
Then there is $\varepsilon_0 > 0$ such that, for every $0 < \varepsilon \le \varepsilon_0$:

1. the map $\phi = f / \abs{f} \colon S_\varepsilon \setminus K_\varepsilon \to S^1$ is a smooth locally trivial [[fibre bundle|CX4M8K61AB]];
2. each fibre $F_\theta = \phi^{-1}(e^{i\theta})$ is a smooth manifold of real dimension $2n$, called the *Milnor fibre* of $f$ at $0$.

## Remarks

Milnor proved this in his 1968 book on singular points of complex hypersurfaces.
The proof shows, with the curve selection lemma, that for small $\varepsilon$ the map $\phi$ has no critical points on $S_\varepsilon \setminus K_\varepsilon$.
One then builds a vector field on $S_\varepsilon \setminus K_\varepsilon$ that $\phi$ sends to the unit tangent field of $S^1$ and that is controlled near $K_\varepsilon$.
Its flow carries each fibre onto the others.
An equivalent form, used often, is the fibration $f \colon B_\varepsilon \cap f^{-1}(\partial D_\delta) \to \partial D_\delta$, where $B_\varepsilon$ is the closed ball and $D_\delta$ a disc of radius $0 < \delta \ll \varepsilon$.

Example: for $f(z_0, z_1) = z_0 z_1$ on $\C^2$, the link is a pair of circles forming a Hopf link in $S^3$.
The fibre in the tube form is $\set{z_0 z_1 = \delta} \cap B_\varepsilon$, an annulus, which has the homotopy type of a circle.

The radius must be small.
On a large sphere, $f^{-1}(0)$ may meet the sphere non-transversally or other critical points of $f$ may intervene, and the conclusion can fail.

## Explanations

### L1 human

Take a hypersurface with a singular point and look at it through a small sphere around that point.
Away from the hypersurface, the argument of $f$ is an angle, so it gives a map from the rest of the sphere to the circle.
Milnor's theorem says that this map is a fibration: all its fibres look the same.
The sphere minus the link is swept out by them as the angle turns once around the circle.
The common fibre, the Milnor fibre, is a smooth model of the hypersurface near the singular point, slightly pushed off the singular value.

### L2 human

The Milnor fibration is the starting point of the topology of hypersurface singularities.
Its fibre carries the [[Milnor number|1ZE51P7GRQ]], and for an isolated singularity the [[fibre is a bouquet of spheres|X5HMTTGB62]].
Going once around the circle gives a diffeomorphism of the fibre, whose action on homology is the monodromy studied in the [[monodromy theorem|DQP63REKEK]].
For plane curves, $n = 1$, the link is a link in $S^3$ and the Milnor fibre is a Seifert surface of it, which connects singularity theory with knot theory.
