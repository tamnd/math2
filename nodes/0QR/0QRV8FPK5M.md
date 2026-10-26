---
tag: 0QRV8FPK5M
kind: definition
name: Residue class
aliases: [congruence-class]
msc: [11A07]
defines: 01RSTGNTXG
uses: [0TPW25CBN6]
sources:
  - url: https://en.wikipedia.org/wiki/Modular_arithmetic
    locator: Congruence classes
---

## Definition

Let $n$ be a positive integer and let $a$ be an integer.
The residue class of $a$ modulo $n$ is the set $\overline{a} = \{ b \in \mathbb{Z} : b \equiv a \pmod n \}$ of the integers [[congruent|0TPW25CBN6]] to $a$ modulo $n$.
Thus $\overline{a} = \{ a + k n : k \in \mathbb{Z} \} = a + n \mathbb{Z}$.

## Remarks

Two residue classes $\overline{a}$ and $\overline{b}$ are equal if $a \equiv b \pmod n$, and they have no common element otherwise.
There are exactly $n$ residue classes modulo $n$: $\overline{0}, \overline{1}, \dots, \overline{n - 1}$.
Other notations are $[a]$, $[a]_n$ and $a \bmod n$.
The residue classes are the elements of the ring of [[integers modulo n|01N3AYAA6N]].

## Explanations

### L1 human

Modulo $3$, each integer falls in one of three boxes: the multiples of $3$, the numbers $1$ more than a multiple of $3$, and the numbers $2$ more.
Each box is a residue class. For example, $\overline{1} = \{ \dots, -5, -2, 1, 4, 7, \dots \}$.
