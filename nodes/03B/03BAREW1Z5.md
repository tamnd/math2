---
tag: 03BAREW1Z5
kind: statement
role: proposition
name: Generalized Euclid's lemma
msc: [11A05]
uses: [0GFKP8F8AG, 096PW7Q014]
sources:
  - url: https://en.wikipedia.org/wiki/Euclid%27s_lemma
    locator: Formulations
---

## Statement

Let $n$, $a$ and $b$ be integers.
If $n \mid a b$ and $n$ and $a$ are [[coprime|0GFKP8F8AG]], then $n \mid b$.

## Remarks

When $n$ is a prime $p$ and $p \nmid a$, then $p$ and $a$ are coprime. So this result implies [[Euclid's lemma|051VYKA1EX]].
The proof uses [[Bézout's identity|0DQVHMYAGA]]: from $n x + a y = 1$ we get $b = n b x + a b y$, and $n$ divides both terms.
For example, $5 \mid 3 \cdot 10$ and $\gcd(5, 3) = 1$, so $5 \mid 10$.

## Explanations

### L1 human

If $n$ divides $a b$ but has no common factor with $a$, then all the factors of $n$ must come from $b$.
For example, $4 \mid 3 b$ forces $4 \mid b$, because $3$ gives no factor $2$.
