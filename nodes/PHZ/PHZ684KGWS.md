---
tag: PHZ684KGWS
kind: statement
role: theorem
name: Dimension of the generalized eigenspace
msc: ["15A18", "15A21"]
topics: [Z6S6PWMJPH]
audience: ug2
about: [0AJ035ZTZE, 0FY42N02DV]
uses: [07PNDWA7CE, 0S7A0EMPF4, 0BZ81AJNWF, 0EP59ESQ94]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_eigenvector
    locator: Generalized eigenspaces
  - book: isbn:9783031410253
    locator: Chapter 8
  - book: isbn:9780134860244
    locator: Section 7.1
---

## Statement

The generalized eigenspace of $\lambda$ has exactly the dimension of the algebraic multiplicity of $\lambda$, and the $n$th power of $T - \lambda$ already reaches it.
Let $F$ be a field, let $V$ be a vector space over $F$ of finite dimension $n \ge 1$, and let $T \colon V \to V$ be linear.
Let $\lambda \in F$, and let $m_\lambda$ be the [[algebraic multiplicity|0FY42N02DV]] of $\lambda$, which is $0$ when $\lambda$ is not a root of $p_T$.
Let $V_\lambda$ be the [[generalized eigenspace|0AJ035ZTZE]] of $T$ for $\lambda$.
Then the following hold.

1. The kernels $\ker (T - \lambda \id_V)^j$ are constant from some index $k \le m_\lambda$ on, and $V_\lambda = \ker (T - \lambda \id_V)^k = \ker (T - \lambda \id_V)^n$.
2. The dimension is $\dim V_\lambda = m_\lambda$.
3. The space $V_\lambda$ is $T$-[[invariant|0ACX5QT8TE]], and the [[characteristic polynomial|0J5EMJRRFM]] of the restriction $T|_{V_\lambda}$ is $(t - \lambda)^{m_\lambda}$.
4. We have $V = V_\lambda \oplus \operatorname{im} (T - \lambda \id_V)^n$, and $T - \lambda \id_V$ is invertible on the second summand.
5. We have $V_\lambda \ne 0$ exactly when $\lambda$ is an eigenvalue of $T$.

## Remarks

### Why each hypothesis is needed

Finite dimension is needed for part 1.
For the derivative $D$ on $\R[x]$, the generalized eigenspace for $0$ is all of $\R[x]$, because each polynomial dies after finitely many derivatives.
But no single power of $D$ is zero, since $D^j x^j = j! \ne 0$.

The exponent cannot be lowered to $1$.
For the [[shear|SBDF8APDF7]] $S$, the kernel $\ker(S - I)$ is a line, while $V_1 = \ker(S - I)^2 = F^2$.
Part 2 also compares with the algebraic multiplicity and not the geometric one, and the shear shows the difference: its geometric multiplicity is $1$ and $\dim V_1 = 2$.

### What it gives you

The eigenspace lies in $V_\lambda$, so the geometric multiplicity is at most the algebraic multiplicity.
A Jordan chain in $V_\lambda$ is linearly independent, so every generalized eigenvector for $\lambda$ has rank at most $m_\lambda$.

When $p_T$ splits, the multiplicities add up to $n$, so $\sum_\lambda \dim V_\lambda = n$.
Together with the independence of the $V_\lambda$, this gives the [[decomposition into generalized eigenspaces|0Z3GDY89T5]].
It also gives a test: $T$ is [[diagonalizable|07SQCNV233]] exactly when $p_T$ splits and $V_\lambda$ equals the eigenspace for each eigenvalue $\lambda$.

### The converse

The numbers $\dim V_\lambda$ do not determine $T$ up to similarity.
The shear and the identity on $F^2$ both have $\dim V_1 = 2$, but the identity is diagonalizable and the shear is not.
The finer data are the dimensions of all the kernels $\ker (T - \lambda)^j$, which the sub-area on canonical forms uses.

### Generalizations

When $p_T$ does not split, the factor $t - \lambda$ is replaced by an irreducible factor $p$ of $p_T$.
Then $\dim \ker p(T)^n$ equals $\deg p$ times the multiplicity of $p$ in $p_T$, which is part of the [[primary decomposition theorem|49ZHBMYKVE]].
For a finitely generated torsion module over a principal ideal domain, the primary part for a prime $p$ plays the role of $V_\lambda$.

## History

The result is a standard step on the way to the [[Jordan normal form|085HQ5G5TE]], which Camille Jordan published in 1870.

## Explanations

### L1 human

The generalized eigenspace for $\lambda$ collects all vectors that $T - \lambda$ eventually sends to zero.
Its size is exactly the number of times $\lambda$ appears as a root of the characteristic polynomial.
For a $2 \times 2$ matrix with the double root $2$, the generalized eigenspace for $2$ is the whole plane, even when only one line is stretched by $2$.

### L2 human

Let $A = \begin{pmatrix} 3 & 1 \\ -1 & 1 \end{pmatrix}$ over $\R$.
The trace is $4$ and the determinant is $3 + 1 = 4$, so $p_A = t^2 - 4t + 4 = (t - 2)^2$ and $m_2 = 2$.
Subtract $2I$ and square:
$$A - 2I = \begin{pmatrix} 1 & 1 \\ -1 & -1 \end{pmatrix}, \qquad (A - 2I)^2 = \begin{pmatrix} 1 - 1 & 1 - 1 \\ -1 + 1 & -1 + 1 \end{pmatrix} = 0.$$
The eigenspace is the line spanned by $(1, -1)$, and $V_2 = \R^2$.
Check: $\dim V_2 = 2 = m_2$, as part 2 says, and the kernels stop growing at $k = 2 \le m_2$.

The typical use is to know the size of each piece before you look for a Jordan basis.
Watch out: the eigenspace has dimension $1$, which is smaller than $m_2 = 2$, so it is not the piece you need.

### L3 human

In module language, $V_\lambda$ is the $(t - \lambda)$-primary part of the $F[t]$-module $V$.
Its length as a module over the local ring $F[t]_{(t - \lambda)}$ is the multiplicity of $\lambda$ in $p_T$.
For a representation of a nilpotent Lie algebra over $\C$, the analogous pieces are the generalized weight spaces.
