---
tag: ~dc156adc
kind: statement
role: proposition
name: Converse of Wilson's theorem
msc: [11A51]
uses: [~27a8d2db, ~f3c51c16]
sources:
  - url: https://en.wikipedia.org/wiki/Wilson%27s_theorem
    locator: Composite modulus
---

## Statement

Let $n$ be an integer with $n > 1$.
If $(n - 1)! \equiv -1 \pmod n$, then $n$ is a [[prime number|~f3c51c16]].

## Remarks

With [[Wilson's theorem|~27a8d2db]], this gives: an integer $n > 1$ is prime if and only if $(n - 1)! \equiv -1 \pmod n$.
The proof: if $n = a b$ with $1 < a < n$, then $a$ divides $(n - 1)!$. A congruence $(n - 1)! \equiv -1 \pmod n$ would give $a \mid 1$, which is false.
In fact $(n - 1)! \equiv 0 \pmod n$ for each composite $n > 4$, and $3! \equiv 2 \pmod 4$.
This primality test is not practical, because $(n - 1)!$ needs about $n$ multiplications.

## Explanations

### L1 human

For a composite number $n$, a factor of $n$ appears in the product $1 \cdot 2 \cdots (n - 1)$.
So the product cannot leave the remainder $n - 1$. For example, $5! = 120 \equiv 0 \pmod 6$.
