---
tag: 4AXC8NESM4
kind: definition
name: Proper holomorphic map
msc: [32H35, 32H02]
defines: TM528Q96ZD
uses: [3MQTWKBBBT, 15XEBGNGHC, 0TVJZYB6SH]
sources:
  - url: https://en.wikipedia.org/wiki/Proper_map
---

## Definition

Let $\Omega_1 \subset \C^n$ and $\Omega_2 \subset \C^m$ be domains, that is, nonempty connected open sets.
A [[holomorphic map|3MQTWKBBBT]] $F \colon \Omega_1 \to \Omega_2$ is *proper* if $F^{-1}(K)$ is [[compact|0TVJZYB6SH]] for every compact set $K \subset \Omega_2$.
The same condition defines proper holomorphic maps between complex manifolds.

## Remarks

Equivalent form: $F$ is proper if and only if it has the following property.
For every sequence $(z_k)$ in $\Omega_1$ that eventually leaves every compact subset of $\Omega_1$, the sequence $(F(z_k))$ eventually leaves every compact subset of $\Omega_2$.
For bounded domains this says that $\operatorname{dist}(F(z), \partial\Omega_2) \to 0$ as $\operatorname{dist}(z, \partial\Omega_1) \to 0$.

Example: let $\mathbb{D}$ be the unit disc and $F(z) = z^k$ with $k \ge 1$.
A compact $K \subset \mathbb{D}$ lies in a closed disc $\set{\abs{w} \le r}$ with $r < 1$, and $F^{-1}(K)$ is a closed subset of $\set{\abs{z} \le r^{1/k}}$, hence compact.
The map $(z_1, z_2) \mapsto (z_1, z_2^2)$ of the unit polydisc in $\C^2$ to itself is proper for the same reason.

Non-example: the inclusion $F \colon \set{\abs{z} < 1/2} \to \mathbb{D}$ is holomorphic but not proper.
For the compact set $K = \set{\abs{w} \le 1/2}$, the preimage $F^{-1}(K) = \set{\abs{z} < 1/2}$ is not compact.

A proper holomorphic map between domains of the same dimension $n$ is surjective, its fibres are finite, and it is a finite branched covering.
A [[biholomorphism|FX92PP3HZR]] is a proper holomorphic map.
The proper holomorphic self-maps of $\mathbb{D}$ are exactly the finite [[Blaschke products|9N6R5ADJXT]].
