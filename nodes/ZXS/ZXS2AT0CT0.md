---
tag: ZXS2AT0CT0
kind: definition
name: Lattice gauge theory
msc: [81T25, 81T13, 82B20]
defines: ZBJY59W3Z5
uses: [EVHCE5VR6Y, VY0HXD3GC4, 707DEWCCFX]
sources:
  - url: https://en.wikipedia.org/wiki/Lattice_gauge_theory
---

## Definition

Let $d \ge 2$ and $L \ge 2$ be integers, and let $\Lambda = (\Z / L\Z)^d$ be a periodic lattice with its set $E$ of oriented nearest-neighbour edges.
Let $G \subseteq U(N)$ be a [[compact|EVHCE5VR6Y]] Lie group of $N \times N$ unitary matrices, with normalized [[Haar measure|VY0HXD3GC4]] $dU$.
A *lattice gauge field* is a map $U \colon E \to G$, written $e \mapsto U_e$, such that $U_{\bar e} = U_e^{-1}$ when $\bar e$ is $e$ with the opposite orientation.
For a plaquette $p$, a unit square of $\Lambda$ with boundary edges $e_1, e_2, e_3, e_4$ in order, set $U_p = U_{e_1} U_{e_2} U_{e_3} U_{e_4}$.
For $\beta > 0$, the *Wilson action* is
$$S(U) = \beta \sum_{p} \left( 1 - \frac{1}{N} \operatorname{Re} \operatorname{tr} U_p \right),$$
summed over the plaquettes.
Choose one orientation of each edge, and let $E_+ \subseteq E$ be the chosen edges.
A lattice gauge field is then the same as an element of $G^{E_+}$.
*Lattice gauge theory* with gauge group $G$ is the probability measure
$$d\mu(U) = \frac{1}{Z} e^{-S(U)} \prod_{e \in E_+} dU_e$$
on $G^{E_+}$, where $Z$ is the normalizing constant.
The expectation of a function $f$ is $\langle f \rangle = \int f \, d\mu$.

## Remarks

A lattice gauge transformation is a map $g \colon \Lambda \to G$; it acts by $U_e \mapsto g(x) U_e \, g(y)^{-1}$ for an edge $e$ from $x$ to $y$.
It changes $U_p$ into $g(x) U_p \, g(x)^{-1}$, where $x$ is the starting corner of $p$, so $\operatorname{tr} U_p$ and the action do not change.
The Haar measure is invariant too, so $\mu$ is gauge invariant; this is the lattice version of the [[gauge group|707DEWCCFX]] symmetry.

Example: $G = U(1)$, with $U_e = e^{i\theta_e}$.
Then $U_p = e^{i\theta_p}$, where $\theta_p$ is the signed sum of the four angles around $p$, and $S(U) = \beta \sum_p (1 - \cos\theta_p)$.
Let $a > 0$ be the lattice spacing and $e > 0$ a coupling, and let $\theta_e = a e A_e$ for a smooth potential $A$, where $A_e$ is the component of $A$ along $e$.
Then $\theta_p \approx a^2 e F_p$, where $F_p$ is the component of $F = dA$ on $p$, and $S \approx \frac{\beta e^2}{2} \sum_p a^4 F_p^2$.
For $d = 4$ and $\beta = 1/e^2$ this is a Riemann sum for the Euclidean Maxwell action $\frac14 \int F_{\mu\nu} F_{\mu\nu} \, d^4x$.

Non-example: the function $\sum_{e} \operatorname{Re}\operatorname{tr} U_e$ is not gauge invariant, because $\operatorname{tr}(g(x) U_e \, g(y)^{-1})$ differs from $\operatorname{tr} U_e$ when $g(x) \ne g(y)$.

The natural observables are traces of products of edge variables around closed paths, the [[Wilson loops|61YB1GGZ7B]].
For $G = SU(3)$ and $d = 4$, with quark fields added, the theory is lattice [[quantum chromodynamics|SEE8XD0APW]].
