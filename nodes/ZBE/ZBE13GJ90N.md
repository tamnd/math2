---
tag: ZBE13GJ90N
kind: definition
name: Costas array
msc: [05B20, 94A55, 05B15]
defines: MM4XQXEQQG
uses: [05RWFKVTJ7, 08SP3DF8NB]
sources:
  - url: https://en.wikipedia.org/wiki/Costas_array
---

## Definition

Let $n \ge 1$ and let $f$ be a [[permutation|05RWFKVTJ7]] of $\set{1, \dots, n}$.
Consider the $n \times n$ [[permutation matrix|08SP3DF8NB]] with a one in row $f(i)$ of column $i$ for each $i$.
It is a *Costas array* if the $n(n-1)/2$ vectors
$$\big(j - i, \; f(j) - f(i)\big), \qquad 1 \le i < j \le n,$$
are pairwise distinct.
Equivalently, for each $h$ with $1 \le h \le n - 1$, the differences $f(i + h) - f(i)$, $1 \le i \le n - h$, are pairwise distinct.

## Remarks

Example: $n = 3$ and $f = (1, 3, 2)$, that is, $f(1) = 1$, $f(2) = 3$, $f(3) = 2$.
For $h = 1$ the differences are $3 - 1 = 2$ and $2 - 3 = -1$, which are distinct; for $h = 2$ there is only one difference.
So $f$ gives a Costas array.

Non-example: the identity permutation $f = (1, 2, 3)$ has, for $h = 1$, the differences $1$ and $1$, which coincide; so it is not a Costas array.

The Welch construction: let $p$ be a prime and $\alpha$ a primitive root modulo $p$; then $f(i) = \alpha^i \bmod p$ for $i = 1, \dots, p - 1$ is a Costas array of order $p - 1$.
For $p = 5$ and $\alpha = 2$ this gives $f = (2, 4, 3, 1)$.
