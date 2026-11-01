---
tag: RS7Z7NTDX9
kind: definition
name: Normal number
msc: [11K16]
defines: C98T2T5FJS
uses: [08GR54CKEA, 0NCJ5WXN6Z]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_number
---

## Definition

Let $b \ge 2$ be an integer, and let $x$ be a real number.
Write the fractional part $x - \floor{x}$ in base $b$ as $0.d_1 d_2 d_3 \ldots$ with digits $d_i \in \set{0, 1, \dots, b-1}$.
When there are two such expansions, take the one that does not end in an infinite run of the digit $b - 1$.
For a finite string $w$ of $k$ digits and an integer $n \ge 1$, let $N(w, n)$ be the number of indices $i$ with $1 \le i \le n - k + 1$ such that $d_i d_{i+1} \cdots d_{i+k-1} = w$.
The number $x$ is *normal in base $b$* if
$$\lim_{n \to \infty} \frac{N(w, n)}{n} = b^{-k}$$
for every $k \ge 1$ and every string $w$ of $k$ digits.
The number $x$ is *absolutely normal* if it is normal in base $b$ for every integer $b \ge 2$.

## Remarks

Example: Champernowne's number $0.1234567891011121314\ldots$, formed by the decimal digits of the positive integers in order, is normal in base $10$.
Non-example: $x = 1/3 = 0.333\ldots$ in base $10$ is not normal, since for $w = 1$ one has $N(w, n) = 0$ for all $n$, so the limit is $0 \ne 1/10$.
In the same way, no [[rational number|0NCJ5WXN6Z]] is normal in any base, because its expansion is eventually periodic.
A number is *simply normal* in base $b$ if the condition holds for strings of length $k = 1$.
Normality in base $b$ is equivalent to the [[equidistribution modulo one|XM6DH57BWY]] of the sequence $(b^n x)_{n \ge 0}$.
Here $\floor{x}$ is the [[floor|08GR54CKEA]] of $x$.
