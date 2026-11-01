---
tag: YQ21C2N2HX
kind: definition
name: Hurwitz zeta function
msc: [11M35, 11M06]
defines: G4SW7HJG88
uses: [8MWTEF6462, 0M3YQJ81NB, 0ZZ7ZYDR8W, 1XWBY4N0VT, 7XB5VJKDPG]
sources:
  - url: https://en.wikipedia.org/wiki/Hurwitz_zeta_function
---

## Definition

Let $a$ be a real number with $a > 0$, and let $s$ be a complex number with $\operatorname{Re} s > 1$.
The *Hurwitz zeta function* is
$$\zeta(s, a) = \sum_{n=0}^{\infty} \frac{1}{(n + a)^{s}},$$
where $(n + a)^{s} = e^{s \log(n + a)}$ with the real logarithm.
The series converges absolutely for $\operatorname{Re} s > 1$.
For fixed $a$, the function $s \mapsto \zeta(s, a)$ has an [[analytic continuation|0M3YQJ81NB]] to a [[meromorphic function|0ZZ7ZYDR8W]] on $\C$, and this continuation is also written $\zeta(s, a)$.

## Remarks

For $a = 1$, the series is $\sum_{n \ge 1} n^{-s}$, so $\zeta(s, 1)$ is the [[Riemann zeta function|1XWBY4N0VT]] $\zeta(s)$.
For $a = 1/2$, the terms are $2^s (2n + 1)^{-s}$, so $\zeta(s, 1/2) = 2^s \sum_{m \text{ odd}} m^{-s} = (2^s - 1)\zeta(s)$.
The value $s = 1$ is not allowed in the series: there the terms behave like $1/n$ and the series diverges.
The continuation has a single pole, at $s = 1$; it is simple with residue $1$.
For a [[Dirichlet character|7XB5VJKDPG]] $\chi$ modulo $q$, grouping $n$ by its residue gives
$$L(s, \chi) = q^{-s} \sum_{r=1}^{q} \chi(r)\, \zeta\!\left(s, \frac{r}{q}\right).$$
Some authors also allow complex $a$ with $\operatorname{Re} a > 0$.
