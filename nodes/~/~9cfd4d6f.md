---
tag: ~9cfd4d6f
kind: statement
role: corollary
name: Degree of a simple extension is the degree of the minimal polynomial
msc: [12F05]
uses: [~973f8b7f, ~dede2e51, ~fe14474d]
sources:
  - url: https://en.wikipedia.org/wiki/Simple_extension
    locator: Definition
---

## Statement

Let $L/K$ be a [[field extension|~05511c4e]] and let $a \in L$ be algebraic over $K$ with [[minimal polynomial|~fe14474d]] $m_a$ of degree $n$.
Then $[K(a) : K] = n$, and $1, a, a^2, \dots, a^{n-1}$ is a basis of $K(a)$ over $K$.

## Remarks

The proof: by [[the structure theorem|~973f8b7f]], $K(a) \cong K[x]/(m_a)$. By polynomial division, the classes of $1, x, \dots, x^{n-1}$ are a basis of $K[x]/(m_a)$.
For example, $[\mathbb{Q}(\sqrt[3]{2}) : \mathbb{Q}] = 3$, with the basis $1, \sqrt[3]{2}, \sqrt[3]{4}$.
With the [[tower law|~1fa33f36]], the degree of every element of a finite extension $L/K$ divides $[L : K]$.

## Explanations

### L1 human

The degree of the field you get by adding one algebraic element is the degree of its minimal polynomial.
Each element of $K(a)$ is a polynomial in $a$ of degree less than $n$, in exactly one way.
