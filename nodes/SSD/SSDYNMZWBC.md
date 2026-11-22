---
tag: SSDYNMZWBC
kind: proof
name: Proof of the extreme values of a quadratic form from the Rayleigh quotient
msc: [15A18, 15A63]
topics: [6TSCEW8QMK]
audience: ug1
proves: YS4HT1EYE5
methods: [0NTF6DMVAP]
uses: [T7MFPSY009, 0MB8HQW495, 0VR671PHE5, 0B5H4208Z9]
sources:
  - url: https://en.wikipedia.org/wiki/Rayleigh_quotient
    locator: Bounds for Hermitian M
---

## Proof

We show that on unit vectors the form $q_A$ is the Rayleigh quotient of the operator $\mathbf{x} \mapsto A \mathbf{x}$, and then we apply the theorem on the Rayleigh quotient.
We work in $\mathbb{R}^m$ with the dot product, and we write $T(\mathbf{x}) = A \mathbf{x}$.

1. The operator $T$ is [[self-adjoint|0MB8HQW495]], because $A^{\mathsf{T}} = A$ gives $(A \mathbf{x}) \cdot \mathbf{y} = \mathbf{x}^{\mathsf{T}} A^{\mathsf{T}} \mathbf{y} = \mathbf{x} \cdot (A \mathbf{y})$ for all $\mathbf{x}, \mathbf{y}$.
2. The eigenvalues and eigenvectors of $T$ are those of $A$, since $T \mathbf{x} = \lambda \mathbf{x}$ means $A \mathbf{x} = \lambda \mathbf{x}$.
3. Let $\mathbf{u}$ be a unit vector, so $\mathbf{u} \cdot \mathbf{u} = 1$.
   Then the Rayleigh quotient of $T$ at $\mathbf{u}$ is $R(\mathbf{u}) = (A \mathbf{u}) \cdot \mathbf{u} / (\mathbf{u} \cdot \mathbf{u}) = \mathbf{u}^{\mathsf{T}} A \mathbf{u} = q_A(\mathbf{u})$.
4. By part 1 of [[the Rayleigh quotient statement|T7MFPSY009]] and step 3, $\lambda_m \le q_A(\mathbf{u}) \le \lambda_1$ for every unit vector $\mathbf{u}$.
5. Let $\mathbf{v} = \mathbf{u}_1 / \lVert \mathbf{u}_1 \rVert$.
   It is a unit vector, and $A \mathbf{v} = \lambda_1 \mathbf{v}$ because $A$ is linear.
6. Then $q_A(\mathbf{v}) = \mathbf{v}^{\mathsf{T}} (\lambda_1 \mathbf{v}) = \lambda_1 (\mathbf{v} \cdot \mathbf{v}) = \lambda_1$.
7. By steps 4 and 6, $\lambda_1$ is a value of $q_A$ on unit vectors and no value is larger, so it is the largest value.
   This proves part 1.
8. The same argument with $\mathbf{u}_m / \lVert \mathbf{u}_m \rVert$ and the lower bound of step 4 proves part 2.
9. By step 3 and part 2 of [[the Rayleigh quotient statement|T7MFPSY009]], a unit vector $\mathbf{u}$ has $q_A(\mathbf{u}) = \lambda_1$ exactly when $\mathbf{u}$ is an [[eigenvector|0B5H4208Z9]] of $A$ for $\lambda_1$.
   The same statement for $\lambda_m$ gives the rest of part 3.

## Idea

On unit vectors the denominator of the Rayleigh quotient is $1$, so the quotient and the quadratic form are the same function there.
The result is therefore the Rayleigh quotient theorem for the self-adjoint operator $\mathbf{x} \mapsto A \mathbf{x}$, read on the unit sphere.
The only extra work is to check that the bounds are reached, by evaluating at unit eigenvectors.

## Variants

A direct proof uses [[the principal axis theorem|0PR5P9Z4KM]].
Write $\mathbf{x} = P \mathbf{y}$ with $P$ orthogonal, so that $\lVert \mathbf{y} \rVert = \lVert \mathbf{x} \rVert = 1$ and $q_A = \sum_i \lambda_i y_i^2$.
Then $\lambda_m \sum_i y_i^2 \le \sum_i \lambda_i y_i^2 \le \lambda_1 \sum_i y_i^2$, and the outer sums are $1$.
Equality on the right forces $y_i = 0$ whenever $\lambda_i < \lambda_1$, which says that $\mathbf{x}$ is an eigenvector for $\lambda_1$.

A proof by calculus uses compactness.
The unit sphere is compact and $q_A$ is continuous, so a maximum exists, and at a point of maximum the method of [[Lagrange multipliers|0VKKP8X6Q6]] gives $\nabla q_A = 2\mu \mathbf{x}$.
Since $\nabla q_A = 2A\mathbf{x}$, this says $A\mathbf{x} = \mu \mathbf{x}$, and then $q_A(\mathbf{x}) = \mu$, so the maximum is an eigenvalue, and it must be the largest one.
