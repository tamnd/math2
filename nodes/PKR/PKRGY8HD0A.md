---
tag: PKRGY8HD0A
kind: definition
name: Bromwich justification of the Heaviside calculus
msc: [44A45, 44A10]
defines: GD8B883592
uses: [QQ98C2AXZP, 5KNAXNHRY6, 0PHN07KVQT, 0V49JEZW06]
sources:
  - url: https://en.wikipedia.org/wiki/Operational_calculus
---

## Definition

Let $c \ge 0$, and let $\varphi$ be a holomorphic function on the half-plane $\operatorname{Re} s > c$.
Let $\gamma > c$, and suppose that for each $t > 0$ the integral below converges.
Here the integral is the limit, as $R \to \infty$, of the integrals over the segment from $\gamma - iR$ to $\gamma + iR$.
The *Bromwich interpretation* of the Heaviside expression $\varphi(p) H$ is the function
$$x(t) = \frac{1}{2\pi i} \int_{\gamma - i\infty}^{\gamma + i\infty} \frac{\varphi(s)}{s} \, e^{st} \, ds, \qquad t > 0,$$
a [[Bromwich integral|5KNAXNHRY6]], with $x(t) = 0$ for $t < 0$.

## Remarks

Under suitable growth conditions on $\varphi$, the [[Laplace transform|0V49JEZW06]] of $x$ is $\varphi(s)/s$, so this interpretation agrees with the Laplace transform reading of the [[Heaviside operational calculus|QQ98C2AXZP]].
By Cauchy's theorem, the value does not depend on $\gamma > c$.
When $\varphi$ is meromorphic and the line can be closed to the left, $x(t)$ is the sum of the [[residues|0PHN07KVQT]] of $\varphi(s) e^{st} / s$.

Example: $\varphi(p) = p^{-n}$ with $n \ge 0$.
For $t > 0$, the line can be closed to the left, and the only pole of $e^{st}/s^{n+1}$ is at $0$, with residue $t^n / n!$.
So $x(t) = t^n/n!$, which is Heaviside's rule $p^{-n} H = t^n H / n!$.

Non-example: $\varphi(s) = e^{-s^2}$ is entire, but on the line $s = \gamma + iy$ one has $\abs{\varphi(s)} = e^{y^2 - \gamma^2}$.
So the integrand grows without bound, the integral diverges for every $t$, and $\varphi(p) H$ has no Bromwich interpretation.
