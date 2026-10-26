---
tag: ~db3a40ac
kind: statement
role: proposition
name: Congruence is compatible with multiplication
msc: [11A07]
uses: [~e79e2431]
sources:
  - url: https://en.wikipedia.org/wiki/Modular_arithmetic
    locator: Basic properties
---

## Statement

Let $n$ be a positive integer, and let $a$, $b$, $c$ and $d$ be integers.
If $a \equiv b \pmod n$ and $c \equiv d \pmod n$, then $a c \equiv b d \pmod n$.

## Remarks

The proof: $a c - b d = a (c - d) + d (a - b)$, and $n$ divides both terms.
With [[compatibility with addition|~540362e0]], this result shows that the multiplication of [[integers modulo n|~6506d19f]] is well defined.
By induction, it gives [[compatibility with powers|~cbfd25d2]].

## Explanations

### L1 human

To find the remainder of a product, you can multiply the remainders and reduce again.
For example, the last digit of $27 \cdot 43$ is the last digit of $7 \cdot 3 = 21$, that is, $1$. This is the case $n = 10$.
