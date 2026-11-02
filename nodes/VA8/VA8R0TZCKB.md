---
tag: VA8R0TZCKB
kind: statement
role: theorem
name: Masur–Veech theorem
msc: ["37E35", "32G15", "37A25"]
uses: [CEHHBBD6NT, NZZE9KCAD8, 19JFF3GY9F, FJZRW9P0K3, 0V9PMN0RBH, ZZGC6BZNJ5]
about: [CEHHBBD6NT]
sources:
  - url: https://en.wikipedia.org/wiki/Translation_surface
---

## Statement

Let $g \ge 1$ and let $k_1, \dots, k_n \ge 0$ be integers with $k_1 + \cdots + k_n = 2g - 2$.
Let $\mathcal{H}_1(k_1, \dots, k_n)$ be the stratum of [[translation surfaces|CEHHBBD6NT]] $(X, \omega)$ of genus $g$ and area $\int_X \frac{i}{2} \omega \wedge \bar\omega = 1$ whose form $\omega$ has $n$ zeros of orders $k_1, \dots, k_n$.
Let $\nu$ be the Masur–Veech measure on it, and let $g_t$, $t \in \R$, be the Teichmüller geodesic flow, the action of the diagonal matrices $\begin{pmatrix} e^t & 0 \\ 0 & e^{-t} \end{pmatrix}$.
Let $\mathcal{C}$ be a connected component of $\mathcal{H}_1(k_1, \dots, k_n)$.
Then:

1. The total measure $\nu(\mathcal{C})$ is finite.
2. The flow $g_t$ on $\mathcal{C}$ is ergodic with respect to $\nu$.

## Remarks

The stratum $\mathcal{H}(k_1, \dots, k_n)$ of all such surfaces, of any area, has local period coordinates.
Take a basis $\gamma_1, \dots, \gamma_{2g + n - 1}$ of the relative homology $H_1(X, \Sigma; \Z)$, where $\Sigma$ is the set of zeros.
Then the map $(X, \omega) \mapsto (\int_{\gamma_j} \omega)_j \in \C^{2g + n - 1}$ is a local chart.
The Masur–Veech measure on $\mathcal{H}$ is Lebesgue measure in these charts, normalized so that the lattice of periods in $\Z + i\Z$ has covolume $1$.
The measure $\nu$ on $\mathcal{H}_1$ is the cone measure: $\nu(E)$ is the Lebesgue measure of the set of $r \cdot (X, \omega)$ with $(X, \omega) \in E$ and $0 < r \le 1$.
The group $SL(2, \R)$ acts on translation surfaces by acting linearly on the polygons, it preserves area, and the measure $\nu$ is invariant under it.

Masur and Veech proved the finiteness of the volume and the main consequence below independently in 1982, and the strata are not compact, so finiteness is not automatic.
Consequence: for $\nu$-almost every translation surface, the vertical straight-line flow is [[uniquely ergodic|NZZE9KCAD8]].
Through the first return map to a transversal, this gives Keane's conjecture: almost every [[interval exchange transformation|19JFF3GY9F]] with an irreducible permutation is uniquely ergodic.

## Explanations

### L1 human

Translation surfaces of a given shape type form a space, and this space has a natural notion of volume.
The theorem says that this volume is finite, and that a natural flow on the space, which stretches each surface horizontally and squeezes it vertically, mixes up the space thoroughly.
From this one learns that for a randomly chosen surface, a straight line in a fixed direction spreads out evenly over the whole surface.

### L2 human

The strata $\mathcal{H}_1(k_1, \dots, k_n)$ are moduli spaces of abelian differentials, fibred over the [[moduli space|FJZRW9P0K3]] of Riemann surfaces of genus $g$.
The flow $g_t$ projects to geodesics for the Teichmüller metric on [[Teichmüller space|ZZGC6BZNJ5]].
Ergodicity of $g_t$ is a starting point for counting problems, such as the asymptotic number of cylinders of closed geodesics on a typical surface.
The passage from ergodicity of $g_t$ to unique ergodicity of almost every vertical flow uses Masur's criterion.
If the orbit $g_t(X, \omega)$ returns infinitely often to a compact set as $t \to \infty$, then the vertical flow is uniquely ergodic.
