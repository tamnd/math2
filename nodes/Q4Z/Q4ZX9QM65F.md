---
tag: Q4ZX9QM65F
kind: proof
name: Proof of the characteristic and minimal polynomial of a companion matrix
msc: ["15A21", "15A18"]
topics: [GEBYZKYV3D]
audience: ug2
proves: XYR7GPH20K
methods: [0NTF6DMVAP, 0ASJVEFA9J]
uses: [0VH1TC1PWF, 03NDVCSHSB, 0VTAD25A3G, 093X6MN6Y6, 039HF58KQ5, 0ZZQ2E1MTE, 0E3MV6E6MG]
sources:
  - url: https://en.wikipedia.org/wiki/Companion_matrix
    locator: lead section
---

## Proof

1. By the [[definition of $C$|0VH1TC1PWF]], column $i$ of $C$ is $e_{i+1}$ for $i < n$, and column $n$ is $-c_0 e_1 - c_1 e_2 - \cdots - c_{n-1} e_n$. So $C e_i = e_{i+1}$ for $i < n$.
2. By induction on $i$, $C^{i-1} e_1 = e_i$ for $1 \le i \le n$: the case $i = 1$ is $C^0 e_1 = e_1$, and $C^{i} e_1 = C e_i = e_{i+1}$ for $i < n$ by step 1. This proves part 1.
3. Let $f = a_0 + a_1 x + \cdots + a_{n-1} x^{n-1}$ be nonzero, of degree less than $n$. By step 2, $f(C) e_1 = a_0 e_1 + a_1 e_2 + \cdots + a_{n-1} e_n$, which is nonzero.
4. So no nonzero polynomial of degree less than $n$ annihilates $C$. Hence $\deg m_C \ge n$.
5. By steps 1 and 2, $p(C) e_1 = C^n e_1 + \sum_{i=0}^{n-1} c_i C^i e_1 = C e_n + \sum_{i=0}^{n-1} c_i e_{i+1}$.
6. By step 1, $C e_n = -\sum_{i=0}^{n-1} c_i e_{i+1}$. So $p(C) e_1 = 0$.
7. For each $j$, $p(C) e_j = p(C) C^{j-1} e_1 = C^{j-1} p(C) e_1 = 0$, since [[polynomials in $C$|0E3MV6E6MG]] commute with each other. So $p(C) = 0$.
8. By the [[divisibility property of the minimal polynomial|0VTAD25A3G]], $m_C$ divides $p$.
9. By steps 4 and 8, $m_C$ is a monic divisor of $p$ of degree at least $n = \deg p$. So $m_C = p$. This proves part 2.
10. The characteristic polynomial $\chi_C = \det(xI - C)$ is monic of degree $n$.
11. By the theorem that [[the minimal polynomial divides the characteristic polynomial|093X6MN6Y6]], $p = m_C$ divides $\chi_C$.
12. Both are monic of degree $n$, so $\chi_C = p$. This proves part 3.
13. For the row version: $\det(xI - C^{\mathsf T}) = \det((xI - C)^{\mathsf T}) = \det(xI - C)$ by the [[rule for the determinant of a transpose|0ZZQ2E1MTE]].
14. Also $f(C^{\mathsf T}) = f(C)^{\mathsf T}$ for every $f$, so $f(C^{\mathsf T}) = 0$ if and only if $f(C) = 0$. Hence $C^{\mathsf T}$ has the same minimal polynomial $p$.

## Idea

The vector $e_1$ is cyclic, since $C$ moves $e_1$ through all basis vectors.
So no polynomial of degree below $n$ kills $C$, while the last column is built so that $p$ kills $e_1$ and hence $C$.
The characteristic polynomial is then forced by the Cayley-Hamilton divisibility and the degree.

## Variants

A direct proof of part 3 expands $\det(xI - C)$ along the last column, or uses induction on $n$ with expansion along the first row.
The minors along the last column are triangular, and the expansion gives $x^n + c_{n-1} x^{n-1} + \cdots + c_0$.
This direct proof works over every commutative ring.
