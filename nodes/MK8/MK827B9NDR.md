---
tag: MK827B9NDR
kind: definition
name: Poisson boundary
msc: [60J50, 60B15, 31C35]
defines: 6EEF2E8XPF
uses: [WAS9EANSJJ, 059TJN0NZ1, SASP14MA1Z, Y1EGR8DF84]
sources:
  - url: https://en.wikipedia.org/wiki/Poisson_boundary
---

## Definition

Let $\Gamma$ be a countable group and let $\mu$ be a [[probability measure|059TJN0NZ1]] on $\Gamma$.
It defines the [[random walk|WAS9EANSJJ]] $X_n = g_1 g_2 \cdots g_n$ with independent steps $g_k$ of law $\mu$.
A function $f \colon \Gamma \to \R$ is $\mu$-*harmonic* if $f(g) = \sum_{h \in \Gamma} \mu(h) f(gh)$ for every $g \in \Gamma$.
Let $H^\infty(\Gamma, \mu)$ be the space of bounded $\mu$-harmonic functions.
A *Poisson boundary* of $(\Gamma, \mu)$ is a standard probability space $(B, \nu)$ with a measurable action of $\Gamma$ such that:

1. $\nu$ is $\mu$-stationary: $\sum_{h \in \Gamma} \mu(h)\, h_* \nu = \nu$.
2. The Poisson transform $\varphi \mapsto f_\varphi$, with $f_\varphi(g) = \int_B \varphi(g \xi) \, d\nu(\xi)$, is a bijection from $L^\infty(B, \nu)$ onto $H^\infty(\Gamma, \mu)$.

## Remarks

Clause 1 makes each $f_\varphi$ harmonic: $\sum_h \mu(h) \int_B \varphi(gh\xi) \, d\nu(\xi) = \int_B \varphi(g\xi) \, d\Big(\sum_h \mu(h) h_* \nu\Big)(\xi) = f_\varphi(g)$.
The Poisson boundary exists and is unique up to a $\Gamma$-equivariant measure isomorphism.
One construction takes the space of ergodic components of the shift on the space of sample paths of the walk, with the image of the path measure.
Example: let $\Gamma = \Z^d$ and let the support of $\mu$ generate $\Z^d$ as a group.
By the Choquet–Deny theorem the bounded harmonic functions are constant, so a one-point space is a Poisson boundary.
Non-example: for the free group $F_2$ on $a, b$ and $\mu$ uniform on $\set{a, a^{-1}, b, b^{-1}}$, a one-point space fails clause 2, since there are nonconstant bounded harmonic functions.
In that case a Poisson boundary is the space of infinite reduced words in $a^{\pm 1}, b^{\pm 1}$ with the law of the limit of $X_n$.
For the simple random walk on a Cayley graph, a trivial Poisson boundary is the same as the [[Liouville property|Y1EGR8DF84]] of the graph.
