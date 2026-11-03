---
tag: GPHXXRY1YV
kind: definition
name: Moufang loop
msc: [20N05, 17D05]
defines: H0TJPNCMXD
uses: [ZJD31SPPFP]
sources:
  - url: https://en.wikipedia.org/wiki/Moufang_loop
---

## Definition

A *loop* is a [[quasigroup|ZJD31SPPFP]] $L$ with an element $e$ such that $ea = ae = a$ for all $a \in L$.
A *Moufang loop* is a loop $L$ such that
$$z(x(zy)) = ((zx)z)y \quad \text{for all } x, y, z \in L.$$

## Remarks

In a loop, this identity is equivalent to each of $x(z(yz)) = ((xz)y)z$, $(zx)(yz) = (z(xy))z$ and $(zx)(yz) = z((xy)z)$.
A loop is Moufang exactly when it is both a left and a right [[Bol loop|S4E8XV37MS]].

Example: the nonzero octonions $\mathbb{O} \setminus \set{0}$ under multiplication.
They form a loop with identity $1$, since $\mathbb{O}$ is a division algebra.
The identity holds because the octonions satisfy the [[Moufang identities|CZ2BZQN2EV]] as an [[alternative algebra|N8K9SSVMRN]].
It is not a group, because octonion multiplication is not associative.

Non-example: the loop $L = \set{e, a, b, c, d}$ with the multiplication table below, where the row gives the left factor.

| $\cdot$ | $e$ | $a$ | $b$ | $c$ | $d$ |
|---|---|---|---|---|---|
| $e$ | $e$ | $a$ | $b$ | $c$ | $d$ |
| $a$ | $a$ | $e$ | $c$ | $d$ | $b$ |
| $b$ | $b$ | $c$ | $d$ | $e$ | $a$ |
| $c$ | $c$ | $d$ | $a$ | $b$ | $e$ |
| $d$ | $d$ | $b$ | $e$ | $a$ | $c$ |

Each element occurs once in each row and column, so $L$ is a loop with identity $e$.
Take $z = a$, $x = e$, $y = b$: then $z(x(zy)) = a(ab) = ac = d$, while $((zx)z)y = (aa)b = eb = b$.
