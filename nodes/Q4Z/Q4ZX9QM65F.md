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

We follow $e_1$ through the basis to get part 1, show that $p$ is the shortest polynomial that kills $C$, and then get the characteristic polynomial from divisibility and degree.

1. By the [[definition of $C$|0VH1TC1PWF]], column $i$ of $C$ is $e_{i+1}$ for $i < n$, and column $n$ is $-c_0 e_1 - c_1 e_2 - \cdots - c_{n-1} e_n$. So $C e_i = e_{i+1}$ for $i < n$.
2. We prove $C^{i-1} e_1 = e_i$ for $1 \le i \le n$ by induction on $i$. The case $i = 1$ is $C^0 e_1 = e_1$, and if $C^{i-1} e_1 = e_i$ with $i < n$, then $C^i e_1 = C e_i = e_{i+1}$ by step 1. This proves part 1.
3. Let $f = a_0 + a_1 x + \cdots + a_{n-1} x^{n-1}$ be a nonzero polynomial of degree less than $n$. By step 2, $f(C) e_1 = a_0 e_1 + a_1 e_2 + \cdots + a_{n-1} e_n$, and this vector is nonzero because some $a_i \ne 0$.
4. So no nonzero polynomial of degree less than $n$ annihilates $C$, and hence $\deg m_C \ge n$.
5. Now apply $p$ to $e_1$. By step 2, $p(C) e_1 = C^n e_1 + \sum_{i=0}^{n-1} c_i C^i e_1 = C e_n + \sum_{i=0}^{n-1} c_i e_{i+1}$.
6. By the last column of $C$, $C e_n = -\sum_{i=0}^{n-1} c_i e_{i+1}$, so $p(C) e_1 = 0$.
7. For each $j$, $p(C) e_j = p(C) C^{j-1} e_1 = C^{j-1} p(C) e_1 = 0$, because [[polynomials in $C$|0E3MV6E6MG]] commute with each other. So $p(C) = 0$.
8. By the [[divisibility property of the minimal polynomial|0VTAD25A3G]], $m_C$ divides $p$.
9. By steps 4 and 8, $m_C$ is a monic divisor of $p$ of degree at least $n = \deg p$, so $m_C = p$. This proves part 2.
10. The characteristic polynomial $\chi_C = \det(xI - C)$ is monic of degree $n$.
11. By the theorem that [[the minimal polynomial divides the characteristic polynomial|093X6MN6Y6]], $p = m_C$ divides $\chi_C$.
12. Both are monic of degree $n$, so $\chi_C = p$. This proves part 3.
13. For the row version, $\det(xI - C^{\mathsf T}) = \det((xI - C)^{\mathsf T}) = \det(xI - C)$ by the [[rule for the determinant of a transpose|0ZZQ2E1MTE]].
14. Also $f(C^{\mathsf T}) = f(C)^{\mathsf T}$ for every polynomial $f$, so $f(C^{\mathsf T}) = 0$ exactly when $f(C) = 0$. Hence $C^{\mathsf T}$ has the same minimal polynomial $p$.

## Idea

The vector $e_1$ walks through the whole basis under $C$, so a polynomial of degree below $n$ cannot kill even $e_1$.
The last column is built so that $p$ kills $e_1$, and then $p$ kills every $e_j = C^{j-1} e_1$ as well.
So $p$ is the minimal polynomial, and the characteristic polynomial, which is a monic multiple of degree $n$, must be $p$ too.

## Variants

A direct proof of part 3 expands $\det(xI - C)$ along the last column.
That column is $(c_0, c_1, \dots, c_{n-2}, x + c_{n-1})$, and each minor along it is the determinant of a block triangular matrix.
With its sign and its minor, the entry $c_{i-1}$ in row $i < n$ contributes $c_{i-1} x^{i-1}$, and the last entry contributes $(x + c_{n-1}) x^{n-1}$.
Another direct proof uses induction on $n$ and expands along the first row.
These direct proofs work over every commutative ring, where the argument with the minimal polynomial is not available.
