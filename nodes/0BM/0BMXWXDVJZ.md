---
tag: 0BMXWXDVJZ
kind: statement
role: corollary
name: Fermat's little theorem in the form a^p = a
msc: [11A07]
uses: [0M25PRN3WQ]
sources:
  - url: https://en.wikipedia.org/wiki/Fermat%27s_little_theorem
    locator: lead section
---

## Statement

Let $p$ be a [[prime number|0SN0MAEKYX]] and let $a$ be an integer.
Then $a^p \equiv a \pmod p$.

## Remarks

If $p \nmid a$, multiply [[Fermat's little theorem|0M25PRN3WQ]] $a^{p-1} \equiv 1 \pmod p$ by $a$. If $p \mid a$, both sides are $0$ modulo $p$.
Conversely, this form implies the form $a^{p-1} \equiv 1$: cancel $a$, which is allowed when $p \nmid a$.
In the ring $\mathbb{Z}/p\mathbb{Z}$, the form says that $x^p = x$ for each element $x$.

## Explanations

### L1 human

The form $a^p \equiv a$ needs no hypothesis on $a$.
For example, with $p = 3$: $0^3 = 0$, $1^3 = 1$, $2^3 = 8 \equiv 2$, and $4^3 = 64 \equiv 1 \equiv 4 \pmod 3$.
