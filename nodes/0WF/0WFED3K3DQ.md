---
tag: 0WFED3K3DQ
kind: statement
role: theorem
name: Sylvester's law of inertia
msc: [15A63, "11E04"]
topics: [6TSCEW8QMK]
audience: ug1
about: [0RBQS1JJCR]
uses: [0N28QN4CYA, 0SPYAGE7T0, 0HZNE5QZDJ, 0Z3FEWZ8HA, NZJDNC6EP6]
proofs: [RDKYJR8P1R]
formal:
  - system: lean4
    library: mathlib
    decl: QuadraticForm.equivalent_signType_weighted_sum_squared
    match: weaker
sources:
  - url: https://en.wikipedia.org/wiki/Sylvester's_law_of_inertia
    locator: Statement
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Real quadratic forms
  - book: isbn:9780134860244
same_as:
  wikidata: Q1752621
  wikipedia: Sylvester's law of inertia
---

## Statement

1. Let $A$ be a real [[symmetric|0N28QN4CYA]] $n \times n$ matrix. Let $P$ and $P'$ be invertible real $n \times n$ matrices such that $D = P^T A P$ and $D' = P'^T A P'$ are diagonal. Then $D$ and $D'$ have the same numbers $p$, $q$ and $r$ of positive, negative and zero diagonal entries.
2. Let $Q$ be a [[quadratic form|0HZNE5QZDJ]] on a real vector space $V$ of dimension $n$. Then $V$ has a basis in which
$$Q(x_1, \dots, x_n) = x_1^2 + \cdots + x_p^2 - x_{p+1}^2 - \cdots - x_{p+q}^2,$$
   where $p$ and $q$ are the numbers of part 1 for the matrix of $Q$ in any basis.
3. Two real symmetric $n \times n$ matrices are [[congruent|NZJDNC6EP6]] if and only if they have the same $p$ and the same $q$. So two real quadratic forms on $V$ are equivalent if and only if they have the same $p$ and $q$.

## Remarks

### Why each hypothesis is needed

- The field must be ordered, so that "positive" has a meaning. Over $\C$, the forms $x^2$ and $-x^2$ are equivalent through $x \mapsto ix$, so only the rank is an invariant; see [[the complex classification|0CEX9BRXRZ]].
- Over $\Q$, part 1 still holds, since $\Q \subset \R$. But part 3 fails: $x^2$ and $2x^2$ both have $p = 1$ and $q = 0$. They are not equivalent over $\Q$, since $2$ is not the square of a rational number.
- Part 1 is about [[congruence|NZJDNC6EP6]] $P^T A P$, which is the change of basis rule for forms. Similarity $P^{-1} A P$ is the change of basis rule for linear maps, a different question.

### Consequences

- The triple $(p, q, r)$ is the [[signature|07EZA80NEH]] of $Q$, and $p + q$ is its rank.
- $p$ is the largest dimension of a subspace on which $Q$ is [[positive definite|0RP20HFYM3]]. The proof shows this directly.
- By [[the principal axis theorem|0PR5P9Z4KM]], $p$, $q$ and $r$ are the numbers of positive, negative and zero eigenvalues of $A$, counted with multiplicity.
- Over $\R$, there are exactly $(n + 1)(n + 2)/2$ equivalence classes of quadratic forms in $n$ variables, one for each pair $(p, q)$ with $p + q \le n$.

### Converse

Part 3 contains the converse: matrices with the same $p$ and $q$ are congruent, because both are congruent to the normal form of part 2.

### Generalizations

- The same statement and proof hold for Hermitian matrices, with $P^* A P$ in place of $P^T A P$. Wikipedia states this version in its section on generalizations.
- The proof by subspaces uses only the order of $\R$, so part 1 holds over every ordered field. Part 2 needs square roots of positive elements, as in $\R$.

## History

According to Wikipedia, the law is named after Sylvester, who published its proof in 1852.

## Explanations

### L1 human

A real quadratic form can be written as a sum of squares in many ways.
The numbers of plus signs and minus signs are always the same.
For example, $x^2 + 2xy = (x + y)^2 - y^2$ has one plus sign and one minus sign.
Another way, $x^2 + 2xy = 2(x + \frac y2)^2 - x^2 - \frac{y^2}2$, would give three squares, but it uses three expressions for two variables, so it is not a change of variables.

### L2 human

Worked example: we write $Q = 2xy$ in two ways.

1. With $x = s + t$, $y = s - t$: $Q = 2s^2 - 2t^2$.
2. With $x = u + 3v$, $y = u - \frac v3$: $Q = 2u^2 + \frac{16}{3} uv - 2v^2$. This one is not diagonal, so complete the square: $Q = 2(u + \frac43 v)^2 - \frac{50}{9} v^2$.
3. Both have one positive and one negative coefficient. The law says that no change of variables gives two positive ones.

A trap: the diagonal entries of a non-diagonal symmetric matrix do not show the signature; see [[the example with $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$|~26da1679]].

### L3 human

Part 3 says that the Witt group of $\R$ is $\Z$, with the class of a nondegenerate form sent to $p - q$.
Over an ordered field the map $\langle a_1, \dots, a_n \rangle \mapsto \#\set{i : a_i > 0} - \#\set{i : a_i < 0}$ is the signature homomorphism.
For indefinite forms, the group of linear maps that keep $Q$ is the [[indefinite orthogonal group|M2900DMEW6]] $O(p, q)$.
