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

Let $F$ be a field, $n \ge 1$, and $A \in M_n(F)$.
Let $d_1 \mid d_2 \mid \cdots \mid d_r$ be the [[invariant factors|F7GJPMVBXA]] of $A$, with $m_i = \deg d_i$, so $m_1 + \cdots + m_r = n$.
Let $\mathcal{C}(A) = \{X \in M_n(F) : XA = AX\}$ be the centralizer of $A$, the set of [[matrices that commute with $A$|8G3X8MPG7E]].
Let $F[A] = \{f(A) : f \in F[x]\}$.

1. $\mathcal{C}(A)$ is a subalgebra of $M_n(F)$ that contains $F[A]$, and $\dim_F F[A] = \deg \mu_A = m_r$, where $\mu_A$ is the [[minimal polynomial|03NDVCSHSB]].
2. $\dim_F \mathcal{C}(A) = \sum_{i=1}^{r} \sum_{j=1}^{r} \deg \gcd(d_i, d_j) = \sum_{i=1}^{r} (2r - 2i + 1)\, m_i$.
3. $\dim_F \mathcal{C}(A) \ge n$, with equality if and only if $A$ is cyclic, that is, $r = 1$ and $\mu_A = \chi_A$.
4. $\mathcal{C}(A) = F[A]$ if and only if $A$ is cyclic. So if $A$ is cyclic, every matrix that commutes with $A$ is a polynomial in $A$.

## Remarks

### Why each hypothesis is needed

The condition that $A$ is cyclic in part 4 is necessary.
For $A = I_2$, every $2 \times 2$ matrix commutes with $A$, but $F[A]$ is the set of scalar matrices, of dimension $1$.
The condition $n \ge 1$ only excludes the empty matrix, which has no invariant factors.

### Consequences

- If $A$ has $n$ distinct eigenvalues in $F$, then $A$ is cyclic, and every matrix that commutes with $A$ is a polynomial in $A$.
- If $A$ is cyclic and $B$ commutes with $A$, then $B$ is a polynomial in $A$ of degree less than $n$, and this polynomial is unique.
- For a cyclic $A$ and every $X$ with $XA = A^{\mathsf T} X$, part 4 applied to $A$ gives $X = T f(A)$ for one fixed invertible $T$ with $TA = A^{\mathsf T} T$. This is used in the [[similarity of a matrix and its transpose|C708QKZPE6]].

### Generalizations

In the module language of an [[endomorphism as an $F[x]$-module|KGVTFBZX59]], $\mathcal{C}(A)$ is the ring of $F[x]$-module endomorphisms of $F^n$.
The same count holds for any finitely generated torsion module over a principal ideal domain: the length of $\operatorname{Hom}(R/(a), R/(b))$ is the length of $R/(\gcd(a, b))$.
Suppose that $\chi_A$ splits over $F$, and let $\lambda^{(\mu)}$ be the partition of Jordan block sizes at each eigenvalue $\mu$.
Then the formula reads $\dim \mathcal{C}(A) = \sum_\mu \sum_j (\lambda^{(\mu)\prime}_j)^2$, the sum of the squares of the column lengths of the [[Young diagrams|096AHMB3P4]].

## History

The first significant results on commuting matrices were proved by Ferdinand Georg Frobenius in 1878.

## Explanations

### L1 human

Fix a square matrix $A$.
The matrices that commute with $A$ form a vector space.
This space always has dimension at least $n$.
It has dimension exactly $n$ when $A$ is cyclic, and then each matrix in it is a polynomial in $A$.

### L2 human

Count the dimension from the invariant factors.

1. For $A = I_2$, the invariant factors are $x - 1, x - 1$, so $r = 2$ and $m_1 = m_2 = 1$. The formula gives $3 \cdot 1 + 1 \cdot 1 = 4$, which is all of $M_2(F)$.
2. For $A = J_2(0) \oplus J_1(0)$, the invariant factors are $x, x^2$. The formula gives $3 \cdot 1 + 1 \cdot 2 = 5$.
3. For $A = J_2(0) \oplus J_2(0)$, the invariant factors are $x^2, x^2$. The formula gives $3 \cdot 2 + 1 \cdot 2 = 8$.
4. For $A = \operatorname{diag}(1, 2)$, the only invariant factor is $(x - 1)(x - 2)$. The formula gives $2 = n$, and the centralizer is the set of diagonal matrices, equal to $F[A]$.

The trap is to count the pairs $(i, j)$ with $i \le j$ only: the sum runs over all ordered pairs.

### L3 human

The matrices that commute with $A$ are the $F[x]$-linear endomorphisms of $F^n_A$.
The module $F^n_A$ is $\bigoplus_i F[x]/(d_i)$, so its endomorphisms form a block matrix of the spaces $\operatorname{Hom}(F[x]/(d_j), F[x]/(d_i))$.
Each of these spaces has dimension $\deg \gcd(d_i, d_j) = m_{\min(i, j)}$.
A cyclic module $F[x]/(d)$ has endomorphism ring $F[x]/(d)$, which is the image of $F[x]$ in this case.
