---
tag: ZWPWDMZKD2
kind: proof
name: Proof that similar matrices have the same characteristic polynomial
msc: [15A15, 15A18]
proves: 0TYMASG33Y
uses: [039HF58KQ5, 0TWTS88TWN, 076JGP6R3T, 073E4XC016, 0RXD6EZYBK, 04CPJ6AF00, 0Z4BWARC38, 027KDW2K72, 0Q9EZS90GY]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_polynomial
    locator: Properties
---

## Proof

We write $t I - P^{-1} A P$ as a conjugate of $t I - A$ and use the product rule.

1. Let $A$ and $P$ be $n \times n$ matrices over $K$, with $P$ invertible. Let $Q = P^{-1}$, so $Q P = P Q = I_n$.
2. The ring $K$ is a subring of the [[polynomial ring|0Q9EZS90GY]] $K[t]$, which is commutative. So we view $A$, $P$, $Q$ as matrices over $K[t]$. The products $QP$ and $PQ$ do not change.
3. The scalar $t$ commutes with every matrix in products. So $Q (t I_n) P = t (Q P) = t I_n$, by the definition of the [[matrix product|076JGP6R3T]].
4. By [[distributivity|0RXD6EZYBK]] and [[associativity|073E4XC016]], $Q (t I_n - A) P = Q (t I_n) P - Q A P = t I_n - Q A P$.
5. By the definition of the [[characteristic polynomial|039HF58KQ5]] and step 4, $p_{QAP}(t) = \det\big(Q (t I_n - A) P\big)$, a determinant over $K[t]$.
6. By the [[product rule|04CPJ6AF00]] over $K[t]$, this equals $\det Q \cdot \det(t I_n - A) \cdot \det P$.
7. By commutativity of $K[t]$ and the product rule, this equals $\det(Q P) \det(t I_n - A) = \det I_n \cdot p_A(t)$.
8. By the [[determinant of the identity|0Z4BWARC38]], $\det I_n = 1$. So $p_{P^{-1} A P}(t) = p_A(t)$.
9. If $B$ is [[similar|027KDW2K72]] to $A$, then $B = P^{-1} A P$ for an invertible $P$. By step 8, $p_B = p_A$.

## Idea

The matrix $t I$ commutes with everything, so $t I - P^{-1} A P = P^{-1} (t I - A) P$. Taking determinants, the factors $\det P^{-1}$ and $\det P$ cancel.
