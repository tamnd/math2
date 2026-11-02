---
tag: ZY724M2NKQ
kind: definition
name: Fundamental solution
msc: [35A08, "35E05"]
defines: K2NK9A8M5F
uses: [6DZETZ5T9G, HS65DW0HXH, 0KPHENZ5S7]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_solution
---

## Definition

Let $P = \sum_{\abs{\alpha} \le m} a_\alpha(x) \partial^\alpha$ be a [[linear differential operator|6DZETZ5T9G]] on $\R^n$ with smooth coefficients.
A distribution is a continuous linear functional on the space of [[test functions|HS65DW0HXH]] on $\R^n$.
Let $\delta$ be the [[Dirac delta|0KPHENZ5S7]] at the origin, the distribution $\delta(\varphi) = \varphi(0)$.
A *fundamental solution* of $P$ is a distribution $E$ on $\R^n$ with $P E = \delta$ in the sense of distributions.
Explicitly, this means $E\left(P^{t} \varphi\right) = \varphi(0)$ for every test function $\varphi$, where $P^{t} \varphi = \sum_{\abs{\alpha} \le m} (-1)^{\abs{\alpha}} \partial^\alpha (a_\alpha \varphi)$ is the formal transpose of $P$.

## Remarks

Example: on $\R$, the Heaviside function $H$, with $H(x) = 1$ for $x > 0$ and $H(x) = 0$ for $x < 0$, is a fundamental solution of $P = d/dx$.
Indeed, for a test function $\varphi$ one has $H(-\varphi') = -\int_0^\infty \varphi'(x) \, dx = \varphi(0)$.
Example: on $\R^3$, $E(x) = -1/(4 \pi \abs{x})$ is a fundamental solution of the [[Laplacian|0E0B6RA8K0]], and on $\R^2$, $E(x) = \frac{1}{2\pi} \log \abs{x}$ is one.
Non-example: on $\R$, the constant function $1$ is not a fundamental solution of $d/dx$, since its derivative is $0$ and not $\delta$.
A fundamental solution is not unique: adding any distribution $F$ with $P F = 0$ gives another one.
If $P$ has constant coefficients and $f$ is a test function, then $u = E * f$ is smooth and solves $P u = f$.
Every nonzero operator with constant coefficients has a fundamental solution, by the [[Malgrange–Ehrenpreis theorem|3173Y813V7]].

## Explanations

### L1 human

A fundamental solution is a solution of the equation with a unit point source at the origin as right-hand side.
