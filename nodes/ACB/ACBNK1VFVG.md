---
tag: ACBNK1VFVG
kind: statement
role: lemma
name: Kernels lemma
msc: ["15A04", "15A21"]
topics: [Z6S6PWMJPH]
audience: ug2
about: [0ACX5QT8TE]
uses: [0BNEXSKNRV, 02YFME3RGW, 041JTZCK9Q, 0VY3WPP9Y3]
sources:
  - url: https://en.wikipedia.org/wiki/Jordan%E2%80%93Chevalley_decomposition
    locator: Decomposition of a linear operator
  - book: isbn:9780135367971
    locator: Section 6.8
  - book: isbn:9783031410253
    locator: Chapter 8
---

## Statement

When two polynomials have no common factor, the vectors killed by their product split uniquely into a part killed by the first and a part killed by the second, and the split is given by polynomials in $T$.
Let $F$ be a field, let $V$ be a vector space over $F$ of any dimension, and let $T \colon V \to V$ be linear.
Let $p, q \in F[t]$ be coprime, that is, their [[greatest common divisor|02WF878BH1]] is $1$, and choose $a, b \in F[t]$ with $a p + b q = 1$.

1. The [[kernel|0S23E6YE83]] of $(p q)(T)$ is a [[direct sum|0XYYT5KNTX]]:
   $$\ker (p q)(T) = \ker p(T) \oplus \ker q(T).$$
2. On $\ker (p q)(T)$, the projection onto $\ker p(T)$ along $\ker q(T)$ is the restriction of $(b q)(T)$, and the projection onto $\ker q(T)$ along $\ker p(T)$ is the restriction of $(a p)(T)$.
   Both are [[polynomials in $T$|0E3MV6E6MG]].
3. If $(p q)(T) = 0$, then $V = \ker p(T) \oplus \ker q(T)$, with $\ker p(T) = \operatorname{im} q(T)$ and $\ker q(T) = \operatorname{im} p(T)$.
4. More generally, let $p_1, \dots, p_k \in F[t]$ be pairwise coprime.
   Then $\ker (p_1 \cdots p_k)(T) = \ker p_1(T) \oplus \dots \oplus \ker p_k(T)$, and the projections onto the summands are restrictions of polynomials in $T$.

Each summand $\ker p_i(T)$ is a $T$-[[invariant subspace|0ACX5QT8TE]].

## Remarks

### A first example

Let $A = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$, $p = t - 1$ and $q = t - 2$.
These are coprime, and $p - q = 1$, so we may take $a = 1$ and $b = -1$.
The product kills $A$:
$$(A - I)(A - 2I) = \begin{pmatrix} 0 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} -1 & 1 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}.$$
So part 3 applies, and the two projections of part 2 are
$$(b q)(A) = 2I - A = \begin{pmatrix} 1 & -1 \\ 0 & 0 \end{pmatrix}, \qquad (a p)(A) = A - I = \begin{pmatrix} 0 & 1 \\ 0 & 1 \end{pmatrix}.$$
The first has image $F e_1 = \ker(A - I)$, and the second has image $F (1, 1) = \ker(A - 2I)$.
Check: the two matrices add up to $I$, and $(A - I)^2 = A - I$.
So every vector splits as $(x, y) = (x - y, 0) + (y, y)$, one eigenvector for each eigenvalue.

### Watch out: coprimality is needed

Drop the hypothesis that $p$ and $q$ are coprime, and take $p = q = t$ with the nilpotent matrix $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$.
Then $N^2 = 0$, so $\ker (p q)(N) = \ker N^2 = F^2$.
But $\ker N + \ker N = F e_1$ is only a line, so the conclusion of part 1 fails.
Finite dimension, on the other hand, is not needed: the proof uses only the identity $a p + b q = 1$, so the lemma holds in every vector space.

### What it gives you

Most decompositions of a single linear map start from the kernels lemma.
If $(t - \lambda_1) \cdots (t - \lambda_k)$ with distinct $\lambda_i$ kills $T$, then part 4 makes $V$ the direct sum of the eigenspaces, which is the [[minimal polynomial criterion|0MPAJRB23T]] for diagonalizability.
For the factorization of the minimal polynomial into powers of distinct irreducible polynomials, it gives the [[primary decomposition theorem|49ZHBMYKVE]].
When the characteristic polynomial splits, it gives the [[decomposition into generalized eigenspaces|0Z3GDY89T5]].
Since each projection is a polynomial in $T$, it commutes with every map that commutes with $T$, so every such map preserves each summand.

### The converse

The converse is false.
Take $p = q = t$ and $T = \id_V$.
Both $\ker p(T)$ and $\ker (p q)(T) = \ker \id_V$ are $0$, so the equation of part 1 holds as $0 = 0 \oplus 0$, although $p$ and $q$ are not coprime.

### Generalizations

The lemma is the [[Chinese remainder theorem|0FNN9B4W64]] $F[t]/(p q) \cong F[t]/(p) \times F[t]/(q)$, applied to the $F[t]$-module $V$ in which $t$ acts as $T$.
It holds in every module $M$ over a principal ideal domain $R$: for coprime $p, q \in R$, the elements of $M$ killed by $p q$ form the direct sum of the elements killed by $p$ and of those killed by $q$.
In the [[structure theorem for modules over a principal ideal domain|TXMV0YDACG]], this splits a torsion module into its primary parts.

### Try it

Let $A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ over $\Q$, with $p = t - 1$ and $q = t + 1$, so $(p q)(A) = A^2 - I = 0$.
Find $a, b$ with $a p + b q = 1$, write down the two projections, and split $(5, 1)$.
You should get $a = -\tfrac{1}{2}$, $b = \tfrac{1}{2}$, and
$$(5, 1) = (3, 3) + (2, -2),$$
where $A$ fixes $(3, 3)$ and negates $(2, -2)$.

## History

The name translates the French "lemme des noyaux", the usual name of the result in French textbooks.
Hoffman and Kunze prove the general form inside the primary decomposition theorem, in Section 6.8.

## Explanations

### L1 human

Suppose a machine $T$ obeys two rules at once, and the two rules have nothing in common.
Then every input splits into one part that obeys the first rule and one part that obeys the second.
The split is unique, and you can compute it with the machine itself.
For the matrix with rows $(1, 1)$ and $(0, 2)$, the vector $(3, 1)$ splits as $(2, 0) + (1, 1)$: the matrix keeps the first part and doubles the second.

### L2 human

Here is the typical use.
Let $T$ be a linear map with $T^2 = I$, over a field in which $2 \ne 0$.
The polynomial $t^2 - 1 = (t - 1)(t + 1)$ kills $T$, and the factors are coprime because
$$\tfrac{1}{2}(t + 1) - \tfrac{1}{2}(t - 1) = 1.$$
With $p = t - 1$, $q = t + 1$, $a = -\tfrac{1}{2}$ and $b = \tfrac{1}{2}$, part 2 gives the projections
$$\tfrac{1}{2}(T + I) \text{ onto } \ker(T - I), \qquad \tfrac{1}{2}(I - T) \text{ onto } \ker(T + I).$$
For the swap $T(x, y) = (y, x)$ these send $(x, y)$ to $\tfrac{1}{2}(x + y, x + y)$ and to $\tfrac{1}{2}(x - y, y - x)$, which add up to $(x, y)$.
So when $2 \ne 0$, every involution makes $V$ the direct sum of its eigenspaces for $1$ and $-1$.
The trap is to forget coprimality: in characteristic $2$ the two factors are equal, and the shear $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ over $\mathbb{F}_2$ squares to $I$ but is not diagonalizable.

### L3 human

In the ring $F[t]/(p q)$, the classes $e_1 = b q$ and $e_2 = a p$ are orthogonal idempotents with $e_1 + e_2 = 1$.
They act on $\ker (p q)(T)$ as the projections of part 2.
The same idempotents give the projections onto generalized eigenspaces, and they show that the semisimple part of the [[Jordan-Chevalley decomposition|011K11VPJN]] is a polynomial in $T$.
