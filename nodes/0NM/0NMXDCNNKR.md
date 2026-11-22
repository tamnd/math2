---
tag: 0NMXDCNNKR
kind: statement
role: theorem
name: Trace is the sum of the eigenvalues
msc: ["15A15", "15A18"]
topics: [6R1D6QPY3S]
audience: ug2
about: [0XC1RDBY7A, 0BQAA2BK3Q]
uses: [0ZND7NQ970, 0S7A0EMPF4, 07PTPSZPME, 039HF58KQ5]
formal:
  - system: lean4
    library: mathlib
    decl: Matrix.trace_eq_sum_roots_charpoly
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Trace_(linear_algebra)
    locator: Trace as the sum of eigenvalues
  - book: isbn:9780134860244
---

## Statement

The sum of the diagonal entries of a square matrix equals the sum of its eigenvalues, and the same holds for every power of the matrix.
Let $F$ be a field, let $n \ge 1$ and let $A$ be an $n \times n$ matrix over $F$.
Assume that the [[characteristic polynomial|039HF58KQ5]] of $A$ splits over $F$:
$$p_A(t) = (t - \lambda_1)(t - \lambda_2) \cdots (t - \lambda_n), \qquad \lambda_1, \dots, \lambda_n \in F.$$
Then the following hold.

1. $\operatorname{tr} A = \lambda_1 + \lambda_2 + \dots + \lambda_n$.
2. For each $k \ge 1$, $\operatorname{tr}(A^k) = \lambda_1^k + \lambda_2^k + \dots + \lambda_n^k$.

The $\lambda_i$ are the [[eigenvalues|0BQAA2BK3Q]] of $A$, and each appears as often as its [[algebraic multiplicity|0FY42N02DV]].

## Remarks

### A first check

Take $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, the [[symmetric matrix with eigenvalues 1 and 3|Z6K3QPP7DY]].
Its trace is $2 + 2 = 4$, and the eigenvalues add up to $1 + 3 = 4$.
For the squares, multiply out the matrix:
$$A^2 = \begin{pmatrix} 5 & 4 \\ 4 & 5 \end{pmatrix}, \qquad \operatorname{tr}(A^2) = 10 = 1^2 + 3^2.$$
The diagonal entries $2, 2$ are not the eigenvalues, yet their sum is right.
That is the content of the theorem: the trace does not see the eigenvalues one by one, but it sees their sum exactly.

A matrix with no real eigenvalue gives the same picture over $\mathbb{C}$.
The [[real matrix with complex eigenvalues|XGRN8RY29P]] $\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$ has $p_A(t) = (t - 1)^2 + 1 = t^2 - 2t + 2$, with the roots $1 + i$ and $1 - i$.
Their sum is $2$, the trace.

### Why each hypothesis is needed

The eigenvalues must be counted with algebraic multiplicity.
The [[shear|HTAWRAC3QE]] $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has the single eigenvalue $1$, but its trace is $2$.
The sum of the distinct eigenvalues gives $1$, which is wrong; the sum $1 + 1$ with multiplicity is right.

The characteristic polynomial must split, or the sum is not defined in $F$.
Over $\mathbb{R}$, the matrix $\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$ has no eigenvalue at all, while its trace is $2$.
The way out is to pass to a field where $p_A$ splits, such as $\mathbb{C}$.
The trace and $p_A$ do not change when we view $A$ over the larger field, so the roots in a splitting field always add up to $\operatorname{tr} A$.
Over $\mathbb{C}$, and over every algebraically closed field, the hypothesis holds for every matrix.

### What it gives you

The theorem finds a missing eigenvalue.
The [[3 by 3 matrix with 4 on the diagonal and 1 elsewhere|7XFGVVTZ2X]] has trace $12$.
The matrix $A - 3I$ has all entries $1$, so it has rank $1$ and $3$ is an eigenvalue of algebraic multiplicity at least $2$; the vector $(1, 1, 1)$ gives the eigenvalue $6$.
The trace then forces the list $6, 3, 3$, because $12 - 6 - 3 = 3$.

Nilpotent and idempotent matrices are two more uses.
A [[nilpotent matrix|07BSPZPSMF]] has only the eigenvalue $0$, so its trace is $0$.
An [[idempotent matrix|0KCE8CG86P]] has only the eigenvalues $0$ and $1$, and $1$ occurs as often as the rank, so over a field of characteristic $0$ its trace equals its rank.
Over $\mathbb{C}$, the eigenvalues of $e^A$ are the $e^{\lambda_i}$, and this leads to $\det(e^A) = e^{\operatorname{tr} A}$, as in the [[proof for the matrix exponential|W69VC0G18A]].

### The converse

Can the traces of the powers recover the eigenvalues?
Over a field of characteristic $0$, yes: [[Newton's identities|0WG2A3HE0S]] turn the power sums $\operatorname{tr}(A^k)$ for $1 \le k \le n$ into the coefficients of $p_A$, and so into the eigenvalues with multiplicity.
In particular, if $\operatorname{tr}(A^k) = 0$ for all $k \ge 1$, then $p_A = t^n$ and $A$ is nilpotent.
In characteristic $p$ this fails.
Over $\mathbb{F}_p$ the matrices $0$ and $I_p$ both have $\operatorname{tr}(A^k) = 0$ for every $k$, since $\operatorname{tr}(I_p) = p = 0$, but their eigenvalues are $0$ and $1$.

### Generalizations

The same formulas hold for an endomorphism of a finite-dimensional space, with the [[trace of the linear map|0KZDNGA561]], since the trace and the characteristic polynomial do not depend on the basis.
For trace class operators on a Hilbert space, Lidskii's theorem says that the trace is the sum of the eigenvalues, counted with algebraic multiplicity.

## History

The relation is a case of the formulas of Viète, which give the sum of the roots of a monic polynomial as the negative of its second coefficient.
The [[proof by comparing coefficients|92AK0G8APE]] makes this precise.

## Explanations

### L1 human

The trace of a square matrix is the sum of the numbers on its main diagonal.
The theorem says that this sum is also the sum of the eigenvalues, the stretch factors of the matrix.
For the matrix with rows $(2, 1)$ and $(1, 2)$, the diagonal gives $2 + 2 = 4$.
The stretch factors are $1$ and $3$, and they also add up to $4$.
A repeated stretch factor must be counted each time it occurs.

### L2 human

Here is a typical use: check a claimed list of eigenvalues of
$$A = \begin{pmatrix} 3 & 1 & 0 \\ 0 & 2 & 0 \\ 1 & 1 & 1 \end{pmatrix}.$$
Someone claims that the eigenvalues are $1$, $2$ and $3$.
The trace is $3 + 2 + 1 = 6 = 1 + 2 + 3$, so the claim passes the first test.
For a second test, compute the diagonal of $A^2$: row $i$ of $A$ times column $i$ of $A$ gives $9$, $4$ and $0 + 0 + 1 = 1$, so $\operatorname{tr}(A^2) = 14$.
The claim gives $1 + 4 + 9 = 14$, so it passes again.
Expansion of $\det(tI - A)$ along the second row confirms it: $(t - 2)\big((t - 3)(t - 1) - 0\big)$, with the roots $1, 2, 3$.
Watch out: two lists with the same sum can still differ, so the trace alone checks a claim but cannot prove it.

### L3 human

The coefficient of $t^{n-1}$ in $p_A$ is $-\operatorname{tr} A$, so part 1 is Viète's formula for $p_A$.
Part 2 says that $\operatorname{tr}(A^k)$ is the $k$-th power sum of the eigenvalues, and Newton's identities pass between these power sums and the elementary symmetric functions, which are the other coefficients of $p_A$.
In Mathlib, `Matrix.trace_eq_sum_roots_charpoly` states part 1 over an algebraically closed field, with the multiset of roots of $p_A$.
The trace is also the derivative of the determinant at the identity, $\det(I + \varepsilon A) = 1 + \varepsilon \operatorname{tr} A + O(\varepsilon^2)$, and this is the link to Lie algebras that the exponential formula expresses.
