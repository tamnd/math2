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

Let $F$ be a field, let $V$ be a vector space over $F$ of finite dimension $n \ge 1$, and let $T \colon V \to V$ be linear with [[minimal polynomial|03NDVCSHSB]] $m_T$.

1. The following conditions are equivalent.
    1. $T$ is [[diagonalizable|07SQCNV233]] over $F$.
    2. $f(T) = 0$ for some polynomial $f = (t - a_1) \cdots (t - a_r)$ with pairwise distinct $a_j \in F$.
    3. $m_T = (t - \lambda_1) \cdots (t - \lambda_k)$ with pairwise distinct $\lambda_i \in F$, that is, $m_T$ splits over $F$ and has simple roots.
2. If these conditions hold, then $\lambda_1, \dots, \lambda_k$ are the distinct [[eigenvalues|0BQAA2BK3Q]] of $T$.
3. If $T$ is diagonalizable and $U \subseteq V$ is a $T$-[[invariant subspace|0ACX5QT8TE]], then $U = \bigoplus_i \big(U \cap E_{\lambda_i}\big)$, and the [[restriction|0KN7EPH7Z0]] $T|_U$ is diagonalizable.

For an $n \times n$ matrix $A$ over $F$, the same holds with $m_A$ and the map $x \mapsto A x$.

## Remarks

### Why each hypothesis is needed

- The roots must be simple. The [[shear|~58e14c85]] $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has $m = (t - 1)^2$ and is not diagonalizable.
- The roots must lie in $F$. Over $\R$, the rotation $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ has $m = t^2 + 1$, which has simple roots $\pm i$ in $\C$ but does not split over $\R$.
- The condition is on the minimal polynomial, not on the [[characteristic polynomial|0J5EMJRRFM]]. The identity $I_2$ has $p = (t - 1)^2$ but $m = t - 1$, and it is diagonal.

### Consequences

- Every [[projection|033DA1WE8Y]] $P$ with $P^2 = P$ is diagonalizable, since $t^2 - t = t(t - 1)$ annihilates it. Its eigenvalues lie in $\{0, 1\}$.
- If $2 \ne 0$ in $F$, every involution $A^2 = I$ is diagonalizable, since $t^2 - 1 = (t - 1)(t + 1)$ and $1 \ne -1$.
- Over $\mathbb{F}_2$, the shear satisfies $A^2 = I$ but is not diagonalizable, because there $t^2 - 1 = (t - 1)^2$.
- Over $\C$, every matrix with $A^m = I$ for some $m \ge 1$ is diagonalizable, since $t^m - 1$ has the $m$ distinct [[roots of unity|057BH3JC9S]] as roots.
- This fails over $\R$: the rotation by a right angle has order $4$ but no real eigenvalue. It also fails over $\mathbb{F}_p$: the shear has order $p$.
- By part 3, a diagonalizable map stays diagonalizable on each invariant subspace. This is the key step of [[simultaneous diagonalization|0FK17N4DKA]].
- The test needs no eigenvectors. If some product of distinct linear factors kills $T$, then $T$ is diagonalizable.

### Converse

Each condition in part 1 implies the others, so every converse holds.
The converse of part 3 is false: $T|_U$ and the quotient map can both be diagonalizable while $T$ is not, as for the shear with $U = F e_1$.

### Generalizations

Without the splitting condition, $m_T$ with no repeated irreducible factor means that $T$ is [[semisimple|08VRX3Q4PB]]: each invariant subspace has an invariant complement.
For a general $m_T = \prod_i p_i^{e_i}$, the [[primary decomposition|~81757fe9]] splits $V$ into the pieces $\ker p_i(T)^{e_i}$.
The exponent of $t - \lambda$ in $m_T$ is the size of the largest Jordan block for $\lambda$ in the [[Jordan normal form|085HQ5G5TE]].

## History

The criterion appears in the treatment of the primary decomposition by Hoffman and Kunze, Section 6.4.
We do not know of a first source.

## Explanations

### L1 human

Some matrices satisfy a simple equation, such as $A^2 = A$ or $A^2 = I$.
If the equation, written as a polynomial, factors into different linear pieces, then the matrix can be made diagonal.
The smallest such polynomial is the minimal polynomial.
A repeated piece, such as $(t - 1)^2$, means that the matrix cannot be made diagonal.

### L2 human

Let $A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ over $\R$.

1. $A^2 = I$, so $f = t^2 - 1 = (t - 1)(t + 1)$ annihilates $A$.
2. The roots $1$ and $-1$ are distinct and real. By condition 2, $A$ is diagonalizable over $\R$.
3. Eigenvectors are $(1, 1)$ for $1$ and $(1, -1)$ for $-1$.
4. With $P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$, we get $A P = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} = P \operatorname{diag}(1, -1)$.

The typical use is a polynomial identity such as $A^2 = A$, $A^2 = I$ or $A^3 = A$, which proves diagonalizability at once.
The trap is to read the characteristic polynomial instead of the minimal polynomial: $(t - 1)^2$ for $I_2$ does not prevent diagonalizability.

### L3 human

The proof by the [[kernels lemma|~4b2aa8fd]] splits $V$ into the kernels of the coprime factors of $m_T$, and each kernel is an eigenspace.
In the language of modules, $V$ is a module over $F[t]/(m_T)$, and simple roots make this ring a product of copies of $F$, by the Chinese remainder theorem.
A module over a finite product of fields is a direct sum of the corresponding pieces, which here are the eigenspaces.
For a family of operators, the same idea shows that a commutative algebra generated by diagonalizable elements is diagonalizable as a whole.
