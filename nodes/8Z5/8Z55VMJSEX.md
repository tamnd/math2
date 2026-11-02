---
tag: 8Z55VMJSEX
kind: statement
role: theorem
name: Cantor–Lebesgue theorem
msc: [42A63, 42A20]
uses: [FZK2M8KGXQ, 2Z2QVWZ262, WVKDC011KP, BYNV84PF86]
about: [FZK2M8KGXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Set_of_uniqueness
---

## Statement

Let $(a_n)_{n \ge 1}$ and $(b_n)_{n \ge 1}$ be real numbers.
Let $E \subset \R$ be a measurable set of positive [[Lebesgue measure|2Z2QVWZ262]].
Assume that $a_n \cos nx + b_n \sin nx \to 0$ as $n \to \infty$ for every $x \in E$.
Then $a_n \to 0$ and $b_n \to 0$.

## Remarks

Proof idea: write $a_n \cos nx + b_n \sin nx = \rho_n \cos(nx + \varphi_n)$ with $\rho_n = \sqrt{a_n^2 + b_n^2}$.
If $\rho_n \not\to 0$, then $\rho_{n_j} \ge \varepsilon > 0$ along a subsequence, so $\cos^2(n_j x + \varphi_{n_j}) \to 0$ on $E$.
Replace $E$ by a bounded subset of positive measure.
By [[dominated convergence|BYNV84PF86]], $\int_E \cos^2(n_j x + \varphi_{n_j}) \, dx \to 0$.
But this integral equals $\frac{1}{2} \abs{E} + \frac{1}{2} \int_E \cos(2 n_j x + 2 \varphi_{n_j}) \, dx$, and the last integral tends to $0$ by the [[Riemann–Lebesgue lemma|WVKDC011KP]], a contradiction.

In complex form: if $c_n e^{inx} + c_{-n} e^{-inx} \to 0$ for every $x$ in a set of positive measure, then $c_n \to 0$ as $\abs{n} \to \infty$.
So a [[trigonometric series|FZK2M8KGXQ]] that converges on a set of positive measure has coefficients tending to $0$.

Example: if $\sum_n (a_n \cos nx + b_n \sin nx)$ converges for every $x$ in $[0, 1]$, its terms tend to $0$ there, so $a_n, b_n \to 0$.

Positive measure is needed: at the single point $x = 0$ the terms $n \sin nx$ are all $0$, but $b_n = n \not\to 0$.

## Explanations

### L1 human

If a sequence of waves with amplitudes $\rho_n$ dies out at every point of a set of positive length, then the amplitudes themselves must go to $0$.
A wave of large amplitude cannot be small on a large set, because it oscillates and spends a fixed fraction of the time far from $0$.

### L2 human

The theorem is the first step in the proof of [[Cantor's uniqueness theorem|NSS3XW4BYZ]].
It reduces questions about convergent trigonometric series to series whose coefficients tend to $0$, where Riemann's methods apply.
Its proof is a typical use of the Riemann–Lebesgue lemma together with a convergence theorem for integrals.
