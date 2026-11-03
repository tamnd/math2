---
tag: QN4BAA9HEC
kind: definition
name: Reed–Muller code
msc: [94B05]
defines: XXKX4RN9YK
uses: [E85KREWV60, 0X05GS525E, 0ZXZ82FTX2, M2X88AXM17, JA3DP8NM0A]
sources:
  - url: https://en.wikipedia.org/wiki/Reed%E2%80%93Muller_code
---

## Definition

Let $m \ge 1$ and $0 \le r \le m$ be integers, and list the $2^m$ points of $\F_2^m$ in a fixed order $v_1, \dots, v_{2^m}$.
The *Reed–Muller code* $\mathrm{RM}(r, m)$ is the binary code
$$\mathrm{RM}(r, m) = \set{(p(v_1), \dots, p(v_{2^m})) : p \in \F_2[x_1, \dots, x_m], \ \deg p \le r}.$$

## Remarks

Since $x^2 = x$ on $\F_2$, one may restrict to multilinear polynomials, and the monomials $x_{i_1} \cdots x_{i_s}$ with $s \le r$ and $i_1 < \cdots < i_s$ give a basis.
So $\mathrm{RM}(r, m)$ is a [[linear code|E85KREWV60]] of length $2^m$ and dimension $\sum_{i=0}^{r} \binom{m}{i}$.
Its [[minimum distance|M2X88AXM17]] is $2^{m - r}$, attained by the monomial $x_1 x_2 \cdots x_r$.
For $r < m$, the [[dual code|JA3DP8NM0A]] of $\mathrm{RM}(r, m)$ is $\mathrm{RM}(m - r - 1, m)$.
Another description is the recursion $\mathrm{RM}(r, m) = \set{(u, u + v) : u \in \mathrm{RM}(r, m-1), \ v \in \mathrm{RM}(r-1, m-1)}$ for $0 < r < m$.

Example: $\mathrm{RM}(1, 3)$ has length $8$, dimension $1 + 3 = 4$ and minimum distance $4$.
The polynomial $x_1$ gives a word of weight $4$.
Every nonconstant affine polynomial takes the value $1$ on exactly half of $\F_2^3$.
So all nonzero codewords other than the all-ones word have weight $4$.
This $[8, 4, 4]$ code is equivalent to the extended [[Hamming code|D68NF1S2NW]].

Non-example: the value lists of the polynomials of degree exactly $r$ do not form $\mathrm{RM}(r, m)$.
For $r \ge 1$ they do not even form a linear code, since the zero word is missing.
Special cases: $\mathrm{RM}(0, m)$ is the [[repetition code|PZV5HW9BT7]] of length $2^m$, and $\mathrm{RM}(m, m) = \F_2^{2^m}$.
