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

Let $F$ be a field and let $A$ be an $n \times n$ matrix over $F$, with $n \ge 1$.
Assume that the characteristic polynomial of $A$ splits over $F$ as $p_A(t) = (t - \lambda_1) \cdots (t - \lambda_n)$.

1. $\tr A = \lambda_1 + \lambda_2 + \cdots + \lambda_n$.
2. For each $k \ge 1$, $\tr(A^k) = \lambda_1^k + \lambda_2^k + \cdots + \lambda_n^k$.

## Remarks

The $\lambda_i$ are the [[eigenvalues|0BQAA2BK3Q]] of $A$, each repeated according to its [[algebraic multiplicity|0FY42N02DV]].
The hypothesis always holds over $\C$, and over any algebraically closed field.

### Why each hypothesis is needed

- The eigenvalues must be counted with algebraic multiplicity. For $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$, the only eigenvalue is $1$, but the trace is $2 = 1 + 1$.
- The polynomial must split. Over $\R$, $\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$ has $p_A = t^2 - 2t + 2$, no real eigenvalue, and the trace $2$.
- Without a splitting field, the statement holds after extending the field: the roots of $p_A$ in a splitting field sum to $\tr A$.

### Consequences

- The trace of a [[nilpotent matrix|07BSPZPSMF]] is $0$, and over a field of characteristic $0$, $\tr(A^k) = 0$ for all $k \ge 1$ implies that $A$ is nilpotent.
- The trace of an [[idempotent matrix|0KCE8CG86P]] over a field of characteristic $0$ is its rank, because its eigenvalues are $0$ and $1$.
- Over $\C$, $\det(e^A) = e^{\tr A}$, by the proof that the [[determinant of the exponential is the exponential of the trace|W69VC0G18A]].

### Converse

The traces $\tr(A^k)$ for $1 \le k \le n$ determine the eigenvalues with multiplicity over a field of characteristic $0$, by [[Newton's identities|0WG2A3HE0S]].
In characteristic $p$ they do not: the zero matrix and $I_p$ over $\mathbb{F}_p$ have $\tr(A^k) = 0$ for all $k$.

### Generalizations

The same formulas hold for an endomorphism of a finite-dimensional space, with the [[trace of the linear map|0KZDNGA561]].
For trace class operators on a Hilbert space, Lidskii's theorem states that the trace is the sum of the eigenvalues.

## History

The relation is a case of the formulas of Viète, which give the sum of the roots of a monic polynomial as the negative of its second coefficient.

## Explanations

### L1 human

The trace of a square matrix is the sum of its diagonal entries.
The theorem says that it is also the sum of the eigenvalues, each counted as often as it occurs as a root.
For a diagonal matrix this is clear, because the eigenvalues are the diagonal entries.
The theorem says that it stays true for every complex matrix, even when the diagonal entries are not the eigenvalues.

### L2 human

We check the theorem for $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, with eigenvalues $1$ and $3$.

1. $\tr A = 4 = 1 + 3$.
2. $A^2 = \begin{pmatrix} 5 & 4 \\ 4 & 5 \end{pmatrix}$, so $\tr(A^2) = 10 = 1^2 + 3^2$.
3. $A^3 = A^2 A = \begin{pmatrix} 14 & 13 \\ 13 & 14 \end{pmatrix}$, so $\tr(A^3) = 28 = 1^3 + 3^3$.

The typical use is to check computed eigenvalues, or to find a missing eigenvalue from the others and the trace.
A trap: the theorem gives the sum of the eigenvalues, not each eigenvalue.

### L3 human

The trace is the coefficient of $t^{n-1}$ in $p_A$, up to sign, so the theorem is Viète's formula for $p_A$.
The power sum formula says that $\tr(A^k)$ is the $k$-th power sum of the eigenvalues, which links the trace to the [[Newton's identities|0WG2A3HE0S]].
In Mathlib, `Matrix.trace_eq_sum_roots_charpoly` states part 1 over an algebraically closed field, with the multiset of roots of $p_A$.
