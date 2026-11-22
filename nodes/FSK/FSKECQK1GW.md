---
tag: FSKECQK1GW
kind: statement
role: proposition
name: Characterizations of nilpotent endomorphisms
msc: ["15A04", "15A18"]
topics: [Z6S6PWMJPH]
audience: ug2
about: [063D5Z2C70]
uses: [0M8MHYERTY, 0MKABWDRNC, 0BZ81AJNWF, 0ZND7NQ970]
sources:
  - url: https://en.wikipedia.org/wiki/Nilpotent_matrix
    locator: Characterization
  - book: isbn:9783031410253
    locator: Chapter 8
---

## Statement

A map on an $n$-dimensional space is nilpotent exactly when its $n$th power is zero, exactly when it is strictly upper triangular in some basis, and exactly when its characteristic polynomial is $t^n$.
Let $F$ be a field, let $V$ be a vector space over $F$ of finite dimension $n \ge 1$, and let $T \colon V \to V$ be linear.
The following conditions are equivalent.

1. $T$ is [[nilpotent|063D5Z2C70]], that is, $T^k = 0$ for some $k \ge 1$.
2. $T^n = 0$.
3. There is a basis of $V$ in which the matrix of $T$ is strictly [[upper triangular|0N4XY7Z3NN]], that is, upper triangular with zero diagonal.
4. The [[characteristic polynomial|0J5EMJRRFM]] of $T$ is $t^n$.

If these hold, then $0$ is an [[eigenvalue|0BQAA2BK3Q]] of $T$, and it is the only one.
If $F$ is [[algebraically closed|0PF6TM8TWT]], then the conditions are also equivalent to the following.

5. $0$ is the only eigenvalue of $T$.

## Remarks

### Why each hypothesis is needed

Condition 5 needs the characteristic polynomial to split.
Over $\R$, the matrix
$$R = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & -1 \\ 0 & 1 & 0 \end{pmatrix}$$
has $p_R = t(t^2 + 1)$.
Its only real eigenvalue is $0$, but $R^2 = \operatorname{diag}(0, -1, -1) \ne 0$, and $R$ is not nilpotent.
The hidden eigenvalues $\pm i$ appear only over $\C$.

Finite dimension is needed for condition 2.
The derivative on $\R[x]$ sends each polynomial to $0$ after finitely many steps, but no single power of it is $0$.

### What it gives you

Condition 2 gives a bound for free: the index of a nilpotent map is at most $n$.
So the minimal polynomial of a nilpotent $T$ is $t^k$, where $k \le n$ is the index.

Condition 4 gives the trace and the determinant, which are coefficients of $p_T$, so both are $0$ for a nilpotent map.
It also gives a cheap test for $2 \times 2$ matrices: $A$ is nilpotent exactly when $\operatorname{tr} A = 0$ and $\det A = 0$, since then $p_A = t^2$.

A nonzero nilpotent $T$ is not [[diagonalizable|07SQCNV233]].
A diagonal matrix whose only eigenvalue is $0$ is the zero matrix, and a map similar to the zero matrix is zero.

### The converse

The theorem is a list of equivalences, so each condition is a converse of the others.
In particular, condition 3 is sufficient on its own: every strictly upper triangular matrix is nilpotent, by the [[triangular power argument|AW5RBMW7RK]].
The extra statement on eigenvalues has no converse without condition 5: the matrix $R$ shows that $0$ can be the only real eigenvalue of a map that is not nilpotent.

### Generalizations

The triangular form of condition 3 is the case of the single eigenvalue $0$ in [[triangularization|0363JMQ42Y]].
Over any commutative ring, a matrix $A$ is nilpotent exactly when all coefficients of its characteristic polynomial except the leading one are nilpotent.
Over a field the only nilpotent element is $0$, and this reduces to condition 4.
In Lie theory, [[Engel's theorem|V0ZWMA3FTH]] gives one common strictly upper triangular form for a whole Lie algebra of nilpotent matrices.
If $S$ and $T$ are nilpotent and $S T = T S$, then $S + T$ is nilpotent, by the [[binomial theorem for commuting matrices|DS9TS6AFMW]].

## History

Benjamin Peirce introduced the word "nilpotent" in his *Linear Associative Algebra* of 1870.

## Explanations

### L1 human

A nilpotent matrix becomes the zero matrix after you multiply it by itself enough times.
In size $n$, it never needs more than $n$ factors.
For example, a $2 \times 2$ nilpotent matrix always has a zero square.
Its only eigenvalue is $0$, and in a good basis all its entries on and below the diagonal are zero.

### L2 human

Test $A = \begin{pmatrix} 2 & -4 \\ 1 & -2 \end{pmatrix}$.
The trace is $2 - 2 = 0$ and the determinant is $-4 + 4 = 0$, so $p_A = t^2$.
By condition 4, $A$ is nilpotent, and by condition 2, $A^2 = 0$.
Check:
$$A^2 = \begin{pmatrix} 4 - 4 & -8 + 8 \\ 2 - 2 & -4 + 4 \end{pmatrix} = 0.$$

Now find the triangular basis of condition 3.
The kernel of $A$ is spanned by $(2, 1)$, since $2 \cdot 2 - 4 \cdot 1 = 0$.
Take the basis $((2, 1), (1, 0))$: then $A(2, 1) = 0$ and $A(1, 0) = (2, 1)$, so the matrix is $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$.
The typical use is to test nilpotence by the characteristic polynomial instead of computing many powers.
Watch out: $A$ has no zero entries, so the entries alone tell you nothing.

### L3 human

The nilpotent matrices of size $n$ form a closed set, the nilpotent cone, cut out by the vanishing of the non-leading coefficients of the characteristic polynomial.
Up to similarity, they are classified by the partitions of $n$, through the sizes of their Jordan blocks.
The proof of the [[dimension of the generalized eigenspace|PHZ684KGWS]] uses condition 4 on the nilpotent part of $T - \lambda$.
