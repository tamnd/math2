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

We write the new dual forms in the old dual basis with unknown coefficients and evaluate them on the new basis.

1. The matrix $P$ is invertible, because a change of basis matrix between two bases is invertible; see the [[change of basis matrix|0KWXYZPJKN]].
2. The family $(b_i^*)$ is a basis of $V^*$, by the theorem on the [[dimension of the dual space|00889YD15K]]. So for each $k$ there are unique scalars $q_{ik}$ with $c_k^* = \sum_i q_{ik} b_i^*$, and we let $Q = (q_{ik})$.
3. Fix $k$ and $j$. Since $c_j = \sum_l p_{lj} b_l$ and the forms are linear,
$$c_k^*(c_j) = \sum_i q_{ik} \sum_l p_{lj}\, b_i^*(b_l).$$
4. Since $b_i^*(b_l) = \delta_{il}$ by the definition of the [[dual basis|0W6M3PSD08]], only the terms with $l = i$ remain:
$$c_k^*(c_j) = \sum_i q_{ik} p_{ij} = (Q^{\mathsf{T}} P)_{kj}.$$
5. By the definition of the dual basis of $C$, $c_k^*(c_j) = \delta_{kj}$. So $Q^{\mathsf{T}} P = I$.
6. Multiply on the right by $P^{-1}$, which exists by step 1. This gives $Q^{\mathsf{T}} = P^{-1}$.
7. Take transposes on both sides to get $Q = (P^{-1})^{\mathsf{T}}$, which is the first claim.
8. For the coordinates, let $f = \sum_k \gamma_k c_k^*$. Substituting step 2 gives
$$f = \sum_k \gamma_k \sum_i q_{ik} b_i^* = \sum_i (Q\gamma)_i\, b_i^*.$$
9. The $B^*$-coordinates of $f$ are unique, because $(b_i^*)$ is a basis, so $\beta = Q\gamma$.
10. The matrix $Q$ is invertible with inverse $P^{\mathsf{T}}$, since $(P^{-1})^{\mathsf{T}} P^{\mathsf{T}} = (P P^{-1})^{\mathsf{T}} = I$. Multiplying $\beta = Q\gamma$ by $P^{\mathsf{T}}$ gives $\gamma = P^{\mathsf{T}} \beta$, which is the second claim.

## Idea

The new dual forms are unknown, but they are combinations of the old dual forms, and they must satisfy $c_k^*(c_j) = \delta_{kj}$.
Evaluating the combinations on the new basis turns all $n^2$ of these conditions into the single matrix equation $Q^{\mathsf{T}} P = I$.
Since $P$ is invertible, this equation has exactly one solution, $Q = (P^{-1})^{\mathsf{T}}$.

## Variants

A proof without coordinates uses the linear map $A \colon V \to V$ with $A b_j = c_j$ for each $j$.
Then $c_k^* = b_k^* \circ A^{-1}$, because $b_k^*(A^{-1} c_j) = b_k^*(b_j) = \delta_{kj}$, and the defining property of the dual basis fixes $c_k^*$.
The matrix statement then follows from the theorem on the [[matrix of the dual map|0ZPB3180AY]], applied to $A^{-1}$.

In $F^n$ with the standard basis as $B$, the proof is one line.
The rows of $P^{-1}$ satisfy $(P^{-1} P)_{kj} = \delta_{kj}$, so row $k$ of $P^{-1}$ is the form $c_k^*$, and its coordinates are column $k$ of $(P^{-1})^{\mathsf{T}}$.
