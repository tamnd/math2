---
tag: EPN6C0X93V
kind: definition
name: Symplectic capacity
msc: [53D35]
defines: 8KCB5KJKNT
uses: [CAN490EPRT]
sources:
  - url: https://en.wikipedia.org/wiki/Non-squeezing_theorem
---

## Definition

Fix $n \ge 1$.
Let $B^{2n}(1)$ be the open unit ball and $Z^{2n}(1) = \set{(x, y) \in \R^{2n} : x_1^2 + y_1^2 < 1}$ the open unit cylinder, both with the standard symplectic form $\omega_0$.
A *symplectic capacity* on [[symplectic manifolds|CAN490EPRT]] of dimension $2n$ is a function $c$ assigning to each such manifold $(M, \omega)$ a value $c(M, \omega) \in [0, \infty]$ such that:

1. (Monotonicity) If there is a symplectic embedding $(M, \omega) \to (N, \tau)$, then $c(M, \omega) \le c(N, \tau)$.
2. (Conformality) $c(M, \lambda \omega) = \abs{\lambda} \, c(M, \omega)$ for every real $\lambda \ne 0$.
3. (Normalization) $c(B^{2n}(1), \omega_0) = c(Z^{2n}(1), \omega_0) = \pi$.

## Remarks

Example: the *Gromov width* $w(M, \omega) = \sup \set{\pi r^2 : B^{2n}(r) \text{ embeds symplectically in } (M, \omega)}$.
Monotonicity holds because an embedding into $M$ composed with $M \to N$ is an embedding into $N$.
Conformality holds because scaling by $\sqrt{\abs{\lambda}}$ (and swapping $x$ and $y$ if $\lambda < 0$) maps $(B(r), \lambda\omega_0)$ to $(B(\sqrt{\abs{\lambda}}\, r), \omega_0)$ symplectically.
The value $\pi$ on the ball is clear, and the value $\pi$ on the cylinder is exactly [[Gromov's non-squeezing theorem|RDX55HQ3XT]].

Non-example: for $n \ge 2$, the function $c(M, \omega) = \left( \int_M \omega^n / n! \right)^{1/n}$, suitably rescaled, satisfies monotonicity and conformality, but fails normalization, because the cylinder has infinite volume.

Some authors drop the normalization and only ask for nontriviality, $0 < c(B^{2n}(1))$ and $c(Z^{2n}(1)) < \infty$.
Other examples are the Hofer–Zehnder capacity and the Ekeland–Hofer capacities.
The Gromov width is the smallest normalized capacity.
