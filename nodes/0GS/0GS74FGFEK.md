---
tag: 0GS74FGFEK
kind: definition
name: Degree of a field extension
msc: [12F05]
defines: 0EAJ2XXADC
uses: [0WQ1A8SHTZ]
sources:
  - url: https://en.wikipedia.org/wiki/Degree_of_a_field_extension
    locator: Definition and notation
---

## Definition

Let $L/K$ be a [[field extension|0WQ1A8SHTZ]].
The field $L$ is a vector space over $K$, with the addition of $L$ and the multiplication $K \times L \to L$ of $L$.
The degree of $L/K$ is the dimension of this vector space, and it is written $[L : K]$.

## Remarks

The degree is a positive integer or an infinite cardinal.
One has $[L : K] = 1$ if and only if $L = K$.
Examples: $[\mathbb{C} : \mathbb{R}] = 2$, with the basis $1, i$. Also, $[\mathbb{Q}(\sqrt{2}) : \mathbb{Q}] = 2$, with the basis $1, \sqrt{2}$.
The field $\mathbb{R}$ has infinite degree over $\mathbb{Q}$, because $\mathbb{Q}$ is countable and $\mathbb{R}$ is not.

## Explanations

### L1 human

The degree counts how many elements of the big field you need, as a basis, to write every element with coefficients in the small field.
Every complex number is $a + b i$ with $a, b$ real, so the degree of $\mathbb{C}$ over $\mathbb{R}$ is $2$.
