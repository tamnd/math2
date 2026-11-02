---
tag: E8YK1W16NV
kind: definition
name: Homotopy principle
msc: [58A20, 57R42]
defines: Y2S9GWG1J1
uses: [F45VQ47GPV, 9YA6S6HD9V]
sources:
  - url: https://en.wikipedia.org/wiki/Homotopy_principle
---

## Definition

Let $M$ and $N$ be [[smooth manifolds|F45VQ47GPV]], let $r \ge 1$, and let $J^r(M, N)$ be the jet bundle of $r$-jets of smooth maps $M \to N$, with projection $J^r(M, N) \to M$.
A *differential relation* of order $r$ is a subset $\mathcal{R} \subseteq J^r(M, N)$.
A *formal solution* of $\mathcal{R}$ is a continuous section $F \colon M \to J^r(M, N)$ with $F(M) \subseteq \mathcal{R}$.
A formal solution is *holonomic* if $F = j^r f$ for a smooth map $f \colon M \to N$, where $j^r f$ is the $r$-jet extension of $f$.
In that case $f$ is a *genuine solution* of $\mathcal{R}$.
The relation $\mathcal{R}$ satisfies the *h-principle* if every formal solution is [[homotopic|9YA6S6HD9V]] to a holonomic one.
The homotopy must run through formal solutions of $\mathcal{R}$.

## Remarks

Every genuine solution gives a formal solution, so the h-principle says that the only obstruction to solving $\mathcal{R}$ is the homotopy-theoretic obstruction to finding a formal solution.
Stronger versions ask that the inclusion of holonomic solutions into formal solutions be a weak homotopy equivalence; the parametric h-principle is of this kind.
Example: let $\dim M < \dim N$ and let $\mathcal{R} \subseteq J^1(M, N)$ be the set of $1$-jets whose linear part is injective.
Genuine solutions are immersions, formal solutions are fibrewise injective bundle maps $TM \to TN$, and the Smale–Hirsch theorem shows that $\mathcal{R}$ satisfies the h-principle.
Non-example: for $M = S^1$, $N = \R$ and the analogous relation of injective $1$-jets, the section $F(x) = (0, \text{the linear map } v \mapsto v)$, using the standard trivialisation of $TS^1$, is a formal solution.
But there is no genuine solution, because a smooth function on the compact circle has a maximum, where its derivative is zero; so the h-principle fails.
