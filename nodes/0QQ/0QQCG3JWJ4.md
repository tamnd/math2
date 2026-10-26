---
tag: 0QQCG3JWJ4
kind: definition
name: Positive definite matrix
msc: [15B57, 15A63]
defines: 0KX66CZMBB
uses: [0EKZCX4K3P, 0N28QN4CYA]
sources:
  - url: https://en.wikipedia.org/wiki/Definite_matrix
    locator: Definitions
---

## Definition

Let $A$ be an $n \times n$ complex [[Hermitian matrix|0P17NGQQMQ]].
The matrix $A$ is *positive definite* when
$$x^* A x > 0 \qquad \text{for all } x \in \C^n \text{ with } x \ne 0.$$
A real [[symmetric matrix|0VR671PHE5]] $A$ is positive definite when $x^T A x > 0$ for all $x \in \R^n$ with $x \ne 0$.

## Remarks

For a Hermitian $A$, the number $x^* A x$ is always real.
The identity matrix and $\begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$ are positive definite.
$A$ is positive definite if and only if all its eigenvalues are positive.
$A$ is positive definite if and only if $\langle x, y \rangle = y^* A x$ is an inner product on $\C^n$.

## Explanations

### L1 human

A positive definite matrix gives a positive number $x^T A x$ for every nonzero vector $x$.
Such matrices behave like positive numbers in many ways: they have square roots and positive determinants.
They appear as Hessians at minima and as covariance matrices.
