---
tag: ~4b2aa8fd
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

Let $F$ be a field, let $V$ be a vector space over $F$ of any dimension, and let $T \colon V \to V$ be linear.
Let $p, q \in F[t]$ be coprime, that is, their [[greatest common divisor|02WF878BH1]] is $1$, and choose $a, b \in F[t]$ with $a p + b q = 1$.

1. The [[kernel|0S23E6YE83]] of $(p q)(T)$ is a [[direct sum|0XYYT5KNTX]]:
$$\ker (p q)(T) = \ker p(T) \oplus \ker q(T).$$
2. On $\ker (p q)(T)$, the projection onto $\ker p(T)$ along $\ker q(T)$ is the restriction of $(b q)(T)$, and the projection onto $\ker q(T)$ along $\ker p(T)$ is the restriction of $(a p)(T)$. Both are [[polynomials in $T$|0E3MV6E6MG]].
3. If $(p q)(T) = 0$, then $V = \ker p(T) \oplus \ker q(T)$, with $\ker p(T) = \operatorname{im} q(T)$ and $\ker q(T) = \operatorname{im} p(T)$.
4. More generally, let $p_1, \dots, p_k \in F[t]$ be pairwise coprime. Then $\ker (p_1 \cdots p_k)(T) = \ker p_1(T) \oplus \cdots \oplus \ker p_k(T)$, and the projections onto the summands are restrictions of polynomials in $T$.

Each summand $\ker p_i(T)$ is a $T$-[[invariant subspace|0ACX5QT8TE]].

## Remarks

### Why each hypothesis is needed

- The polynomials must be coprime. Take $p = q = t$ and the nilpotent $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$. Then $\ker N^2 = F^2$, but $\ker N + \ker N = F e_1$.
- No finiteness is needed. The lemma holds for any vector space, and even for modules over $F[t]$.

### Consequences

- The [[minimal polynomial criterion|0MPAJRB23T]]: if $(t - \lambda_1) \cdots (t - \lambda_k)$ with distinct $\lambda_i$ kills $T$, then $V$ is the direct sum of the eigenspaces.
- The [[primary decomposition theorem|~81757fe9]]: the factorization of the minimal polynomial into powers of distinct irreducible polynomials splits $V$ into invariant pieces.
- The [[decomposition into generalized eigenspaces|0Z3GDY89T5]] over an algebraically closed field.
- Each projection commutes with every map that commutes with $T$, since it is a polynomial in $T$. So it preserves every $T$-invariant subspace.

### Converse

The converse is false for a single $T$.
For $p = q = t$ and $T = \id_V$, both kernels are $0$, so the sum is direct, although $p$ and $q$ are not coprime.

### Generalizations

The lemma is the Chinese remainder theorem $F[t]/(p q) \cong F[t]/(p) \times F[t]/(q)$, applied to the $F[t]$-module $V$ with $t$ acting as $T$.
It holds in any module $M$ over a principal ideal domain $R$: for coprime $p, q \in R$, the elements killed by $p q$ form the direct sum of those killed by $p$ and by $q$.
In the structure theorem for modules over a principal ideal domain, this gives the decomposition of a torsion module into primary parts.

## History

The name is a translation of the French "lemme des noyaux", which is the usual name in French textbooks.
Hoffman and Kunze prove the general form inside the primary decomposition theorem, Section 6.8.

## Explanations

### L1 human

Suppose a machine $T$ satisfies two separate equations at once, and the equations have nothing in common.
Then every vector splits into one part that satisfies the first equation and one part that satisfies the second.
The split is unique, and it can be computed with polynomials in $T$.

### L2 human

Let $A = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$, $p = t - 1$ and $q = t - 2$.

1. $(p q)(A) = (A - I)(A - 2I) = \begin{pmatrix} 0 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} -1 & 1 \\ 0 & 0 \end{pmatrix} = 0$.
2. Bézout: $p - q = 1$, so $a = 1$ and $b = -1$.
3. The projection onto $\ker(A - I)$ is $(b q)(A) = 2I - A = \begin{pmatrix} 1 & -1 \\ 0 & 0 \end{pmatrix}$, with image $F e_1$.
4. The projection onto $\ker(A - 2I)$ is $(a p)(A) = A - I = \begin{pmatrix} 0 & 1 \\ 0 & 1 \end{pmatrix}$, with image spanned by $(1, 1)$.
5. Their sum is $I$, and $(A - I)^2 = A - I$. So $F^2 = F e_1 \oplus F(1, 1)$, and $(x, y) = (x - y, 0) + (y, y)$.

The typical use is to split $V$ along a factorization of a polynomial that kills $T$.
The trap is to forget coprimality: $\ker T^2$ is not $\ker T \oplus \ker T$.

### L3 human

For an $F[t]$-module $V$, the elements $e_1 = b q$ and $e_2 = a p$ are orthogonal idempotents modulo $p q$.
They act on $\ker (p q)(T)$ as the projections of part 2.
In Lie theory and in the theory of algebraic groups, the same idempotents give the projections onto generalized weight spaces, and they show that the semisimple part of the [[Jordan-Chevalley decomposition|011K11VPJN]] is a polynomial in $T$.
