---
tag: HN0AXS6VSG
kind: definition
name: Dirichlet series
msc: [11M41, 30B50]
defines: 8MWTEF6462
uses: [0NM626FH6Q, 0YBDSJARWN, 07GJV36896]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet_series
---

## Definition

Let $a \colon \set{1, 2, 3, \dots} \to \C$ be a function, called an arithmetic function.
For $s \in \C$ and an integer $n \ge 1$, let $n^{-s} = e^{-s \log n}$, using the [[complex exponential|07GJV36896]].
The *Dirichlet series* of $a$ is the [[series|0NM626FH6Q]]
$$F(s) = \sum_{n=1}^{\infty} \frac{a(n)}{n^s},$$
considered as a function of $s$ at the points where it converges.

## Remarks

Let $\sigma_a$ be the infimum of the real $\sigma$ such that $\sum_n \abs{a(n)} n^{-\sigma}$ converges, the abscissa of [[absolute convergence|0YBDSJARWN]].
The series converges absolutely for $\operatorname{Re} s > \sigma_a$ and defines a holomorphic function there.
It also has an abscissa of convergence $\sigma_c$, with $\sigma_c \le \sigma_a \le \sigma_c + 1$.
Example: for $a(n) = (-1)^{n+1}$, the series $\sum (-1)^{n+1} n^{-s}$ converges for $\operatorname{Re} s > 0$ and converges absolutely for $\operatorname{Re} s > 1$, so $\sigma_c = 0$ and $\sigma_a = 1$.
Non-example: the power series $\sum_{n} a_n z^n$ is not a Dirichlet series, since its terms are powers $z^n$ of the variable rather than $n^{-s}$.
If $F$ and $G$ are the Dirichlet series of $a$ and $b$, both absolutely convergent at $s$, then $F(s) G(s)$ is the Dirichlet series of the [[Dirichlet convolution|037F589D1D]] $a * b$ at $s$.
For example $\sum_n \mu(n) n^{-s} = 1/\zeta(s)$ for $\operatorname{Re} s > 1$, with $\mu$ the [[Möbius function|0FANE7P0DY]].
