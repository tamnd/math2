---
tag: M2W79VF0TN
kind: statement
role: theorem
name: Palais–Smale theory of critical points
msc: ["58E05", 58B20, 47J30]
uses: [R8DMMW0E9M, 4724KRNHAT, 9ZQC7ARWTT, W5BHHXCYXA, YW8HBW1GJX]
about: [9ZQC7ARWTT, 4724KRNHAT]
sources:
  - url: https://en.wikipedia.org/wiki/Palais–Smale_compactness_condition
---

## Statement

Let $M$ be a $C^\infty$ [[Hilbert manifold|R8DMMW0E9M]] with a complete Riemannian metric.
Let $f \colon M \to \R$ be a $C^2$ function that is bounded below and satisfies the [[Palais–Smale condition|4724KRNHAT]].
This means that every sequence $(p_n)$ with $(f(p_n))$ bounded and $\norm{\nabla f(p_n)} \to 0$ has a convergent subsequence.
For $c \in \R$ let $M^c = \set{p \in M : f(p) \le c}$.

1. (Deformation) If $a < b$ and $f^{-1}[a, b]$ contains no critical point of $f$, then $M^a$ is a strong [[deformation retract|YW8HBW1GJX]] of $M^b$.
2. (Minimum) The infimum of $f$ is attained, and every point where it is attained is a critical point of $f$.
3. (Lusternik–Schnirelmann bound) The number of critical points of $f$ is at least $\operatorname{cat}(M) + 1$, where $\operatorname{cat}$ is the normalized [[Lusternik–Schnirelmann category|W5BHHXCYXA]].

## Remarks

The proof of the deformation statement follows the flow of $-\nabla f / \norm{\nabla f}^2$ on $f^{-1}[a, b]$.
The Palais–Smale condition gives a positive lower bound for $\norm{\nabla f}$ there, and completeness of the metric lets the flow run until it reaches $M^a$.
For the minimum, suppose $c = \inf f$ were not a critical value.
Then the condition would give $\varepsilon > 0$ with no critical value in $[c, c + \varepsilon]$.
The same flow, extended below $c$, would push the nonempty set $M^{c + \varepsilon}$ into a sublevel set $M^{c'}$ with $c' < c$, which is empty.
For the third statement, the minimax values $c_k = \inf \set{\sup_A f : A \subseteq M \text{ closed}, \ \operatorname{cat}_M(A) \ge k}$ for $k = 0, \dots, \operatorname{cat}(M)$ are critical values, as in [[Lusternik–Schnirelmann theory|QARH15D2PN]], and equal values force infinitely many critical points.

Example: the energy functional on paths with fixed endpoints in a compact Riemannian manifold, or on its free loop space, satisfies these hypotheses.
This gives existence of geodesics and is the setting of the [[Lyusternik–Fet theorem|EXZA8ZA8P6]].
Without the Palais–Smale condition the conclusions fail: $f(x) = e^x$ on $\R$ is bounded below and has no critical point, so its infimum $0$ is not attained.
The [[mountain pass theorem|EPXNCSP2MN]] is another critical point theorem that rests on the same condition.

## Explanations

### L1 human

On a compact manifold, every continuous function has a minimum, and topology forces further critical points.
In infinite dimensions this fails, because a minimizing sequence can run off to infinity.
Palais and Smale found one condition on the function that restores what is needed: almost-critical sequences must have convergent subsequences.
With it, the classical statements about minima, deformations and the number of critical points hold again.

### L2 human

These results are the base of variational methods for nonlinear partial differential equations and for geodesics.
To apply them, one checks the Palais–Smale condition for a concrete functional, typically with Sobolev embeddings and compactness theorems.
The deformation statement is the engine of all minimax arguments, including the [[mountain pass theorem|EPXNCSP2MN]] and the Lusternik–Schnirelmann bound.
The same results hold for $C^1$ functions on complete Finsler manifolds modelled on Banach spaces, with a pseudo-gradient vector field in place of the gradient.
