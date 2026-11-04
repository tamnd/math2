---
tag: N1N8WBSARF
kind: proof
name: Proof that congruence is compatible with multiplication
msc: [11A07]
proves: 072D5G4SK6
uses: [0TPW25CBN6, 096PW7Q014]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Modular_arithmetic
    locator: Basic properties
---

## Proof

1. Let $n$ be a positive integer, and let $a, b, c, d$ be integers with $a \equiv b \pmod n$ and $c \equiv d \pmod n$.
2. By the definition of [[congruence modulo n|0TPW25CBN6]], $n$ [[divides|096PW7Q014]] $a - b$ and $n$ divides $c - d$. So there are integers $s$ and $t$ with $a - b = n s$ and $c - d = n t$.
3. Expanding gives $a (c - d) + d (a - b) = a c - a d + a d - b d = a c - b d$.
4. By steps 2 and 3, $a c - b d = a n t + d n s = n (a t + d s)$.
5. Since $a t + d s$ is an integer, $n$ divides $a c - b d$.
6. Hence $a c \equiv b d \pmod n$.

## Idea

Change one factor at a time: first replace $c$ by $d$, then $a$ by $b$. Each change alters the product by a multiple of $n$, because the change in the factor is a multiple of $n$.
