---
tag: 4JWHKNGS4Y
kind: definition
name: Character sum
msc: [11L40, 11L10]
defines: VTYJ9419C7
uses: [7XB5VJKDPG]
sources:
  - url: https://en.wikipedia.org/wiki/Character_sum
---

## Definition

Let $q \ge 1$ be an integer, and let $\chi$ be a [[Dirichlet character|7XB5VJKDPG]] modulo $q$.
Let $M$ be an integer and $N \ge 1$.
The *character sum* of $\chi$ over the interval $(M, M + N]$ is
$$S_\chi(M, N) = \sum_{n = M + 1}^{M + N} \chi(n).$$
More generally, a character sum is a sum $\sum_{n \in A} \chi(f(n))$ over a finite set $A$ of integers, where $f$ is a polynomial with integer coefficients.

## Remarks

Example: let $\chi$ be the Legendre symbol modulo $5$, so $\chi(1) = \chi(4) = 1$, $\chi(2) = \chi(3) = -1$ and $\chi(5) = 0$.
Then $S_\chi(0, 3) = 1 - 1 - 1 = -1$ and $S_\chi(0, 5) = 0$.
Non-example: the sum $\sum_{n \le N} \mu(n)$ of the [[Möbius function|0FANE7P0DY]] is not a character sum, since $\mu$ is not a Dirichlet character: $\mu(4) = 0$ but $\mu(2)\mu(2) = 1$, so $\mu$ is not completely multiplicative.
Orthogonality gives the complete sum: $S_\chi(M, q) = 0$ if $\chi$ is not principal, and $S_\chi(M, q) = \varphi(q)$ if $\chi$ is principal, where $\varphi$ is [[Euler's totient function|0DAMHCT17R]].
Thus $\abs{S_\chi(M, N)} \le \varphi(q)$ for every nonprincipal $\chi$.
The Pólya–Vinogradov inequality improves this to $\abs{S_\chi(M, N)} \le C \sqrt{q} \log q$ for nonprincipal $\chi$, with an absolute constant $C$.
