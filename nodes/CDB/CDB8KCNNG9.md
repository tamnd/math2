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

Let $F$ be a field, let $V$ be a vector space over $F$ of finite dimension $n \ge 1$, and let $T \colon V \to V$ be linear with [[characteristic polynomial|0J5EMJRRFM]] $p_T$.

1. For each [[eigenvalue|0BQAA2BK3Q]] $\lambda$ of $T$, the [[geometric multiplicity|099TWVJ909]] $\dim \ker(T - \lambda \id_V)$ satisfies $1 \le \dim \ker(T - \lambda \id_V) \le m_\lambda$, where $m_\lambda$ is the [[algebraic multiplicity|0FY42N02DV]] of $\lambda$.
2. $T$ is [[diagonalizable|07SQCNV233]] if and only if both of these conditions hold:
    - $p_T$ splits over $F$, that is, $p_T = (t - \lambda_1)^{m_1} \cdots (t - \lambda_k)^{m_k}$ with pairwise distinct $\lambda_i \in F$;
    - $\dim \ker(T - \lambda_i \id_V) = m_i$ for each $i$.

The same holds for an $n \times n$ matrix $A$ over $F$ and the map $x \mapsto A x$.

## Remarks

### Why each hypothesis is needed

- The splitting condition is needed. The rotation $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ over $\R$ has no eigenvalue, so the second condition holds for no $\lambda$ and says nothing, but $T$ is not diagonalizable over $\R$.
- The condition on each eigenvalue is needed. The [[shear|SBDF8APDF7]] $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has $p = (t - 1)^2$, which splits, but its eigenspace is a line, so $1 < 2$.
- So "$n$ eigenvalues counted with multiplicity" does not imply diagonalizable. It is only the first condition.

### Consequences

- The diagonalization algorithm: factor $p_T$, compute a basis of each eigenspace by row reduction, and compare its size with the exponent. If all sizes agree, the bases together form the columns of $P$.
- An eigenvalue with $m_\lambda = 1$ always passes the test, by part 1. So only the repeated eigenvalues must be checked.
- If $n$ distinct eigenvalues exist, then all $m_i = 1$, and $T$ is diagonalizable, as in [[distinct eigenvalues imply diagonalizable|0Y95Z7MT02]].
- Over an algebraically closed field, the first condition always holds, and $T$ is diagonalizable if and only if each geometric multiplicity equals the algebraic one.

### Converse

The statement is an equivalence, so its converse holds.
Part 1 has no converse: any pair $1 \le g \le m$ occurs, for example as the geometric and algebraic multiplicities of $0$ for a nilpotent matrix of size $m$ with $g$ Jordan blocks.

### Generalizations

The difference $m_\lambda - \dim \ker(T - \lambda \id_V)$ measures how far $T$ is from diagonalizable at $\lambda$.
In the [[Jordan normal form|085HQ5G5TE]], the geometric multiplicity is the number of Jordan blocks for $\lambda$, and the algebraic multiplicity is the sum of their sizes.
The [[generalized eigenspace|0AJ035ZTZE]] always has dimension $m_\lambda$, by the [[dimension formula|PHZ684KGWS]].

## History

The comparison of the geometric and the algebraic multiplicity is the standard textbook test, for example in Friedberg, Insel and Spence, Section 5.2.
We do not know of a first source.

## Explanations

### L1 human

Each stretch factor of a matrix appears a certain number of times as a root of a polynomial.
Each stretch factor also comes with a space of special directions.
The matrix can be made diagonal exactly when, for each factor, the number of independent special directions equals the number of times the factor appears.
For the shear, the factor $1$ appears twice but has only one special direction, so it fails.

### L2 human

Test $A = \begin{pmatrix} 5 & 4 & 2 \\ 0 & 1 & 0 \\ -2 & -2 & 0 \end{pmatrix}$.

1. Expanding along the second row, $p_A = (t - 1)\big((t - 5) t + 4\big) = (t - 1)(t^2 - 5t + 4) = (t - 1)^2 (t - 4)$.
2. So $p_A$ splits, with $m_1 = 2$ and $m_4 = 1$.
3. $A - I = \begin{pmatrix} 4 & 4 & 2 \\ 0 & 0 & 0 \\ -2 & -2 & -1 \end{pmatrix}$ has rank $1$, since the third row is $-\tfrac{1}{2}$ times the first. So $\dim \ker(A - I) = 2 = m_1$.
4. The eigenvalue $4$ is simple, so it passes by part 1.
5. Hence $A$ is diagonalizable. A basis of $\ker(A - I)$ is $(1, -1, 0)$, $(1, 0, -2)$, and $\ker(A - 4I)$ is spanned by $(2, 0, -1)$.
6. With $P$ having these three columns, $A P = P \operatorname{diag}(1, 1, 4)$: for example $A(2, 0, -1) = (8, 0, -4)$.

The trap is to stop after step 2: a split characteristic polynomial is not enough.

### L3 human

Part 1 is a special case of the block triangular form: the eigenspace is an invariant subspace on which $T$ is a scalar.
The test is a computable criterion, but numerically it is unstable, because the rank of $A - \lambda I$ jumps under small perturbations.
The [[minimal polynomial criterion|0MPAJRB23T]] is an equivalent test, which needs no eigenvectors.
