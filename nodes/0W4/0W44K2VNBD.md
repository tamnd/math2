---
tag: 0W44K2VNBD
kind: definition
name: Sesquilinear form
msc: ["15A63"]
topics: [DYAK7YMK7B]
audience: ug1
defines: 054YEQ0Y8M
uses: [05EGHEQZAW, 0BJV24C4SY]
sources:
  - url: https://en.wikipedia.org/wiki/Sesquilinear_form
    locator: Complex vector spaces
  - url: https://en.wikipedia.org/wiki/Sesquilinear_form
    locator: Convention
inventory: [RRQ6XR7ZBC]
---

## Definition

Let $V$ be a [[vector space|05EGHEQZAW]] over $\C$.
A *sesquilinear form* on $V$ is a map $h \colon V \times V \to \C$ such that, for all $u, v, w \in V$ and $a \in \C$:

1. $h(u + v, w) = h(u, w) + h(v, w)$ and $h(au, w) = a\, h(u, w)$;
2. $h(u, v + w) = h(u, v) + h(u, w)$ and $h(u, aw) = \bar a\, h(u, w)$, where $\bar a$ is the [[complex conjugate|0BJV24C4SY]] of $a$.

So $h$ is linear in the first slot and conjugate-linear in the second slot.

## Notation

Let $(e_1, \dots, e_n)$ be a basis of $V$.
The *matrix* of $h$ is $M = (h(e_i, e_j))_{i, j}$, and $h(x, y) = x^T M \bar y$ for the coordinate vectors $x, y$.
Many authors, especially in physics, use the other convention: conjugate-linear in the first slot and linear in the second, with $h(x, y) = x^* A y$.

## Remarks

The convention here is the one of most mathematics books; the physics convention comes from the bra-ket notation of Dirac.
A sesquilinear form is *Hermitian* when $h(v, u) = \overline{h(u, v)}$ for all $u, v$; see [[Hermitian form|8NJ7XY6F1S]].
On $\C^n$, each sesquilinear form is $h(x, y) = x^T M \bar y$ for exactly one $n \times n$ complex matrix $M$, namely $M_{ij} = h(e_i, e_j)$.
A change of basis with the invertible matrix $P$ replaces $M$ by $P^T M \bar P$.
A complex [[inner product|0NB0AWGJBW]] is a positive definite Hermitian sesquilinear form.
More generally, over a field $F$ with an automorphism $\sigma$ of order $2$, a $\sigma$-sesquilinear form replaces $\bar a$ by $\sigma(a)$.

## Explanations

### L1 human

Over the complex numbers, bilinear forms cannot be positive, because $B(iv, iv) = -B(v, v)$.
Sesquilinear forms fix this by conjugating the scalar in one slot.
The standard inner product $\sum_i x_i \bar y_i$ on $\C^n$ is the main example.

### L2 human

For $h(x, y) = x_1 \bar y_1 + 2 x_1 \bar y_2 + 3 x_2 \bar y_2$ on $\C^2$, the matrix is $M = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$.
For $x = (1, 0)$ and $y = (0, i)$ we get $h(x, y) = 2 \cdot 1 \cdot \bar i = -2i$, and $x^T M \bar y = (1, 2) \cdot (0, -i) = -2i$.
A trap: in the physics convention the same matrix gives $x^* M y$, which is a different form; always state the convention.
