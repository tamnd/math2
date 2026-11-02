---
tag: FEZ2HAFZTM
kind: definition
name: Ramanujan theta function
msc: [11F27, 33D15]
defines: 1CBZA8MQJW
uses: [09FTAET5Z4, Y1X8ZZQ7VM]
sources:
  - url: https://en.wikipedia.org/wiki/Ramanujan_theta_function
---

## Definition

Let $a, b \in \C \setminus \set{0}$ with $\abs{ab} < 1$.
*Ramanujan's general theta function* is
$$f(a, b) = \sum_{n=-\infty}^{\infty} a^{n(n+1)/2}\, b^{n(n-1)/2}.$$
Its standard special cases, for $q \in \C$ with $\abs{q} < 1$, are
$$\varphi(q) = f(q, q), \qquad \psi(q) = f(q, q^3), \qquad f(-q) = f(-q, -q^2).$$

## Remarks

The series converges absolutely: for $n \ge 0$ the term is $(ab)^{n(n-1)/2} a^n$, and for $n < 0$ it is $(ab)^{m(m-1)/2} b^{m}$ with $m = -n$, so the terms decay like $\abs{ab}^{n^2/2}$.
Replacing $n$ by $-n$ shows $f(a, b) = f(b, a)$.
The [[Jacobi triple product|JFP2DGMNXT]] gives $f(a, b) = (-a; ab)_\infty\, (-b; ab)_\infty\, (ab; ab)_\infty$ with the [[q-Pochhammer symbol|Y1X8ZZQ7VM]].

Example: $\psi(q) = \sum_{n \in \Z} q^{n(n+1)/2 + 3n(n-1)/2} = \sum_{n \in \Z} q^{2n^2 - n}$.
The exponents for $n = 0, 1, -1, 2, -2, \dots$ are $0, 1, 3, 6, 10, \dots$, the triangular numbers, each once, so $\psi(q) = \sum_{k \ge 0} q^{k(k+1)/2}$.
Also $f(-q) = \sum_{n \in \Z} (-1)^n q^{n(3n-1)/2} = (q; q)_\infty$, by [[Euler's pentagonal number theorem|R587SR9GNV]].

Non-example: $f(a, b)$ is not defined for $a = b = 1$, since $\abs{ab} = 1$ and the series $\sum_{n \in \Z} 1$ diverges.

In the notation of the Jacobi theta function, $f(q e^{2iz}, q e^{-2iz}) = \vartheta_3(z, q)$.
