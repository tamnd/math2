---
tag: QXGTCEDC53
kind: proof
name: Proof of the existence and uniqueness of the normalized alternating n-linear form
msc: ["15A15", "15A75"]
topics: [DTBK11SR77]
audience: ug2
proves: 1C8RRWHD45
methods: [0NTF6DMVAP, GQHHNV79PA, 01XM7JEKHY]
uses: [0MSWYWHYF5, 0SDMPMCN43, VJZVSTWYYW, 0SK90238BH, 0JEJJCB0EX, 0FWVRHBRWM, 06DW9BAWB1, 02E1T12PP4]
sources:
  - url: https://en.wikipedia.org/wiki/Leibniz_formula_for_determinants
    locator: Formal statement and proof
---

## Proof

Write $r_1, \dots, r_n$ for the rows of $A$, and $e_1, \dots, e_n$ for the standard basis of $K^n$ written as rows.

**Part 1.**

1. Fix $k$ and $\sigma$. The product $a_{1 \sigma(1)} \cdots a_{n \sigma(n)}$ has exactly one factor from row $k$, namely $a_{k \sigma(k)}$.
2. So, with the other rows fixed, the product is a linear function of $r_k$: it is $a_{k \sigma(k)}$ times a constant.
3. A sum of functions that are linear in $r_k$ is linear in $r_k$. So $L$ is [[multilinear|0SDMPMCN43]] in the rows.
4. Let rows $k$ and $l$ be equal, with $k < l$, and let $\tau$ be the [[transposition|0FWVRHBRWM]] that exchanges $k$ and $l$.
5. The map $\sigma \mapsto \sigma \tau$ is a bijection of $S_n$ onto itself, with inverse $\sigma \mapsto \sigma \tau$.
6. By the [[homomorphism property of the sign|0JEJJCB0EX]], $\sgn(\sigma \tau) = -\sgn(\sigma)$. So the bijection sends the even permutations onto the odd permutations.
7. Compare the products of $\sigma$ and $\sigma \tau$. For $i \notin \set{k, l}$ the factors $a_{i \sigma(i)}$ agree. The factor of $\sigma \tau$ in row $k$ is $a_{k \sigma(l)} = a_{l \sigma(l)}$, and in row $l$ it is $a_{l \sigma(k)} = a_{k \sigma(k)}$, because rows $k$ and $l$ are equal.
8. So the two products are equal, and their signs are opposite. Group the terms of $L(A)$ in the pairs $\set{\sigma, \sigma\tau}$ with $\sigma$ even. Each pair contributes $0$, so $L(A) = 0$ and $L$ is [[alternating|0MSWYWHYF5]].
9. For $A = I_n$, the product $a_{1 \sigma(1)} \cdots a_{n \sigma(n)}$ is $1$ if $\sigma(i) = i$ for all $i$, and $0$ otherwise. So only the identity contributes, with sign $1$, and $L(I_n) = 1$.

**Part 2.** Let $D$ be multilinear and alternating in the rows.

10. Each row is $r_i = \sum_{j=1}^n a_{ij} e_j$.
11. Expand $D(r_1, \dots, r_n)$ by linearity in row $1$, then in row $2$, and so on. This gives
$$D(A) = \sum_{f} a_{1 f(1)} \cdots a_{n f(n)}\, D(e_{f(1)}, \dots, e_{f(n)}),$$
where $f$ runs over all maps $\set{1, \dots, n} \to \set{1, \dots, n}$.
12. If $f$ is not injective, then $e_{f(i)} = e_{f(j)}$ for some $i \neq j$, and $D(e_{f(1)}, \dots, e_{f(n)}) = 0$ because $D$ is alternating.
13. An injective map of a finite set to itself is a bijection, so the remaining $f$ are the permutations $\sigma \in S_n$.
14. By part 2 of the [[antisymmetry theorem|VJZVSTWYYW]], $D(e_{\sigma(1)}, \dots, e_{\sigma(n)}) = \sgn(\sigma)\, D(e_1, \dots, e_n) = \sgn(\sigma)\, D(I_n)$.
15. So $D(A) = D(I_n) \sum_{\sigma} \sgn(\sigma)\, a_{1 \sigma(1)} \cdots a_{n \sigma(n)} = D(I_n)\, L(A)$.

**Part 3.**

16. By part 1, $L$ has the three properties, so such a function exists.
17. If $D$ has the three properties, then $D(A) = 1 \cdot L(A)$ by part 2. So $D = L$.

**Part 4.**

18. Sums and scalar multiples of alternating multilinear forms are alternating multilinear, so these forms make a $K$-module.
19. By part 2, each such form is $D(I_n)\, L$, so $L$ generates the module.
20. If $c L = 0$ for some $c \in K$, then $c = c L(I_n) = 0$ by part 1. So $L$ is a basis, and the module is [[free|02E1T12PP4]] of rank $1$.

## Idea

Multilinearity expands $D(A)$ into $n^n$ terms, one for each choice of a column in each row.
The alternating property kills the terms with a repeated column and turns the others into $\pm D(I_n)$.
What remains is the Leibniz sum, and a direct check shows that this sum has the required properties.

## Variants

Existence can also be proved by induction on $n$ with the expansion along the first row: one checks that the recursive formula is multilinear, alternating and $1$ on $I_n$.
This is the approach of Hoffman and Kunze and of many first courses; it avoids the sign of a permutation but needs more care for the alternating property.
