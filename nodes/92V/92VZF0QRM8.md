---
tag: 92VZF0QRM8
kind: statement
role: theorem
name: Similarity via the characteristic matrix
aliases: [smith-normal-form-of-the-characteristic-matrix, similarity-and-equivalence-of-characteristic-matrices]
msc: ["15A21", "15A54"]
topics: [GEBYZKYV3D]
audience: grad
about: [0E89HQATM8, F7GJPMVBXA]
uses: [027KDW2K72, MV28Z5N9XX, 0CMHSGTWXB, F7GJPMVBXA, 0BT9BYWVRY, 0C8WYW4KYQ, 0VSSPAFM2C]
sources:
  - url: https://en.wikipedia.org/wiki/Smith_normal_form
    locator: Similarity
  - url: https://en.wikipedia.org/wiki/Smith_normal_form
    locator: Definition
  - book: isbn:9780135367971
    locator: Section 7.4
---

## Statement

Two matrices over a field are similar exactly when their characteristic matrices $xI - A$ and $xI - B$ can be turned into each other by invertible row and column operations over $F[x]$, and the Smith normal form of $xI - A$ lists the invariant factors of $A$.

Let $F$ be a field and $A, B \in M_n(F)$.
The *characteristic matrix* of $A$ is $xI - A \in M_n(F[x])$.
Two matrices $M, N \in M_n(F[x])$ are [[equivalent|0CMHSGTWXB]] over $F[x]$ when $N = UMV$ for matrices $U, V$ that are invertible in $M_n(F[x])$, that is, whose determinants are nonzero constants.

1. The following three conditions are equivalent.
   (a) $A$ and $B$ are [[similar|027KDW2K72]] over $F$.
   (b) $xI - A$ and $xI - B$ are equivalent over $F[x]$.
   (c) $xI - A$ and $xI - B$ have the same [[Smith normal form|MV28Z5N9XX]] over $F[x]$, with monic diagonal entries.
2. The Smith normal form of $xI - A$ is $\operatorname{diag}(1, \dots, 1, d_1, \dots, d_r)$, where $d_1 \mid \cdots \mid d_r$ are the [[invariant factors|F7GJPMVBXA]] of $A$ and there are $n - r$ entries equal to $1$.
3. Let $D_0 = 1$, and for $1 \le k \le n$ let $D_k$ be the monic [[greatest common divisor|0C8WYW4KYQ]] of all $k \times k$ [[minors|0BT9BYWVRY]] of $xI - A$, the $k$-th *determinantal divisor*.
   Then the $k$-th diagonal entry of the Smith normal form is $D_k / D_{k-1}$, and $D_n = \det(xI - A)$ is the [[characteristic polynomial|0VSSPAFM2C]] of $A$.

## Remarks

### A first reduction

Take $A = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$, so that
$$xI - A = \begin{pmatrix} x - 2 & -1 \\ 0 & x - 2 \end{pmatrix}.$$
Swap the two columns, and multiply the new first row by $-1$:
$$\begin{pmatrix} -1 & x - 2 \\ x - 2 & 0 \end{pmatrix} \to \begin{pmatrix} 1 & -(x - 2) \\ x - 2 & 0 \end{pmatrix}.$$
Subtract $x - 2$ times row $1$ from row $2$, and then add $x - 2$ times column $1$ to column $2$:
$$\begin{pmatrix} 1 & -(x - 2) \\ 0 & (x - 2)^2 \end{pmatrix} \to \begin{pmatrix} 1 & 0 \\ 0 & (x - 2)^2 \end{pmatrix}.$$
So the Smith normal form is $\operatorname{diag}(1, (x - 2)^2)$, and $A$ has the single invariant factor $(x - 2)^2$.
Check by part 3: the entry $-1$ gives $D_1 = 1$, and $D_2 = \det(xI - A) = (x - 2)^2$.

### Why each hypothesis is needed

The ring $F[x]$ is the right ring, and both smaller and larger rings fail.
Over $F$ itself, $xI - A$ is not even a matrix, and equivalence of $A$ and $B$ over $F$ compares only their ranks.
The [[equivalent matrices that are not similar|6CKAMR5WK9]] show how much is lost that way.
Over the field $F(x)$ of rational functions, $\det(xI - A) = \chi_A$ is a nonzero element, so $xI - A$ is invertible there.
Any two invertible matrices are equivalent, so over $F(x)$ condition (b) would hold for every pair $A, B$.
What matters is that $U$ and $V$ are invertible over $F[x]$, with constant nonzero determinants.

### What it gives you

Similarity becomes a computation: row and column operations over $F[x]$, with no root finding.
For a $3 \times 3$ example take $A = J_2(1) \oplus J_1(1)$, with
$$xI - A = \begin{pmatrix} x - 1 & -1 & 0 \\ 0 & x - 1 & 0 \\ 0 & 0 & x - 1 \end{pmatrix}.$$
The entry $-1$ gives $D_1 = 1$.
The $2 \times 2$ minors include $(x - 1)^2$ and $-(x - 1)$, from rows $1, 3$ and columns $2, 3$, and every $2 \times 2$ minor is a multiple of $x - 1$, so $D_2 = x - 1$.
Finally $D_3 = (x - 1)^3$, so the Smith normal form is $\operatorname{diag}(1, x - 1, (x - 1)^2)$.

Three facts are read off at once.
The minimal polynomial is $D_n / D_{n-1}$, the last diagonal entry.
A matrix is cyclic exactly when $D_{n-1} = 1$, because then only one diagonal entry is not $1$.
A matrix is similar to its transpose, because $xI - A^{\mathsf T} = (xI - A)^{\mathsf T}$ and transposing a matrix does not change its set of minors.

### The converse

Each part is already an equivalence, so there is no separate converse to state.
The theorem does not say that every matrix over $F[x]$ is equivalent to a characteristic matrix.
For $xI - A$ the diagonal entries of the Smith form are nonzero and their degrees add up to $n$, and a matrix such as $\operatorname{diag}(1, x^3)$ of size $2$ fails this.

### Watch out

Only invertible operations are allowed.
You may multiply a row by a nonzero constant, but not by a polynomial such as $x - 2$, and you may not divide by one.
For example, multiplying row $2$ of $xI - 2I_2 = \operatorname{diag}(x - 2, x - 2)$ by $1/(x - 2)$ would give $\operatorname{diag}(x - 2, 1)$ and suggest the invariant factor $x - 2$ alone, which has the wrong degree.

### Generalizations

For a principal ideal domain $R$ and a module with a presentation matrix $M$, the Smith normal form of $M$ gives the invariant factors of the module.
For $R = \mathbb{Z}$ this computes the structure of a finitely generated abelian group.
For pencils $xB - A$ with two matrices, Kronecker's theory of pencils classifies the pairs $(A, B)$ up to the equivalence $(A, B) \mapsto (PAQ, PBQ)$.

## History

The Smith normal form is named after Henry John Stephen Smith, who studied it for integer matrices.
In older books the variable is written $\lambda$, and matrices over $F[\lambda]$ are called $\lambda$-matrices.

## Explanations

### L1 human

To decide whether two matrices are the same map in different coordinates, we can work with matrices of polynomials.
From each matrix we form $x$ times the identity minus the matrix.
Then we simplify these polynomial matrices by row and column operations until they are diagonal, in a standard form.
For the matrix with rows $(2, 1)$ and $(0, 2)$ the standard form has the diagonal $1$ and $(x - 2)^2$.
The two matrices are similar exactly when their standard forms are equal.

### L2 human

Here is a typical problem: are $A = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$ and $B = 2I_2$ similar over $\mathbb{Q}$?
They have the same characteristic polynomial $(x - 2)^2$, so that test is not enough.

The first reduction above gave the Smith normal form $\operatorname{diag}(1, (x - 2)^2)$ for $xI - A$.
For $B$, every entry of $xI - B = \operatorname{diag}(x - 2, x - 2)$ is a multiple of $x - 2$, and $x - 2$ itself is an entry, so $D_1 = x - 2$.
Then $D_2 = (x - 2)^2$, and the Smith normal form is $\operatorname{diag}(x - 2, x - 2)$.
The two forms differ, so $A$ and $B$ are not similar.
The invariant factors are $(x - 2)^2$ for $A$ and $x - 2, x - 2$ for $B$.

The typical use is to compute invariant factors by hand for small matrices, or by computer algebra for large ones.
The trap is the illegal division of the "Watch out" above.

### L3 human

The matrix $xI - A$ is a presentation matrix of the [[module of $A$|KGVTFBZX59]]: there is an exact sequence
$$F[x]^n \xrightarrow{xI - A} F[x]^n \to F^n_A \to 0.$$
So the theorem says that a module over a principal ideal domain is determined by the Smith normal form of a square presentation matrix.
The same computation finds the homology of chain complexes over $\mathbb{Z}$ and the structure of finitely presented abelian groups.
In the theory of [[conjugacy classes of $GL_n(\mathbb{F}_q)$|4FV9TDGWWH]] it turns the classification into a statement about lists of polynomials.
