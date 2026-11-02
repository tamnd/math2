---
tag: 7TVFY6NZDB
kind: definition
name: Weak Lp space
msc: ["46E30", 42B35]
defines: H4C888M5AZ
uses: [P15VQS5DJ9, YYNCJSR0PJ, HQVXKEMN5N, RARTMA0ZEC]
sources:
  - url: https://en.wikipedia.org/wiki/Lorentz_space
---

## Definition

Let $(X, \Sigma, \mu)$ be a [[measure space|P15VQS5DJ9]] and let $0 < p < \infty$.
For a [[measurable function|YYNCJSR0PJ]] $f$ on $X$ with real or complex values, let
$$\norm{f}_{p,\infty} = \sup_{t > 0} \, t \, \mu(\set{x \in X : \abs{f(x)} > t})^{1/p}.$$
The *weak $L^p$ space* $L^{p,\infty}(\mu)$ is the set of measurable functions $f$ with $\norm{f}_{p,\infty} < \infty$, modulo equality [[almost everywhere|RARTMA0ZEC]].

## Remarks

Example: on $\R^n$ with Lebesgue measure, $f(x) = \abs{x}^{-n/p}$ lies in $L^{p,\infty}$.
The set $\set{\abs{f} > t}$ is the open ball of radius $t^{-p/n}$, with measure $\omega_n t^{-p}$, where $\omega_n$ is the volume of the unit ball.
So $\norm{f}_{p,\infty} = \omega_n^{1/p}$, while $\int \abs{f}^p \, dx = \int \abs{x}^{-n} \, dx = \infty$.

Non-example: on $(0, 1)$ with Lebesgue measure, $g(x) = x^{-2}$ is not in $L^{1,\infty}$.
For $t > 1$, $\set{g > t} = (0, t^{-1/2})$, so $t \, \mu(\set{g > t}) = t^{1/2}$, which is unbounded.

Chebyshev's inequality $t^p \mu(\set{\abs{f} > t}) \le \int \abs{f}^p \, d\mu$ gives $\norm{f}_{p,\infty} \le \norm{f}_p$, so $L^p \subseteq L^{p,\infty}$.
The map $\norm{\cdot}_{p,\infty}$ is a quasinorm, not a norm.
The triangle inequality holds only with a constant: $\norm{f + g}_{p,\infty} \le \max(2, 2^{1/p}) (\norm{f}_{p,\infty} + \norm{g}_{p,\infty})$.
It follows from $\set{\abs{f + g} > t} \subseteq \set{\abs{f} > t/2} \cup \set{\abs{g} > t/2}$.
