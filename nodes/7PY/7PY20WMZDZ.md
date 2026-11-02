---
tag: 7PY20WMZDZ
kind: definition
name: Group C*-algebra
msc: ["22D25", "46L05", "22D15"]
defines: JKANN4VBYH
uses: [AHV05ZBCYW, 6GD25S53ND, 74BPYJNZTM]
sources:
  - url: https://en.wikipedia.org/wiki/Group_algebra_of_a_locally_compact_group
---

## Definition

Let $G$ be a [[locally compact group|AHV05ZBCYW]] with left Haar measure $\mu$, and let $L^1(G)$ be its [[group algebra|6GD25S53ND]].
For a [[unitary representation|74BPYJNZTM]] $\pi$ of $G$ on a Hilbert space $H$ and $f \in L^1(G)$, let $\pi(f)$ be the bounded operator on $H$ given by
$$\ip{\pi(f)u}{v} = \int_G f(x) \ip{\pi(x)u}{v} \, d\mu(x) \quad (u, v \in H).$$
For $f \in L^1(G)$ put
$$\norm{f}_* = \sup_\pi \norm{\pi(f)},$$
where $\pi$ runs over all unitary representations of $G$.
The *group C\*-algebra* $C^*(G)$ is the completion of $L^1(G)$ for the norm $\norm{\cdot}_*$.
The *reduced group C\*-algebra* $C^*_r(G)$ is the closure of $\set{\lambda(f) : f \in L^1(G)}$ in the bounded operators on $L^2(G)$, where $\lambda$ is the left regular representation.

## Remarks

The supremum is finite, since $\norm{\pi(f)} \le \norm{f}_1$, and $\norm{\cdot}_*$ is a norm on $L^1(G)$, since the left regular representation is injective on $L^1(G)$.
Both $C^*(G)$ and $C^*_r(G)$ are C*-algebras.

Example: for $G = \Z$, the Fourier transform $f \mapsto \sum_n f(n) z^n$ identifies $C^*(\Z)$ and $C^*_r(\Z)$ with the algebra $C(\mathbb{T})$ of continuous functions on the circle with the supremum norm.

Non-example: $L^1(G)$ with its own norm $\norm{\cdot}_1$ is in general not a C\*-algebra.
In $\ell^1(\Z)$, let $f = \delta_0 + \delta_1 - \delta_2$.
Then $f^* * f = 3\delta_0 - \delta_2 - \delta_{-2}$, so $\norm{f^* * f}_1 = 5$, while $\norm{f}_1^2 = 9$, and the C\*-identity $\norm{f^* f} = \norm{f}^2$ fails.

There is always a surjective homomorphism $C^*(G) \to C^*_r(G)$; it is an isomorphism exactly when $G$ is amenable.
