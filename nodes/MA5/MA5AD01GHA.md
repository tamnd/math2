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

We expand the value of the form on a sum for parts 1 and 2, use $-1 = 1$ for part 3, and write the value $B(v, v)$ in coordinates for part 4.

Part 1.

1. Let $u, v \in V$. Bilinearity in each slot gives
$$B(u + v, u + v) = B(u, u) + B(u, v) + B(v, u) + B(v, v).$$
2. The form $B$ is [[alternating|08ZQAKBKHF]], so $B(u + v, u + v)$, $B(u, u)$ and $B(v, v)$ are all $0$.
3. Step 1 becomes $0 = B(u, v) + B(v, u)$, so $B(u, v) = -B(v, u)$, and $B$ is skew-symmetric.

Part 2.

4. Let $v \in V$. Skew-symmetry with $u = v$ gives $B(v, v) = -B(v, v)$, so $2B(v, v) = 0$.
5. The [[characteristic|1ZB13N78XW]] of $F$ is not $2$, so $2 = 1 + 1 \ne 0$ in $F$, and $2$ has an inverse in the field $F$.
6. Multiplying the equation of step 4 by $2^{-1}$ gives $B(v, v) = 0$. This holds for every $v$, so $B$ is alternating.

Part 3.

7. In characteristic $2$ we have $1 + 1 = 0$, so $-1 = 1$ and $-c = c$ for every $c \in F$.
8. So for all $u, v$ the condition $B(u, v) = -B(v, u)$ is the same as $B(u, v) = B(v, u)$, and skew-symmetry is symmetry.

Part 4.

9. Suppose that $B$ is alternating. By the definition of the [[matrix|0P24YW565F]], $A_{ii} = B(e_i, e_i) = 0$.
10. By part 1, $A_{ji} = B(e_j, e_i) = -B(e_i, e_j) = -A_{ij}$ for all $i, j$, so $A^{\mathsf{T}} = -A$.
11. Conversely, suppose that $A^{\mathsf{T}} = -A$ and $A_{ii} = 0$ for all $i$. Let $v$ have the coordinate column $x$.
12. By the [[correspondence theorem|ZVMJAF7D53]], $B(v, v) = x^{\mathsf{T}} A x$. Group the terms with indices $(i, j)$ and $(j, i)$:
$$x^{\mathsf{T}} A x = \sum_{i} A_{ii} x_i^2 + \sum_{i < j} (A_{ij} + A_{ji})\, x_i x_j.$$
13. Each $A_{ii}$ is $0$ by hypothesis, and each $A_{ij} + A_{ji}$ is $0$ because $A_{ji} = -A_{ij}$. So $B(v, v) = 0$ for every $v$, and $B$ is alternating.

This proves all four parts.

## Idea

The value of a form on a sum $u + v$ contains two mixed terms, $B(u, v)$ and $B(v, u)$.
If every value on equal vectors is zero, the mixed terms must cancel, and that cancellation is skew-symmetry.
Going back needs a division by $2$, so it breaks down exactly when $1 + 1 = 0$.
The matrix test separates the same two kinds of terms: the diagonal entries are the values $B(e_i, e_i)$, and the pairs off the diagonal are the mixed terms.

## Variants

Part 2 also follows from part 4.
Outside characteristic $2$, the condition $A^{\mathsf{T}} = -A$ gives $A_{ii} = -A_{ii}$, so $2A_{ii} = 0$ and $A_{ii} = 0$, and part 4 then shows that $B$ is alternating.
This route needs a finite basis, while the argument of steps 4 to 6 works in every dimension.
