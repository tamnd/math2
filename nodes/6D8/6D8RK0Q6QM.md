---
tag: 6D8RK0Q6QM
kind: definition
name: Regular sequence
msc: [13D02, 13C15]
defines: 69R5R2FCS5
uses: [0310REJJY8, 0NZ8JA25WK, 0NNRDW10RZ]
sources:
  - url: https://en.wikipedia.org/wiki/Regular_sequence
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]] and let $M$ be an [[$R$-module|0NZ8JA25WK]].
A sequence $x_1, \ldots, x_n$ of elements of $R$ is an *$M$-regular sequence* if:

1. for each $i = 1, \ldots, n$, the element $x_i$ is a non-zero-divisor on $M / (x_1, \ldots, x_{i-1}) M$, that is, $x_i m = 0$ in this quotient implies $m = 0$ in it;
2. $M / (x_1, \ldots, x_n) M \ne 0$.

A *regular sequence* of $R$ is an $R$-regular sequence.

## Remarks

Example: in $R = K[x_1, \ldots, x_n]$ with $K$ a field, the variables form a regular sequence, since $R/(x_1, \ldots, x_{i-1}) \cong K[x_i, \ldots, x_n]$ is a domain in which $x_i \ne 0$, and $R/(x_1, \ldots, x_n) \cong K \ne 0$.
Non-example: in $K[x, y]$ the sequence $x, xy$ fails clause 1, because $xy$ is zero in $K[x,y]/(x)$ and so kills the nonzero element $1$.
A sequence that satisfies only clause 1 is called *weakly regular*.
The order matters in general: in $K[x, y, z]$, the sequence $x, y(1-x), z(1-x)$ is regular but $y(1-x), z(1-x), x$ is not.
If $R$ is a Noetherian local ring, $M$ is finitely generated and all $x_i$ lie in the maximal ideal, then every permutation of an $M$-regular sequence is $M$-regular.
