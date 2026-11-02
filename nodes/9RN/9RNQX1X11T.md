---
tag: 9RNQX1X11T
kind: definition
name: Jacobi transform
msc: [44A20, 33C45]
defines: 72TSY1Z4VA
uses: [YCK709QB06, TRD7DSF2KR]
sources:
  - url: https://en.wikipedia.org/wiki/Jacobi_polynomials
---

## Definition

Fix real numbers $\alpha > -1$ and $\beta > -1$, and let $w(x) = (1 - x)^\alpha (1 + x)^\beta$ for $-1 < x < 1$.
Let $P_n^{(\alpha, \beta)}$ be the [[Jacobi polynomial|TRD7DSF2KR]] of degree $n$.
Let $F \colon (-1, 1) \to \C$ be a function such that $w F$ is integrable on $(-1, 1)$.
The *Jacobi transform* of $F$ is the sequence
$$f(n) = \int_{-1}^{1} w(x)\, P_n^{(\alpha, \beta)}(x)\, F(x)\, dx, \qquad n = 0, 1, 2, \dots$$

## Remarks

Let $h_n = \int_{-1}^{1} w(x)\, P_n^{(\alpha, \beta)}(x)^2\, dx > 0$.
For $F$ in the weighted space $L^2(w)$, the inverse transform is the expansion $F = \sum_{n \ge 0} \frac{f(n)}{h_n} P_n^{(\alpha, \beta)}$, which converges in $L^2(w)$.

Let $R[F] = w^{-1} \frac{d}{dx}\left( (1 - x)^{\alpha + 1} (1 + x)^{\beta + 1} F' \right)$.
If $F$ is smooth enough and the boundary terms vanish, two integrations by parts and the Jacobi differential equation give that the transform of $R[F]$ is $-n(n + \alpha + \beta + 1) f(n)$.

Example: $F = P_m^{(\alpha, \beta)}$ has $f(n) = 0$ for $n \ne m$ and $f(m) = h_m$, by orthogonality.

Non-example: for $\alpha = -1$ the weight $(1 - x)^{-1}(1 + x)^\beta$ is not integrable near $x = 1$, so already $F = 1$ has no transform; this is why $\alpha, \beta > -1$ is required.

For $\alpha = \beta = \lambda - 1/2$ one gets, up to constant factors, the [[Gegenbauer transform|TMNNRRRGAS]].
