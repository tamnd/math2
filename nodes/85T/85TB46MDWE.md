---
tag: 85TB46MDWE
kind: proof
name: Proof of the change of dual basis lemma
msc: ["15A03", "15A04"]
topics: [9K7FFF26QR]
audience: ug2
proves: SXWX10HSB6
methods: [0NTF6DMVAP]
uses: [0W6M3PSD08, 0KWXYZPJKN, 0TWTS88TWN, 00889YD15K, 0R8X9XA83A]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_basis
    locator: Examples
---

## Proof

1. $P$ is invertible, because a change of basis matrix between two bases is invertible; see the [[change of basis matrix|0KWXYZPJKN]].
2. The family $(b_i^*)$ is a basis of $V^*$, by the theorem on the [[dimension of the dual space|00889YD15K]]. So for each $k$ there are unique scalars $q_{ik}$ with $c_k^* = \sum_i q_{ik} b_i^*$.
3. Fix $k$ and $j$. By linearity and $c_j = \sum_l p_{lj} b_l$, we get $c_k^*(c_j) = \sum_i q_{ik} \sum_l p_{lj}\, b_i^*(b_l)$.
4. Since $b_i^*(b_l) = \delta_{il}$, only the terms with $l = i$ remain. So $c_k^*(c_j) = \sum_i q_{ik} p_{ij} = (Q^{\mathsf{T}} P)_{kj}$.
5. By the definition of the [[dual basis|0W6M3PSD08]], $c_k^*(c_j) = \delta_{kj}$. So $Q^{\mathsf{T}} P = I$.
6. Multiply on the right by $P^{-1}$, which exists by step 1. This gives $Q^{\mathsf{T}} = P^{-1}$.
7. Take transposes: $Q = (P^{-1})^{\mathsf{T}}$. This is the first claim.
8. For the coordinates, let $f = \sum_k \gamma_k c_k^*$. By step 2, $f = \sum_k \gamma_k \sum_i q_{ik} b_i^* = \sum_i (Q\gamma)_i\, b_i^*$.
9. The $B^*$-coordinates of $f$ are unique, so $\beta = Q \gamma$.
10. The matrix $Q$ is invertible with $Q^{-1} = P^{\mathsf{T}}$, since $(P^{-1})^{\mathsf{T}} P^{\mathsf{T}} = (P P^{-1})^{\mathsf{T}} = I$. So $\gamma = P^{\mathsf{T}} \beta$.

## Idea

Write the new dual forms in the old dual basis with unknown coefficients.
The defining equations $c_k^*(c_j) = \delta_{kj}$ become one matrix equation $Q^{\mathsf{T}} P = I$, which has the single solution $Q = (P^{-1})^{\mathsf{T}}$.

## Variants

- One can avoid coordinates. Let $A \colon V \to V$ be the linear map with $A b_j = c_j$. Then $c_k^* = b_k^* \circ A^{-1}$, because $b_k^*(A^{-1} c_j) = b_k^*(b_j) = \delta_{kj}$. The matrix statement follows from the theorem on the [[matrix of the dual map|0ZPB3180AY]].
- In $F^n$ with the standard basis, the proof is one line: the rows of $P^{-1}$ satisfy $(P^{-1} P)_{kj} = \delta_{kj}$, so they are the forms $c_k^*$.
