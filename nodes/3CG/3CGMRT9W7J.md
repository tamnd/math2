---
tag: 3CGMRT9W7J
kind: statement
role: theorem
name: Milnor fibration theorem
msc: [32S55, 58K10, 14B05]
uses: [CX4M8K61AB, 0YTCMFB4HC, 5JSWM1HBX2, P9CM4GQ2T0]
about: [0YTCMFB4HC]
sources:
  - url: https://en.wikipedia.org/wiki/Milnor_map
retired:
  date: 2026-11-03
  reason: duplicate
  successor: [KTFG1S2SMG]
  note: "The polynomial case of KTFG1S2SMG, which states the theorem for a holomorphic germ."
---

## Statement

Let $f \colon \C^{n+1} \to \C$ be a nonconstant polynomial with $f(0) = 0$, where $n \ge 0$.
For $\varepsilon > 0$ let $S_\varepsilon$ be the [[sphere|P9CM4GQ2T0]] of radius $\varepsilon$ about $0$ in $\C^{n+1}$, and let $K = f^{-1}(0) \cap S_\varepsilon$.

1. For all sufficiently small $\varepsilon > 0$, the map
$$\phi = \frac{f}{\abs{f}} \colon S_\varepsilon \setminus K \to S^1$$
is a smooth locally trivial [[fibration|CX4M8K61AB]].
2. Suppose moreover that $0$ is an isolated [[critical point|0YTCMFB4HC]] of $f$, with Milnor number
$$\mu = \dim_\C \C\{z_0, \ldots, z_n\} \big/ \left( \frac{\partial f}{\partial z_0}, \ldots, \frac{\partial f}{\partial z_n} \right).$$
Then each fibre of $\phi$ has the homotopy type of a [[wedge|5JSWM1HBX2]] of $\mu$ spheres of dimension $n$.

## Remarks

The fibration is the Milnor fibration, its fibre is the Milnor fibre, and $K$ is the link of the singularity.
In the isolated case $K$ is a smooth manifold of real dimension $2n - 1$, and Milnor showed that it is $(n-2)$-connected.
Example: for $f = z_0^2 + z_1^3$ with $n = 1$, the link $K$ in $S^3$ is the trefoil knot, and $\mu = 1 \cdot 2 = 2$.
The Milnor fibre is a punctured torus, which has the homotopy type of a wedge of two circles.
For $f = z_0^2 + z_1^2$ the link is the Hopf link and the fibre is an annulus, homotopic to one circle, in agreement with $\mu = 1$.
The theorem holds equally for germs of holomorphic functions at $0$.
Milnor proved it in his book *Singular points of complex hypersurfaces*; the proof uses a curve selection lemma from real algebraic geometry.

## Explanations

### L1 human

Take a complex polynomial with a singular point at the origin and look at it on a tiny sphere around that point.
The zero set cuts the sphere in a knot or link, such as the trefoil for $z_0^2 + z_1^3$.
The rest of the sphere is swept out by a circle's worth of pieces, one for each argument of $f$.
All of them have the same shape, and all are bounded by the link.
The theorem says that these pieces are as simple as possible up to homotopy: each is a bouquet of spheres, as many as the Milnor number.

### L2 human

The Milnor fibration is the basic topological structure attached to an isolated hypersurface singularity.
The monodromy of the fibration acts on the middle homology of the fibre, a free abelian group of rank $\mu$.
Its eigenvalues and the Seifert form carry much of the topology of the singularity.
For $n = 1$ the link is an algebraic knot or link in $S^3$, and the fibre is a Seifert surface, so plane curve singularities give fibred links.
The Milnor number appearing in the theorem is also the dimension of the local algebra used in [[finite determinacy|EGPP69XA4F]] and the classification of [[simple critical points|M5437FP73G]].
