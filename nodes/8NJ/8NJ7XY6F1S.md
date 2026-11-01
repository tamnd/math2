---
tag: 8NJ7XY6F1S
kind: definition
name: Hermitian form
msc: [15A63, "11E39"]
defines: 48P4A1CX85
uses: [05EGHEQZAW, 054YEQ0Y8M, 0FTH2E9TAS]
sources:
  - url: https://en.wikipedia.org/wiki/Sesquilinear_form
---

## Definition

Let $V$ be a vector space over $\C$.
Let $h \colon V \times V \to \C$ be a [[sesquilinear form|054YEQ0Y8M]], linear in the first argument and conjugate-linear in the second.
The form $h$ is a *Hermitian form* on $V$ when
$$h(v, u) = \overline{h(u, v)} \qquad \text{for all } u, v \in V,$$
where the bar is the [[complex conjugate|0FTH2E9TAS]].

## Remarks

Example: on $\C^2$, let $h(x, y) = x_1 \overline{y_1} + 2 x_2 \overline{y_2}$.
It is sesquilinear, and $h(y, x) = y_1 \overline{x_1} + 2 y_2 \overline{x_2} = \overline{h(x, y)}$, so it is Hermitian.
Non-example: $h(x, y) = x_1 \overline{y_2}$ on $\C^2$ is sesquilinear but not Hermitian, because $h(e_1, e_2) = 1$ while $h(e_2, e_1) = 0$.
Taking $u = v$ gives $h(v, v) = \overline{h(v, v)}$, so $h(v, v)$ is real for every $v$.
On $\C^n$, every Hermitian form is $h(x, y) = y^* M x$ for one [[Hermitian matrix|0P17NGQQMQ]] $M$, that is, $M^* = M$.
Some authors take the form conjugate-linear in the first argument instead; the condition $h(v, u) = \overline{h(u, v)}$ is the same.
