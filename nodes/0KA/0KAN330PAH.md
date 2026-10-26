---
tag: 0KAN330PAH
kind: definition
name: Nondegenerate bilinear form
msc: [15A63]
defines: 01NHFZF2SK
uses: [0P799D6AMN]
sources:
  - url: https://en.wikipedia.org/wiki/Degenerate_bilinear_form
    locator: Nondegenerate forms
---

## Definition

Let $F$ be a field and let $V$ be a finite-dimensional vector space over $F$.
A [[bilinear form|0SQZMXB6GP]] $B$ on $V$ is *nondegenerate* when, for each $u \in V$,
$$B(u, v) = 0 \text{ for all } v \in V \implies u = 0.$$
A bilinear form that is not nondegenerate is *degenerate*.

## Remarks

$B$ is nondegenerate if and only if its matrix in a basis has a nonzero determinant.
So, in finite dimensions, the condition in the first argument is equivalent to the same condition in the second argument.
$B$ is nondegenerate if and only if $u \mapsto B(u, \cdot)$ is an isomorphism from $V$ to its dual space.
Each inner product is nondegenerate; the form $B(x, y) = x_1 y_1$ on $\R^2$ is degenerate.

## Explanations

### L1 human

A form is nondegenerate when it can detect every nonzero vector.
For each nonzero $u$, some $v$ gives $B(u, v) \ne 0$.
In matrix terms, the matrix of the form is invertible.
