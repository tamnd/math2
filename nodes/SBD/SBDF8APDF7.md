---
tag: SBDF8APDF7
kind: example
name: The shear matrix is not diagonalizable
msc: ["15A20", "15A21"]
topics: [Z6S6PWMJPH]
audience: ug1
instance_of: [0DTCBCKEJP]
not_instance_of:
  - target: 07SQCNV233
    note: the only eigenvalue is 1 and its eigenspace is a line, so there is no basis of eigenvectors over any field
  - target: D0AP2R7272
    note: there are not two independent eigenvectors to form the columns of Q
  - target: 0TNR9BQ871
    note: the powers cannot be computed as P D^k P^(-1), since the matrix is not diagonalizable
  - target: 08VRX3Q4PB
    note: the invariant line spanned by e1 has no invariant complement
  - target: 063D5Z2C70
    note: the matrix is invertible, so none of its powers is 0
uses: [0Y17PEKF24, 0QS8P74F2Z, 0M8MHYERTY, 0AYEPBQMAW, 039HF58KQ5]
sources:
  - url: https://en.wikipedia.org/wiki/Diagonalizable_matrix
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Defective_matrix
    locator: Jordan block
---

## Example

Let $F$ be any field and let $S = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ over $F$.
This is the shear, a [[transvection|0DTCBCKEJP]] of the plane.
We write $S = I + N$ with $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, and we check its properties one at a time.

1. The [[characteristic polynomial|0VSSPAFM2C]] is $\det(tI - S) = (t - 1)^2$, because $tI - S$ is triangular with both diagonal entries $t - 1$.
   So the only eigenvalue is $1$.
2. The [[eigenspace|0G0RFPG8HR]] is $\ker(S - I) = \ker N$.
   Since $N(x, y) = (y, 0)$, this kernel is the line $F e_1$ of vectors $(x, 0)$.
   So two eigenvectors are always multiples of each other, and $F^2$ has no basis of eigenvectors.
3. Hence $S$ is not [[diagonalizable|07SQCNV233]] over $F$.
   A direct check: a diagonal form would have the eigenvalue $1$ twice, so it would be $I$, and then $S = P I P^{-1} = I$, which is false.
4. The line $F e_1$ is [[invariant|0ACX5QT8TE]], since $S e_1 = e_1$.
   Every invariant line is spanned by an eigenvector, so by step 2 it is the only invariant line.
   So $F e_1$ has no invariant complement, and $S$ is not [[semisimple|08VRX3Q4PB]].
5. The shear is not [[nilpotent|063D5Z2C70]]: $\det S = 1$, so $\det S^k = 1$ and $S^k \ne 0$ for every $k$.
6. The powers have a simple form.
   Since $N^2 = 0$ and $N$ commutes with $I$, the binomial theorem gives
$$S^k = (I + N)^k = I + k N = \begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix} \quad \text{for every } k \ge 0.$$

## Remarks

The shear is the standard example of the trap in diagonalization.
It has two eigenvalues counted with multiplicity, as many as its size, and it is still not diagonalizable.
The powers in step 6 also show the failure: their corner entry grows like $k$, while every power of a diagonalizable matrix whose only eigenvalue is $1$ equals $I$.

The conclusion does not depend on the field.
Over a field of characteristic $p > 0$, step 6 gives $S^p = I + pN = I$, so $S$ has finite order $p$, and it is still not diagonalizable.
Over $\C$, by contrast, every matrix of finite order is diagonalizable, so the shear has infinite order there.

Changing the numbers shows where the line between the cases runs.
For $\begin{pmatrix} 1 & a \\ 0 & 1 \end{pmatrix}$ with $a \ne 0$ the same argument works, and for $a = 0$ the matrix is $I$, which is diagonal.
For $\begin{pmatrix} 1 & 1 \\ 0 & d \end{pmatrix}$ with $d \ne 1$, the eigenvalues $1$ and $d$ are distinct, and the matrix is diagonalizable.
The eigenspace of $1$ is a line, but the [[generalized eigenspace|0AJ035ZTZE]] of $1$ is all of $F^2$, since $(S - I)^2 = N^2 = 0$.

## Explanations

### L1 human

The shear slides each horizontal line sideways, by an amount equal to its height.
Only the horizontal arrows keep their direction.
So there is only one special direction, and a diagonal form would need two.
Each time we apply the shear again, the sideways slide grows by one more step.

### L2 human

Let us check the formula for $S^k$ by induction, without the binomial theorem.
For $k = 0$, we have $S^0 = I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$.
If $S^k = \begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}$, then
$$S^{k+1} = S^k S = \begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 1 + k \\ 0 & 1 \end{pmatrix},$$
so the formula holds for every $k \ge 0$.
Watch out: you cannot "diagonalize" $S$ with the single eigenvector $e_1$, because a $2 \times 2$ matrix $P$ whose columns are both multiples of $e_1$ is not invertible.
