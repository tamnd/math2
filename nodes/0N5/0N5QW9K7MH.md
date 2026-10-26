---
tag: 0N5QW9K7MH
kind: statement
role: corollary
name: Degree of a simple extension is the degree of the minimal polynomial
msc: [12F05]
uses: [0ZN39QDTP9, 0GS74FGFEK, 0GK1WB9R98]
sources:
  - url: https://en.wikipedia.org/wiki/Simple_extension
    locator: Definition
---

## Statement

Let $L/K$ be a [[field extension|0WQ1A8SHTZ]] and let $a \in L$ be algebraic over $K$ with [[minimal polynomial|0GK1WB9R98]] $m_a$ of degree $n$.
Then $[K(a) : K] = n$, and $1, a, a^2, \dots, a^{n-1}$ is a basis of $K(a)$ over $K$.

## Remarks

The proof: by [[the structure theorem|0ZN39QDTP9]], $K(a) \cong K[x]/(m_a)$. By polynomial division, the classes of $1, x, \dots, x^{n-1}$ are a basis of $K[x]/(m_a)$.
For example, $[\mathbb{Q}(\sqrt[3]{2}) : \mathbb{Q}] = 3$, with the basis $1, \sqrt[3]{2}, \sqrt[3]{4}$.
With the [[tower law|0A7KJ68XHT]], the degree of every element of a finite extension $L/K$ divides $[L : K]$.

## Explanations

### L1 human

The degree of the field you get by adding one algebraic element is the degree of its minimal polynomial.
Each element of $K(a)$ is a polynomial in $a$ of degree less than $n$, in exactly one way.
