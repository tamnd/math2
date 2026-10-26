---
tag: 0M25PRN3WQ
kind: statement
role: theorem
name: Fermat's little theorem
msc: [11A07]
uses: [0SN0MAEKYX, 0TPW25CBN6]
sources:
  - url: https://en.wikipedia.org/wiki/Fermat%27s_little_theorem
    locator: lead section
same_as:
  wikidata: Q188295
  wikipedia: Fermat's little theorem
---

## Statement

Let $p$ be a [[prime number|0SN0MAEKYX]] and let $a$ be an integer that $p$ does not divide.
Then $a^{p-1} \equiv 1 \pmod p$.

## Remarks

An equivalent form is [[Fermat's little theorem in the form a^p = a|0BMXWXDVJZ]]: $a^p \equiv a \pmod p$ for each integer $a$.
In the ring $\mathbb{Z}/p\mathbb{Z}$, the statement is $x^{p-1} = 1$ for each nonzero $x$. It follows from [[Lagrange's theorem|3C53TD]] for the multiplicative [[group|G5S1M9]] of $\mathbb{Z}/p\mathbb{Z}$, which has $p - 1$ elements.
[[Euler's theorem|0VC4DVE7DQ]] generalizes the result to each modulus $n$.
The converse is false. For example, $2^{340} \equiv 1 \pmod{341}$, but $341 = 11 \cdot 31$. See [[Fermat pseudoprime|02M2K4QH9P]].

## History

Fermat stated the theorem in a letter of 1640, without a proof. Euler published the first known proof in 1736. Leibniz had a proof earlier, in an unpublished manuscript.

## Explanations

### L1 human

Take $p = 5$ and $a = 2$: $2^4 = 16 = 3 \cdot 5 + 1$, so $2^4 \equiv 1 \pmod 5$.
The theorem says that this always happens for a prime $p$ and a number $a$ that $p$ does not divide.
It lets you reduce large powers: $2^{100} = (2^4)^{25} \equiv 1 \pmod 5$.
