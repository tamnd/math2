---
tag: 4N5FGYKAFW
kind: definition
name: Whitney C-infinity topology
msc: [58D15, 58C25]
defines: 7PN9MD1PQB
uses: [F45VQ47GPV, 0CQHFPGJ45, 1QE0Z0756D, HC3VBBCJQP, 0ZH5AJ2ED7, RG15F0TWPW]
sources:
  - url: https://en.wikipedia.org/wiki/Whitney_topologies
---

## Definition

Let $M$ and $N$ be [[smooth manifolds|F45VQ47GPV]] and let $C^\infty(M, N)$ be the set of smooth maps from $M$ to $N$.
For an integer $k \ge 0$, let $J^k(M, N)$ be the manifold of [[$k$-jets|1QE0Z0756D]] of maps from $M$ to $N$, the [[jet bundle|HC3VBBCJQP]] of the trivial bundle $M \times N \to M$.
Each $f \in C^\infty(M, N)$ has the jet map $j^k f \colon M \to J^k(M, N)$, $p \mapsto j^k_p f$.
For an open set $U \subseteq J^k(M, N)$, put
$$\mathcal{M}(U) = \set{ f \in C^\infty(M, N) : j^k f(M) \subseteq U }.$$
The sets $\mathcal{M}(U)$, with $U$ open in $J^k(M, N)$, form a base of a [[topology|0CQHFPGJ45]] on $C^\infty(M, N)$, the *Whitney $C^k$ topology*.
The *Whitney $C^\infty$ topology* is the topology whose base is the union over all $k \ge 0$ of these bases.

## Remarks

With the Whitney $C^\infty$ topology, $C^\infty(M, N)$ is a [[Baire space|0ZH5AJ2ED7]].
If $M$ is compact, it coincides with the weak $C^\infty$ topology, the topology of uniform convergence of all derivatives, which is built from the [[compact-open topology|RG15F0TWPW]] on jets.
If $M$ is not compact, it is much finer.

Example: for $M = N = \R$, let $\varepsilon \colon \R \to (0, \infty)$ be continuous and let $f \in C^\infty(\R, \R)$.
The set $U = \set{ (x, y) \in \R \times \R : \abs{y - f(x)} < \varepsilon(x) }$ is open in $J^0(\R, \R) = \R \times \R$.
So $\mathcal{M}(U) = \set{ g : \abs{g(x) - f(x)} < \varepsilon(x) \text{ for all } x }$ is an open neighbourhood of $f$.

Non-example: the constant maps $f_n = 1/n$ do not converge to $0$ in the Whitney $C^\infty$ topology on $C^\infty(\R, \R)$, although they converge uniformly with all derivatives.
Take $f = 0$ and $\varepsilon(x) = 1/(1 + x^2)$ above.
For each $n$, $1/n > \varepsilon(x)$ for large $\abs{x}$, so no $f_n$ lies in this neighbourhood of $0$.
