---
tag: 0BNEXSKNRV
kind: definition
name: Polynomial of an endomorphism
msc: ["15A04", "15A54"]
topics: [6R1D6QPY3S]
audience: ug2
defines: 0E3MV6E6MG
uses: [0PTF1PTJK0]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_polynomial
    locator: lead section
  - book: isbn:9783031410253
    locator: Chapter 5
---

## Definition

We define what it means to substitute a linear map, or a square matrix, into a polynomial.

Let $F$ be a field, let $V$ be a vector space over $F$, and let $T \colon V \to V$ be an [[endomorphism|0PTF1PTJK0]].
Let $p(x) = c_0 + c_1 x + \dots + c_d x^d$ be a polynomial in $F[x]$.
The *value of $p$ at $T$* is the endomorphism
$$p(T) = c_0 \operatorname{id}_V + c_1 T + c_2 T^2 + \dots + c_d T^d,$$
where $T^0 = \operatorname{id}_V$ and $T^k = T \circ T^{k-1}$ for $k \ge 1$.
For an $n \times n$ matrix $A$ over $F$, the value is $p(A) = c_0 I_n + c_1 A + \dots + c_d A^d$, with matrix powers.
The set $\{ p(T) : p \in F[x] \}$ is written $F[T]$.

## Notation

Mathlib writes `Polynomial.aeval T p` for $p(T)$.
Some books write $p[T]$, and most state the convention $T^0 = I$ once and then use it silently.

## Remarks

Each part of the definition has a job.
The power $T^k$ is a composite, so for matrices it is the matrix product $A \cdot A \cdots A$ and not a power of the entries.
The convention $T^0 = \operatorname{id}_V$ turns the constant $c_0$ into the map $c_0 \operatorname{id}_V$, which is what makes $p(T)$ an endomorphism.
Without it, $c_0 + c_1 T$ would add a scalar to a map.

With these choices, the map $p \mapsto p(T)$ is a homomorphism of $F$-algebras from $F[x]$ to $\operatorname{End}_F(V)$.
It keeps sums and scalar multiples term by term, and it keeps products because $T^j T^k = T^{j+k}$ and composition distributes over sums.
So $(pq)(T) = p(T)q(T)$ and $1(T) = \operatorname{id}_V$, and any two polynomials in $T$ commute, which makes $F[T]$ a commutative subalgebra of $\operatorname{End}_F(V)$.
If $Tv = \lambda v$, then $T^k v = \lambda^k v$ by induction on $k$, so $p(T)v = p(\lambda)v$.
For matrices, $p(SAS^{-1}) = S\,p(A)\,S^{-1}$, because $(SAS^{-1})^k = SA^kS^{-1}$.

For a small example, take $A = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}$ and $p(x) = x^2 - x - 1$.
Then $A^2 = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$, and
$$p(A) = A^2 - A - I = \begin{pmatrix} 1 - 0 - 1 & 1 - 1 - 0 \\ 1 - 1 - 0 & 2 - 1 - 1 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}.$$
This $p$ is the characteristic polynomial of $A$, since $\operatorname{tr} A = 1$ and $\det A = -1$.
A case that misses the definition is the entrywise rule: squaring each entry of $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ gives the matrix back, while the value of $x^2$ at it is the zero matrix.
The concept page on [[polynomials of an endomorphism|0E3MV6E6MG]] develops the rules and the eigenvalues of $p(T)$.

## Explanations

### L1 human

You can put a matrix into a polynomial, because matrices can be added, scaled and multiplied.
The constant term becomes a multiple of the identity matrix.
For example, $p(x) = x^2 - 3x + 2$ gives $p(A) = A^2 - 3A + 2I$.
The power $A^2$ means $A$ times $A$, not each entry squared.

### L2 human

Here is a check with the matrix $A = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}$ above and $q(x) = x^3$.
Multiply $A^2$ by $A$:
$$A^3 = \begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix}.$$
Since $A^2 = A + I$, we also get $A^3 = A \cdot A^2 = A^2 + A = 2A + I$, and indeed $2A + I = \begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix}$.
The entries $1, 2, 3$ are Fibonacci numbers, and the same reduction gives every power of $A$ as a combination of $A$ and $I$.
Watch out: the constant $-1$ in $p$ becomes $-I$, not the number $-1$.
