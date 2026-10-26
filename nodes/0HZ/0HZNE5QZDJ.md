---
tag: 0HZNE5QZDJ
kind: definition
name: Quadratic form
msc: [15A63, "11E04"]
defines: 0RBQS1JJCR
uses: [05EGHEQZAW, 0P799D6AMN]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Definitions
---

## Definition

Let $F$ be a field and let $V$ be a finite-dimensional vector space over $F$.
A *quadratic form* on $V$ is a map $Q \colon V \to F$ such that:

1. $Q(av) = a^2 Q(v)$ for all $a \in F$ and $v \in V$.
2. The map $(u, v) \mapsto Q(u + v) - Q(u) - Q(v)$ is a [[bilinear form|0SQZMXB6GP]] on $V$.

## Remarks

On $F^n$, the quadratic forms are the maps $Q(x) = \sum_{i,j} a_{ij} x_i x_j$, that is, homogeneous polynomials of degree $2$.
In matrix notation, $Q(x) = x^T A x$ for an $n \times n$ matrix $A$.
If the characteristic of $F$ is not $2$, the matrix $A$ can be chosen symmetric, and then it is unique.
For example, $Q(x, y) = x^2 + 3xy + 2y^2$ is a quadratic form on $\R^2$.

## Explanations

### L1 human

A quadratic form is a polynomial in which every term has degree two, such as $x^2 - 4xy + y^2$.
It is the simplest kind of function after linear functions.
The squared length $x_1^2 + \cdots + x_n^2$ is the main example.
