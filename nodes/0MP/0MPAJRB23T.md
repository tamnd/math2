---
tag: 0MPAJRB23T
kind: statement
role: theorem
name: Diagonalizable iff the minimal polynomial splits with simple roots
msc: ["15A20", "15A18"]
topics: [Z6S6PWMJPH]
audience: ug2
about: [07SQCNV233, 03NDVCSHSB]
uses: [0Y17PEKF24, 0V58FPM3EQ, 0BNEXSKNRV, 0AYEPBQMAW]
sources:
  - url: https://en.wikipedia.org/wiki/Diagonalizable_matrix
    locator: Characterization
  - book: isbn:9780135367971
    locator: Section 6.4
  - book: isbn:9783031410253
    locator: Chapter 8
---

## Statement

A map is diagonalizable exactly when some product of distinct linear factors kills it, and then its minimal polynomial is such a product.
Let $F$ be a field, let $V$ be a vector space over $F$ of finite dimension $n \ge 1$, and let $T \colon V \to V$ be linear with [[minimal polynomial|03NDVCSHSB]] $m_T$.

1. The following conditions are equivalent.
    1. $T$ is [[diagonalizable|07SQCNV233]] over $F$.
    2. $f(T) = 0$ for some polynomial $f = (t - a_1) \cdots (t - a_r)$ with pairwise distinct $a_j \in F$.
    3. $m_T = (t - \lambda_1) \cdots (t - \lambda_k)$ with pairwise distinct $\lambda_i \in F$, that is, $m_T$ splits over $F$ and has simple roots.
2. If these conditions hold, then $\lambda_1, \dots, \lambda_k$ are exactly the distinct [[eigenvalues|0BQAA2BK3Q]] of $T$.
3. If $T$ is diagonalizable and $U \subseteq V$ is a $T$-[[invariant subspace|0ACX5QT8TE]], then $U = \bigoplus_i \big(U \cap E_{\lambda_i}\big)$, and the [[restriction|0KN7EPH7Z0]] $T|_U$ is diagonalizable.

For an $n \times n$ matrix $A$ over $F$, the same holds with $m_A$ and the map $x \mapsto A x$.

## Remarks

### Why each hypothesis is needed

The roots must be simple.
The [[shear|SBDF8APDF7]] $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has $m = (t - 1)^2$, with a double root, and it is not diagonalizable.

The roots must lie in $F$.
Over $\R$, the rotation $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ has $m = t^2 + 1$.
This polynomial has the simple roots $\pm i$ in $\C$, but it does not split over $\R$, and the rotation is not diagonalizable over $\R$.

The condition concerns the minimal polynomial, not the [[characteristic polynomial|0J5EMJRRFM]].
The identity $I_2$ has $p = (t - 1)^2$ with a double root, but $m = t - 1$, and $I_2$ is diagonal.

### What it gives you

The criterion needs no eigenvectors: one polynomial identity settles the question.
Every [[projection|033DA1WE8Y]] $P$ with $P^2 = P$ is diagonalizable, because $t^2 - t = t(t - 1)$ kills it, and its eigenvalues lie in $\{0, 1\}$.
If $1 + 1 \ne 0$ in $F$, every involution, a matrix with $A^2 = I$, is diagonalizable, because $t^2 - 1 = (t - 1)(t + 1)$ and $1 \ne -1$.
Over $\C$, every matrix with $A^m = I$ for some $m \ge 1$ is diagonalizable, because $t^m - 1$ has the $m$ distinct [[roots of unity|057BH3JC9S]] as its roots.

Part 3 says that a diagonalizable map stays diagonalizable on every invariant subspace.
This is the step that makes [[simultaneous diagonalization|0FK17N4DKA]] work, since the eigenspaces of one map are invariant under every map that commutes with it.

### Watch out

The field enters through the factorization, so the same matrix can pass over one field and fail over another.
Over $\mathbb{F}_2$ the shear satisfies $A^2 = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} = I$, but there $t^2 - 1 = (t - 1)^2$, so it is not diagonalizable.
In the same way, over $\mathbb{F}_p$ the shear has order $p$, and over $\R$ the rotation by a right angle has order $4$ with no real eigenvalue.
So "finite order implies diagonalizable" holds over $\C$ and fails over $\R$ and over every $\mathbb{F}_p$.

### The converse

The three conditions of part 1 are equivalent, so each converse there holds.
The converse of part 3 is false.
For the shear and $U = F e_1$, the restriction $T|_U$ is the identity of $U$ and the map induced on $F^2 / U$ is the identity too, but the shear itself is not diagonalizable.

### Generalizations

Without the splitting condition, a minimal polynomial with no repeated irreducible factor means that $T$ is [[semisimple|08VRX3Q4PB]], so that every invariant subspace has an invariant complement.
For a general $m_T = \prod_i p_i^{e_i}$, the [[primary decomposition|49ZHBMYKVE]] splits $V$ into the pieces $\ker p_i(T)^{e_i}$.
The exponent of $t - \lambda$ in $m_T$ is the size of the largest Jordan block for $\lambda$ in the [[Jordan normal form|085HQ5G5TE]], so the criterion says that every Jordan block has size $1$.

## History

Hoffman and Kunze prove the criterion in Section 6.4 of their textbook, in the chapter on elementary canonical forms.
We know of no single first source for it.

## Explanations

### L1 human

Some matrices satisfy a short equation, such as $A^2 = A$ or $A^2 = I$.
Write the equation as a polynomial in $t$, for example $t^2 - 1$.
If the polynomial factors into different pieces of the form $t - a$, then the matrix can be made diagonal.
A repeated piece, such as $(t - 1)^2$ in the smallest such polynomial, means that the matrix cannot be made diagonal.

### L2 human

Let us show without eigenvalue computations that $A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ is diagonalizable over $\R$.
Squaring gives $A^2 = I$, so the polynomial $f = t^2 - 1 = (t - 1)(t + 1)$ kills $A$.
Its roots $1$ and $-1$ are distinct and real, so condition 2 holds, and $A$ is diagonalizable over $\R$.
To find $P$, note that $(1, 1)$ is fixed by $A$ and $(1, -1)$ is sent to its negative.
With these columns,
$$P D P^{-1} = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} \cdot \frac{1}{2} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = \frac{1}{2} \begin{pmatrix} 0 & 2 \\ 2 & 0 \end{pmatrix} = A,$$
where the first factor is $P D$ for $D = \operatorname{diag}(1, -1)$ and the second is $P^{-1}$.
The typical use is an identity such as $A^2 = A$, $A^2 = I$ or $A^3 = A$, which proves diagonalizability at once.
Watch out: read the minimal polynomial, not the characteristic polynomial, since the double root of $(t - 1)^2$ for $I_2$ does not prevent diagonalization.

### L3 human

The [[proof by the kernels lemma|ZAYD2GV1KT]] splits $V$ into the kernels of the coprime factors $T - \lambda_i$ of $m_T$, and each kernel is an eigenspace.
In the language of modules, $V$ is a module over the ring $F[t]/(m_T)$.
When the roots are simple and lie in $F$, the Chinese remainder theorem makes this ring a product of $k$ copies of $F$.
A module over such a product is a direct sum of pieces, one for each factor, and here the pieces are the eigenspaces.
The same idea shows that a commutative algebra of operators generated by diagonalizable elements can be diagonalized all at once.
