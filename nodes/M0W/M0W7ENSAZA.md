---
tag: M0W7ENSAZA
kind: proof
name: Proof of the estimation lemma
msc: [30A10]
proves: 0DJMGPN8K9
uses: [00FWNP9TXY, 05RCDKHZM6, 080RWVVSB6, 0MBWQKM8QR, 06SESV7GQY, 0FJZMBX0ZZ]
sources:
  - url: https://en.wikipedia.org/wiki/Estimation_lemma
---

## Proof

We first prove $\abs{\int g} \le \int \abs{g}$ for a continuous complex function $g$, then apply it piece by piece.

1. Let $[p, q]$ be an interval and $g : [p, q] \to \C$ continuous. Its real and imaginary parts and $\abs{g}$ are continuous, so they are [[Riemann integrable|06SESV7GQY]]. Put $I = \int_p^q g(t) \, dt$.
2. For a complex constant $\lambda$, $\int_p^q \lambda g = \lambda I$. This follows from the [[linearity of the real integral|080RWVVSB6]] applied to $\operatorname{Re}(\lambda g)$ and $\operatorname{Im}(\lambda g)$.
3. If $I = 0$, then $\abs{I} \le \int_p^q \abs{g}$, since $\abs{g} \ge 0$. Otherwise put $\lambda = \abs{I} / I$, so that $\abs{\lambda} = 1$ and $\lambda I = \abs{I}$.
4. By step 2, $\abs{I} = \lambda I = \int_p^q \lambda g$. This number is real, so it equals $\int_p^q \operatorname{Re}(\lambda g)$.
5. We have $\operatorname{Re}(\lambda g) \le \abs{\lambda g} = \abs{g}$. By the [[monotonicity of the integral|0MBWQKM8QR]], $\abs{I} \le \int_p^q \abs{g(t)} \, dt$.
6. Now choose $a = t_0 < t_1 < \dots < t_m = b$ such that $\gamma$ is continuously differentiable on each $[t_{j-1}, t_j]$. Put $g(t) = f(\gamma(t)) \gamma'(t)$, which is continuous on each such piece.
7. By the [[definition of the contour integral|00FWNP9TXY]] and [[additivity over intervals|05RCDKHZM6]], $\int_\gamma f(z) \, dz = \sum_{j=1}^{m} \int_{t_{j-1}}^{t_j} g(t) \, dt$. In the same way, $L(\gamma) = \sum_{j=1}^m \int_{t_{j-1}}^{t_j} \abs{\gamma'(t)} \, dt$.
8. By the [[triangle inequality|0FJZMBX0ZZ]] and step 5, $\abs{\int_\gamma f(z) \, dz} \le \sum_{j=1}^m \int_{t_{j-1}}^{t_j} \abs{f(\gamma(t))} \abs{\gamma'(t)} \, dt$.
9. Since $\gamma(t)$ lies on the image of $\gamma$, $\abs{f(\gamma(t))} \abs{\gamma'(t)} \le M \abs{\gamma'(t)}$. By monotonicity and linearity, the right side of step 8 is at most $M \sum_{j} \int_{t_{j-1}}^{t_j} \abs{\gamma'(t)} \, dt = M L(\gamma)$.

## Idea

Rotating by the unit number $\lambda$ turns the integral into a nonnegative real number, which is the integral of a real part. A real part is never larger than the modulus, so the integral of $\abs{g}$ wins. Then bound $\abs{f}$ by $M$.
