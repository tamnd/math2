---
tag: ZBXBQYKP5W
kind: definition
name: Littlewood–Paley square function
msc: [42B25]
defines: H4E1PW67Z1
uses: [D1PAT0K446, SASP14MA1Z, DPVM34ADZV]
sources:
  - url: https://en.wikipedia.org/wiki/Littlewood%E2%80%93Paley_theory
---

## Definition

Let $n \ge 1$, and let $\chi$, $\psi$ and $\Delta_j$, $j \in \Z$, be as in the [[Littlewood–Paley decomposition|D1PAT0K446]] on $\R^n$.
Let $f$ be in the [[Lp space|SASP14MA1Z]] $L^p(\R^n)$ for some $1 \le p \le \infty$.
The *Littlewood–Paley square function* of $f$ is the function $Sf \colon \R^n \to [0, \infty]$ given by
$$Sf(x) = \left( \sum_{j \in \Z} \abs{\Delta_j f(x)}^2 \right)^{1/2}.$$

## Remarks

The operator $f \mapsto Sf$ is not linear, but it is sublinear: $S(f + g) \le Sf + Sg$, by the triangle inequality in $\ell^2$.
It depends on the choice of $\chi$, but the $L^p$ norms of square functions built from two choices are comparable for $1 < p < \infty$.

Example: assume moreover that $\chi$ is radial and nonincreasing in $\abs{\xi}$, so that $\psi \ge 0$.
For each $\xi \ne 0$ at most two of the numbers $\psi(2^{-j}\xi)$ are nonzero, and they sum to $1$.
So $\frac{1}{2} \le \sum_j \psi(2^{-j}\xi)^2 \le 1$.
By Plancherel's theorem for the [[Fourier transform|DPVM34ADZV]], $\norm{Sf}_2^2 = \int \sum_j \psi(2^{-j}\xi)^2 \abs{\hat f(\xi)}^2 \, d\xi$, hence $\frac{1}{2}\norm{f}_2^2 \le \norm{Sf}_2^2 \le \norm{f}_2^2$ for $f \in L^2(\R^n)$.

Non-example: the constant function $1$ is not in any $L^p(\R^n)$ with $p < \infty$.
As a tempered distribution its Fourier transform is the point mass at $0$, and $\psi(0) = 0$, so every $\Delta_j 1$ vanishes and the formula gives $S1 = 0$ although $1 \ne 0$.
This is why the comparison of $\norm{Sf}_p$ and $\norm{f}_p$ needs $p < \infty$.
