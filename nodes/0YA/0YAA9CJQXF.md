---
tag: 0YAA9CJQXF
kind: definition
name: Primitive element of a finite field
msc: ["12E20"]
defines: 00QSK85Y2X
uses: [08RTDHX1SK, 0EBZ3G455G]
sources:
  - url: https://en.wikipedia.org/wiki/Primitive_element_(finite_field)
    locator: lead section
---

## Definition

Let $F$ be a [[finite field|08RTDHX1SK]] of order $q$.
An element $\alpha \in F$ is a primitive element of $F$ if $\alpha$ generates the multiplicative group $F^\times$.
That is, $F^\times = \{ \alpha, \alpha^2, \dots, \alpha^{q-1} = 1 \}$.

## Remarks

Primitive elements exist, because [[$F^\times$ is cyclic|0EBZ3G455G]]. There are exactly $\varphi(q - 1)$ of them, where $\varphi$ is Euler's totient function.
The element $2$ is a primitive element of $\mathbb{F}_3$ and of $\mathbb{F}_5$, but not of $\mathbb{F}_7$. The element $3$ is a primitive element of $\mathbb{F}_7$.
A primitive element $\alpha$ of $F$ generates $F$ as a [[simple extension|0P6SBR7YM2]] of its prime subfield. The converse is false in general.

## Explanations

### L1 human

A primitive element is one whose powers give every nonzero element of the field.
It works like a base for logarithms in the finite field.
