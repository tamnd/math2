---
tag: 72AQPHFDE0
kind: proof
name: Proof of the change of basis formula
msc: [15A04]
proves: 0MQXVZEBMT
uses: [0YQSGNYE3K, 0MKRHZB3WS, 032Q9FB8MT, 0EB9N0S33C, 0753Y2X5K6, 073E4XC016, 04CYQHN6MC, 0KCQ9Y3QKA]
sources:
  - url: https://dec41.user.srcf.net/notes/IB_M/linear_algebra_thm_proof.pdf
    locator: Section 2.4
---

## Proof

We compute $T(b'_j)$ in the basis $C$ in two ways, and then show that $Q$ is invertible.

1. Let $n = \dim V$ and $m = \dim W$. Write $B = (b_1, \dots, b_n)$, $B' = (b'_1, \dots, b'_n)$, $C = (c_1, \dots, c_m)$ and $C' = (c'_1, \dots, c'_m)$.
2. By the definition of the [[change of basis matrix|0MKRHZB3WS]], $P = (p_{kj})$ and $Q = (q_{ik})$ satisfy $b'_j = \sum_{k=1}^n p_{kj} b_k$ and $c'_k = \sum_{i=1}^m q_{ik} c_i$.
3. Let $M = [T]_{C,B} = (\mu_{ik})$ and $M' = [T]_{C',B'} = (\mu'_{kj})$. By the definition of the [[matrix of a linear map|0YQSGNYE3K]], $T(b_k) = \sum_{i} \mu_{ik} c_i$ and $T(b'_j) = \sum_{k} \mu'_{kj} c'_k$.
4. Fix $j$. By step 3 and then step 2, $T(b'_j) = \sum_{k=1}^m \mu'_{kj} \sum_{i=1}^m q_{ik} c_i = \sum_{i=1}^m (Q M')_{ij}\, c_i$, using the [[matrix product|032Q9FB8MT]].
5. By step 2 and linearity, $T(b'_j) = \sum_{k=1}^n p_{kj} T(b_k) = \sum_{k=1}^n p_{kj} \sum_{i=1}^m \mu_{ik} c_i = \sum_{i=1}^m (M P)_{ij}\, c_i$.
6. The [[coordinates|04CYQHN6MC]] of $T(b'_j)$ in the [[basis|0KCQ9Y3QKA]] $C$ are unique. Comparing steps 4 and 5 gives $(QM')_{ij} = (MP)_{ij}$ for all $i, j$. So $QM' = MP$.
7. Now we show that $Q$ is invertible. Let $R = (r_{ki})$ be the change of basis matrix from $C'$ to $C$, so that $c_i = \sum_{k=1}^m r_{ki} c'_k$.
8. By steps 2 and 7, $c'_l = \sum_{i=1}^m q_{il} c_i = \sum_{k=1}^m \left(\sum_{i=1}^m r_{ki} q_{il}\right) c'_k = \sum_{k=1}^m (RQ)_{kl}\, c'_k$.
9. Also $c'_l = \sum_k \delta_{kl} c'_k$, where $\delta_{kl}$ is $1$ if $k = l$ and $0$ otherwise. By uniqueness of coordinates in $C'$, $RQ = I_m$.
10. By [[one-sided inverses of square matrices|0753Y2X5K6]], $Q$ is [[invertible|0EB9N0S33C]] with $Q^{-1} = R$.
11. Multiply $QM' = MP$ on the left by $Q^{-1}$. By [[associativity|073E4XC016]], $M' = (Q^{-1} Q) M' = Q^{-1}(QM') = Q^{-1}(MP) = Q^{-1} M P$.
12. So $[T]_{C',B'} = Q^{-1} [T]_{C,B} P$.
13. For an endomorphism $T$ of $V$ with $C = B$ and $C' = B'$, $Q$ is the change of basis matrix from $B$ to $B'$. So $Q = P$, and $[T]_{B'} = P^{-1} [T]_B P$.

## Idea

Expand $T(b'_j)$ in the old output basis $C$ in two ways. Going through the new output basis $C'$ gives column $j$ of $QM'$. Going through the old input basis $B$ gives column $j$ of $MP$. Equating them and inverting $Q$ gives the formula.
