---
tag: GCNQZFRZ4B
kind: proof
name: Proof that congruence is compatible with addition
msc: [11A07]
proves: 00FWBN7F0Y
uses: [0TPW25CBN6, 096PW7Q014]
sources:
  - url: https://en.wikipedia.org/wiki/Modular_arithmetic
    locator: Basic properties
---

## Proof

1. Let $n$ be a positive integer and let $a$, $b$, $c$, $d$ be integers with $a \equiv b \pmod n$ and $c \equiv d \pmod n$.
2. By the definition of [[congruence modulo n|0TPW25CBN6]], $n \mid a - b$ and $n \mid c - d$.
3. By the definition of [[divisibility|096PW7Q014]], there are integers $k$ and $l$ with $a - b = n k$ and $c - d = n l$.
4. Then $(a + c) - (b + d) = (a - b) + (c - d) = n k + n l = n (k + l)$.
5. Since $k + l$ is an integer, $n \mid (a + c) - (b + d)$.
6. Hence $a + c \equiv b + d \pmod n$.

## Idea

The difference of the two sums is the sum of the two differences. Both differences are multiples of $n$, and a sum of multiples of $n$ is again a multiple of $n$.
