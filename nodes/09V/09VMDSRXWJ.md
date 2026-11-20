---
tag: 09VMDSRXWJ
kind: concept
name: Singular value
msc: [15A18]
topics: [SS4EVPKT3A]
audience: ug1
uses: [0K2TX12X58, 0AM050KCAW, 0BQAA2BK3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_value
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Singular_value
    locator: Basic properties
  - book: isbn:9780321982384
    locator: Section 7.4
  - book: isbn:9783031410253
    locator: Chapter 7
same_as:
  wikidata: Q4166054
  wikipedia: Singular value
inventory: [VPY36AXZE7]
---

## Summary

Let $A$ be an $m \times n$ complex matrix.
The matrix $A^* A$ is [[positive semidefinite|01MMVW8CKC]], so its eigenvalues $\lambda_1 \ge \dots \ge \lambda_n$ are real and nonnegative.
The singular values of $A$ are the numbers $\sigma_i = \sqrt{\lambda_i}$, by the [[formal definition|0K2TX12X58]].
They measure how much $A$ stretches space in its main directions, and they exist for every matrix, also for rectangular ones.

## Motivation

Eigenvalues describe a square matrix that maps a space to itself.
They do not exist for a rectangular matrix, and for a square matrix they can hide how much the matrix stretches vectors.
For example, $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has the eigenvalues $1, 1$, but it stretches $(0, 1)$ to $(1, 1)$, a longer vector.
The singular values describe the size of $Ax$ for unit vectors $x$.
The unit sphere goes to an ellipsoid, and the singular values are the lengths of its semi-axes.
They are the diagonal of the [[singular value decomposition|000NPTMX6J]].

## Notation

- We write $\sigma_1(A) \ge \sigma_2(A) \ge \dots$, always in decreasing order.
- Books differ on how many values to list. Some books list $n$ values, from $A^* A$. Others list $\min(m, n)$ values, or only the $r = \rank A$ nonzero ones. The nonzero values are the same in all conventions.
- $\sigma_{\max}(A) = \sigma_1(A)$, and $\sigma_{\min}(A)$ is the last listed value.

## Remarks

### Examples

- [[The matrix $\begin{pmatrix} 3 & 0 \\ 4 & 5 \end{pmatrix}$|B546BDVFQZ]] has the singular values $3\sqrt5$ and $\sqrt5$. Its eigenvalues are $3$ and $5$.
- [[The $3 \times 2$ matrix $\begin{pmatrix} 1 & 1 \\ 1 & 0 \\ 0 & 1 \end{pmatrix}$|GK1B93DKD3]] has the singular values $\sqrt3$ and $1$.
- A diagonal matrix $\operatorname{diag}(d_1, \dots, d_n)$ has the singular values $\abs{d_1}, \dots, \abs{d_n}$, sorted in decreasing order.
- A [[unitary matrix|0AR68JTMDT]] has all singular values $1$, since $U^* U = I$.
- A rank-one matrix $u v^*$ with $u \in \C^m$, $v \in \C^n$ has one nonzero singular value, $\norm u \norm v$. Indeed $(uv^*)^* (uv^*) = \norm{u}^2 v v^*$, with the nonzero eigenvalue $\norm u^2 \norm v^2$.

### Non-examples

- [[The eigenvalues of $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$|S3ZGYKVBRR]] are $1, 1$, but its singular values are $\tfrac{\sqrt5 + 1}{2}$ and $\tfrac{\sqrt5 - 1}{2}$.
- The eigenvalues of $\operatorname{diag}(-2, 1)$ are $-2$ and $1$. Singular values are never negative; here they are $2$ and $1$.
- The eigenvalues of $A^* A$ are not the singular values of $A$. They are the squares $\sigma_i^2$.

### Basic properties

- The number of nonzero singular values is the rank of $A$, by [[the rank theorem for singular values|6VXM1T8PG7]].
- $\sigma_1(A) = \max_{\norm x = 1} \norm{Ax}$, the [[operator norm|06EKW1AKXF]] for the Euclidean norms. This is also in that theorem.
- $\sigma_1^2 + \dots + \sigma_n^2 = \norm{A}_F^2$, the square of the [[Frobenius norm|JT8Q204E4R]].
- $A$ and $A^*$ have the same nonzero singular values.
- $\sigma_i(WAV) = \sigma_i(A)$ for unitary $W$ and $V$, since $(WAV)^*(WAV) = V^* A^* A V$ has the same eigenvalues as $A^* A$.
- For a [[normal matrix|0MR0BYF0K2]], the singular values are the absolute values of the eigenvalues. For a positive semidefinite matrix, they are the eigenvalues.
- For an $n \times n$ matrix, $\abs{\det A} = \sigma_1 \cdots \sigma_n$, since $\abs{\det A}^2 = \det(A^* A) = \lambda_1 \cdots \lambda_n$.

### History

According to the Wikipedia article on singular values, the concept was introduced by Erhard Schmidt in 1907, who called the numbers eigenvalues.
The same article says that the name singular value was first quoted by Smithies in 1937.

### Common errors

- Students use the eigenvalues of $A$ as its singular values. [[The shear example|S3ZGYKVBRR]] shows the difference.
- Students forget the square root and use the eigenvalues of $A^* A$.
- Students list the singular values in increasing order; the convention is decreasing.

## Explanations

### L1 human

A matrix turns a circle into an ellipse.
The singular values are the half-lengths of the long axis and the short axis of that ellipse.
To compute them, form $A^T A$, find its eigenvalues, and take their square roots.
For $A = \begin{pmatrix} 3 & 0 \\ 4 & 5 \end{pmatrix}$, $A^T A$ has the eigenvalues $45$ and $5$, so the singular values are $3\sqrt5$ and $\sqrt5$.

### L2 human

Recipe:

1. Compute $A^* A$, an $n \times n$ positive semidefinite matrix.
2. Find its eigenvalues $\lambda_1 \ge \dots \ge \lambda_n \ge 0$.
3. Take $\sigma_i = \sqrt{\lambda_i}$.

If $m < n$, it is faster to use $A A^*$, which is $m \times m$; it has the same nonzero eigenvalues.
Uses: the rank of a matrix is the number of nonzero singular values, and the ratio $\sigma_1 / \sigma_n$ measures how close a square matrix is to a singular one.
A trap: the eigenvalues of a non-normal matrix can be much smaller than its largest singular value.

### L3 human

The singular values are the complete invariants of a matrix under $A \mapsto W A V$ with $W, V$ unitary.
So two $m \times n$ matrices are unitarily equivalent in this sense exactly when they have the same singular values.
The singular values are $1$-Lipschitz functions of $A$ in the operator norm, by Weyl's perturbation inequality; this belongs to matrix analysis.
For [[compact operators|QSJKPKPM7H]] on a Hilbert space, singular values are defined in the same way, and they lead to the Schatten classes of functional analysis.
