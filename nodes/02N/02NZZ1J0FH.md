---
tag: 02NZZ1J0FH
kind: definition
name: Splitting field
msc: [12F05]
defines: 0KXQKX9P63
uses: [0SHMC00RJV, 0MA5B744K3, 0WQ1A8SHTZ]
sources:
  - url: https://en.wikipedia.org/wiki/Splitting_field
    locator: Definition
---

## Definition

Let $K$ be a [[field|0QA8CHH8MG]] and let $f \in K[x]$ be nonzero.
A splitting field of $f$ over $K$ is a [[field extension|0WQ1A8SHTZ]] $L/K$ with these two properties.

1. The polynomial $f$ [[splits|0SHMC00RJV]] over $L$, as $f = c \, (x - a_1) \cdots (x - a_n)$.
2. The field $L$ is [[generated over $K$|0MA5B744K3]] by the roots: $L = K(a_1, \dots, a_n)$.

## Remarks

Splitting fields [[exist|01441KDGBY]] and are [[unique up to isomorphism|069A3BC3EP]].
The splitting field of $x^2 + 1$ over $\mathbb{R}$ is $\mathbb{C}$.
The splitting field of $x^3 - 2$ over $\mathbb{Q}$ is $\mathbb{Q}(\sqrt[3]{2}, \omega)$ with $\omega = e^{2\pi i/3}$. Its degree over $\mathbb{Q}$ is $6$.
The splitting field of $x^q - x$ over $\mathbb{F}_p$, for $q = p^n$, is the [[finite field|08RTDHX1SK]] with $q$ elements.

## Explanations

### L1 human

A splitting field is the smallest field that contains all the roots of a polynomial.
It is where the polynomial factors completely.
For $x^3 - 2$, the real cube root of $2$ is not enough, because the other two roots are not real.
