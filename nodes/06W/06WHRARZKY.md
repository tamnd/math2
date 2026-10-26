---
tag: 06WHRARZKY
kind: statement
role: theorem
name: Existence of Laurent expansions on an annulus
aliases: [laurents-theorem, laurent-expansion-theorem]
msc: [30B10]
uses: [0AJ0YVK743, 0X3XD2ATB0, 0DG0Z72CQD, 0T7ABX4CWE]
sources:
  - url: https://en.wikipedia.org/wiki/Laurent_series
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Laurent_series
    locator: Uniqueness
---

## Statement

Let $c \in \mathbb{C}$, let $0 \le r < R \le \infty$, and let $A = \{z : r < |z - c| < R\}$ be an [[annulus|0AJ0YVK743]].
Let $f : A \to \mathbb{C}$ be [[holomorphic|0DG0Z72CQD]] on $A$.
Then there are unique complex numbers $(a_n)_{n \in \mathbb{Z}}$ such that the [[Laurent series|0X3XD2ATB0]] $\sum_{n \in \mathbb{Z}} a_n (z - c)^n$ converges to $f(z)$ for each $z \in A$.
For each $\rho$ with $r < \rho < R$ and each $n \in \mathbb{Z}$,
$$a_n = \frac{1}{2 \pi i} \oint_{|z - c| = \rho} \frac{f(z)}{(z - c)^{n+1}} \, dz.$$
The series converges absolutely on $A$ and uniformly on each closed annulus $\rho_1 \le |z - c| \le \rho_2$ with $r < \rho_1 \le \rho_2 < R$.

## Remarks

Uniqueness means: each Laurent series that converges to $f$ on $A$ has these coefficients. So we can find them by any method, for example with known power series.
For example, on $0 < |z| < 1$, $\frac{1}{z(1 - z)} = \frac{1}{z} + 1 + z + z^2 + \cdots$. On $|z| > 1$, the same function is $-\frac{1}{z^2} - \frac{1}{z^3} - \cdots$.
If $f$ is holomorphic on the whole disc $|z - c| < R$, then $a_n = 0$ for $n < 0$, and the Laurent series is the Taylor series.

## Explanations

### L1 human

On a ring around $c$, each holomorphic function is a sum of powers of $z - c$, with negative and positive exponents.
The coefficients come from circle integrals, as for Taylor series. The same function can have different Laurent series on different rings.
