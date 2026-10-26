---
tag: ~e8defa3b
kind: statement
role: theorem
name: The characteristic of an integral domain is zero or prime
msc: [13G05]
uses: [~1e7ebd1c, ~6bd4a5ff]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_(algebra)
    locator: Case of rings
---

## Statement

Let $R$ be an [[integral domain|~6bd4a5ff]].
Then the [[characteristic|~1e7ebd1c]] of $R$ is $0$ or a prime number.

## Remarks

The proof: suppose that the characteristic is $n = a b$ with $1 < a, b < n$. Then $(a \cdot 1)(b \cdot 1) = n \cdot 1 = 0$, but $a \cdot 1 \neq 0$ and $b \cdot 1 \neq 0$.
The characteristic is not $1$, because $1 \neq 0$ in an integral domain.
In particular, the characteristic of a [[field|~92ce2090]] is $0$ or a prime number.
The ring $\mathbb{Z}/6\mathbb{Z}$ has characteristic $6$, and it is not an integral domain.

## Explanations

### L1 human

If $6 \cdot 1 = 0$ in a ring, then $(2 \cdot 1)(3 \cdot 1) = 0$.
In an integral domain, this forces $2 \cdot 1 = 0$ or $3 \cdot 1 = 0$.
So the least $n$ with $n \cdot 1 = 0$ cannot be a product of two smaller numbers.
