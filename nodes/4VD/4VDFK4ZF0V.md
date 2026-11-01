---
tag: 4VDFK4ZF0V
kind: definition
name: Rack and quandle
msc: [57K12, 20N02]
defines: X74VY86TSX
uses: [0SJ3RX9TXA, 0M418FE7BB, 0GG9TVW90M, G5S1M9, 0DXD4QSZ8A]
sources:
  - url: https://en.wikipedia.org/wiki/Racks_and_quandles
---

## Definition

Let $X$ be a [[set|0SJ3RX9TXA]] with a [[binary operation|0M418FE7BB]] $\triangleleft$.
The pair $(X, \triangleleft)$ is a *rack* if:

1. $a \triangleleft (b \triangleleft c) = (a \triangleleft b) \triangleleft (a \triangleleft c)$ for all $a, b, c \in X$.
2. For all $a, b \in X$ there is exactly one $c \in X$ with $a \triangleleft c = b$.

A rack is a *quandle* if moreover:

3. $a \triangleleft a = a$ for all $a \in X$.

## Remarks

Clause 2 says that for each $a$ the map $x \mapsto a \triangleleft x$ is a [[bijection|0GG9TVW90M]] of $X$, and clause 1 says that this bijection is an automorphism of $(X, \triangleleft)$.

Example: the conjugation quandle of a [[group|G5S1M9]] $G$, with $a \triangleleft b = a b a^{-1}$, the [[conjugate|0DXD4QSZ8A]] of $b$ by $a$.
Clause 1: both sides equal $a b c b^{-1} a^{-1}$, since $(aba^{-1})(aca^{-1})(aba^{-1})^{-1} = abcb^{-1}a^{-1}$.
Clause 2: $c = a^{-1} b a$ is the only solution.
Clause 3: $a a a^{-1} = a$.

Example: the dihedral quandle on $\Z/n\Z$, with $a \triangleleft b = 2a - b$.
Both sides of clause 1 equal $2a - 2b + c$, clause 2 has the solution $c = 2a - b$, and $2a - a = a$.

Non-example: a rack that is not a quandle.
Let $\sigma$ be a permutation of $X$ other than the identity, and let $a \triangleleft b = \sigma(b)$.
Both sides of clause 1 equal $\sigma(\sigma(c))$, and clause 2 holds since $\sigma$ is a bijection.
But $a \triangleleft a = \sigma(a) \ne a$ for each $a$ moved by $\sigma$, so clause 3 fails.

Some authors write the operation on the other side, with $(c \triangleright b) \triangleright a = (c \triangleright a) \triangleright (b \triangleright a)$.
