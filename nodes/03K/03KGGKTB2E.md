---
tag: 03KGGKTB2E
kind: statement
role: theorem
name: Wilson's theorem
msc: [11A07]
uses: [0SN0MAEKYX, 0TPW25CBN6]
sources:
  - url: https://en.wikipedia.org/wiki/Wilson%27s_theorem
    locator: lead section
same_as:
  wikidata: Q276082
  wikipedia: Wilson's theorem
---

## Statement

Let $p$ be a [[prime number|0SN0MAEKYX]].
Then $(p - 1)! \equiv -1 \pmod p$.

## Remarks

A proof: in $\mathbb{Z}/p\mathbb{Z}$, each element of $\{ \overline{1}, \dots, \overline{p - 1} \}$ has an inverse. Only $\overline{1}$ and $\overline{-1}$ are their own inverses. The other elements cancel in pairs in the product.
For example, $4! = 24 \equiv -1 \pmod 5$ and $6! = 720 \equiv -1 \pmod 7$.
The [[converse of Wilson's theorem|06WRV8HFDY]] also holds, so the congruence characterizes the primes.

## History

Ibn al-Haytham stated the result about the year 1000. Edward Waring announced it in 1770 and named his student John Wilson as its discoverer. Lagrange gave the first proof in 1771.

## Explanations

### L1 human

Multiply all the numbers from $1$ to $p - 1$, and divide by $p$. The remainder is always $p - 1$.
For $p = 7$: $1 \cdot 2 \cdot 3 \cdot 4 \cdot 5 \cdot 6 = 720 = 102 \cdot 7 + 6$.
