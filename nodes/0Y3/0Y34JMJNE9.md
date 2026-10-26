---
tag: 0Y34JMJNE9
kind: statement
role: theorem
name: Gauss–Wantzel theorem
msc: [12F05]
uses: [0FMN2MN7TM, 0SK1VHZ5R2, 0SSSM1D475]
sources:
  - url: https://en.wikipedia.org/wiki/Constructible_polygon
    locator: Conditions for constructibility
---

## Statement

Let $n \ge 3$.
The regular $n$-gon can be constructed with straightedge and compass if and only if $n = 2^k p_1 p_2 \cdots p_t$, with $k, t \ge 0$ and $p_1, \dots, p_t$ distinct Fermat primes.

## Remarks

A Fermat prime is a prime number of the form $2^{2^m} + 1$. The known Fermat primes are $3, 5, 17, 257$ and $65537$.
The regular $n$-gon is constructible if and only if $e^{2\pi i/n}$ is a [[constructible number|0FMN2MN7TM]]. Its degree over $\mathbb{Q}$ is $\varphi(n)$, by the [[irreducibility of $\Phi_n$|0SK1VHZ5R2]].
The condition on $n$ holds if and only if $\varphi(n)$ is a power of $2$.
So the $17$-gon and the $15$-gon are constructible, but the $7$-gon and the $9$-gon are not.

## History

Carl Friedrich Gauss proved in 1796 that the regular $17$-gon is constructible.
In his 1801 book Disquisitiones Arithmeticae, he gave the sufficient condition.
Pierre Wantzel gave a full proof of the necessity in 1837.

## Explanations

### L1 human

The theorem tells exactly which regular polygons you can draw with straightedge and compass.
The answer depends on the prime factors of the number of sides.
Only Fermat primes, each used at most once, and powers of $2$ are allowed.
