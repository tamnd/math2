---
tag: 5AW92FEEXJ
kind: proof
name: Proof that the composite of linear maps is linear
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
proves: FSXBBV9C76
methods: [0NTF6DMVAP, 41JZ39GE3F]
uses: [05YBKMRVAR, 0RJF668P1T, 0CCQV3884B, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Definition and first consequences
  - book: isbn:9780134860244
    locator: Section 2.3
---

## Proof

We pass sums and scalars through $S$ and then through $T$ for part 1, and for part 2 we compare the columns of $AB$ with the images of the columns of $B$.

1. Let $u_1, u_2 \in U$; by the [[definition of the composite|05YBKMRVAR]], $(T \circ S)(u_1 + u_2) = T(S(u_1 + u_2))$.
2. Since $S$ is additive, $S(u_1 + u_2) = S(u_1) + S(u_2)$.
3. Since $T$ is additive, $T(S(u_1) + S(u_2)) = T(S(u_1)) + T(S(u_2))$.
4. Steps 1 to 3 give $(T \circ S)(u_1 + u_2) = (T \circ S)(u_1) + (T \circ S)(u_2)$.
5. Let $a \in F$ and $u \in U$; homogeneity of $S$ and then of $T$ gives $T(S(au)) = T(a\,S(u)) = a\,T(S(u))$.
6. Steps 4 and 5 are the two conditions of a [[linear map|0RJF668P1T]], so $T \circ S$ is linear, which is part 1.
7. For part 2, let $x \in F^p$; then $(T_A \circ T_B)(x) = A(Bx)$.
8. Let $b_1, \dots, b_p$ be the columns of $B$; by the column view of the [[matrix-vector product|0CCQV3884B]], $Bx = x_1 b_1 + \dots + x_p b_p$.
9. The map $T_A$ is linear, so $A(Bx) = x_1 A b_1 + \dots + x_p A b_p$.
10. By the [[definition of the matrix product|076JGP6R3T]], column $k$ of $AB$ is $A b_k$.
11. So the right side of step 9 is $(AB)x$, by the column view of step 8 applied to $AB$, and hence $T_A \circ T_B = T_{AB}$.

## Idea

Each map lets sums and scalars pass through it, so two maps in a row also let them pass.
For matrices, the columns of $AB$ are the images under $A$ of the columns of $B$, and that is the composite written in coordinates.

## Variants

Part 1 also follows in one line from the single condition $S(au + v) = a\,S(u) + S(v)$:
$$T(S(au + v)) = T(a\,S(u) + S(v)) = a\,T(S(u)) + T(S(v)).$$
Part 2 can also be proved entry by entry, by exchanging the order of two finite sums:
$$\bigl(A(Bx)\bigr)_i = \sum_j a_{ij} \sum_k b_{jk} x_k = \sum_k \Bigl(\sum_j a_{ij} b_{jk}\Bigr) x_k = \bigl((AB)x\bigr)_i.$$
