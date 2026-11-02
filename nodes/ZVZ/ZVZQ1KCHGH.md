---
tag: ZVZQ1KCHGH
kind: definition
name: Partial difference equation
msc: [39A14]
defines: 4B7M4A1MH0
uses: [0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Recurrence_relation
---

## Definition

Let $d \ge 2$, let $\Omega \subseteq \Z^d$, and let $a_1, \dots, a_r \in \Z^d$ be fixed shift vectors.
Let $F \colon \Omega \times \R^{r} \to \R$ be a given [[function|0EPAT51DXQ]].
A *partial difference equation* for an unknown function $u \colon \Z^d \to \R$ is a condition of the form
$$F\big(m, u(m + a_1), u(m + a_2), \dots, u(m + a_r)\big) = 0 \quad \text{for all } m \in \Omega.$$
A *solution* is a function $u$ that satisfies it for every $m \in \Omega$.

## Remarks

Example: the explicit scheme for the heat equation,
$$u(j, n+1) = u(j, n) + \lambda \big( u(j+1, n) - 2u(j, n) + u(j-1, n) \big), \qquad (j, n) \in \Z \times \N,$$
with a constant $\lambda > 0$, is a partial difference equation with $d = 2$ and shifts $(0, 1), (0, 0), (1, 0), (-1, 0)$.

Non-example: $u(n+2) = u(n+1) + u(n)$ for $u \colon \Z \to \R$ involves only one integer variable, so $d = 1$ and it is an ordinary difference equation.

One may also take $u$ defined only on a subset of $\Z^d$ that contains all the points $m + a_i$, as in the heat scheme on $\Z \times \N$.
For example, the binomial coefficients $c(n, k) = \binom{n}{k}$ on $\N^2$ satisfy $c(n+1, k+1) = c(n, k) + c(n, k+1)$.
The values may also lie in another field or ring instead of $\R$.
