---
tag: QB1QD9E6VH
kind: proof
name: Proof of the determinant of a triangular matrix by the Leibniz formula
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
proves: 0K1KKMFHYH
methods: [0NTF6DMVAP, 0WCP0PVET6]
uses: [016PE4VZ8Q, 0MKABWDRNC, 0EZSD6T9E0, 0SK90238BH]
sources:
  - url: https://en.wikipedia.org/wiki/Triangular_matrix
    locator: Properties
---

## Proof

We show that every permutation other than the identity picks an entry from the zero side of the diagonal, so that only one term of the Leibniz sum survives.

1. By the [[Leibniz formula|016PE4VZ8Q]],
$$\det A = \sum_{\sigma \in S_n} \sgn(\sigma) \prod_{i=1}^{n} a_{i \sigma(i)}.$$
2. Let $\sigma \in S_n$ with $\sigma(i) \ge i$ for all $i$.
   Since $\sigma$ is a bijection of $\{1, \dots, n\}$, the numbers $\sigma(1), \dots, \sigma(n)$ are $1, \dots, n$ in some order, so $\sum_i \sigma(i) = \sum_i i$.
3. So the numbers $\sigma(i) - i$ are all $\ge 0$ and have sum $0$.
   Hence $\sigma(i) = i$ for all $i$, and $\sigma$ is the identity.
4. In the same way, if $\sigma(i) \le i$ for all $i$, then $\sigma$ is the identity.
5. Let $A$ be [[upper triangular|0MKABWDRNC]], so that $a_{ij} = 0$ for $i > j$, and let $\sigma$ be a permutation other than the identity.
   By steps 2 and 3, some $i$ has $\sigma(i) < i$.
   Then $a_{i \sigma(i)} = 0$, so the term of $\sigma$ in step 1 is $0$.
6. Let $A$ be [[lower triangular|0EZSD6T9E0]], so that $a_{ij} = 0$ for $i < j$, and let $\sigma$ be a permutation other than the identity.
   By step 4, some $i$ has $\sigma(i) > i$.
   Then $a_{i \sigma(i)} = 0$, so the term of $\sigma$ in step 1 is $0$.
7. In both cases only the identity contributes to the sum.
   The identity is a product of zero transpositions, so its [[sign|0SK90238BH]] is $(-1)^0 = 1$.
8. So $\det A = a_{11} a_{22} \cdots a_{nn}$.

## Idea

Each term of the Leibniz formula takes one entry from each row and one from each column.
A permutation other than the identity cannot stay on or above the diagonal everywhere, because the column indices must add up to the same total as the row indices.
So it steps below the diagonal somewhere, and it also steps above it somewhere.
In a triangular matrix one of those entries is zero, and only the diagonal product survives.

## Variants

A second proof uses the [[Laplace expansion|0C08BQ3M05]] and induction on $n$.
In an upper triangular matrix the first column has only the entry $a_{11}$, so expansion along it gives $a_{11}$ times the determinant of a smaller upper triangular matrix.
A lower triangular matrix is handled by expansion along the first row in the same way.

A third proof uses row operations when all $a_{ii}$ are units.
Adding multiples of lower rows clears the entries above the diagonal of an upper triangular matrix, which leaves the diagonal matrix $\operatorname{diag}(a_{11}, \dots, a_{nn})$.
Taking the factor $a_{ii}$ out of each row leaves $I_n$, whose determinant is $1$.
