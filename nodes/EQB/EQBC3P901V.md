---
tag: EQBC3P901V
kind: statement
role: theorem
name: Heisenberg inequality for the Fourier transform
msc: ["42A38", "81S07"]
uses: [DPVM34ADZV, SASP14MA1Z, HPZHRZ0502, HHNR31W3WD, 0RFWW56Y22]
about: [DPVM34ADZV]
sources:
  - url: https://en.wikipedia.org/wiki/Uncertainty_principle
---

## Statement

Let $f \in L^2(\R)$, and let $\hat f$ be its Fourier transform on $L^2(\R)$, normalized so that $\hat f(\xi) = \int_\R f(x) e^{-2\pi i x \xi}\, dx$ for integrable $f$.
Then for all real numbers $a$ and $b$,
$$\left( \int_\R (x - a)^2 \abs{f(x)}^2\, dx \right) \left( \int_\R (\xi - b)^2 \abs{\hat f(\xi)}^2\, d\xi \right) \ge \frac{\norm{f}_2^4}{16 \pi^2}.$$
Equality holds if and only if $f(x) = C e^{2\pi i b x} e^{-c (x - a)^2}$ for some $C \in \C$ and $c > 0$.

## Remarks

For a Schwartz function $f$ and $a = b = 0$, integrate by parts: $\int \abs{f}^2\, dx = -\int x\, \frac{d}{dx}\abs{f(x)}^2\, dx = -2 \operatorname{Re} \int x f(x) \overline{f'(x)}\, dx$.
The [[Cauchy–Schwarz inequality|0RFWW56Y22]] bounds this by $2 \norm{x f}_2 \norm{f'}_2$.
By the [[differentiation rule|HHNR31W3WD]] and the [[Plancherel theorem|HPZHRZ0502]], $\norm{f'}_2 = 2\pi \norm{\xi \hat f}_2$.
Squaring gives the inequality; translation in $x$ and modulation by $e^{2\pi i b x}$ give general $a$ and $b$, and a density argument gives all $f$ in [[$L^2(\R)$|SASP14MA1Z]].
Equality in Cauchy–Schwarz forces $f' = -2c x f$, whose solutions are Gaussians.

If one of the two integrals is infinite and $f \ne 0$, then the other is positive, so the left side is $+\infty$ and the inequality holds.

Example: for $f(x) = e^{-\pi x^2}$, one has $\hat f = f$, $\norm{f}_2^2 = 2^{-1/2}$ and $\int x^2 e^{-2\pi x^2}\, dx = \frac{1}{4\pi} 2^{-1/2}$, so the left side equals $\frac{1}{16\pi^2} \cdot \frac12 = \frac{\norm{f}_2^4}{16\pi^2}$.

## Explanations

### L1 human

If $\abs{f}^2$ is a probability density, its spread around a point $a$ and the spread of $\abs{\hat f}^2$ around a point $b$ cannot both be small.
Their product is at least $1/(16\pi^2)$.
In quantum mechanics, position and momentum are related by this Fourier transform, and the inequality becomes Heisenberg's uncertainty principle.

### L2 human

The proof is a commutator argument: the operators of multiplication by $x$ and of differentiation do not commute, and Cauchy–Schwarz turns this into a lower bound.
The same scheme gives the Robertson uncertainty relation for any two self-adjoint operators.
The inequality also follows from the entropic uncertainty principle, since among densities with a given variance the Gaussian has the largest entropy.
In $\R^n$ the analogous bound is $\norm{\abs{x} f}_2 \norm{\abs{\xi} \hat f}_2 \ge \frac{n}{4\pi} \norm{f}_2^2$.
