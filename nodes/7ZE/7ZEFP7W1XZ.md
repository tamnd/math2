---
tag: 7ZEFP7W1XZ
kind: definition
name: Jet bundle
msc: [58A20, 55R10]
defines: HC3VBBCJQP
uses: [CX4M8K61AB, F45VQ47GPV, 1QE0Z0756D, P4DZM975BV]
sources:
  - url: https://en.wikipedia.org/wiki/Jet_bundle
---

## Definition

Let $\pi \colon E \to M$ be a smooth [[fiber bundle|CX4M8K61AB]] over a [[smooth manifold|F45VQ47GPV]] $M$, and let $k \ge 0$ be an integer.
A local section of $\pi$ is a smooth map $s \colon U \to E$, with $U \subseteq M$ open, such that $\pi \circ s = \id_U$.
For $p \in U$, let $j^k_p s$ be the [[$k$-jet|1QE0Z0756D]] of $s$ at $p$, viewed as a map from $M$ to $E$.
The *$k$-th jet manifold* of $\pi$ is the set
$$J^k \pi = \set{ j^k_p s : p \in M,\ s \text{ a local section of } \pi \text{ defined near } p }.$$
It comes with the maps $\pi_k \colon J^k \pi \to M$, $j^k_p s \mapsto p$, and $\pi_{k,0} \colon J^k\pi \to E$, $j^k_p s \mapsto s(p)$.

Let $(x^1, \dots, x^n, u^1, \dots, u^m)$ be adapted coordinates on an open set of $E$, so that $x^i$ are coordinates on $M$ and $u^\alpha$ are fiber coordinates.
They induce coordinates $(x^i, u^\alpha, u^\alpha_I)$ on $J^k\pi$, where $I$ runs over multi-indices with $1 \le \abs{I} \le k$ and
$$u^\alpha_I(j^k_p s) = \frac{\partial^{\abs{I}} s^\alpha}{\partial x^I}(p).$$
These charts make $J^k\pi$ a smooth manifold.
With this structure, $\pi_k \colon J^k\pi \to M$ is called the *$k$-th jet bundle* of $\pi$.

## Remarks

The maps $\pi_k$ and $\pi_{k,0}$, and more generally the maps $J^k\pi \to J^l\pi$ for $l < k$ that forget the higher derivatives, are smooth fiber bundles.
If $E$ is a [[vector bundle|P4DZM975BV]], then $J^k\pi \to M$ is again a vector bundle.

Example: for the trivial bundle $\pi \colon \R \times \R \to \R$, $(x, u) \mapsto x$, the local sections are graphs of functions $u = s(x)$.
The first jet manifold has the global coordinates $(x, u, u_x)$, so $J^1\pi \cong \R^3$, and $j^1_p s = (p, s(p), s'(p))$.

Non-example: the $k$-jets of all smooth maps $M \to E$, not only of sections, form the larger space $J^k(M, E)$.
A jet of a map $f$ with $\pi \circ f \ne \id$ near $p$ is not in $J^k\pi$, because the definition admits only sections.
