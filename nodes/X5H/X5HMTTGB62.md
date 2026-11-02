---
tag: X5HMTTGB62
kind: statement
role: theorem
name: Milnor fibre is a bouquet of spheres
msc: [32S55, 32S25, 32S50]
uses: [VTGYEES3VS, KTFG1S2SMG, 1ZE51P7GRQ, XZG6MTSWCN, 5JSWM1HBX2, P9CM4GQ2T0]
about: [KTFG1S2SMG, 1ZE51P7GRQ]
sources:
  - url: https://en.wikipedia.org/wiki/Milnor_map
---

## Statement

Let $n \ge 1$ and let $f$ be a holomorphic function near $0$ in $\C^{n+1}$ with an [[isolated singularity|VTGYEES3VS]] at $0$.
Let $F$ be its Milnor fibre, the fibre of the [[Milnor fibration|KTFG1S2SMG]] of $f$ at $0$.
Let $\mu$ be the [[Milnor number|1ZE51P7GRQ]] of $f$ at $0$.
Then $F$ is [[homotopy equivalent|XZG6MTSWCN]] to a [[wedge sum|5JSWM1HBX2]] of $\mu$ copies of the [[sphere|P9CM4GQ2T0]] $S^n$.

## Remarks

The proof has three steps.
Morse theory shows that $F$ has the homotopy type of a finite CW complex of dimension at most $n$.
Milnor shows that, for an isolated singularity, $F$ is $(n-1)$-connected.
A finite CW complex of dimension $n$ that is $(n-1)$-connected is homotopy equivalent to a wedge of $n$-spheres.
For $n \ge 2$ this follows from the Hurewicz and Whitehead theorems, and for $n = 1$ a connected graph is homotopy equivalent to a wedge of circles.
The number of spheres is the rank of $H_n(F; \Z)$, which Milnor identifies with $\mu$ through the degree of the gradient map.

Example: for $f = z_0^2 + \cdots + z_n^2$, $\mu = 1$, and the fibre $\set{z_0^2 + \cdots + z_n^2 = \delta}$ near $0$ is homotopy equivalent to the single sphere $\set{x \in \R^{n+1} : x_0^2 + \cdots + x_n^2 = \delta}$ for $\delta > 0$.

The hypothesis that the singularity is isolated is needed.
For $f(z_0, z_1, z_2) = z_0 z_1$ on $\C^3$, the Milnor fibre is homotopy equivalent to a circle, not to a wedge of $2$-spheres.

## Explanations

### L1 human

The Milnor fibre is a smooth model of a singular hypersurface near its singular point.
The theorem says that, up to continuous deformation, this model is just a bunch of spheres of the middle dimension glued at one point.
The number of spheres is the Milnor number, which can be computed by algebra.

### L2 human

The theorem shows that the reduced homology of the Milnor fibre is concentrated in degree $n$ and is free of rank $\mu$.
So the monodromy of the [[Milnor fibration|KTFG1S2SMG]] is described by a single $\mu \times \mu$ integer matrix, and the intersection form on $H_n(F; \Z)$ is a $\mu \times \mu$ integer form.
A basis of $H_n(F; \Z)$ can be chosen of [[vanishing cycles|M5EK9AKXNR]], one for each nondegenerate critical point of a generic perturbation of $f$.
This is the setting of [[Picard–Lefschetz theory|FFYQAVT7MB]].
