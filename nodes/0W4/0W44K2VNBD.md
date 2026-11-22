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

A sesquilinear form pairs two vectors of a complex space, linearly in the first vector and with conjugated scalars in the second.
Let $V$ be a [[vector space|05EGHEQZAW]] over $\mathbb{C}$.
A *sesquilinear form* on $V$ is a map $h \colon V \times V \to \mathbb{C}$ such that, for all $u, v, w \in V$ and $a \in \mathbb{C}$:

1. $h(u + v, w) = h(u, w) + h(v, w)$ and $h(au, w) = a\, h(u, w)$;
2. $h(u, v + w) = h(u, v) + h(u, w)$ and $h(u, aw) = \bar a\, h(u, w)$, where $\bar a$ is the [[complex conjugate|0BJV24C4SY]] of $a$.

So $h$ is linear in the first slot and conjugate-linear in the second slot.

## Notation

Let $(e_1, \dots, e_n)$ be a basis of $V$.
The *matrix* of $h$ in this basis is $M = (h(e_i, e_j))_{i, j}$, and $h(x, y) = x^{\mathsf{T}} M \bar y$ for the coordinate columns $x$ and $y$.
Physics books and Mathlib use the other convention: conjugate-linear in the first slot and linear in the second, with $h(x, y) = x^* A y$.

## Remarks

Condition 1 is the same as for a [[bilinear form|0P799D6AMN]].
Condition 2 keeps additivity in the second slot but replaces $a$ by $\bar a$, and this one change is what allows $h(v, v) > 0$ for every $v \ne 0$.
For example, $h(x, y) = x_1 \bar y_1 + 2 x_1 \bar y_2 + 3 x_2 \bar y_2$ on $\mathbb{C}^2$ is sesquilinear, with $M = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$.
For $x = (1, 0)$ and $y = (0, i)$, the formula gives $h(x, y) = 2 \cdot 1 \cdot \bar i = -2i$, and $x^{\mathsf{T}} M \bar y = (1, 2) \cdot (0, -i) = -2i$ as well.

The map $B(x, y) = x_1 y_1$ on $\mathbb{C}$ fails condition 2, since $B(1, i) = i$ while condition 2 asks for $\bar i\, B(1, 1) = -i$.
A change of basis with the invertible matrix $P$ replaces $M$ by $P^{\mathsf{T}} M \bar P$.
The form is *Hermitian* when $h(v, u) = \overline{h(u, v)}$ for all $u, v$, as in the [[definition of a Hermitian form|8NJ7XY6F1S]], and a complex [[inner product|0NB0AWGJBW]] is a positive definite Hermitian form.
Over a field $F$ with an automorphism $\sigma$ of order $2$, a $\sigma$-sesquilinear form replaces $\bar a$ by $\sigma(a)$.
The concept page [[sesquilinear form|054YEQ0Y8M]] gives more examples and the main properties.

## Explanations

### L1 human

Over the complex numbers, a plain bilinear form cannot be positive, because $B(iv, iv) = i^2 B(v, v) = -B(v, v)$.
A sesquilinear form takes the conjugate of the scalar in the second slot.
Then $h(iv, iv) = i \cdot \bar i\, h(v, v) = h(v, v)$, and positive values become possible.
The standard inner product $x_1 \bar y_1 + \dots + x_n \bar y_n$ on $\mathbb{C}^n$ is the main example.

### L2 human

To check that a map $h$ is sesquilinear, fix $w$ and check that $u \mapsto h(u, w)$ is linear, then fix $u$ and check that $w \mapsto \overline{h(u, w)}$ is linear.
For $h(x, y) = i x_2 \bar y_1$ on $\mathbb{C}^2$, the first map is $x \mapsto (i \bar y_1) x_2$, which is linear.
The conjugate of the second is $y \mapsto (\overline{i x_2})\, y_1$, which is linear too, so $h$ is sesquilinear.
Watch out: in the physics convention the same matrix $M$ gives the form $x^* M y$, which is a different form, so always state which slot is conjugated.
