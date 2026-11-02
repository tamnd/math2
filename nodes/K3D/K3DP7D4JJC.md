---
tag: K3DP7D4JJC
kind: statement
role: theorem
name: Jacobi eigenvalue algorithm
msc: [65F15]
uses: [0VR671PHE5, 0W02QESPJQ, 0E89HQATM8, 044JNC7ZAA, JT8Q204E4R, 0BQAA2BK3Q]
about: [HCJ2ETX89Z]
sources:
  - url: https://en.wikipedia.org/wiki/Jacobi_eigenvalue_algorithm
same_as:
  wikidata: Q1677726
  wikipedia: Jacobi eigenvalue algorithm
---

## Statement

Let $A \in \R^{n \times n}$, $n \ge 2$, be [[symmetric|0VR671PHE5]], and let $\mathrm{off}(A)^2 = \sum_{i \ne j} a_{ij}^2$.
For indices $p < q$ with $a_{pq} \ne 0$, let $J = J(p, q, \theta)$ be the rotation in the $(p, q)$ coordinate plane, where $\theta \in [-\pi/4, \pi/4]$ solves $\cot 2\theta = (a_{qq} - a_{pp})/(2 a_{pq})$.
Then $A' = J^T A J$ is symmetric, has the same [[eigenvalues|0BQAA2BK3Q]] as $A$, satisfies $a'_{pq} = 0$, and
$$\mathrm{off}(A')^2 = \mathrm{off}(A)^2 - 2 a_{pq}^2.$$
The *classical Jacobi method* chooses at each step a pair $(p, q)$ with $\abs{a_{pq}}$ maximal among the off-diagonal entries and sets $A_{k+1} = J_k^T A_k J_k$, starting from $A_0 = A$.
Then
$$\mathrm{off}(A_{k+1})^2 \le \Bigl( 1 - \frac{2}{n(n-1)} \Bigr) \mathrm{off}(A_k)^2,$$
so $A_k$ converges to a [[diagonal matrix|044JNC7ZAA]] whose diagonal entries are the eigenvalues of $A$.

## Remarks

The rotation $J$ is an [[orthogonal matrix|0W02QESPJQ]], so $A'$ is [[similar|0E89HQATM8]] to $A$ and the [[Frobenius norm|JT8Q204E4R]] $\norm{A'}_F = \norm{A}_F$ is unchanged.
On the $2 \times 2$ block in rows and columns $p, q$, the choice of $\theta$ diagonalizes the block.
So the sum of squares of that block's diagonal grows by $2 a_{pq}^2$.
The other entries in rows and columns $p, q$ are only rotated, so their total square sum does not change.
If $\abs{a_{pq}}$ is maximal among the $n(n-1)$ off-diagonal entries, then $a_{pq}^2 \ge \mathrm{off}(A)^2 / (n(n-1))$, which gives the linear bound.
The diagonal entries of $A_k$ approach the eigenvalues because each eigenvalue lies within $\mathrm{off}(A_k)$ of some diagonal entry, by Weyl's inequality.

Example: for $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, $\cot 2\theta = 0$ gives $\theta = \pi/4$, and one rotation gives $\mathrm{diag}(1, 3)$.
In practice the local convergence is quadratic once the off-diagonal part is small.
The product $J_0 J_1 \cdots J_k$ of the rotations converges to an orthogonal matrix whose columns are eigenvectors.

## Explanations

### L1 human

The Jacobi method diagonalizes a symmetric matrix by a sequence of plane rotations.
Each rotation kills one off-diagonal entry; later rotations may make it nonzero again, but the total size of the off-diagonal part always drops.
After enough rotations the matrix is nearly diagonal and the eigenvalues can be read off the diagonal.

### L2 human

The method dates from Jacobi in 1846 and was revived on early computers.
It is slower than the [[QR algorithm|B6F8YWHYZ5]] on a serial computer.
But it computes small eigenvalues of well-scaled positive definite matrices to high relative accuracy, and it is easy to parallelize.
Cyclic variants sweep through all pairs in a fixed order instead of searching for the largest entry, and they also converge.
A one-sided version applied to $A^T A$ implicitly computes the [[singular value decomposition|000NPTMX6J]].
