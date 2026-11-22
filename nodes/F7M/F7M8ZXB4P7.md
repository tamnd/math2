---
tag: F7M8ZXB4P7
kind: statement
role: proposition
name: Equivalent conditions for an orthogonal matrix
aliases: [orthogonal-matrix-inverse-is-transpose]
msc: ["15B10"]
topics: [AZS5BPF5H3]
audience: ug1
about: [0W02QESPJQ]
uses: [0QRBVFJ50X, 0TWTS88TWN, 0W809K6AW0, 0FWJ0VW561]
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section6-3.xml#L1851
    locator: src/section6-3.xml:1851
  - url: https://en.wikipedia.org/wiki/Orthogonal_matrix
    locator: Matrix properties
  - book: isbn:9780134860244
    locator: Section 6.5
---

## Statement

Seven tests for a square matrix, on columns, rows, inverses, dot products and lengths, all say the same thing.
Let $Q$ be a real $n \times n$ matrix, and give $\R^n$ the dot product $x \cdot y = x^Ty$ and the norm $\norm{x} = \sqrt{x \cdot x}$.
Then the following conditions are equivalent.

1. $Q^TQ = I_n$, that is, $Q$ is an [[orthogonal matrix|0QRBVFJ50X]].
2. $QQ^T = I_n$.
3. $Q$ is [[invertible|0TWTS88TWN]] and $Q^{-1} = Q^T$.
4. The columns of $Q$ form an [[orthonormal basis|0FWJ0VW561]] of $\R^n$.
5. The rows of $Q$ form an orthonormal basis of $\R^n$.
6. $Qx \cdot Qy = x \cdot y$ for all $x, y \in \R^n$.
7. $\norm{Qx} = \norm{x}$ for all $x \in \R^n$.

## Remarks

### Why each hypothesis is needed

The matrix must be square for conditions 2, 3 and 5.
The $3 \times 2$ matrix $A$ with columns $(1, 0, 0)$ and $(0, 1, 0)$ has $A^TA = I_2$, but $AA^T = \operatorname{diag}(1, 1, 0)$, and its rows are not orthonormal.

Condition 4 asks for two things at once, and neither half is enough alone.
The [[matrix $\begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}$|B5SD0BTPZG]] has orthogonal columns of length $\sqrt{2}$, and $Q^TQ = 2I$.
The columns $(1, 0)$ and $\frac{1}{\sqrt{2}}(1, 1)$ are unit vectors, but their dot product is $\frac{1}{\sqrt{2}} \ne 0$.

### What it gives you

The inverse of an orthogonal matrix costs nothing to compute: it is the transpose.
If $Q$ is orthogonal, then $Q^T$ is orthogonal, since conditions 1 and 2 swap when $Q$ is replaced by $Q^T$.
The coordinates of $x$ in the orthonormal basis $q_1, \dots, q_n$ of the columns are the dot products $q_j \cdot x$, because $Q^{-1}x = Q^Tx$.
By condition 7, the map $x \mapsto Qx$ is a [[linear isometry|07SJXTWVQW]] of $\R^n$ exactly when $Q$ is orthogonal.

For example, $Q = \frac{1}{5}\begin{pmatrix} 3 & -4 \\ 4 & 3 \end{pmatrix}$ has columns of squared length $\frac{9 + 16}{25} = 1$ and dot product $\frac{-12 + 12}{25} = 0$.
So $Q^{-1} = \frac{1}{5}\begin{pmatrix} 3 & 4 \\ -4 & 3 \end{pmatrix}$, and the rows $\frac{1}{5}(3, -4)$ and $\frac{1}{5}(4, 3)$ are orthonormal too.

### Generalizations

For complex matrices the same list holds with the conjugate transpose $Q^*$ in place of $Q^T$ and the standard inner product of $\C^n$, which gives the [[conditions for a unitary matrix|GZ7NG7J3J8]].
For a linear map between finite-dimensional inner product spaces, the [[equivalent conditions for a linear isometry|95ST99SEW7]] give the same list without coordinates.

## Explanations

### L1 human

For a square table of numbers, several tests say the same thing.
The columns are perpendicular arrows of length $1$, and so are the rows.
To undo the matrix, you flip it over its diagonal.
And the matrix keeps the length of every arrow.
If one test passes, all of them pass.

### L2 human

Here is a full check of $Q = \frac{1}{3}\begin{pmatrix} 2 & -1 & 2 \\ 2 & 2 & -1 \\ -1 & 2 & 2 \end{pmatrix}$ by condition 4.
The columns are $\frac{1}{3}(2, 2, -1)$, $\frac{1}{3}(-1, 2, 2)$ and $\frac{1}{3}(2, -1, 2)$, and each has squared length $\frac{4 + 4 + 1}{9} = 1$.
The three dot products of pairs of columns are
$$\tfrac{-2 + 4 - 2}{9} = 0, \qquad \tfrac{4 - 2 - 2}{9} = 0, \qquad \tfrac{-2 - 2 + 4}{9} = 0.$$
So condition 4 holds, and condition 3 gives $Q^{-1} = Q^T$ at once.
Check with condition 5: the rows $\frac{1}{3}(2, -1, 2)$, $\frac{1}{3}(2, 2, -1)$ and $\frac{1}{3}(-1, 2, 2)$ are the columns in another order, so they are orthonormal too.
To solve $Qx = b$ you now compute $x = Q^Tb$.
Watch out: for a matrix that is not square, orthonormal columns do not give orthonormal rows.

### L3 human

Condition 6 says that $Q$ keeps the bilinear form $x^Ty$, and condition 1 is the same statement written with the matrix $I_n$ of this form.
For a symmetric bilinear form with an invertible matrix $B$, the analogous condition $Q^TBQ = B$ defines the orthogonal group of the form.
The step from condition 1 to condition 2 uses that a one-sided inverse of a square matrix is a two-sided inverse.
That step fails for operators on infinite-dimensional spaces, where an isometry need not be onto.
