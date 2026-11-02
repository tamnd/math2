---
tag: 74DV24XGKZ
kind: definition
name: Euler–Poisson equation for higher derivatives
msc: [49K05, 34B15]
defines: XBNAJ1RRET
uses: [JRQZ803Q5Y, PS0VV149ET, 09EGC6F8PT]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%E2%80%93Lagrange_equation
---

## Definition

Let $k \ge 1$ and $a < b$.
Let $L \colon [a, b] \times \R^{k+1} \to \R$, written $L(x, z_0, z_1, \dots, z_k)$, be a function of class $C^{k+1}$, and write $L_{z_j}$ for its [[partial derivative|09EGC6F8PT]] in $z_j$.
Consider the functional
$$J(y) = \int_a^b L\big(x, y(x), y'(x), \dots, y^{(k)}(x)\big) \, dx.$$
The *Euler–Poisson equation* of $J$ is the equation
$$\sum_{j=0}^{k} (-1)^j \frac{d^j}{dx^j} \Big( L_{z_j}\big(x, y(x), y'(x), \dots, y^{(k)}(x)\big) \Big) = 0, \qquad a \le x \le b,$$
for an unknown $y \in C^{2k}([a, b])$.

## Remarks

For $k = 1$ it is the [[Euler–Lagrange equation|PS0VV149ET]] $L_{z_0} - \frac{d}{dx} L_{z_1} = 0$ of an [[integral functional|JRQZ803Q5Y]].
A minimiser $y \in C^{2k}([a, b])$ of $J$ among functions with prescribed $y^{(j)}(a)$ and $y^{(j)}(b)$ for $0 \le j \le k - 1$ solves it.
To see this, take variations $\eta$ with $\eta^{(j)}(a) = \eta^{(j)}(b) = 0$ for $j < k$, integrate the term with $\eta^{(j)}$ by parts $j$ times, and apply the fundamental lemma of the calculus of variations.

Example: for $k = 2$ and $L = \frac{1}{2} z_2^2$, one has $L_{z_0} = L_{z_1} = 0$ and $L_{z_2} = z_2$, so the equation is $y'''' = 0$.
Every cubic polynomial solves it.
Non-example: $y(x) = x^4$ does not solve this equation, since $y'''' = 24$.
