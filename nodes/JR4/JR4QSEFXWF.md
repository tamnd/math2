---
tag: JR4QSEFXWF
kind: definition
name: Dirichlet character
msc: [11A25, 11M06]
defines: 7XB5VJKDPG
uses: [0VZ48N083F, 0RXKW044R4, 03VFZ2WETT, 0JYTG5K9Y4]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet_character
---

## Definition

Let $q \ge 1$ be an integer.
A *Dirichlet character modulo $q$* is a function $\chi \colon \Z \to \C$ such that:

1. $\chi(n + q) = \chi(n)$ for all $n \in \Z$.
2. $\chi(n) = 0$ if $\gcd(n, q) > 1$, and $\chi(n) \ne 0$ if $\gcd(n, q) = 1$.
3. $\chi(mn) = \chi(m)\chi(n)$ for all $m, n \in \Z$.

The *principal character* $\chi_0$ modulo $q$ has $\chi_0(n) = 1$ for $n$ [[coprime|0VZ48N083F]] to $q$ and $\chi_0(n) = 0$ otherwise.

## Remarks

Example: for $q = 4$, let $\chi(n) = 0$ for even $n$, $\chi(n) = 1$ for $n \equiv 1$ and $\chi(n) = -1$ for $n \equiv 3 \pmod 4$.
Clauses 1 and 2 are clear.
For clause 3 it suffices to check odd classes: $1 \cdot 1 \equiv 1$, $1 \cdot 3 \equiv 3$ and $3 \cdot 3 \equiv 1 \pmod 4$ match $1 \cdot 1 = 1$, $1 \cdot (-1) = -1$ and $(-1)(-1) = 1$.
Non-example: for $q = 3$, the function $f(n) = r$, where $r \in \set{0, 1, 2}$ is the remainder of $n$ modulo $3$, satisfies clauses 1 and 2 but not clause 3, since $f(2 \cdot 2) = f(4) = 1 \ne 4 = f(2) f(2)$.
Equivalently, a Dirichlet character modulo $q$ is a [[group homomorphism|0JYTG5K9Y4]] $(\Z/q\Z)^\times \to \C^\times$ from the unit group of the [[integers modulo q|03VFZ2WETT]], extended by $0$ on the classes not coprime to $q$.
Hence each value $\chi(n)$ with $\gcd(n, q) = 1$ is a $\varphi(q)$-th root of unity, and there are exactly $\varphi(q)$ characters modulo $q$, where $\varphi$ is [[Euler's totient function|0DAMHCT17R]].
Each Dirichlet character is a [[completely multiplicative function|0RXKW044R4]].
The Legendre symbol $n \mapsto (n/p)$ is a Dirichlet character modulo an odd prime $p$.
