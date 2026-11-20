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

- The matrix must be square for conditions 2, 3 and 5. The $3 \times 2$ matrix $A$ with the columns $(1, 0, 0)$ and $(0, 1, 0)$ has $A^TA = I_2$, but $AA^T = \operatorname{diag}(1, 1, 0)$.
- In condition 4, orthogonal columns are not enough. [[The matrix $\begin{pmatrix} 1 & 1 \\ -1 & 1 \end{pmatrix}$|B5SD0BTPZG]] has orthogonal columns of length $\sqrt{2}$, and $Q^TQ = 2I$.
- In condition 4, unit columns are not enough. The columns $(1, 0)$ and $\frac{1}{\sqrt{2}}(1, 1)$ are unit vectors, but their dot product is $\frac{1}{\sqrt{2}} \neq 0$.

### Consequences

- The inverse of an orthogonal matrix costs nothing to compute: it is the transpose.
- If $Q$ is orthogonal, then $Q^T$ is orthogonal, by conditions 1 and 2.
- The coordinates of $x$ in the orthonormal basis of the columns $q_1, \dots, q_n$ are $q_j \cdot x$, because $Q^{-1}x = Q^Tx$.
- The map $x \mapsto Qx$ is a [[linear isometry|07SJXTWVQW]] of $\R^n$ exactly when $Q$ is orthogonal, by condition 7.

### Converse

The statement is a list of equivalences, so each condition implies each other condition.

### Generalizations

- For complex matrices, the same list holds with the conjugate transpose $Q^*$ in place of $Q^T$ and the standard inner product of $\C^n$. This gives the [[conditions for a unitary matrix|GZ7NG7J3J8]].
- For a linear map between finite-dimensional inner product spaces, the [[equivalent conditions for a linear isometry|95ST99SEW7]] give the same list without coordinates.

## Explanations

### L1 human

For a square table of numbers, several tests say the same thing.
The columns are perpendicular arrows of length $1$.
The rows are perpendicular arrows of length $1$.
To undo the matrix, we can flip it over its diagonal.
And the matrix keeps the length of every arrow.
If one test passes, all of them pass.

### L2 human

Worked example: $Q = \frac{1}{3}\begin{pmatrix} 2 & -1 & 2 \\ 2 & 2 & -1 \\ -1 & 2 & 2 \end{pmatrix}$.

1. The columns are $\frac{1}{3}(2, 2, -1)$, $\frac{1}{3}(-1, 2, 2)$ and $\frac{1}{3}(2, -1, 2)$. Each has squared length $\frac{4 + 4 + 1}{9} = 1$.
2. The dot products of the columns are $\frac{-2 + 4 - 2}{9}$, $\frac{4 - 2 - 2}{9}$ and $\frac{-2 - 2 + 4}{9}$, all $0$.
3. So condition 4 holds, and $Q^{-1} = Q^T$ by condition 3.
4. The rows are $\frac{1}{3}(2, -1, 2)$, $\frac{1}{3}(2, 2, -1)$ and $\frac{1}{3}(-1, 2, 2)$. They are orthonormal too, as condition 5 says.

The typical use: to solve $Qx = b$, we compute $x = Q^Tb$.
A trap: for a non-square matrix, orthonormal columns do not give orthonormal rows.

### L3 human

Condition 6 says that $Q$ keeps the bilinear form $x^Ty$, and condition 1 is the same statement for the matrix $I_n$ of this form.
For a symmetric bilinear form with an invertible matrix $B$, the analogous condition $Q^TBQ = B$ defines the orthogonal group of the form.
The proof of $1 \Leftrightarrow 2$ uses that a one-sided inverse of a square matrix is a two-sided inverse.
This fails for operators on infinite-dimensional spaces, where an isometry need not be surjective.
