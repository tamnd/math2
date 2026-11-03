---
kind: statement
msc:
- 15A03
name: Nonzero subspaces of R^n have a basis and a well-defined dimension
role: theorem
sources:
- locator: ap-linear-algebra.tex:4601
  url: https://github.com/jirilebl/diffyqs/blob/658bcae9fb710f3fae2c9da4ca4524ce157453af/ap-linear-algebra.tex#L4601
tag: TPGDCRJAEC
uses:
- 00YC1D652K
- 0KCQ9Y3QKA
- 03GSZ8RTZJ
---

## Statement

Let $S$ be a [[linear subspace|00YC1D652K]] of $\mathbb{R}^n$ with $S \neq \{\vec{0}\}$.
Then there is exactly one positive integer $k$ such that $S$ has a [[basis|0KCQ9Y3QKA]] $\vec{v}_1, \ldots, \vec{v}_k$ with $k$ vectors.
This $k$ is the [[dimension|03GSZ8RTZJ]] of $S$.
The basis itself is not unique.
For any such basis, each $\vec{w} \in S$ can be written as $\vec{w} = \alpha_1 \vec{v}_1 + \cdots + \alpha_k \vec{v}_k$, and the scalars $\alpha_1, \ldots, \alpha_k$ are determined by $\vec{w}$.

## Remarks

The number of vectors is the same for every basis of $S$.
Different bases give different coefficients for the same vector.
