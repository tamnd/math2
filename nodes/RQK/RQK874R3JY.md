---
tag: RQK874R3JY
kind: proof
name: Proof of the Leibniz formula from the defining properties of the determinant
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
proves: 016PE4VZ8Q
methods: [0NTF6DMVAP, 41JZ39GE3F]
uses: [0C3CFHDN6R, 0PPG793642, 0K4VQB7HWR, 09YB3WQG38, 0Z4BWARC38, 05RWFKVTJ7, 06DW9BAWB1]
sources:
  - url: https://en.wikipedia.org/wiki/Leibniz_formula_for_determinants
    locator: Formal statement and proof
---

## Proof

We write each row of $A$ in the standard basis, expand $\det A$ by multilinearity into $n^n$ pieces, and evaluate each piece with the properties from the [[definition of the determinant|0C3CFHDN6R]].

1. Let $e_1, \dots, e_n$ be the rows of the [[identity matrix|06DW9BAWB1]] $I_n$, so that $e_j$ has entry $1$ in place $j$ and $0$ elsewhere.
2. Row $i$ of $A$ is then
$$r_i = \sum_{j=1}^{n} a_{ij} e_j.$$
3. For a map $f \colon \{1, \dots, n\} \to \{1, \dots, n\}$, let $E_f$ be the matrix whose row $i$ is $e_{f(i)}$.
4. Apply [[multilinearity in the rows|0PPG793642]] to the sum of step 2 in row $1$, then in row $2$ of each resulting term, and so on up to row $n$.
   Each choice of one index $j = f(i)$ in every row $i$ gives one term, so
$$\det A = \sum_{f} \Bigl(\prod_{i=1}^{n} a_{i f(i)}\Bigr) \det E_f,$$
   where the sum runs over all $n^n$ maps $f$ of step 3.
5. Suppose that $f$ is not injective, so $f(i) = f(k)$ for some $i \ne k$.
   Then rows $i$ and $k$ of $E_f$ are equal, and $\det E_f = 0$ by the rule for [[equal rows|0K4VQB7HWR]].
6. An injective map from the finite set $\{1, \dots, n\}$ to itself is a bijection.
   So the maps $f$ that remain are exactly the [[permutations|05RWFKVTJ7]] $\sigma \in S_n$.
7. For $\sigma \in S_n$, the matrix $E_\sigma$ is $I_n$ with its rows rearranged by $\sigma$.
   Write $\sigma$ as a product of $t$ transpositions; then $E_\sigma$ arises from $I_n$ by $t$ row swaps.
   Each swap changes the sign of the determinant, by the [[effect of row operations|09YB3WQG38]], so $\det E_\sigma = (-1)^t \det I_n = \operatorname{sgn}(\sigma) \det I_n$.
8. By the [[determinant of the identity|0Z4BWARC38]], $\det I_n = 1$, so $\det E_\sigma = \operatorname{sgn}(\sigma)$.
9. Steps 4 to 8 together give
$$\det A = \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma) \prod_{i=1}^{n} a_{i \sigma(i)}.$$

## Idea

Each row is a combination of the standard rows $e_1, \dots, e_n$, so multilinearity breaks $\det A$ into $n^n$ simple pieces, one for each way to pick a standard row in every position.
A piece that uses some standard row twice has two equal rows and is zero.
The pieces that survive are the identity matrix with its rows shuffled by a permutation, and such a shuffle has determinant equal to the sign of the permutation.
What is left is the Leibniz sum.

## Variants

For $n = 2$ the computation is short enough to write in full.
Multilinearity gives four pieces,
$$\det A = a_{11} a_{21} \det(e_1, e_1) + a_{11} a_{22} \det(e_1, e_2) + a_{12} a_{21} \det(e_2, e_1) + a_{12} a_{22} \det(e_2, e_2),$$
the first and last vanish, and the other two give $a_{11} a_{22} - a_{12} a_{21}$.

The same computation, done for any alternating multilinear function $D$ in place of $\det$, shows $D(A) = D(I_n) \sum_\sigma \operatorname{sgn}(\sigma) \prod_i a_{i \sigma(i)}$.
That is part 2 of the [[existence and uniqueness theorem|1C8RRWHD45]], and with $D = \det$ it gives the formula at once.
