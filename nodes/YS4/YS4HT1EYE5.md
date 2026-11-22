---
tag: YS4HT1EYE5
kind: statement
role: theorem
name: Extreme values of a quadratic form on unit vectors
aliases: [constrained-optimization-of-quadratic-forms]
msc: [15A18, 15A63]
topics: [6TSCEW8QMK]
audience: ug1
about: [0RBQS1JJCR, 0VR671PHE5]
uses: [0RBQS1JJCR, 0VR671PHE5, 0BQAA2BK3Q, T7MFPSY009]
proofs: [SSDYNMZWBC]
sources:
  - locator: src/section7-2.xml:839
    url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section7-2.xml#L839
  - url: https://en.wikipedia.org/wiki/Rayleigh_quotient
    locator: Bounds for Hermitian M
  - book: isbn:9780321982384
---

## Statement

On the unit sphere, a real quadratic form reaches its largest value at an eigenvector of the largest eigenvalue, and its smallest value at an eigenvector of the smallest eigenvalue, and these values are the eigenvalues themselves.

Let $A$ be a real [[symmetric matrix|0VR671PHE5]] of size $m \times m$, and let $q_A(\mathbf{u}) = \mathbf{u}^{\mathsf{T}} A \mathbf{u}$ be its [[quadratic form|0RBQS1JJCR]] on $\mathbb{R}^m$.
List the [[eigenvalues|0BQAA2BK3Q]] of $A$ in decreasing order, $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_m$, and choose vectors $\mathbf{u}_1, \dots, \mathbf{u}_m$ that form a basis of $\mathbb{R}^m$ with $A \mathbf{u}_i = \lambda_i \mathbf{u}_i$.

1. Over all unit vectors $\mathbf{u}$, the largest value of $q_A(\mathbf{u})$ is $\lambda_1$, and it is reached at $\mathbf{u}_1 / \lVert \mathbf{u}_1 \rVert$.
2. Over all unit vectors $\mathbf{u}$, the smallest value of $q_A(\mathbf{u})$ is $\lambda_m$, and it is reached at $\mathbf{u}_m / \lVert \mathbf{u}_m \rVert$.
3. A unit vector $\mathbf{u}$ has $q_A(\mathbf{u}) = \lambda_1$ if and only if $A \mathbf{u} = \lambda_1 \mathbf{u}$, and it has $q_A(\mathbf{u}) = \lambda_m$ if and only if $A \mathbf{u} = \lambda_m \mathbf{u}$.

This is the case of real symmetric matrices of [[the extreme values of the Rayleigh quotient|T7MFPSY009]].

## Remarks

### A first computation

Take $q = 5x^2 + 4xy + 2y^2$, with matrix $A = \begin{pmatrix} 5 & 2 \\ 2 & 2 \end{pmatrix}$ and eigenvalues $6$ on $(2, 1)$ and $1$ on $(-1, 2)$.
The theorem says that on the unit circle $q$ lies between $1$ and $6$.
Try a few unit vectors:
$$q(1, 0) = 5, \qquad q(0, 1) = 2, \qquad q\left( \tfrac{1}{\sqrt{2}}, \tfrac{1}{\sqrt{2}} \right) = \tfrac{11}{2}.$$
All three values lie in $[1, 6]$.
At $(2, 1)/\sqrt{5}$ the value is $(20 + 8 + 2)/5 = 6$, and at $(-1, 2)/\sqrt{5}$ it is $(5 - 8 + 8)/5 = 1$, so both ends are reached.
[[The ellipse example|GP4XSY4FNH]] and [[the Rayleigh quotient example|3FXAQ6P15S]] use the same matrix.

### Why each hypothesis is needed

The matrix must be symmetric, or the eigenvalues must come from its symmetric part.
The matrix $\begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix}$ has only the eigenvalue $1$, but its form $x^2 + 4xy + y^2$ is $3$ at $(1, 1)/\sqrt{2}$.
Its symmetric part $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ has the eigenvalues $3$ and $-1$, and these are the true extremes.

The vectors must have length $1$.
Without that bound, $q_A(t \mathbf{u}) = t^2 q_A(\mathbf{u})$ grows without limit as $t$ grows whenever $\lambda_1 > 0$, so there is no maximum.

The space must be real for the form $\mathbf{u}^{\mathsf{T}} A \mathbf{u}$.
For complex vectors, the right form is $\bar{\mathbf{u}}^{\mathsf{T}} A \mathbf{u}$ with $A$ Hermitian, as in [[the Rayleigh quotient statement|T7MFPSY009]].

### What it gives you

Scaling a vector $\mathbf{x} \ne 0$ to the unit vector $\mathbf{x}/\lVert \mathbf{x} \rVert$ gives the bounds
$$\lambda_m \lVert \mathbf{x} \rVert^2 \le \mathbf{x}^{\mathsf{T}} A \mathbf{x} \le \lambda_1 \lVert \mathbf{x} \rVert^2 \qquad \text{for every } \mathbf{x} \in \mathbb{R}^m.$$
So $q_A$ is [[positive definite|0RP20HFYM3]] exactly when $\lambda_m > 0$, and negative definite exactly when $\lambda_1 < 0$.
The bounds also give the operator norm of a symmetric matrix as $\max(\lvert \lambda_1 \rvert, \lvert \lambda_m \rvert)$.

### The converse and the values between

Part 3 is already an equivalence, so the extremes are reached only at eigenvectors.
Every number between $\lambda_m$ and $\lambda_1$ is also a value of $q_A$ on unit vectors when $m \ge 2$.
The reason is that the unit sphere is connected and $q_A$ is continuous, so its values on the sphere form an interval.

### Generalizations

The other eigenvalues are extremes too: $\lambda_2$ is the maximum of $q_A$ on the unit vectors orthogonal to $\mathbf{u}_1$.
[[The Courant-Fischer theorem|CJK2HS2508]] gives every $\lambda_k$ as a max-min over subspaces, with no need to know the eigenvectors first.
With a positive definite matrix $M$ in place of the identity, the extremes of $\mathbf{x}^{\mathsf{T}} A \mathbf{x}$ on the set $\mathbf{x}^{\mathsf{T}} M \mathbf{x} = 1$ are the largest and smallest roots of $\det(A - \lambda M) = 0$.

### Try it

First, find the largest value of $3x^2 + 2xy + 3y^2$ on the unit circle.
The eigenvalues of $\begin{pmatrix} 3 & 1 \\ 1 & 3 \end{pmatrix}$ are $4$ and $2$, so the largest value is $4$, reached at $\pm(1, 1)/\sqrt{2}$.

Second, find the smallest value of $x^2 + y^2 + z^2 + 2xy$ on the unit sphere.
The matrix has blocks $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$ and $(1)$, with eigenvalues $2$, $0$ and $1$, so the smallest value is $0$, reached at $\pm(1, -1, 0)/\sqrt{2}$.

## Explanations

### L1 human

Walk around the unit circle and record the value of a quadratic form at each point.
The values go up and down, and they have a largest and a smallest value.
For $5x^2 + 4xy + 2y^2$ the largest is $6$ and the smallest is $1$, and these are the two eigenvalues of its matrix.
They are reached in the directions of the principal axes of the form.

### L2 human

Here is a typical problem: find the largest value of $q = x^2 + 4xy + y^2$ on the unit circle, and the point where it is reached.
Write the matrix with half of $4$ in each off-diagonal place, $A = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$.
Its characteristic polynomial is $(1 - t)^2 - 4 = (t - 3)(t + 1)$, so $\lambda_1 = 3$, with eigenvector $(1, 1)$.
The maximum is $3$, at the unit vectors $\pm(1, 1)/\sqrt{2}$.
Check: $q(1/\sqrt{2}, 1/\sqrt{2}) = \tfrac{1}{2}(1 + 4 + 1) = 3$.
No calculus was needed, only one eigenvalue problem.
Watch out: give the point as a unit vector, so normalize the eigenvector before you state the answer.

### L3 human

In the coordinates of [[the principal axis theorem|0PR5P9Z4KM]], $q_A = \sum_i \lambda_i y_i^2$ with $\sum_i y_i^2 = 1$.
So on the sphere $q_A$ is a weighted average of the eigenvalues, with weights $y_i^2$, and an average lies between the smallest and the largest of the numbers averaged.
This is the basis of [[principal component analysis|ABXD13M340]], where $A$ is a covariance matrix and $\lambda_1$ is the largest variance of a projection onto a line.
The critical points of $q_A$ on the sphere, found by [[Lagrange multipliers|0VKKP8X6Q6]], are exactly the unit eigenvectors, and the values there are all the eigenvalues.
