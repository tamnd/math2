---
tag: AEABS105PS
kind: definition
name: Direct and inverse theorems of approximation
msc: [41A25, 41A27, 42A10]
defines: TDKKST5AWA
uses: [YDN0T4MEX0, AXCJBSQZWF, J3NJQ5FZJ5, 012PBA0FMD]
sources:
  - url: https://en.wikipedia.org/wiki/Jackson%27s_inequality
---

## Definition

Let $X$ be a normed space of functions and let $V_0 \subseteq V_1 \subseteq \cdots$ be subspaces of $X$.
For $f \in X$ let $E_n(f) = \inf_{v \in V_n} \norm{f - v}$ be the [[error of best approximation|YDN0T4MEX0]].
Let $\Omega(f, \delta)$, for $\delta > 0$, be a measure of smoothness of $f$, such as a [[modulus of continuity|AXCJBSQZWF]].

1. A *direct theorem* is an inequality $E_n(f) \le C \, \Omega(f, 1/n)$ for all $f \in X$ and $n \ge 1$, with $C$ independent of $f$ and $n$.
2. An *inverse theorem* is an implication that bounds $\Omega(f, \delta)$ in terms of the sequence $(E_n(f))_{n \ge 0}$.

## Remarks

Example: let $X$ be the continuous $2\pi$-periodic functions with the uniform norm, and $V_n$ the [[trigonometric polynomials|J3NJQ5FZJ5]] of degree at most $n$.
Jackson's inequality $E_n(f) \le C \, \omega(f, 1/n)$, with $\omega$ the modulus of continuity, is a direct theorem.
Bernstein's theorem, that $E_n(f) \le M n^{-\alpha}$ for all $n \ge 1$ with $0 < \alpha < 1$ implies $\omega(f, \delta) \le M' \delta^{\alpha}$, is an inverse theorem.
Combined, they say that $E_n(f) = O(n^{-\alpha})$ if and only if $f$ is [[Hölder continuous|012PBA0FMD]] with exponent $\alpha$.

Non-example: the bound $E_n(f) \le \norm{f}$, from $0 \in V_n$, is not a direct theorem.
It does not involve any smoothness of $f$ and gives no rate as $n \to \infty$.

Inverse theorems usually rest on inequalities of Bernstein type for the derivatives of elements of $V_n$.
Direct theorems usually rest on good approximating operators, such as convolution with the Jackson kernel.
