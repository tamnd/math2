---
tag: 24GAZHVTGB
kind: definition
name: Dirichlet L-function
msc: [11M06]
defines: 9D2Z543EJQ
uses: [7XB5VJKDPG, 8MWTEF6462, 0ZZ7ZYDR8W, 0M3YQJ81NB, 0G4F0XB9X2]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet_L-function
---

## Definition

Let $q \ge 1$ be an integer and let $\chi$ be a [[Dirichlet character|7XB5VJKDPG]] modulo $q$.
For $s \in \C$ with $\operatorname{Re} s > 1$, the [[Dirichlet series|8MWTEF6462]]
$$L(s, \chi) = \sum_{n=1}^{\infty} \frac{\chi(n)}{n^s}$$
converges absolutely and defines a holomorphic function of $s$.
The *Dirichlet L-function* of $\chi$ is the [[analytic continuation|0M3YQJ81NB]] of this function to a [[meromorphic function|0ZZ7ZYDR8W]] on $\C$, also written $L(s, \chi)$.
If $\chi$ is not principal, $L(s, \chi)$ is an [[entire function|0G4F0XB9X2]].
If $\chi = \chi_0$ is principal, $L(s, \chi_0)$ has a single pole, a simple pole at $s = 1$.

## Remarks

For $\operatorname{Re} s > 1$ there is an Euler product $L(s, \chi) = \prod_p (1 - \chi(p) p^{-s})^{-1}$ over the primes $p$.
For the principal character, $L(s, \chi_0) = \zeta(s) \prod_{p \mid q} (1 - p^{-s})$, where $\zeta$ is the [[Riemann zeta function|1XWBY4N0VT]].
Example: for the nonprincipal character $\chi$ modulo $4$, the series at $s = 1$ converges and $L(1, \chi) = 1 - \frac{1}{3} + \frac{1}{5} - \cdots = \frac{\pi}{4}$, by the [[Leibniz formula for pi|037FD5NBRT]].
Non-example: $\sum_{n} (-1)^{n+1} n^{-s}$ is a Dirichlet series with $2$-periodic coefficients, but it is not a Dirichlet L-function, since $f(n) = (-1)^{n+1}$ is not a Dirichlet character: $f(4) = -1 \ne 1 = f(2) f(2)$.
For a primitive character the completed L-function satisfies a functional equation relating $s$ and $1 - s$, as for the zeta function.
