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

1. Let $A$ be a real [[symmetric|0N28QN4CYA]] $n \times n$ matrix.
   Let $P$ and $P'$ be invertible real $n \times n$ matrices such that $D = P^{\mathsf{T}} A P$ and $D' = P'^{\mathsf{T}} A P'$ are diagonal.
   Then $D$ and $D'$ have the same numbers $p$, $q$ and $r$ of positive, negative and zero diagonal entries.
2. Let $Q$ be a [[quadratic form|0HZNE5QZDJ]] on a real vector space $V$ of finite dimension $n$.
   Then $V$ has a basis in which
   $$Q(x_1, \dots, x_n) = x_1^2 + \cdots + x_p^2 - x_{p+1}^2 - \cdots - x_{p+q}^2,$$
   where $p$ and $q$ are the numbers of part 1 for the matrix of $Q$ in any basis.
3. Two real symmetric $n \times n$ matrices are [[congruent|NZJDNC6EP6]] if and only if they have the same $p$ and the same $q$.
   So two real quadratic forms on $V$ are equivalent if and only if they have the same $p$ and $q$.

## Remarks

### The idea on one example

A real quadratic form can be written as a sum of squares in many ways, but the number of plus signs and the number of minus signs never change.
Take $Q(x, y) = 2xy$.
The substitution $x = s + t$, $y = s - t$ gives $Q = 2s^2 - 2t^2$.
The substitution $x = u + 3v$, $y = u - \tfrac{1}{3} v$ gives $Q = 2u^2 + \tfrac{16}{3} uv - 2v^2$, and completing the square gives
$$Q = 2\Bigl(u + \frac{4}{3} v\Bigr)^2 - \frac{50}{9} v^2.$$
Check: $2\bigl(u^2 + \tfrac{8}{3} uv + \tfrac{16}{9} v^2\bigr) - \tfrac{50}{9} v^2 = 2u^2 + \tfrac{16}{3} uv - 2v^2$.
The coefficients $2, -2$ and $2, -\tfrac{50}{9}$ differ, but each pair has one positive and one negative entry.
The law says that no invertible change of variables turns $2xy$ into a sum of two positive squares.
This is clear here, since $2xy$ takes negative values, but for forms in many variables the law is the only easy way to see it.

### Why each hypothesis is needed

The field must be ordered, so that "positive" has a meaning.
Over $\mathbb{C}$ the forms $x^2$ and $-x^2$ are equivalent through $x \mapsto ix$, so only the rank $p + q$ is an invariant; see [[the complex classification|0CEX9BRXRZ]].

Part 3 also needs square roots of positive numbers.
Over $\mathbb{Q}$, part 1 still holds, because a rational matrix is a real matrix.
But part 3 fails over $\mathbb{Q}$: the forms $x^2$ and $2x^2$ both have $p = 1$ and $q = 0$, and they are not equivalent over $\mathbb{Q}$, because $2$ is not the square of a rational number.

Part 1 is about [[congruence|NZJDNC6EP6]] $P^{\mathsf{T}} A P$, which is the change of basis rule for forms.
Similarity $P^{-1} A P$ is the change of basis rule for linear maps, and it is a different question with different invariants.

### What it gives you

The triple $(p, q, r)$ is the [[signature|07EZA80NEH]] of $Q$, and $p + q$ is its rank.
The proof shows that $p$ is the largest dimension of a subspace on which $Q$ is [[positive definite|0RP20HFYM3]], so $p$ has a meaning that needs no basis at all.
By [[the principal axis theorem|0PR5P9Z4KM]], $p$, $q$ and $r$ are also the numbers of positive, negative and zero eigenvalues of $A$, counted with multiplicity.

Part 3 is a complete classification.
Over $\mathbb{R}$ there are exactly $(n + 1)(n + 2)/2$ equivalence classes of quadratic forms in $n$ variables, one for each pair $(p, q)$ with $p + q \le n$.
For $n = 2$ this gives $6$ classes, with normal forms $0$, $x^2$, $-x^2$, $x^2 + y^2$, $x^2 - y^2$ and $-x^2 - y^2$.

Part 3 contains its own converse.
Matrices with the same $p$ and $q$ are congruent, because both are congruent to the normal form of part 2.

### Other settings

The same statement and proof hold for complex Hermitian matrices, with $P^* A P$ in place of $P^{\mathsf{T}} A P$.
The proof by subspaces uses only the order of $\mathbb{R}$, so part 1 holds over every ordered field.
Parts 2 and 3 also need a square root of each positive element, as in $\mathbb{R}$.

### Watch out

The diagonal entries of a symmetric matrix that is not diagonal do not show its signature.
The matrix $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ has positive diagonal entries, but its form $x^2 + 4xy + y^2$ is $-2$ at $(1, -1)$; see [[this example|WE1ZY9FZJG]].
Diagonalize first, by completing squares or by eigenvalues, and only then count signs.

### Try it

Write $Q(x, y) = x^2 + 2xy$ as a combination of squares of two independent linear forms, and find $p$ and $q$.
One answer is $(x + y)^2 - y^2$, so $p = 1$ and $q = 1$.
The expression $2(x + \tfrac{1}{2} y)^2 - x^2 - \tfrac{1}{2} y^2$ is also equal to $Q$, but it uses three linear forms in two variables, so it does not come from a change of variables, and the law says nothing about it.

## History

The law is named after James Joseph Sylvester, who published a proof in 1852.

## Explanations

### L1 human

A real quadratic form can be written as a sum of squares with coefficients in many ways.
The coefficients change, but the number of positive ones and the number of negative ones stay the same.
For example, $2xy = 2s^2 - 2t^2$ in one set of variables and $2w^2 - \tfrac{50}{9} v^2$ in another, with $w = u + \tfrac{4}{3} v$ as in the example above.
Both have one plus sign and one minus sign.

### L2 human

To find $p$ and $q$ by hand, complete squares until no cross terms are left, as in [[the diagonalization theorem|0Z3FEWZ8HA]], and count the signs of the coefficients.
The law guarantees that every correct way of doing this gives the same count.
Watch out: the law counts signs, not values, so a diagonal form $2x^2 - 3y^2$ is equivalent to $x^2 - y^2$ over $\mathbb{R}$.

### L3 human

Part 3 says that the Witt group of $\mathbb{R}$ is isomorphic to $\mathbb{Z}$, through the map that sends the class of a nondegenerate form to $p - q$; see [[the Witt group|KFVY0RPGF2]].
Over an ordered field the map $\langle a_1, \dots, a_n \rangle \mapsto \#\{ i : a_i > 0 \} - \#\{ i : a_i < 0 \}$ is the signature homomorphism on the Witt group.
For a nondegenerate indefinite form, the group of linear maps that keep $Q$ is the [[indefinite orthogonal group|M2900DMEW6]] $O(p, q)$.
