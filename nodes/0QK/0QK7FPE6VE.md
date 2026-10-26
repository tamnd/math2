---
tag: 0QK7FPE6VE
kind: statement
role: proposition
name: Dimension of the coordinate space
msc: [15A03]
uses: [05G2G0P224, 0XM8BZD76G]
sources:
  - url: https://en.wikipedia.org/wiki/Dimension_(vector_space)
    locator: Examples
---

## Statement

Let $F$ be a field and let $n \ge 0$ be an integer.
The [[coordinate space|0XM8BZD76G]] $F^n$ has [[dimension|03GSZ8RTZJ]] $n$ over $F$.

## Remarks

The [[standard basis|0V7ZD6P7RK]] $e_1, \dots, e_n$ is a basis of $F^n$ with $n$ vectors.
A consequence: each $n$-dimensional space over $F$ is isomorphic to $F^n$.
In Mathlib, the index type is `Fin n`, and the space is the type of functions `Fin n → F`.

## Explanations

### L1 human

The space of lists of $n$ numbers has dimension $n$.
The $n$ standard unit vectors form a basis.
For example, $\R^3$ has dimension $3$.
