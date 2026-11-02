---
tag: XGBDVQQV0T
kind: statement
role: theorem
name: Hadamard's two-constants theorem
msc: [30C85, 31A15, 30C80]
uses: [CFD7BPM51W, 0NAHXR1FRH, Z1MHMGFNFW, 8D56GQ4AG8, 0Q4CBD3HX0, V00Q05ZW1G, WHS58R43N0]
about: [CFD7BPM51W]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_measure
---

## Statement

Let $\Omega \subset \C$ be a bounded [[domain|0Q4CBD3HX0]] on which the [[Dirichlet problem|8D56GQ4AG8]] is solvable for continuous boundary data.
Let $E \subseteq \partial\Omega$ be a closed set, and let $\omega(z) = \omega(z, E, \Omega)$ be its [[harmonic measure|CFD7BPM51W]] at $z \in \Omega$.
Let $0 < m \le M$, and let $f$ be a [[holomorphic function|0NAHXR1FRH]] on $\Omega$ such that:

1. $\abs{f(z)} \le M$ for all $z \in \Omega$.
2. $\limsup_{z \to \zeta} \abs{f(z)} \le m$ for every $\zeta \in E$.

Then for every $z \in \Omega$,
$$\abs{f(z)} \le m^{\omega(z)} M^{1 - \omega(z)}.$$

## Remarks

Proof idea: the function $\log\abs{f}$ is [[subharmonic|Z1MHMGFNFW]], and $h = \omega \log m + (1 - \omega) \log M$ is harmonic.
Near points of $E$ the bound for $\log\abs{f}$ is $\log m$, elsewhere it is $\log M$, and $h$ takes these boundary values in the generalized (Perron) sense.
A maximum principle for $\log\abs{f} - h$, in the form valid for Perron solutions, gives $\log\abs{f} \le h$.
Example: on the annulus $r_1 < \abs{z} < r_2$ with $E$ the inner circle, $\omega(z) = \log(r_2/\abs{z}) / \log(r_2/r_1)$.
With $m$ and $M$ the maxima of $\abs{f}$ on the two circles, this gives the [[Hadamard three-circle theorem|V00Q05ZW1G]].
On a strip, the same argument gives the [[Hadamard three-lines theorem|WHS58R43N0]].
If $E$ is the whole boundary, then $\omega \equiv 1$ and the theorem reduces to the maximum modulus principle.

## Explanations

### L1 human

Suppose a holomorphic function is at most $M$ everywhere and at most a smaller number $m$ on part of the boundary.
Then inside the region the bound improves, and it improves more at points that "see" more of that part of the boundary.
Harmonic measure measures exactly how much of the boundary a point sees.

### L2 human

The theorem is the main way harmonic measure enters estimates of holomorphic functions.
It turns lower bounds for harmonic measure into upper bounds for holomorphic functions.
Taking logarithms, it says that $\log\abs{f}$ lies below the harmonic interpolation between $\log m$ and $\log M$.
It is a special case of the principle that a subharmonic function lies below the harmonic function with the same boundary bounds.
