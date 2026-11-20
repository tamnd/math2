---
tag: MA5AD01GHA
kind: proof
name: Proof of the relation between alternating and skew-symmetric bilinear forms
msc: ["15A63"]
topics: [DYAK7YMK7B]
audience: ug1
proves: SX9CD5NEPD
methods: [0NTF6DMVAP, TFQ1845T84]
uses: [08ZQAKBKHF, 0P24YW565F, 1ZB13N78XW, ZVMJAF7D53]
sources:
  - url: https://en.wikipedia.org/wiki/Bilinear_form
    locator: Symmetric, skew-symmetric, and alternating forms
---

## Proof

Part 1.

1. Let $u, v \in V$. Bilinearity gives $B(u + v, u + v) = B(u, u) + B(u, v) + B(v, u) + B(v, v)$.
2. $B$ is [[alternating|08ZQAKBKHF]], so $B(u + v, u + v) = 0$, $B(u, u) = 0$ and $B(v, v) = 0$.
3. Step 1 becomes $0 = B(u, v) + B(v, u)$. So $B(u, v) = -B(v, u)$, and $B$ is skew-symmetric.

Part 2.

4. Let $v \in V$. Skew-symmetry with $u = v$ gives $B(v, v) = -B(v, v)$, so $2B(v, v) = 0$.
5. The [[characteristic|1ZB13N78XW]] of $F$ is not $2$, so $2 \neq 0$ in $F$, and $2$ has an inverse in the field $F$.
6. Multiply step 4 by $2^{-1}$. This gives $B(v, v) = 0$, so $B$ is alternating.

Part 3.

7. In characteristic $2$, $1 + 1 = 0$, so $-1 = 1$ and $-c = c$ for every $c \in F$.
8. So the condition $B(u, v) = -B(v, u)$ is the same as $B(u, v) = B(v, u)$.

Part 4.

9. Suppose that $B$ is alternating. By the definition of the [[matrix|0P24YW565F]], $A_{ii} = B(e_i, e_i) = 0$.
10. By part 1, $A_{ji} = B(e_j, e_i) = -B(e_i, e_j) = -A_{ij}$. So $A^T = -A$.
11. Conversely, suppose that $A^T = -A$ and $A_{ii} = 0$ for all $i$. Let $v$ have the coordinate vector $x$.
12. By the [[correspondence theorem|ZVMJAF7D53]], $B(v, v) = x^T A x = \sum_i A_{ii} x_i^2 + \sum_{i < j} (A_{ij} + A_{ji}) x_i x_j$. Here we group the terms $(i, j)$ and $(j, i)$ together.
13. Each $A_{ii}$ is $0$, and each $A_{ij} + A_{ji}$ is $0$ because $A_{ji} = -A_{ij}$. So $B(v, v) = 0$, and $B$ is alternating.

This proves all four parts.

## Idea

The value of a form on $u + v$ contains the two mixed terms $B(u, v)$ and $B(v, u)$.
If all values on equal vectors are zero, the mixed terms cancel, which is skew-symmetry.
In the other direction we must divide by $2$, and this fails in characteristic $2$.
The matrix test separates the diagonal terms from the mixed terms in the same way.

## Variants

Part 2 also follows from part 4: outside characteristic $2$, $A^T = -A$ gives $A_{ii} = -A_{ii}$, so $2A_{ii} = 0$ and $A_{ii} = 0$.
