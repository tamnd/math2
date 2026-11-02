---
tag: JNR9YJTT54
kind: example
name: Milnor's isospectral flat tori
msc: [58J53, 11H06, 11F11]
instance_of: [18MQEGN13R]
uses: [18MQEGN13R, B8TYKV7AA1, 03NM7DZXXC, WN9V7WSJKF, 2CXH65EKY7, GWKN5VG78A]
sources:
  - url: https://en.wikipedia.org/wiki/Isospectral
---

## Example

Let $\Gamma \subset \R^n$ be a [[lattice|WN9V7WSJKF]], and let $T_\Gamma = \R^n / \Gamma$ be the flat [[torus|03NM7DZXXC]] with the metric induced from $\R^n$.
Let $\Gamma^* = \set{v \in \R^n : \ip{v}{\gamma} \in \Z \text{ for all } \gamma \in \Gamma}$ be the dual lattice.
For each $\gamma^* \in \Gamma^*$, the function $x \mapsto e^{2\pi i \ip{\gamma^*}{x}}$ is an eigenfunction of the Laplacian with eigenvalue $4\pi^2 \abs{\gamma^*}^2$.
These functions form an orthogonal basis of $L^2(T_\Gamma)$.
So the [[spectrum|B8TYKV7AA1]] of $T_\Gamma$ is determined by the numbers $N_{\Gamma^*}(r) = \#\set{\gamma^* \in \Gamma^* : \abs{\gamma^*}^2 = r}$.

Take $n = 16$, $\Gamma_1 = E_8 \oplus E_8$, with $E_8$ the [[E8 lattice|2CXH65EKY7]], and $\Gamma_2 = D_{16}^+$.
Both are even unimodular lattices, so $\Gamma_i^* = \Gamma_i$.
The theta series $\sum_{\gamma \in \Gamma_i} q^{\abs{\gamma}^2/2}$ of an even unimodular lattice of rank $16$ is a [[modular form|GWKN5VG78A]] of weight $8$ for $SL_2(\Z)$ with constant term $1$.
That space of modular forms has dimension $1$, so the two theta series are equal, and $N_{\Gamma_1}(r) = N_{\Gamma_2}(r)$ for every $r$.
Hence $T_{\Gamma_1}$ and $T_{\Gamma_2}$ are [[isospectral|18MQEGN13R]].

They are not isometric.
An isometry of flat tori lifts to an affine isometry of $\R^{16}$ whose linear part maps $\Gamma_1$ onto $\Gamma_2$.
But the vectors of squared length $2$ generate a sublattice of index $1$ in $E_8 \oplus E_8$, and a sublattice of index $2$ in $D_{16}^+$, namely $D_{16}$.

## Explanations

### L1 human

A flat torus is a box whose opposite faces are glued, and its frequencies are given by the lengths of the vectors of a lattice.
Milnor noticed in 1964 that two special lattices in $16$ dimensions have exactly the same number of vectors of each length, although they are shaped differently.
So the two tori sound the same but are not the same shape.
This was the first example showing that one cannot always hear the shape of a manifold.
