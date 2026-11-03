---
tag: G7V6BQSPMW
kind: statement
role: theorem
name: Hawkins–Simon condition
msc: [91B66, 15B48]
uses: [PF15E9SVQV, JPQCCFCY8X, 0BT9BYWVRY, 9V7YQA85PC, 0EB9N0S33C]
about: [PF15E9SVQV]
sources:
  - url: https://en.wikipedia.org/wiki/Hawkins%E2%80%93Simon_condition
same_as:
  wikidata: Q28456162
  wikipedia: Hawkins–Simon condition
---

## Statement

Let $A$ be an $n \times n$ [[nonnegative matrix|JPQCCFCY8X]], the technology matrix of an [[input–output model|PF15E9SVQV]], and let $I$ be the $n \times n$ identity matrix.
The following are equivalent:

1. for every $d \in \R^n_+$ there is $x \in \R^n_+$ with $(I - A) x = d$;
2. every leading principal [[minor|0BT9BYWVRY]] of $I - A$ is positive, that is, for $k = 1, \dots, n$ the determinant of the upper left $k \times k$ submatrix of $I - A$ is positive;
3. the [[spectral radius|9V7YQA85PC]] of $A$ is less than $1$.

When they hold, $I - A$ is [[invertible|0EB9N0S33C]] and $(I - A)^{-1} = \sum_{k \ge 0} A^k$ has nonnegative entries.

## Remarks

The conditions say that $I - A$ is a nonsingular [[M-matrix|DNKXHMGQY1]], and the theorem is part of the list of equivalent characterizations of such matrices.
From 3, the [[Neumann series|8QJ91709V2]] $\sum_k A^k$ converges to $(I - A)^{-1}$, which is then nonnegative, so $x = (I - A)^{-1} d$ gives 1.
From 1, solving with $d$ equal to each unit vector gives a matrix $X \ge 0$ with $(I - A) X = I$.
The [[Perron–Frobenius theorem|62NS7PV1M9]] gives a nonzero row vector $v \ge 0$ with $v A = \rho(A) v$.
Multiplying $(I - A) X = I$ on the left by $v$ gives $(1 - \rho(A)) \, v X = v$, and since $v X \ge 0$ and $v \ne 0$, this forces $\rho(A) < 1$.
The equivalence with 2 is proved by induction on $n$, by eliminating one sector at a time.

Example: for $A = \begin{pmatrix} 0 & 0.1 \\ 0.2 & 0 \end{pmatrix}$, the leading principal minors of $I - A$ are $1$ and $1 - 0.02 = 0.98$, both positive, so every final demand can be produced.
For $A = \begin{pmatrix} 0 & 2 \\ 1 & 0 \end{pmatrix}$ the minors are $1$ and $1 - 2 = -1$, and indeed $d = (1, 1)$ needs the negative outputs $x = (-3, -2)$.

Nonnegativity of $A$ is needed.
For $A = \begin{pmatrix} 0 & -1 \\ 0 & 0 \end{pmatrix}$ the leading principal minors of $I - A$ are $1$ and $1$, but $(I - A)^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$, and $d = (0, 1)$ needs $x = (-1, 1)$.

## Explanations

### L1 human

Each industry uses up some of the products of other industries to make its own.
The economy is viable if it can cover these internal needs and still deliver any basket of final goods to consumers.
Hawkins and Simon found a simple test: a list of determinants built from the input coefficients must all be positive.
If the test fails, some sector uses up more than the system can supply, and some demands cannot be met.

### L2 human

The condition is a test for the productivity of the technology matrix in the [[input–output model|PF15E9SVQV]].
In terms of spectral theory it says $\rho(A) < 1$, so the Leontief inverse $(I - A)^{-1} = I + A + A^2 + \cdots$ exists; the terms of this series count the direct and indirect input requirements, round by round.
The same matrix class, the M-matrices, appears in numerical analysis and in the stability of dynamical systems.
