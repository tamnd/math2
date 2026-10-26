---
tag: 0W44K2VNBD
kind: definition
name: Sesquilinear form
msc: [15A63]
defines: 054YEQ0Y8M
uses: [05EGHEQZAW]
sources:
  - url: https://en.wikipedia.org/wiki/Sesquilinear_form
    locator: Complex vector spaces
---

## Definition

Let $V$ be a vector space over $\C$.
A *sesquilinear form* on $V$ is a map $\varphi \colon V \times V \to \C$ such that, for all $u, v, w \in V$ and $a \in \C$:

1. $\varphi(u + v, w) = \varphi(u, w) + \varphi(v, w)$ and $\varphi(au, w) = a\, \varphi(u, w)$.
2. $\varphi(u, v + w) = \varphi(u, v) + \varphi(u, w)$ and $\varphi(u, aw) = \bar a\, \varphi(u, w)$.

## Remarks

Here the form is linear in the first argument; many authors, especially in physics, use linearity in the second argument instead.
A sesquilinear form is *Hermitian* when $\varphi(v, u) = \overline{\varphi(u, v)}$ for all $u, v$.
On $\C^n$, each sesquilinear form is $\varphi(x, y) = y^* M x$ for one $n \times n$ complex matrix $M$.
A complex [[inner product|0NB0AWGJBW]] is a positive definite Hermitian sesquilinear form.

## Explanations

### L1 human

Over the complex numbers, bilinear forms cannot be positive, because $\varphi(iv, iv) = -\varphi(v, v)$.
Sesquilinear forms fix this by conjugating the scalar in one argument.
The standard inner product $\sum_i x_i \overline{y_i}$ on $\C^n$ is the main example.
