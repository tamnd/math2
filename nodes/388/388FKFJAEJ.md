---
tag: 388FKFJAEJ
kind: definition
name: Index of a singular integral operator
msc: ["45E05", 47A53]
defines: GW3B4K1WA5
uses: [E30EA6ETZ4, 0NQSV2EWDR, 012PBA0FMD]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_integral_operators_on_closed_curves
---

## Definition

Let $\Gamma$ be a smooth simple closed curve in $\C$, oriented counterclockwise.
Let $a$ and $b$ be [[Hölder continuous|012PBA0FMD]] functions on $\Gamma$ with $a(t)^2 - b(t)^2 \ne 0$ for all $t \in \Gamma$, and let $k$ be a Hölder continuous function on $\Gamma \times \Gamma$.
Consider the singular integral operator of a [[singular integral equation|E30EA6ETZ4]] of normal type
$$K \varphi(t) = a(t) \, \varphi(t) + \frac{b(t)}{\pi i} \, \mathrm{p.v.} \int_\Gamma \frac{\varphi(\tau)}{\tau - t} \, d\tau + \int_\Gamma k(t, \tau) \, \varphi(\tau) \, d\tau, \quad t \in \Gamma.$$
The *index* of $K$ is the integer
$$\kappa = \frac{1}{2\pi} \Big[ \arg \frac{a(t) - b(t)}{a(t) + b(t)} \Big]_\Gamma.$$
Here the bracket is the change of a continuous branch of the argument of $(a - b)/(a + b)$ after one run of $t$ around $\Gamma$.
In other words, $\kappa$ is the [[winding number|0NQSV2EWDR]] around $0$ of the closed curve $t \mapsto (a(t) - b(t))/(a(t) + b(t))$.

## Remarks

The condition $a^2 - b^2 \ne 0$ says that $a - b$ and $a + b$ do not vanish, so the quotient is a nonvanishing continuous function on $\Gamma$ and its winding number is defined.
Example: on the unit circle, $a(t) = (t + 1)/2$ and $b(t) = (t - 1)/2$ give $a + b = t$ and $a - b = 1$, so $a^2 - b^2 = t \ne 0$.
The quotient is $1/t = e^{-i\theta}$ for $t = e^{i\theta}$, whose argument decreases by $2\pi$, so $\kappa = -1$.
Example: for $a = 0$ and $b = 1$ the quotient is the constant $-1$, so $\kappa = 0$.
Non-example: $a = b = 1$ violates $a^2 - b^2 \ne 0$; the quotient is $0$ everywhere, and no index is defined.
The index does not depend on $k$, and it is additive: the index of a product of two such operators is the sum of their indices.
