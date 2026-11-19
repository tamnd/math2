---
tag: 8A7X3ZSNHB
kind: proof
name: Proof that linear systems are vector equations
proves: E7SAHXQEVC
methods: [41JZ39GE3F, 0NTF6DMVAP]
uses: [0PDVQEP0ZC, 0V8F3E48E6, 0T6MWGZSXA, 0GT4WWGWH2, 0DTY8B9HMS]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_multiplication
    locator: lead section
---

## Proof

Write $A = (a_{ij})$, so that column $j$ is $v_j = (a_{1j}, \dots, a_{mj})^T$.

1. By the definition of the [[matrix-vector product|0PDVQEP0ZC]], entry $i$ of $Ax$ is $\sum_{j=1}^{n} a_{ij} x_j$.
2. Entry $i$ of $x_j v_j$ is $x_j a_{ij}$, by the definition of scalar multiplication in $F^m$.
3. Entry $i$ of $x_1 v_1 + \dots + x_n v_n$ is $\sum_{j=1}^{n} x_j a_{ij}$, by step 2 and entrywise addition.
4. Multiplication in $F$ is commutative, so $x_j a_{ij} = a_{ij} x_j$.
5. By steps 1, 3 and 4, the vectors $Ax$ and $x_1 v_1 + \dots + x_n v_n$ have the same entries.
6. Two vectors in $F^m$ are equal if and only if all their entries are equal.
7. So $Ax = b$ holds if and only if $x_1 v_1 + \dots + x_n v_n = b$, by step 5; this proves (1) $\Leftrightarrow$ (2).
8. Equation $i$ of the [[system|0GT4WWGWH2]] with augmented matrix $[v_1 \; \dots \; v_n \mid b]$ is $a_{i1} x_1 + \dots + a_{in} x_n = b_i$.
9. By step 1, this equation says that entry $i$ of $Ax$ equals $b_i$.
10. So $x$ solves all $m$ equations if and only if $Ax = b$, by step 6; this proves (1) $\Leftrightarrow$ (3).
11. The system is consistent if and only if some $x$ satisfies (2), by step 10 and step 7.
12. That means that $b$ is a [[linear combination|0V8F3E48E6]] of $v_1, \dots, v_n$, which is the definition of $b$ being in their [[span|0DTY8B9HMS]].

## Idea

Write out entry $i$ of each side; all three forms give the same sum $\sum_j a_{ij} x_j$.

## Variants

Over a noncommutative ring, step 4 fails, and the column form must be written with the scalars on the right: $v_1 x_1 + \dots + v_n x_n$.
