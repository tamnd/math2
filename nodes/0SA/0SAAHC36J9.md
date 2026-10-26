---
tag: 0SAAHC36J9
kind: definition
name: Generalised eigenvector
msc: [15A18]
defines: 01H6QKWGDH
uses: [0B5H4208Z9, 0BNEXSKNRV]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_eigenvector
    locator: Overview and definition
---

## Definition

Let $F$ be a field, let $V$ be a vector space over $F$, let $T \colon V \to V$ be an endomorphism, and let $\lambda \in F$.
A *generalised eigenvector* of $T$ for $\lambda$ is a vector $v \in V$ with $v \ne 0$ and
$$(T - \lambda \id_V)^k (v) = 0$$
for some integer $k \ge 1$.
The least such $k$ is the *rank* of the generalised eigenvector.

## Remarks

The generalised eigenvectors of rank $1$ are the [[eigenvectors|0N6960W0BV]].
If a generalised eigenvector for $\lambda$ exists, then $\lambda$ is an eigenvalue.
For $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, the vector $e_2$ is a generalised eigenvector for $1$ of rank $2$, and it is not an eigenvector.

## Explanations

### L1 human

Some matrices do not have enough eigenvectors to make a basis.
Generalised eigenvectors fill the gap: they reach zero after several applications of $T - \lambda \id$ instead of one.
They are the building blocks of the Jordan normal form.
