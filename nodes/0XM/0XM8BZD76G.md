---
tag: 0XM8BZD76G
kind: object
name: Coordinate space
msc: [15A03]
instance_of: [000AYPA9AJ]
sources:
  - url: https://en.wikipedia.org/wiki/Vector_space
    locator: lead section
---

## Description

Let $F$ be a field and let $n \ge 0$ be an integer.
The *coordinate space* $F^n$ is the set of $n$-tuples $(x_1, \dots, x_n)$ with $x_i \in F$.
It is a [[vector space|000AYPA9AJ]] over $F$ with the operations
$$(x_1, \dots, x_n) + (y_1, \dots, y_n) = (x_1 + y_1, \dots, x_n + y_n), \qquad a(x_1, \dots, x_n) = (ax_1, \dots, ax_n).$$
Its zero vector is $(0, \dots, 0)$.

## Remarks

The space $F^n$ has [[dimension|03GSZ8RTZJ]] $n$, with the [[standard basis|0V7ZD6P7RK]] $e_1, \dots, e_n$.
More generally, for a set $I$, the set $F^I$ of all functions $I \to F$ is a vector space with pointwise operations.
Each $n$-dimensional vector space over $F$ is isomorphic to $F^n$.
The real spaces $\R^2$ and $\R^3$ model the plane and ordinary space.

## Explanations

### L1 human

The coordinate space $F^n$ is the space of lists of $n$ numbers.
We add two lists position by position, and we scale a list by scaling each entry.
Every finite-dimensional vector space looks like one of these spaces after we choose a basis.
