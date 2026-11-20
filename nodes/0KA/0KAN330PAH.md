---
tag: 0KAN330PAH
kind: definition
name: Nondegenerate bilinear form
msc: ["15A63"]
topics: [DYAK7YMK7B]
audience: ug1
defines: 01NHFZF2SK
uses: [0P799D6AMN]
formal:
  - system: lean4
    library: mathlib
    decl: LinearMap.BilinForm.Nondegenerate
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Degenerate_bilinear_form
    locator: Nondegenerate forms
---

## Definition

Let $F$ be a field and let $V$ be a finite-dimensional vector space over $F$.
A [[bilinear form|0SQZMXB6GP]] $B$ on $V$ is *nondegenerate* when, for each $u \in V$,
$$B(u, v) = 0 \text{ for all } v \in V \implies u = 0.$$
A bilinear form that is not nondegenerate is *degenerate*.
The set of $u$ with $B(u, v) = 0$ for all $v$ is the *left radical* of $B$, and the set of $v$ with $B(u, v) = 0$ for all $u$ is the *right radical*.

## Notation

For a reflexive form the two radicals agree, and we write $\operatorname{rad} B$ or $V^\perp$.
Mathlib writes `B.Nondegenerate` for `B : LinearMap.BilinForm F V`.

## Remarks

$B$ is nondegenerate if and only if its matrix in a basis has a nonzero determinant, by the [[criteria for nondegeneracy|3ND2FNJ38Y]].
So, in finite dimensions, the condition in the first argument is equivalent to the same condition in the second argument.
$B$ is nondegenerate if and only if $u \mapsto B(u, \cdot)$ is an isomorphism from $V$ to its dual space.
Each inner product is nondegenerate; the form $B(x, y) = x_1 y_1$ on $\R^2$ is degenerate.

## Explanations

### L1 human

A form is nondegenerate when it can detect every nonzero vector.
For each nonzero $u$, some $v$ gives $B(u, v) \ne 0$.
In matrix terms, the matrix of the form is invertible.

### L2 human

For $B(x, y) = x_1 y_1$ on $\R^2$, take $u = (0, 1)$.
Then $B(u, v) = 0 \cdot v_1 = 0$ for every $v$, and $u \neq 0$.
So $B$ is degenerate, and $u$ spans its radical.
A trap: the definition asks for one $u \neq 0$ that gives $0$ with every $v$, not for one pair with value $0$.
