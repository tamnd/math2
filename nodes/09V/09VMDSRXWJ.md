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

A matrix stretches some directions more than others, and the singular values are the stretch factors in its main directions.
Every matrix has them, square or rectangular, and they are never negative.
Let $A$ be an $m \times n$ complex matrix.
The matrix $A^* A$ is [[positive semidefinite|01MMVW8CKC]], so its [[eigenvalues|0BQAA2BK3Q]] $\lambda_1 \ge \dots \ge \lambda_n$ are real and nonnegative.
The *singular values* of $A$ are their square roots,
$$\sigma_i = \sqrt{\lambda_i} \qquad (1 \le i \le n),$$
as the [[formal definition|0K2TX12X58]] states.
If $v_i$ is a unit eigenvector of $A^* A$ for $\lambda_i$, then $\norm{A v_i} = \sigma_i$, so $\sigma_i$ is the length of the image of a main direction.

## Motivation

Eigenvalues describe a square matrix that maps a space to itself.
A rectangular matrix has no eigenvalues at all, and even for a square matrix the eigenvalues can hide how much the matrix stretches vectors.
The shear $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has the eigenvalue $1$ twice, but it sends the unit vector $(0, 1)$ to $(1, 1)$, which has length $\sqrt2$.
So we need numbers that measure lengths, not directions that stay fixed.

The singular values are those numbers.
A matrix sends the unit sphere to an ellipsoid, and the singular values are the lengths of the semi-axes.
They give the rank of a matrix, its operator norm, the distance of a square matrix from the nearest singular one, and the best ways to compress a matrix.
They are the diagonal of the [[singular value decomposition|000NPTMX6J]], they build the [[Moore-Penrose inverse|0YY8VX28JR]], and they measure the error of low-rank approximation in the [[Eckart-Young-Mirsky theorem|JJT6GC055J]].

## Notation

We write $\sigma_1(A) \ge \sigma_2(A) \ge \cdots$, always in decreasing order, and $\sigma_i$ when $A$ is fixed.
The largest is also written $\sigma_{\max}(A)$, and the last value in the list is $\sigma_{\min}(A)$.
Books differ on the length of the list.
Some list $n$ values from $A^* A$, some list $\min(m, n)$ values, and some list only the $r = \rank A$ nonzero values.
The nonzero values are the same in every convention, so only the number of zeros changes.

## Remarks

### A first computation

Take $A = \begin{pmatrix} 3 & 0 \\ 4 & 5 \end{pmatrix}$.
First form $A^{\mathsf{T}} A$:
$$A^{\mathsf{T}} A = \begin{pmatrix} 3 & 4 \\ 0 & 5 \end{pmatrix} \begin{pmatrix} 3 & 0 \\ 4 & 5 \end{pmatrix} = \begin{pmatrix} 25 & 20 \\ 20 & 25 \end{pmatrix}.$$
Its characteristic polynomial is $(25 - t)^2 - 400 = (t - 45)(t - 5)$, so $\lambda_1 = 45$ and $\lambda_2 = 5$.
The singular values are $\sigma_1 = \sqrt{45} = 3\sqrt5 \approx 6.71$ and $\sigma_2 = \sqrt5 \approx 2.24$.
Check with the main direction $v_1 = \tfrac{1}{\sqrt2}(1, 1)$, an eigenvector of $A^{\mathsf{T}} A$ for $45$:
$$A v_1 = \tfrac{1}{\sqrt2}(3, 9), \qquad \norm{A v_1} = \sqrt{\tfrac{9 + 81}{2}} = \sqrt{45}.$$
The eigenvalues of $A$ itself are its diagonal entries $3$ and $5$, which are different numbers.
The [[full SVD of this matrix|B546BDVFQZ]] continues the calculation.

### What the numbers measure

Let $v_1, \dots, v_n$ be an orthonormal basis of eigenvectors of $A^* A$.
Then $\norm{A v_i}^2 = v_i^* A^* A v_i = \lambda_i$, so $\norm{A v_i} = \sigma_i$, and the images $A v_i$ are pairwise orthogonal.
Three facts follow, and the [[theorem on singular values and rank|6VXM1T8PG7]] proves them.
The number of nonzero singular values is the rank of $A$.
The largest singular value is the largest stretch, $\sigma_1 = \max_{\norm x = 1} \norm{Ax}$, which is the [[operator norm|06EKW1AKXF]] for the Euclidean norms.
The sum of the squares is the square of the [[Frobenius norm|JT8Q204E4R]], $\sigma_1^2 + \dots + \sigma_n^2 = \norm{A}_F^2$.
For the matrix above, $45 + 5 = 50 = 9 + 0 + 16 + 25$.

### More examples

The [[tall matrix with rows (1, 1), (1, 0), (0, 1)|GK1B93DKD3]] has $A^{\mathsf{T}} A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ with eigenvalues $3$ and $1$, so its singular values are $\sqrt3$ and $1$.
A diagonal matrix $\operatorname{diag}(d_1, \dots, d_n)$ has the singular values $\abs{d_1}, \dots, \abs{d_n}$, sorted into decreasing order, since $A^* A = \operatorname{diag}(\abs{d_1}^2, \dots, \abs{d_n}^2)$.
A [[unitary matrix|0AR68JTMDT]] has every singular value equal to $1$, because $U^* U = I$.
A rank-one matrix $u v^*$ with $u \in \C^m$ and $v \in \C^n$ has exactly one nonzero singular value, $\norm u \, \norm v$.
The reason is $(u v^*)^* (u v^*) = v (u^* u) v^* = \norm{u}^2 \, v v^*$, whose only nonzero eigenvalue is $\norm{u}^2 \norm{v}^2$.

### What they are not

The singular values are not the absolute values of the eigenvalues in general.
The [[shear with rows (1, 1) and (0, 1)|S3ZGYKVBRR]] has the eigenvalues $1, 1$, but its singular values are $\tfrac{\sqrt5 + 1}{2} \approx 1.618$ and $\tfrac{\sqrt5 - 1}{2} \approx 0.618$.
The two lists agree up to sign only when $A$ is a [[normal matrix|0MR0BYF0K2]], and the shear is not normal.
Singular values are also never negative: $\operatorname{diag}(-2, 1)$ has the eigenvalues $-2$ and $1$ but the singular values $2$ and $1$.
Finally, the eigenvalues of $A^* A$ are not the singular values but their squares; for the first computation they are $45$ and $5$, not $3\sqrt5$ and $\sqrt5$.

### The rules you can use

Unitary factors on either side change nothing: $\sigma_i(WAV) = \sigma_i(A)$ for unitary $W$ and $V$, because $(WAV)^*(WAV) = V^* (A^* A) V$ is similar to $A^* A$.
The matrices $A$ and $A^*$ have the same nonzero singular values, since $A^* A$ and $A A^*$ have the same nonzero eigenvalues.
For a normal matrix the singular values are the absolute values of the eigenvalues, and for a positive semidefinite matrix they are the eigenvalues.
For a square matrix, $\abs{\det A} = \sigma_1 \cdots \sigma_n$, because $\abs{\det A}^2 = \det(A^* A) = \lambda_1 \cdots \lambda_n$.
So a square matrix is invertible exactly when $\sigma_n > 0$.

### Watch out

The most common mistake is to use the eigenvalues of $A$ as its singular values.
For $\begin{pmatrix} 0 & 2 \\ 0 & 0 \end{pmatrix}$ the eigenvalues are $0, 0$, yet the matrix sends $(0, 1)$ to $(2, 0)$, so it stretches by $2$.
The correct move is to form $A^* A = \operatorname{diag}(0, 4)$ and take square roots, which gives $2$ and $0$.
A second mistake is to forget the square root and report $45$ and $5$ for the first computation.

### History

Beltrami in 1873 and Jordan in 1874 found the singular value decomposition of real square matrices, and so these numbers, in the language of bilinear forms.
Erhard Schmidt studied the same numbers for integral operators in 1907, in his work on integral equations.

### Try it

First, find the singular values of the $1 \times 2$ matrix $(3 \;\; 4)$.
Here $A A^{\mathsf{T}} = (25)$, so the nonzero singular value is $5$, and the $2 \times 2$ matrix $A^{\mathsf{T}} A$ adds a second value $0$.

Second, find the singular values of $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$.
The matrix is symmetric, hence normal, with eigenvalues $3$ and $-1$, so its singular values are $3$ and $1$.

## Explanations

### L1 human

A matrix turns a circle into an ellipse.
The singular values are the half-lengths of the long axis and the short axis of that ellipse.
For $A = \begin{pmatrix} 3 & 0 \\ 4 & 5 \end{pmatrix}$ the long half-axis is about $6.71$ and the short one is about $2.24$.
To compute them, form $A^{\mathsf{T}} A$, find its eigenvalues $45$ and $5$, and take square roots.
A singular value of zero means that some direction is squashed flat.

### L2 human

Here is a typical use: find the rank and the largest stretch of $A = \begin{pmatrix} 2 & 2 \\ 1 & 1 \end{pmatrix}$.
Form the small symmetric matrix:
$$A^{\mathsf{T}} A = \begin{pmatrix} 2 & 1 \\ 2 & 1 \end{pmatrix} \begin{pmatrix} 2 & 2 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 5 & 5 \\ 5 & 5 \end{pmatrix}.$$
Its trace is $10$ and its determinant is $0$, so its eigenvalues are $10$ and $0$, and the singular values are $\sqrt{10}$ and $0$.
One singular value is nonzero, so the rank is $1$, and the largest stretch is $\sqrt{10}$.
Check: the unit vector $v_1 = \tfrac{1}{\sqrt2}(1, 1)$ goes to $\tfrac{1}{\sqrt2}(4, 2)$, whose length is $\sqrt{20/2} = \sqrt{10}$.
Also $\norm{A}_F^2 = 4 + 4 + 1 + 1 = 10 = \sigma_1^2 + \sigma_2^2$.
For a wide matrix with $m < n$ it is faster to use the $m \times m$ matrix $A A^*$, which has the same nonzero eigenvalues.
Watch out in floating point: a matrix of rank $1$ often shows a tiny nonzero $\sigma_2$, so numerical rank needs a tolerance.

### L3 human

The singular values are the complete invariants of $m \times n$ matrices under $A \mapsto W A V$ with $W$ and $V$ unitary: two matrices are equivalent in this sense exactly when their singular values agree.
Each $\sigma_k$ has a min-max description, $\sigma_k = \max_{\dim S = k} \min_{x \in S, \norm x = 1} \norm{Ax}$, which follows from the Courant-Fischer theorem for $A^* A$.
Weyl's inequality $\abs{\sigma_k(A) - \sigma_k(B)} \le \sigma_1(A - B)$ makes them stable under small changes of the entries, which is why numerical linear algebra trusts them more than eigenvalues.
For [[compact operators|QSJKPKPM7H]] on a Hilbert space the same definition works with $(T^* T)^{1/2}$, and summability conditions on the singular values define the Schatten classes of functional analysis.
