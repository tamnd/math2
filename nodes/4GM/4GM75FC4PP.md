---
tag: 4GM75FC4PP
kind: definition
name: Maass wave form
msc: [11F37, 11F12, 11F72]
defines: 3R959YSNYP
uses: [X6XGGH5FPW, VEKV1EM77B, 1H6R856P3C, 0V33BNKZ9S, 0BQAA2BK3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Maass_wave_form
---

## Definition

Let $\mathbb{H} = \set{z = x + iy : y > 0}$ be the [[upper half-plane|X6XGGH5FPW]].
Let $\Gamma$ be a [[congruence subgroup|1H6R856P3C]] of $\mathrm{SL}_2(\Z)$, acting on $\mathbb{H}$ by $\gamma z = \frac{az + b}{cz + d}$ for $\gamma = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$.
Let $\Delta = -y^2 \left( \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} \right)$ be the hyperbolic Laplace operator.
A *Maass wave form* for $\Gamma$ is a [[smooth function|0V33BNKZ9S]] $f \colon \mathbb{H} \to \C$ such that:

1. $f(\gamma z) = f(z)$ for all $\gamma \in \Gamma$ and $z \in \mathbb{H}$.
2. There is $\lambda \in \C$ with $\Delta f = \lambda f$.
3. $f$ has moderate growth at every cusp: for every $\sigma \in \mathrm{SL}_2(\Z)$ there is $N > 0$ with $f(\sigma z) = O(y^N)$ as $y \to \infty$, uniformly in $x$.

The number $\lambda$ is the [[eigenvalue|0BQAA2BK3Q]] of $f$.
A *Maass cusp form* is a Maass form whose constant term $\int_0^1 f(\sigma(x + iy)) \, dx$ vanishes at every cusp, that is, for every $\sigma \in \mathrm{SL}_2(\Z)$.

## Remarks

Example: for $\Gamma = \mathrm{SL}_2(\Z)$ and $\mathrm{Re}(s) > 1$, the real-analytic Eisenstein series
$$E(z, s) = \frac{1}{2} \sum_{\substack{(c, d) \in \Z^2 \\ \gcd(c, d) = 1}} \frac{y^s}{\abs{cz + d}^{2s}}$$
is a Maass form with eigenvalue $s(1 - s)$.
Each term is $(\mathrm{Im}\, \gamma z)^s$ for a matrix $\gamma$ with bottom row $(c, d)$, so the sum is $\Gamma$-invariant, and $\Delta y^s = -y^2 s(s-1) y^{s-2} = s(1-s) y^s$ term by term.
It is not a cusp form, since its constant term is $y^s + \varphi(s) y^{1-s}$ for some function $\varphi$.

Non-example: $f(z) = y^s$ satisfies clauses 2 and 3 and is invariant under $z \mapsto z + 1$, but it is not invariant under $z \mapsto -1/z$, so clause 1 fails.

A cusp form decays rapidly at the cusps and is square-integrable on $\Gamma \backslash \mathbb{H}$; the eigenvalue of a nonzero Maass cusp form is then real and positive.
One often writes $\lambda = \frac{1}{4} + r^2$ or $\lambda = s(1 - s)$.
Some authors also allow a weight or a character in clause 1.
