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

Let $F$ be a field, let $V$ be a vector space over $F$ of finite dimension $n \ge 1$, and let $T \colon V \to V$ be linear.
Let $\lambda \in F$, and let $m_\lambda$ be the [[algebraic multiplicity|0FY42N02DV]] of $\lambda$, which is $0$ if $\lambda$ is not a root of $p_T$.
Let $V_\lambda$ be the [[generalized eigenspace|0AJ035ZTZE]] of $T$ for $\lambda$.

1. $V_\lambda = \ker (T - \lambda \id_V)^n$. More precisely, the chain $\ker (T - \lambda \id_V)^j$ is constant from some index $k \le m_\lambda$ on, and $V_\lambda = \ker (T - \lambda \id_V)^k$.
2. $\dim V_\lambda = m_\lambda$.
3. $V_\lambda$ is $T$-[[invariant|0ACX5QT8TE]], and the [[characteristic polynomial|0J5EMJRRFM]] of $T|_{V_\lambda}$ is $(t - \lambda)^{m_\lambda}$.
4. $V = V_\lambda \oplus \operatorname{im} (T - \lambda \id_V)^n$, and $T - \lambda \id_V$ is invertible on the second summand.
5. $V_\lambda \ne 0$ exactly when $\lambda$ is an eigenvalue of $T$.

## Remarks

### Why each hypothesis is needed

- Finite dimension is needed. For the derivative $D$ on $\R[x]$, the generalized eigenspace for $0$ is all of $\R[x]$, and no power of $D$ kills it.
- The exponent $n$ in part 1 cannot be replaced by $1$. For the [[shear|SBDF8APDF7]], $\ker(S - I)$ is a line, while $V_1 = \ker(S - I)^2 = F^2$.
- Part 2 compares $\dim V_\lambda$ with the algebraic multiplicity, not the geometric one. For the shear, the geometric multiplicity is $1$ and $\dim V_1 = 2$.

### Consequences

- The geometric multiplicity is at most the algebraic multiplicity, since the eigenspace lies in $V_\lambda$.
- Every generalized eigenvector for $\lambda$ has rank at most $m_\lambda$.
- If $p_T$ splits, then $\sum_\lambda \dim V_\lambda = n$. With the independence of the $V_\lambda$, this gives the [[decomposition into generalized eigenspaces|0Z3GDY89T5]].
- $T$ is [[diagonalizable|07SQCNV233]] exactly when $p_T$ splits and $V_\lambda$ equals the eigenspace for each eigenvalue $\lambda$.

### Converse

Part 2 has no direct converse: two maps with the same dimensions of generalized eigenspaces need not be similar.
The shear and the identity on $F^2$ both have $\dim V_1 = 2$.

### Generalizations

Over a field where $p_T$ does not split, the role of $t - \lambda$ is taken by an irreducible factor $p$ of $p_T$.
Then $\dim \ker p(T)^n$ is $\deg p$ times the multiplicity of $p$ in $p_T$.
For modules over a principal ideal domain, the primary part for a prime $p$ is the analogue of $V_\lambda$.

## History

The statement is part of the standard route to the [[Jordan normal form|085HQ5G5TE]], as in Axler, Chapter 8, and Friedberg, Insel and Spence, Section 7.1.

## Explanations

### L1 human

The generalized eigenspace for $\lambda$ collects all vectors that $T - \lambda$ eventually sends to zero.
Its size is exactly the number of times $\lambda$ appears as a root of the characteristic polynomial.
So the generalized eigenspaces always have the right size, even when the ordinary eigenspaces are too small.

### L2 human

Let $A = \begin{pmatrix} 3 & 1 \\ -1 & 1 \end{pmatrix}$.

1. The trace is $4$ and the determinant is $3 + 1 = 4$. So $p_A = t^2 - 4t + 4 = (t - 2)^2$, and $m_2 = 2$.
2. $A - 2I = \begin{pmatrix} 1 & 1 \\ -1 & -1 \end{pmatrix}$, with kernel spanned by $(1, -1)$. So the eigenspace is a line.
3. $(A - 2I)^2 = \begin{pmatrix} 1 - 1 & 1 - 1 \\ -1 + 1 & -1 + 1 \end{pmatrix} = 0$. So $V_2 = \R^2$.
4. $\dim V_2 = 2 = m_2$, as part 2 says, and the chain stops at $k = 2 \le m_2$.

The typical use is to find the size of each Jordan part before computing a Jordan basis.
The trap is to stop at the eigenspace: its dimension $1$ is smaller than $m_2 = 2$.

### L3 human

In module language, $V_\lambda$ is the $(t - \lambda)$-primary part of the $F[t]$-module $V$.
Its length as a module over the local ring $F[t]_{(t - \lambda)}$ is the multiplicity of $\lambda$ in $p_T$.
For a representation of a nilpotent Lie algebra, the analogous pieces are the generalized weight spaces.
