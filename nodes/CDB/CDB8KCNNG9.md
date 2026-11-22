---
tag: CDB8KCNNG9
kind: statement
role: theorem
name: Diagonalizability test by multiplicities
msc: ["15A20", "15A18"]
topics: [Z6S6PWMJPH]
audience: ug1
about: [07SQCNV233]
uses: [056SW1E0AC, 0S7A0EMPF4, 0AYEPBQMAW, 0BZ81AJNWF]
sources:
  - url: https://en.wikipedia.org/wiki/Diagonalizable_matrix
    locator: Characterization
  - book: isbn:9780134860244
    locator: Section 5.2
  - book: isbn:9780321982384
    locator: Section 5.3
---

## Statement

A map is diagonalizable exactly when its characteristic polynomial factors into linear factors and every eigenvalue has as many independent eigenvectors as its multiplicity.
Let $F$ be a field, let $V$ be a vector space over $F$ of finite dimension $n \ge 1$, and let $T \colon V \to V$ be linear with [[characteristic polynomial|0J5EMJRRFM]] $p_T$.

1. For each [[eigenvalue|0BQAA2BK3Q]] $\lambda \in F$ of $T$, the [[geometric multiplicity|099TWVJ909]] satisfies
$$1 \le \dim \ker(T - \lambda \id_V) \le m_\lambda,$$
   where $m_\lambda$ is the [[algebraic multiplicity|0FY42N02DV]] of $\lambda$.
2. $T$ is [[diagonalizable|07SQCNV233]] over $F$ if and only if both of these conditions hold:
    - $p_T$ splits over $F$, that is, $p_T = (t - \lambda_1)^{m_1} \cdots (t - \lambda_k)^{m_k}$ with pairwise distinct $\lambda_i \in F$;
    - $\dim \ker(T - \lambda_i \id_V) = m_i$ for each $i$.

The same holds for an $n \times n$ matrix $A$ over $F$ and the map $x \mapsto A x$.

## Remarks

### Why each hypothesis is needed

The splitting condition cannot be dropped.
Over $\R$, the rotation $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ has $p = t^2 + 1$ and no eigenvalue at all.
So the condition on the eigenspaces holds for every eigenvalue, because there are none, but the rotation is not diagonalizable over $\R$.

The condition on each eigenspace cannot be dropped either.
The [[shear|SBDF8APDF7]] $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has $p = (t - 1)^2$, which splits, but its eigenspace is a line, so its geometric multiplicity $1$ is less than $m_1 = 2$.
This is the trap of the subject: having $n$ eigenvalues counted with multiplicity is only the first condition, and it does not imply diagonalizable.

### The diagonalization algorithm

The test turns into a procedure.
Factor $p_T$ over $F$, and stop if it does not split.
For each eigenvalue, row reduce $A - \lambda I$ to find a basis of its kernel, and compare the number of vectors with the exponent $m_\lambda$.
If they agree for every eigenvalue, the bases together give the columns of $P$, and $D$ lists each eigenvalue $\lambda$ exactly $m_\lambda$ times.

Part 1 saves work.
An eigenvalue with $m_\lambda = 1$ has geometric multiplicity between $1$ and $1$, so it always passes, and only the repeated eigenvalues need a check.
In particular, $n$ distinct eigenvalues in $F$ make every $m_i = 1$, which gives the rule that [[n distinct eigenvalues imply diagonalizable|0Y95Z7MT02]].
Over an algebraically closed field such as $\C$, the first condition always holds, and only the eigenspaces need checking.

### The converse

Part 2 is an equivalence, so its converse holds.
Part 1 has a converse of its own: every pair $1 \le g \le m$ occurs.
A nilpotent matrix of size $m$ made of $g$ Jordan blocks has the single eigenvalue $0$ with algebraic multiplicity $m$ and geometric multiplicity $g$.

### Generalizations

The gap $m_\lambda - \dim \ker(T - \lambda \id_V)$ measures how far $T$ is from diagonalizable at $\lambda$.
In the [[Jordan normal form|085HQ5G5TE]], the geometric multiplicity is the number of Jordan blocks for $\lambda$, and the algebraic multiplicity is the sum of their sizes.
The [[generalized eigenspace|0AJ035ZTZE]] always has dimension $m_\lambda$, by the [[dimension formula|PHZ684KGWS]], so the test asks that each generalized eigenspace is an ordinary eigenspace.

## History

The comparison of the two multiplicities is the standard textbook test, for example in Section 5.2 of the textbook of Friedberg, Insel and Spence.
We know of no single first source for it.

## Explanations

### L1 human

Each stretch factor of a matrix appears a certain number of times as a root of the characteristic polynomial.
Each stretch factor also comes with its own family of special directions.
The matrix can be made diagonal exactly when, for each factor, the number of independent special directions equals the number of times the factor appears.
For the shear, the factor $1$ appears twice but has only one special direction, so the shear fails.

### L2 human

Let us test $A = \begin{pmatrix} 5 & 4 & 2 \\ 0 & 1 & 0 \\ -2 & -2 & 0 \end{pmatrix}$ over $\R$.
Expanding $\det(tI - A)$ along the second row gives
$$p_A = (t - 1)\big((t - 5) t + 4\big) = (t - 1)(t^2 - 5t + 4) = (t - 1)^2 (t - 4).$$
So $p_A$ splits, with $m_1 = 2$ and $m_4 = 1$, and only the eigenvalue $1$ needs a check.
The matrix $A - I$ has the rows $(4, 4, 2)$, $(0, 0, 0)$ and $(-2, -2, -1)$, and the third row is $-\tfrac{1}{2}$ times the first, so its rank is $1$.
Its kernel, the plane $2x + 2y + z = 0$, has dimension $2 = m_1$, with the basis $(1, -1, 0)$ and $(1, 0, -2)$.
So $A$ is diagonalizable, and the eigenvalue $4$ gives the third column $(2, 0, -1)$, since $A(2, 0, -1) = (8, 0, -4)$.
With these columns in $P$ and $D = \operatorname{diag}(1, 1, 4)$, we have $\det P = 3$, and multiplying out confirms the result:
$$P D P^{-1} = \begin{pmatrix} 1 & 1 & 8 \\ -1 & 0 & 0 \\ 0 & -2 & -4 \end{pmatrix} \cdot \frac{1}{3} \begin{pmatrix} 0 & -3 & 0 \\ -1 & -1 & -2 \\ 2 & 2 & 1 \end{pmatrix} = \frac{1}{3} \begin{pmatrix} 15 & 12 & 6 \\ 0 & 3 & 0 \\ -6 & -6 & 0 \end{pmatrix} = A.$$
Watch out: stopping after the factorization of $p_A$ is the classic mistake, since a split polynomial alone is not enough.

### L3 human

Part 1 is a special case of the block triangular form: the eigenspace is an invariant subspace on which $T$ acts as a scalar, so it contributes a factor $(t - \lambda)^g$ to $p_T$.
The test is exact in exact arithmetic, but it is unstable in floating point, because the rank of $A - \lambda I$ can jump under a tiny change of the entries.
The [[minimal polynomial criterion|0MPAJRB23T]] is an equivalent test that needs no eigenvectors at all.
