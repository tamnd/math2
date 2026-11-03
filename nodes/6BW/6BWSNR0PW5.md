---
tag: 6BWSNR0PW5
kind: definition
name: Bol loop
msc: [20N05]
defines: S4E8XV37MS
uses: [ZJD31SPPFP]
sources:
  - url: https://en.wikipedia.org/wiki/Bol_loop
---

## Definition

A *loop* is a [[quasigroup|ZJD31SPPFP]] $L$ with an element $e$ such that $ex = xe = x$ for all $x \in L$.
A *left Bol loop* is a loop $L$ such that
$$a(b(ac)) = (a(ba))c \quad \text{for all } a, b, c \in L.$$
A *right Bol loop* is a loop $L$ such that
$$((ca)b)a = c((ab)a) \quad \text{for all } a, b, c \in L.$$
A *Bol loop* is a left Bol loop or a right Bol loop, depending on the convention of the author.

## Remarks

Example: every group is a left and a right Bol loop, since both identities follow from associativity.
The nonzero octonions under multiplication form a [[Moufang loop|H0TJPNCMXD]], hence a left and a right Bol loop, and they are not a group.

Non-example: the loop $L = \set{e, a, b, c, d}$ with the multiplication table below, where the row gives the left factor.

| $\cdot$ | $e$ | $a$ | $b$ | $c$ | $d$ |
|---|---|---|---|---|---|
| $e$ | $e$ | $a$ | $b$ | $c$ | $d$ |
| $a$ | $a$ | $e$ | $c$ | $d$ | $b$ |
| $b$ | $b$ | $c$ | $d$ | $e$ | $a$ |
| $c$ | $c$ | $d$ | $a$ | $b$ | $e$ |
| $d$ | $d$ | $b$ | $e$ | $a$ | $c$ |

Putting $b = e$ in the left Bol identity gives $a(ac) = (aa)c$.
In $L$, $a(ab) = ac = d$ while $(aa)b = eb = b$, so $L$ is not left Bol.
Putting $b = e$ in the right Bol identity gives $(ca)a = c(aa)$, and $(ba)a = ca = d$ while $b(aa) = b$, so $L$ is not right Bol either.

A loop is both left and right Bol exactly when it is a Moufang loop.
