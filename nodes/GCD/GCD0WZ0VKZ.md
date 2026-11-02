---
tag: GCD0WZ0VKZ
kind: definition
name: Conjugate function
msc: [42A50, 31A05]
defines: A1H48DDW49
uses: [050F2FMTKF, 0SYR10HD4R, G12KXDHPPS, DWJF7ABPR1]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_conjugate
---

## Definition

Let $\mathbb{T} = \R / 2\pi\Z$ be the circle, and let $f \colon \mathbb{T} \to \C$ be [[Lebesgue integrable|DWJF7ABPR1]].
The *conjugate function* of $f$ is the function $\tilde f$ on $\mathbb{T}$ given by the [[principal value|0SYR10HD4R]]
$$\tilde f(\theta) = \lim_{\varepsilon \to 0^+} \frac{1}{2\pi} \int_{\varepsilon \le \abs{t} \le \pi} f(\theta - t) \cot\frac{t}{2} \, dt.$$
The limit exists for almost every $\theta \in \mathbb{T}$.

## Remarks

If $f$ is a trigonometric polynomial with [[Fourier series|G12KXDHPPS]] $\sum_k \hat f(k) e^{ik\theta}$, then
$$\tilde f(\theta) = \sum_k (-i \sgn k) \, \hat f(k) e^{ik\theta},$$
with $\sgn 0 = 0$.
For real $f$, let $u$ be the Poisson integral of $f$ in the unit disc, and let $v$ be its [[harmonic conjugate|050F2FMTKF]] with $v(0) = 0$.
Then $v(re^{i\theta}) \to \tilde f(\theta)$ as $r \to 1^-$ for almost every $\theta$.

Example: $f(\theta) = \cos\theta$ has $\tilde f(\theta) = \sin\theta$.
Check: $\cos(\theta - t)\cot(t/2) = \cos\theta \cos t \cot(t/2) + \sin\theta \sin t \cot(t/2)$.
The first term is odd in $t$, so its principal value integral is $0$.
The second uses $\sin t \cot(t/2) = 2\cos^2(t/2) = 1 + \cos t$, whose integral over $[-\pi, \pi]$ is $2\pi$.

Non-example: the integral without the principal value need not exist.
For $f = 1$ near $\theta$ the integrand behaves like $2/t$ near $t = 0$, which is not integrable, while the symmetric limit is $0$ since $\cot(t/2)$ is odd.

The function $\tilde f$ need not be integrable when $f$ is: the operator $f \mapsto \tilde f$ is bounded on $L^p(\mathbb{T})$ only for $1 < p < \infty$.
