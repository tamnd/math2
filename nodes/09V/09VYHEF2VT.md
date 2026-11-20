---
tag: 09VYHEF2VT
kind: definition
name: Orthonormal family
msc: ["15A63", "46C05"]
topics: [1D4JTZ9VS3]
audience: ug1
defines: 0RW9TNNT87
uses: [01EK923SKP, 0TS7VZJBWD, 0KG4D8AP6G]
sources:
  - url: https://en.wikipedia.org/wiki/Orthonormality
    locator: Definition
  - book: isbn:9783031410253
    locator: Chapter 6
formal:
  - system: lean4
    library: mathlib
    decl: Orthonormal
    match: exact
---

## Definition

Let $V$ be an [[inner product space|01EK923SKP]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, and let $I$ be a set.
A family $(e_i)_{i \in I}$ of vectors of $V$ is orthonormal when, for all $i, j \in I$,
$$\ip{e_i}{e_j} = \delta_{ij},$$
where $\delta_{ij} = 1$ if $i = j$ and $\delta_{ij} = 0$ if $i \neq j$.
Equivalently, $\norm{e_i} = 1$ for every $i$ in the [[induced norm|0KG4D8AP6G]], and $e_i$ and $e_j$ are [[orthogonal|0TS7VZJBWD]] for $i \neq j$.
A set $S \subseteq V$ is orthonormal when the family $(s)_{s \in S}$, indexed by $S$ itself, is orthonormal.

## Notation

- For a finite family we write $(e_1, \dots, e_k)$, and some books call it an orthonormal list.
- Mathlib writes `Orthonormal 𝕜 v` for a family `v : ι → E`. It asks `‖v i‖ = 1` for all `i` and `⟪v i, v j⟫ = 0` for `i ≠ j`.

## Remarks

The two forms of the definition agree, because $\ip{e_i}{e_i} = \norm{e_i}^2$, and $\norm{e_i}^2 = 1$ holds exactly when $\norm{e_i} = 1$.
The condition is symmetric in $i$ and $j$, since $\ip{e_j}{e_i} = \overline{\ip{e_i}{e_j}}$ and $\overline{\delta_{ij}} = \delta_{ij}$.
The definition does not ask that the family spans $V$; an orthonormal family that spans $V$ is an [[orthonormal basis|0FWJ0VW561]].
For $V = \mathbb{K}^n$ and $k$ vectors, the condition says $Q^* Q = I_k$ for the $n \times k$ matrix $Q$ with columns $e_1, \dots, e_k$.

## Explanations

### L1 human

An orthonormal family is like a set of coordinate axes: unit vectors at right angles.
All inner products between its vectors are $0$ or $1$.
A vector paired with itself gives $1$, and two different vectors give $0$.

### L2 human

To check the definition for $e_1, \dots, e_k$, compute the $k \times k$ table of all $\ip{e_i}{e_j}$.
The family is orthonormal exactly when this table is the identity matrix $I_k$.
This table is the [[Gram matrix|00SPJSDT3Z]] of the family, up to a transpose.
By conjugate symmetry, it is enough to compute the diagonal and the entries above it.
For $(\frac35, \frac45)$ and $(-\frac45, \frac35)$ in $\mathbb{R}^2$, the diagonal entries are $1$ and the entry above it is $0$.

### L3 human

The definition is the special case of an orthogonal family for a positive definite Hermitian form, with the normalization $\ip{e_i}{e_i} = 1$.
Mathlib states it with norms and pairwise orthogonality, and its inner product is conjugate-linear in the first argument.
The condition $\ip{e_i}{e_j} = \delta_{ij}$ does not depend on that convention.
The same definition works in every inner product space, also in infinite dimension, where an orthonormal family can be uncountable.
