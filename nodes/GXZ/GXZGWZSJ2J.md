---
tag: GXZGWZSJ2J
kind: statement
role: theorem
name: Matrices that commute with a given matrix
aliases: [centralizer-of-a-matrix, dimension-of-the-centralizer-of-a-matrix]
msc: ["15A27"]
topics: [GEBYZKYV3D]
audience: grad
about: [1VC7EJ1ZBZ, 8G3X8MPG7E]
uses: [8G3X8MPG7E, 1VC7EJ1ZBZ, KGVTFBZX59, 096AHMB3P4, F7GJPMVBXA, RK1QVMYW7H, 03NDVCSHSB, 0C8WYW4KYQ]
sources:
  - url: https://en.wikipedia.org/wiki/Commuting_matrices
    locator: Characterizations and properties
  - url: https://en.wikipedia.org/wiki/Commuting_matrices
    locator: History
  - url: https://en.wikipedia.org/wiki/Centralizer_and_normalizer
---

## Statement

The matrices that commute with a given $n \times n$ matrix always form a space of dimension at least $n$, and the dimension is exactly $n$ when the matrix is cyclic, in which case every such matrix is a polynomial in it.

Let $F$ be a field, $n \ge 1$, and $A \in M_n(F)$.
Let $d_1 \mid d_2 \mid \cdots \mid d_r$ be the nonconstant [[invariant factors|F7GJPMVBXA]] of $A$, and let $m_i = \deg d_i$, so that $m_1 + \cdots + m_r = n$.
Let $\mathcal{C}(A) = \{ X \in M_n(F) : XA = AX \}$ be the *centralizer* of $A$, the set of [[matrices that commute with A|8G3X8MPG7E]], and let $F[A] = \{ f(A) : f \in F[x] \}$.

1. $\mathcal{C}(A)$ is a subalgebra of $M_n(F)$ that contains $F[A]$, and $\dim_F F[A] = \deg \mu_A = m_r$, where $\mu_A$ is the [[minimal polynomial|03NDVCSHSB]] of $A$.
2. The dimension of the centralizer is
$$\dim_F \mathcal{C}(A) = \sum_{i=1}^{r} \sum_{j=1}^{r} \deg \gcd(d_i, d_j) = \sum_{i=1}^{r} (2r - 2i + 1)\, m_i.$$
3. $\dim_F \mathcal{C}(A) \ge n$, with equality if and only if $A$ is cyclic, that is, if and only if $r = 1$, or equivalently $\mu_A = \chi_A$.
4. $\mathcal{C}(A) = F[A]$ if and only if $A$ is cyclic.

## Remarks

### Reading the formula on small cases

Take $A = I_2$.
Its invariant factors are $x - 1, x - 1$, so $r = 2$ and $m_1 = m_2 = 1$, and the formula gives
$$3 \cdot 1 + 1 \cdot 1 = 4 = \dim M_2(F).$$
This is right, since every matrix commutes with the identity.

Take $A = \operatorname{diag}(1, 2)$ over $\mathbb{Q}$.
Its only invariant factor is $(x - 1)(x - 2)$, so $r = 1$ and the formula gives $1 \cdot 2 = 2 = n$.
The matrices that commute with $A$ are the diagonal matrices, and each one is a polynomial in $A$: $\operatorname{diag}(s, t) = (2s - t) I + (t - s) A$.
Check: the $(1, 1)$ entry is $2s - t + t - s = s$, and the $(2, 2)$ entry is $2s - t + 2t - 2s = t$.

The field matters only through the invariant factors.
Over $\mathbb{Q}$, let $A = C \oplus C$ with $C = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, the companion matrix of $x^2 + 1$.
The invariant factors are $x^2 + 1, x^2 + 1$, so the dimension is $3 \cdot 2 + 1 \cdot 2 = 8$.
This fits the fact that $\mathbb{Q}[C]$ is a copy of $\mathbb{Q}(i)$ and the centralizer is a copy of $M_2(\mathbb{Q}(i))$, of dimension $4 \cdot 2 = 8$ over $\mathbb{Q}$.

### Why each hypothesis is needed

Cyclicity is needed in parts 3 and 4.
For $A = I_2$ the centralizer is all of $M_2(F)$, of dimension $4 > 2$, while $F[A]$ is the set of scalar matrices, of dimension $1$.
So a matrix that commutes with $A$ need not be a polynomial in $A$, for instance $E_{12}$.

The condition $n \ge 1$ only excludes the empty matrix, which has no invariant factors.
No condition on the field is needed: the theorem holds over every field, including fields where $\chi_A$ does not split.

### What it gives you

If $A$ has $n$ distinct eigenvalues in $F$, then $\mu_A = \chi_A$, so $A$ is cyclic.
Then every matrix that commutes with $A$ is a polynomial in $A$, as in the diagonal example above.

If $A$ is cyclic and $B$ commutes with $A$, then $B = f(A)$ for exactly one polynomial $f$ of degree less than $n$.
The reason is that $I, A, \dots, A^{n-1}$ is a basis of $F[A]$, which has dimension $n$.

The same idea controls the equation $XA = A^{\mathsf T} X$.
If one invertible $T$ satisfies $TA = A^{\mathsf T} T$, then for every solution $X$ the matrix $T^{-1} X$ commutes with $A$.
So for a cyclic $A$ every solution has the form $X = T f(A)$, which is how the [[similarity of a matrix and its transpose|C708QKZPE6]] is studied in detail.

### Watch out

The double sum runs over all ordered pairs $(i, j)$, not only over $i \le j$.
For $A = J_2(0) \oplus J_1(0)$ the invariant factors are $x, x^2$.
The full sum is $1 + 1 + 1 + 2 = 5$, while the pairs with $i \le j$ give only $1 + 1 + 2 = 4$.
The value $5$ is right: a direct computation of the commuting matrices finds five free parameters.

### Generalizations

In the language of an [[endomorphism as an F[x]-module|KGVTFBZX59]], $\mathcal{C}(A)$ is the ring of module endomorphisms of $F^n$ with $x$ acting as $A$.
The count works for any finitely generated torsion module over a principal ideal domain $R$, because $\operatorname{Hom}_R(R/(a), R/(b))$ is isomorphic to $R/(\gcd(a, b))$.

When $\chi_A$ splits over $F$, let $\lambda^{(\mu)}$ be the partition of the Jordan block sizes at the eigenvalue $\mu$.
Then the formula becomes $\dim \mathcal{C}(A) = \sum_\mu \sum_j \bigl(\lambda^{(\mu)\prime}_j\bigr)^2$, the sum of the squares of the column lengths of the [[Young diagrams|096AHMB3P4]].
For $J_3(0) \oplus J_1(0)$ the columns have lengths $2, 1, 1$, and the dimension is $4 + 1 + 1 = 6$.

## History

Frobenius proved the first substantial results on commuting matrices in 1878.

## Explanations

### L1 human

Fix a square matrix $A$ and collect all the matrices $X$ with $XA = AX$.
You can add them and scale them, so they form a space, and that space always contains $I, A, A^2, \dots$.
For a $2 \times 2$ matrix like $\operatorname{diag}(1, 2)$, the commuting matrices are just the diagonal ones, a space of size $2$.
For the identity, every matrix commutes with it, a space of size $4$.
The theorem says that size $n$ is the smallest possible, and it happens exactly for the cyclic matrices.

### L2 human

Here is a typical use: find the dimension of the centralizer of $A = J_2(1) \oplus J_1(1) \oplus J_1(3)$ over $\mathbb{Q}$.
The invariant factors are $d_1 = x - 1$ and $d_2 = (x - 1)^2 (x - 3)$, so $r = 2$, $m_1 = 1$ and $m_2 = 3$.
The formula gives
$$\dim \mathcal{C}(A) = 3 \cdot 1 + 1 \cdot 3 = 6.$$
Check with Young diagrams: the eigenvalue $1$ has blocks $(2, 1)$ with columns $2, 1$, and the eigenvalue $3$ has one block with column $1$, so the sum is $4 + 1 + 1 = 6$.
Since $6 > 4$, the matrix is not cyclic, and some matrix commutes with $A$ without being a polynomial in $A$.
This is how you test cyclicity without searching for a cyclic vector.

### L3 human

The matrices that commute with $A$ are the $F[x]$-linear endomorphisms of $F^n$ with $x$ acting as $A$.
That module is $\bigoplus_i F[x]/(d_i)$, so its endomorphisms form a block matrix whose entries are the spaces $\operatorname{Hom}(F[x]/(d_j), F[x]/(d_i))$.
Each of these spaces has dimension $\deg \gcd(d_i, d_j) = m_{\min(i, j)}$, and adding them gives the formula.
A cyclic module $F[x]/(d)$ has endomorphism ring $F[x]/(d)$ itself, which is the image of $F[x]$, and that is part 4.
Over a finite field the units of $\mathcal{C}(A)$ form the centralizer in the group $GL_n$, and their number gives the class sizes in the [[conjugacy classes of GL_n over a finite field|4FV9TDGWWH]].
