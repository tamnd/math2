---
tag: X3C49PZV9J
kind: statement
role: theorem
name: Hasse's theorem
sources:
  - wikipedia: en:3596006@r1375174347
    locator: Schoof's algorithm, section Hasse's theorem
    note: adopted
    mention: wikipedia://en/3596006#VFL3
    sections: [Statement]
inventory: [YTCJ98PGCG]
---

## Statement

Hasse's theorem states that if $E/\mathbb{F}_{q}$ is an elliptic curve over the finite field $\mathbb{F}_{q}$, then $\# E(\mathbb{F}_q)$ satisfies

$$\mid q + 1 - \# E(\mathbb{F}_{q}) \mid \leq 2\sqrt{q}.$$

This powerful result, given by Hasse in 1934, simplifies our problem by narrowing down $\# E(\mathbb{F}_{q})$ to a finite (albeit large) set of possibilities. Defining $t$ to be $q + 1 - \# E(\mathbb{F}_{q})$, and making use of this result, we now have that computing the value of $t$ modulo $N$ where $N > 4\sqrt{q}$, is sufficient for determining $t$, and thus $\# E(\mathbb{F}_{q})$. While there is no efficient way to compute $t \pmod N$ directly for general $N$, it is possible to compute $t \pmod l$ for $l$ a small prime, rather efficiently. We choose $S=\{l_1,l_2,...,l_r\}$ to be a set of distinct primes such that $\prod l_i = N > 4\sqrt{q}$. Given $t \pmod {l_i}$ for all $l_i\in S$, the [[Chinese remainder theorem|0FNN9B4W64]] allows us to compute $t \pmod N$.

In order to compute $t \pmod l$ for a prime $l \neq p$, we make use of the theory of the Frobenius endomorphism $\phi$ and division polynomials. Note that considering primes $l \neq p$ is no loss since we can always pick a bigger prime to take its place to ensure the product is big enough. In any case Schoof's algorithm is most frequently used in addressing the case $q=p$ since there are more efficient, so called $p$ adic algorithms for small-characteristic fields.
