---
tag: 72AQPHFDE0
kind: proof
name: Proof of the change of basis formula
msc: ["15A04"]
topics: [S6559D61BP]
audience: ug1
proves: 0MQXVZEBMT
uses: [0YQSGNYE3K, 0MKRHZB3WS, 032Q9FB8MT, 0EB9N0S33C, 0753Y2X5K6, 073E4XC016, 04CYQHN6MC, 0KCQ9Y3QKA]
methods: [0NTF6DMVAP]
sources:
  - url: https://dec41.user.srcf.net/notes/IB_M/linear_algebra_thm_proof.pdf
    locator: Section 2.4
---

## Proof

We expand $T(b'_j)$ in the old basis $C$ in two ways, compare the coefficients, and then show that the change of basis matrices are invertible.

1. Let $n = \dim V$ and $m = \dim W$.
   We write $B = (b_1, \dots, b_n)$, $B' = (b'_1, \dots, b'_n)$, $C = (c_1, \dots, c_m)$ and $C' = (c'_1, \dots, c'_m)$.
2. By the definition of the [[change of basis matrix|0MKRHZB3WS]], the matrices $P = (p_{kj})$ and $Q = (q_{ik})$ satisfy
   $$b'_j = \sum_{k=1}^{n} p_{kj}\, b_k, \qquad c'_k = \sum_{i=1}^{m} q_{ik}\, c_i.$$
3. Let $M = [T]_{C,B} = (\mu_{ik})$ and $M' = [T]_{C',B'} = (\mu'_{kj})$.
   By the definition of the [[matrix of a linear map|0YQSGNYE3K]],
   $$T(b_k) = \sum_{i=1}^{m} \mu_{ik}\, c_i, \qquad T(b'_j) = \sum_{k=1}^{m} \mu'_{kj}\, c'_k.$$
4. Fix $j$.
   We substitute the expansion of $c'_k$ from step 2 into the second formula of step 3, and we use the definition of the [[matrix product|032Q9FB8MT]]:
   $$T(b'_j) = \sum_{k=1}^{m} \mu'_{kj} \sum_{i=1}^{m} q_{ik}\, c_i = \sum_{i=1}^{m} (QM')_{ij}\, c_i.$$
5. Now we expand $b'_j$ first, by step 2, and use that $T$ is linear and then the first formula of step 3:
   $$T(b'_j) = \sum_{k=1}^{n} p_{kj}\, T(b_k) = \sum_{k=1}^{n} p_{kj} \sum_{i=1}^{m} \mu_{ik}\, c_i = \sum_{i=1}^{m} (MP)_{ij}\, c_i.$$
6. The [[coordinates|04CYQHN6MC]] of a vector in the [[basis|0KCQ9Y3QKA]] $C$ are unique.
   So steps 4 and 5 give $(QM')_{ij} = (MP)_{ij}$ for all $i$ and $j$, that is, $QM' = MP$.
7. To show that $Q$ is invertible, let $R = (r_{ki})$ be the change of basis matrix from $C'$ to $C$, so that $c_i = \sum_{k=1}^{m} r_{ki}\, c'_k$.
8. We substitute this into the expansion of $c'_l$ from step 2:
   $$c'_l = \sum_{i=1}^{m} q_{il}\, c_i = \sum_{k=1}^{m} \Bigl(\sum_{i=1}^{m} r_{ki}\, q_{il}\Bigr) c'_k = \sum_{k=1}^{m} (RQ)_{kl}\, c'_k.$$
9. Also $c'_l = \sum_k \delta_{kl}\, c'_k$, where $\delta_{kl}$ is $1$ for $k = l$ and $0$ otherwise.
   Coordinates in $C'$ are unique, so $RQ = I_m$.
10. A square matrix with a left inverse is [[invertible|0EB9N0S33C]], by the theorem on [[one-sided inverses of square matrices|0753Y2X5K6]], so $Q^{-1} = R$.
11. We multiply $QM' = MP$ on the left by $Q^{-1}$ and use [[associativity|073E4XC016]]:
    $$M' = (Q^{-1}Q)M' = Q^{-1}(QM') = Q^{-1}(MP) = Q^{-1}MP.$$
    This is part 2, $[T]_{C',B'} = Q^{-1}[T]_{C,B}P$.
12. For a map $T \colon V \to V$ with $C = B$ and $C' = B'$, the matrix $Q$ is the change of basis matrix from $B$ to $B'$, so $Q = P$.
    Then step 11 gives part 3, $[T]_{B'} = P^{-1}[T]_B P$.
13. For part 1, let $v = \sum_j x'_j\, b'_j$, so that $[v]_{B'} = x'$.
    By step 2,
    $$v = \sum_{j=1}^{n} x'_j \sum_{k=1}^{n} p_{kj}\, b_k = \sum_{k=1}^{n} (Px')_k\, b_k,$$
    so $[v]_B = P[v]_{B'}$.
14. Steps 7 to 10, with $V$, $B$ and $B'$ in place of $W$, $C$ and $C'$, show that $P$ is invertible.
    Multiplying step 13 on the left by $P^{-1}$ gives $[v]_{B'} = P^{-1}[v]_B$, which completes part 1.

## Idea

Look at one new basis vector $b'_j$ and its image $T(b'_j)$, and write that image in the old output basis $C$.
If we go through the new output basis $C'$, the coefficients form column $j$ of $QM'$.
If we go through the old input basis $B$, the coefficients form column $j$ of $MP$.
Coordinates are unique, so the two columns agree, and dividing by the invertible $Q$ gives the formula.

## Variants

The shortest proof uses the [[matrix of a composition|05Q1B7MH0M]].
Write $T = \mathrm{id}_W \circ T \circ \mathrm{id}_V$ and take the bases $B'$, $B$, $C$, $C'$ along the way.
The product rule gives $[T]_{C',B'} = [\mathrm{id}_W]_{C',C}\,[T]_{C,B}\,[\mathrm{id}_V]_{B,B'}$, and the outer factors are $Q^{-1}$ and $P$.
Part 1 is the [[coordinate formula|8B63KHW6D5]] $[f(v)]_B = [f]_{B,B'}[v]_{B'}$ applied to the identity map $f = \mathrm{id}_V$.
