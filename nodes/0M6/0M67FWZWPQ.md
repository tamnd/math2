---
tag: 0M67FWZWPQ
kind: statement
role: theorem
name: Existence of inverses modulo n
msc: [11A07]
uses: [00GXTQMY8Z, 0GFKP8F8AG, 0DQVHMYAGA]
sources:
  - url: https://en.wikipedia.org/wiki/Modular_multiplicative_inverse
    locator: Integers modulo m
---

## Statement

Let $n$ be a positive integer and let $a$ be an integer.
Then $a$ has a [[modular multiplicative inverse|00GXTQMY8Z]] modulo $n$ if and only if $a$ and $n$ are [[coprime|0GFKP8F8AG]].

## Remarks

If $\gcd(a, n) = 1$, [[Bézout's identity|0DQVHMYAGA]] gives integers $x$ and $y$ with $a x + n y = 1$. Then $a x \equiv 1 \pmod n$.
Conversely, if $a x \equiv 1 \pmod n$, then $a x + n y = 1$ for some integer $y$, so each common divisor of $a$ and $n$ divides $1$.
The [[extended Euclidean algorithm|0964YQFSA8]] computes the inverse.
For example, $4$ has no inverse modulo $6$, because $\gcd(4, 6) = 2$.

## Explanations

### L1 human

You can "divide by $a$" modulo $n$ exactly when $a$ and $n$ have no common factor.
Modulo $10$, the numbers $1, 3, 7, 9$ have inverses, since $1 \cdot 1$, $3 \cdot 7$ and $9 \cdot 9$ all end with the digit $1$.
The numbers $2, 4, 5, 6, 8$ have no inverse modulo $10$.
