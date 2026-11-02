---
tag: NC1C7EKV1V
kind: definition
name: Positive solutions of integral equations
msc: [45M20, 47B65]
defines: D8PHFS2KAY
uses: [R3SG1SN7JQ, Z344RY5XX1, 77020CY5ZW]
sources:
  - url: https://en.wikipedia.org/wiki/Krein%E2%80%93Rutman_theorem
---

## Definition

Let $(\Omega, \mu)$ be a measure space.
Let $X$ be a space of real-valued functions on $\Omega$, such as $C(\Omega)$ for compact $\Omega$ or $L^p(\Omega, \mu)$.
Its [[positive cone|Z344RY5XX1]] is $X_+ = \set{\varphi \in X : \varphi \ge 0}$, with the inequality almost everywhere in the case of $L^p$.
Consider an [[integral equation|R3SG1SN7JQ]] $\varphi = T\varphi$ on $X$, for example $T\varphi = f + \int_\Omega k(\cdot, y) \varphi(y) \, d\mu(y)$, or a nonlinear one such as a [[Hammerstein equation|T7E2EW2T0G]] $T\varphi = \int_\Omega k(\cdot, y) \, g(y, \varphi(y)) \, d\mu(y)$.

1. A *positive solution* is a solution $\varphi \in X_+$ with $\varphi \ne 0$.
2. A *strictly positive solution* is a solution with $\varphi(x) > 0$ for all $x \in \Omega$ (for almost all $x$, in the case of $L^p$).

## Remarks

Example: on $X = C[0, 1]$ take $\varphi(x) = 1 + \frac12 \int_0^1 \varphi(t) \, dt$.
The right side is constant, so $\varphi = c$ with $c = 1 + \frac{c}{2}$, that is $c = 2$, a strictly positive solution.
More generally, if $k \ge 0$, $f \ge 0$, and the integral operator $K$ has [[spectral radius|9V7YQA85PC]] $r(K) < 1$, the [[Liouville–Neumann series|H1HWSWME6B]] $\varphi = \sum_{n \ge 0} K^n f$ is a sum of nonnegative terms, so the solution is nonnegative.

Non-example: $\varphi(x) = 1 + 2 \int_0^1 \varphi(t) \, dt$ on $[0, 1]$ gives $c = 1 + 2c$, so its only solution is $\varphi = -1$, which is not in $X_+$.
Here $r(K) = 2 > 1$, and the Neumann series argument fails.

For the homogeneous eigenvalue problem $\lambda\varphi = K\varphi$, the [[Krein–Rutman theorem|VADXDK3TKM]] and [[Jentzsch's theorem|P8CAK0FHGJ]] give a positive eigenfunction for the eigenvalue $r(K)$ when $K$ is compact with nonnegative kernel and $r(K) > 0$.
