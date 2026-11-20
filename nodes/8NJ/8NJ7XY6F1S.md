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

Let $V$ be a vector space over $\C$.
Let $h \colon V \times V \to \C$ be a [[sesquilinear form|054YEQ0Y8M]], linear in the first slot and conjugate-linear in the second.
The form $h$ is a *Hermitian form* on $V$ when
$$h(v, u) = \overline{h(u, v)} \qquad \text{for all } u, v \in V,$$
where the bar is the [[complex conjugate|0FTH2E9TAS]].

## Notation

On $\C^n$, with the matrix $M_{ij} = h(e_i, e_j)$, the form is $h(x, y) = x^T M \bar y$, and $M$ is a [[Hermitian matrix|0P17NGQQMQ]]: $M^* = M$.
Some authors take the form conjugate-linear in the first slot instead, and write $h(x, y) = x^* M y$.
The condition $h(v, u) = \overline{h(u, v)}$ is the same in both conventions.

## Remarks

Example: on $\C^2$, let $h(x, y) = x_1 \bar y_1 + 2 x_2 \bar y_2$.
It is sesquilinear, and $h(y, x) = y_1 \bar x_1 + 2 y_2 \bar x_2 = \overline{h(x, y)}$, so it is Hermitian.
Non-example: $h(x, y) = x_1 \bar y_2$ on $\C^2$ is sesquilinear but not Hermitian, because $h(e_1, e_2) = 1$ while $h(e_2, e_1) = 0$.
Taking $u = v$ gives $h(v, v) = \overline{h(v, v)}$, so $h(v, v)$ is real for every $v$.
A Hermitian form $h$ is *positive definite* when $h(v, v) > 0$ for all $v \neq 0$; such a form is a complex [[inner product|0NB0AWGJBW]].

## Explanations

### L1 human

A Hermitian form is a sesquilinear form that conjugates its value when the two vectors are swapped.
So the value of a vector with itself is always real.

### L2 human

For $h(x, y) = x_1 \bar y_1 + 2 x_2 \bar y_2$ and $v = (1 + i, 1)$, we get $h(v, v) = (1 + i)(1 - i) + 2 = 2 + 2 = 4$, a real number.
A trap: the condition is $h(v, u) = \overline{h(u, v)}$, not $h(v, u) = h(u, v)$; the second one fails for this form at $u = e_1$, $v = i e_1$, since $h(e_1, ie_1) = -i$ and $h(ie_1, e_1) = i$.
