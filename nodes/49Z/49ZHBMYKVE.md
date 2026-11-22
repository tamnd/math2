---
tag: 49ZHBMYKVE
kind: statement
role: theorem
name: Primary decomposition theorem
msc: ["15A21", "15A04"]
topics: [Z6S6PWMJPH]
audience: ug2
about: [0ACX5QT8TE, 03NDVCSHSB]
uses: [ACBNK1VFVG, 0V58FPM3EQ, 00X2A9G9W3, 041JTZCK9Q]
sources:
  - book: isbn:9780135367971
    locator: Section 6.8
  - url: https://en.wikipedia.org/wiki/Jordan%E2%80%93Chevalley_decomposition
    locator: Decomposition of a linear operator
---

## Statement

Factor the minimal polynomial of a linear map into powers of distinct irreducible polynomials, and the space splits into one invariant piece for each power, cut out by that power.
Let $F$ be a field, let $V$ be a vector space over $F$ of finite dimension $n \ge 1$, and let $T \colon V \to V$ be linear.
Write its [[minimal polynomial|03NDVCSHSB]] as
$$m_T = p_1^{e_1} \cdots p_k^{e_k},$$
where $p_1, \dots, p_k$ are pairwise distinct monic [[irreducible polynomials|03FKX7Z5DC]] over $F$ and each $e_i \ge 1$.
Let $W_i = \ker p_i(T)^{e_i}$.

1. $V = W_1 \oplus \dots \oplus W_k$, a [[direct sum|0XYYT5KNTX]].
2. Each $W_i$ is a nonzero $T$-[[invariant subspace|0ACX5QT8TE]].
3. The minimal polynomial of the [[restriction|0KN7EPH7Z0]] $T|_{W_i}$ is $p_i^{e_i}$.
4. The projection of $V$ onto $W_i$ along the other summands is a polynomial in $T$.

## Remarks

### A first example

Let $C = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 3 \end{pmatrix}$ over $\R$, with $m_C = (t - 1)^2 (t - 3)$.
The two pieces come from the powers of $t - 1$ and of $t - 3$:
$$(C - I)^2 = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 4 \end{pmatrix}, \qquad C - 3I = \begin{pmatrix} -2 & 1 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & 0 \end{pmatrix}.$$
So $W_1 = \ker (C - I)^2 = \operatorname{span}(e_1, e_2)$ and $W_2 = \ker (C - 3I) = \operatorname{span}(e_3)$.
The Bézout identity for the two factors is
$$\tfrac{1}{4}(t - 1)^2 - \tfrac{1}{4}(t + 1)(t - 3) = \tfrac{1}{4}\big((t^2 - 2t + 1) - (t^2 - 2t - 3)\big) = 1.$$
The projection onto $W_2$ is $\tfrac{1}{4}(C - I)^2 = \operatorname{diag}(0, 0, 1)$, and the projection onto $W_1$ is $I$ minus it, which is $\operatorname{diag}(1, 1, 0)$.
On $W_1$ the map acts as the [[shear|SBDF8APDF7]] $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, with minimal polynomial $(t - 1)^2$, and on $W_2$ it acts as $3$.

### Watch out: use the full exponents

In the first example, $\ker (C - I)$ is only the line $F e_1$, since $(C - I)(x, y, z) = (y, 0, 2 z)$.
So $\ker (C - I) \oplus \ker (C - 3I)$ is a plane, not all of $\R^3$.
The exponent $e_1 = 2$ is what makes the pieces fill the space.
The factors must also be grouped by distinct irreducible polynomials.
If the same factor is split as $p \cdot p$, the two kernels $\ker p(T)$ coincide, and their sum is not direct.

### Finite dimension

Finite dimension ensures that the minimal polynomial exists.
The derivative $D$ on $\R[x]$ satisfies no nonzero polynomial equation.
If $f = c_0 + c_1 t + \dots + c_m t^m \ne 0$ and $j$ is the least index with $c_j \ne 0$, then $f(D) x^m$ has the nonzero term $c_j \frac{m!}{(m - j)!} x^{m - j}$ of top degree, so $f(D) \ne 0$.
The [[kernels lemma|ACBNK1VFVG]] still applies to each polynomial $f$, and splits $\ker f(T)$ in any dimension.

### What it gives you

In a basis adapted to the decomposition, the matrix of $T$ is [[block diagonal|001T5FJDC1]], with one block for each $p_i$.
If $m_T$ splits, with $p_i = t - \lambda_i$, the $W_i$ are the [[generalized eigenspaces|0AJ035ZTZE]], and this is the [[decomposition into generalized eigenspaces|0Z3GDY89T5]].
If all $p_i$ are linear and all $e_i = 1$, the $W_i$ are eigenspaces, and $T$ is diagonalizable, as in the [[minimal polynomial criterion|0MPAJRB23T]].
Every map that commutes with $T$ preserves each $W_i$, since it commutes with the projections, which are polynomials in $T$.

### The converse

Part 1 has a partial converse.
Suppose $V = U_1 \oplus \dots \oplus U_k$ with $T$-invariant $U_i$, and the minimal polynomials $m_i$ of the restrictions $T|_{U_i}$ are pairwise coprime.
Then $m_T = m_1 \cdots m_k$, and $U_i = \ker m_i(T)$ for each $i$.
Indeed $U_i \subseteq \ker m_i(T)$, the kernels lemma makes the $\ker m_i(T)$ a direct sum inside $V$, and comparing dimensions forces equality.

### Generalizations

Here $V$ is a torsion module over $F[t]$, with $t$ acting as $T$.
For every finitely generated torsion module over a principal ideal domain, the same argument splits the module into its primary parts, which is the first step of the [[structure theorem|TXMV0YDACG]].
Each $W_i$ splits further into cyclic pieces, which gives the [[rational canonical form|042JWAR3Q0]] and, when $p_i$ is linear, the [[Jordan normal form|085HQ5G5TE]].

### Try it

Let $A = \begin{pmatrix} 0 & 2 \\ 1 & 0 \end{pmatrix}$, so $m_A = t^2 - 2$.
Over $\Q$ the polynomial $t^2 - 2$ is irreducible, so $k = 1$ and the only piece is $W_1 = \Q^2$.
Over $\R$ it factors as $(t - \sqrt{2})(t + \sqrt{2})$, and you should find the two lines spanned by
$$(\sqrt{2}, 1) \text{ for } \sqrt{2}, \qquad (-\sqrt{2}, 1) \text{ for } -\sqrt{2}.$$
The decomposition depends on the field.

## History

Hoffman and Kunze use the name "primary decomposition theorem" for this result, in Section 6.8.

## Explanations

### L1 human

The minimal polynomial of a matrix breaks into prime pieces, as a whole number breaks into prime factors.
Each prime piece cuts out its own part of the space.
The whole space is the sum of these parts, and the matrix acts on each part separately.
For example, a matrix that rotates a plane and doubles a third direction splits space into that plane and that line.

### L2 human

Let $B = \begin{pmatrix} 0 & -1 & 1 \\ 1 & 0 & 1 \\ 0 & 0 & 2 \end{pmatrix}$ over $\R$.
Expanding along the third row gives $p_B = (t - 2)(t^2 + 1)$, whose factors are distinct and irreducible over $\R$, so $m_B = p_B$.
Squaring,
$$B^2 = \begin{pmatrix} -1 & 0 & 1 \\ 0 & -1 & 3 \\ 0 & 0 & 4 \end{pmatrix}, \qquad B^2 + I = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 3 \\ 0 & 0 & 5 \end{pmatrix}.$$
So $W_1 = \ker(B^2 + I) = \operatorname{span}(e_1, e_2)$, and $W_2 = \ker(B - 2I)$ is spanned by $(1, 3, 5)$, since $B(1, 3, 5) = (2, 6, 10)$.
Division gives $t^2 + 1 = (t - 2)(t + 2) + 5$, so
$$1 = \tfrac{1}{5}(t^2 + 1) - \tfrac{1}{5}(t + 2)(t - 2).$$
The projection onto $W_2$ is $\tfrac{1}{5}(B^2 + I)$, and the projection onto $W_1$ is
$$I - \tfrac{1}{5}(B^2 + I) = \begin{pmatrix} 1 & 0 & -\tfrac{1}{5} \\ 0 & 1 & -\tfrac{3}{5} \\ 0 & 0 & 0 \end{pmatrix}.$$
On $W_1$, $B$ acts as the rotation $e_1 \mapsto e_2$, $e_2 \mapsto -e_1$, with minimal polynomial $t^2 + 1$, and on $W_2$ it acts as $2$.
The typical use is to reduce a question about $T$ to the pieces $T|_{W_i}$, each with a single prime factor.
The trap is to look for eigenvectors in $W_1$: over $\R$, the piece for $t^2 + 1$ has none.

### L3 human

Every $S$ with $S T = T S$ preserves each $W_i$, so the decomposition is respected by the whole centralizer of $T$.
The projections are the images in $F[t]/(m_T)$ of the Chinese remainder idempotents of $F[t]/(p_1^{e_1}) \times \dots \times F[t]/(p_k^{e_k})$.
When $T$ is semisimple, all $e_i = 1$, and each $W_i$ is a vector space over the field $F[t]/(p_i)$.
