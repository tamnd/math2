---
tag: 0R8YXRC9AJ
kind: statement
role: theorem
name: Integers modulo a prime form a field
msc: [11A07]
uses: [01N3AYAA6N, 0SN0MAEKYX, 0DQVHMYAGA]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_field
    locator: lead section
---

## Statement

Let $p$ be a [[prime number|0SN0MAEKYX]].
Then the ring $\mathbb{Z}/p\mathbb{Z}$ of the [[integers modulo p|01N3AYAA6N]] is a field.
That is, each nonzero element of $\mathbb{Z}/p\mathbb{Z}$ has a multiplicative inverse.

## Remarks

The proof: if $\overline{a} \neq \overline{0}$, then $p \nmid a$, so $\gcd(a, p) = 1$. [[Bézout's identity|0DQVHMYAGA]] gives $a x + p y = 1$, and then $\overline{a} \cdot \overline{x} = \overline{1}$.
The converse holds: if $n > 1$ is composite, with $n = a b$ and $1 < a, b < n$, then $\overline{a} \cdot \overline{b} = \overline{0}$, so $\mathbb{Z}/n\mathbb{Z}$ is not a field.
The field $\mathbb{Z}/p\mathbb{Z}$ is often written $\mathbb{F}_p$ or $\mathrm{GF}(p)$. It is the finite field with $p$ elements.

## Explanations

### L1 human

Modulo $7$, you can divide by each nonzero number. For example, $3 \cdot 5 = 15 \equiv 1 \pmod 7$, so $5$ plays the part of $1/3$.
Modulo $6$ this fails: no number $x$ gives $2 x \equiv 1 \pmod 6$, because $2 x$ is always even.
