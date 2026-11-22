---
tag: 8NJ7XY6F1S
kind: definition
name: Hermitian form
msc: ["15A63", "11E39"]
topics: [DYAK7YMK7B]
audience: ug1
defines: 48P4A1CX85
uses: [05EGHEQZAW, 054YEQ0Y8M, 0FTH2E9TAS]
sources:
  - url: https://en.wikipedia.org/wiki/Sesquilinear_form
    locator: Hermitian form
---

## Definition

A Hermitian form is a sesquilinear form whose value turns into its complex conjugate when the two vectors are swapped.
Let $V$ be a vector space over $\mathbb{C}$.
Let $h \colon V \times V \to \mathbb{C}$ be a [[sesquilinear form|054YEQ0Y8M]], linear in the first slot and conjugate-linear in the second.
The form $h$ is a *Hermitian form* on $V$ when
$$h(v, u) = \overline{h(u, v)} \qquad \text{for all } u, v \in V,$$
where the bar is the [[complex conjugate|0FTH2E9TAS]].

## Notation

On $\mathbb{C}^n$, with the matrix $M_{ij} = h(e_i, e_j)$, the form is $h(x, y) = x^{\mathsf{T}} M \bar y$, and $M$ is a [[Hermitian matrix|0P17NGQQMQ]]: $M^* = M$.
Physics books take the form conjugate-linear in the first slot instead, and write $h(x, y) = x^* M y$.
The condition $h(v, u) = \overline{h(u, v)}$ reads the same in both conventions.

## Remarks

The definition has two parts, and each one is needed.
Sesquilinearity fixes how $h$ treats scalars: $h(au, v) = a\, h(u, v)$ and $h(u, av) = \bar a\, h(u, v)$.
The Hermitian condition then ties the two slots together, in the way that symmetry does for a [[symmetric bilinear form|0744CN4MDA]].
The two parts fit: if $h$ is Hermitian, the conjugate-linearity in the second slot follows from the linearity in the first, since $h(u, av) = \overline{h(av, u)} = \overline{a\, h(v, u)} = \bar a\, h(u, v)$.

For an example, take $h(x, y) = x_1 \bar y_1 + 2 x_2 \bar y_2$ on $\mathbb{C}^2$.
It is sesquilinear, and $h(y, x) = y_1 \bar x_1 + 2 y_2 \bar x_2 = \overline{h(x, y)}$, so it is Hermitian.
For a case that fails, take $h(x, y) = x_1 \bar y_2$, which is sesquilinear but not Hermitian, since $h(e_1, e_2) = 1$ while $h(e_2, e_1) = 0$.

Putting $u = v$ gives $h(v, v) = \overline{h(v, v)}$, so $h(v, v)$ is real for every $v$.
A Hermitian form is *positive definite* when $h(v, v) > 0$ for all $v \ne 0$, and such a form is a complex [[inner product|0NB0AWGJBW]].
The concept page [[Hermitian form|48P4A1CX85]] gives more examples and the main properties.

## Explanations

### L1 human

A Hermitian form is a sesquilinear form that conjugates its value when you swap the two vectors.
So if one order gives $1 + 2i$, the other order gives $1 - 2i$.
The value of a vector with itself must then equal its own conjugate, so it is always a real number.

### L2 human

Take $h(x, y) = x_1 \bar y_1 + 2 x_2 \bar y_2$ and $v = (1 + i, 1)$.
Then
$$h(v, v) = (1 + i)(1 - i) + 2 \cdot 1 \cdot 1 = 2 + 2 = 4,$$
a real number, as the definition predicts.
Watch out: the condition is $h(v, u) = \overline{h(u, v)}$, not $h(v, u) = h(u, v)$.
The second one fails for this form at $u = e_1$ and $v = i e_1$, since $h(e_1, i e_1) = \bar i = -i$ while $h(i e_1, e_1) = i$.
