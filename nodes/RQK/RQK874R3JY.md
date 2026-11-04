---
tag: RQK874R3JY
kind: proof
name: Proof of the Leibniz formula from the defining properties of the determinant
msc: [15A15]
proves: 016PE4VZ8Q
uses: [0C3CFHDN6R, 0PPG793642, 0K4VQB7HWR, 09YB3WQG38, 0Z4BWARC38, 05RWFKVTJ7, 06DW9BAWB1]
sources:
  - url: https://en.wikipedia.org/wiki/Leibniz_formula_for_determinants
    locator: Formal statement and proof
---

## Proof

We expand each row in the standard basis and use the properties from the [[definition of the determinant|0C3CFHDN6R]].

1. Let $e_1, \dots, e_n$ be the rows of the [[identity matrix|06DW9BAWB1]] $I_n$. So $e_j$ has entry $1$ in place $j$ and $0$ elsewhere.
2. Row $i$ of $A$ is $\sum_{j=1}^{n} a_{ij} e_j$.
3. For a map $f \colon \set{1, \dots, n} \to \set{1, \dots, n}$, let $E_f$ be the matrix whose row $i$ is $e_{f(i)}$.
4. Apply [[multilinearity|0PPG793642]] in row $1$ to the sum of step 2. Then apply it in row $2$ to each resulting term, and so on up to row $n$.
5. This gives $\det A = \sum_{f} \left(\prod_{i=1}^{n} a_{i, f(i)}\right) \det E_f$. The sum runs over all $n^n$ maps $f$ of step 3.
6. If $f$ is not injective, then $f(i) = f(k)$ for some $i \ne k$. Then rows $i$ and $k$ of $E_f$ are equal, so $\det E_f = 0$ by the rule for [[two equal rows|0K4VQB7HWR]].
7. An injective map from the finite set $\set{1, \dots, n}$ to itself is a bijection. So the remaining maps $f$ are exactly the [[permutations|05RWFKVTJ7]] $\sigma \in S_n$.
8. For $\sigma \in S_n$, row $i$ of $E_\sigma$ is row $\sigma(i)$ of $I_n$. By the rule for [[permuting rows|09YB3WQG38]], $\det E_\sigma = \sgn(\sigma) \det I_n$.
9. By the [[determinant of the identity|0Z4BWARC38]], $\det I_n = 1$. So $\det E_\sigma = \sgn(\sigma)$.
10. Putting steps 5 to 9 together, $\det A = \sum_{\sigma \in S_n} \sgn(\sigma) \prod_{i=1}^{n} a_{i, \sigma(i)}$.

## Idea

Each row is a combination of the standard rows, so multilinearity breaks $\det A$ into $n^n$ simple pieces. A piece with a repeated standard row is zero. The others are row permutations of the identity, whose determinant is the sign of the permutation.
