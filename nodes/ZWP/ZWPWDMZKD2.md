---
tag: ZWPWDMZKD2
kind: proof
name: Proof that similar matrices have the same characteristic polynomial
msc: ["15A15", "15A18"]
topics: [6R1D6QPY3S]
audience: ug1
proves: 0TYMASG33Y
methods: [0NTF6DMVAP, XP5SDYKJX0]
uses: [039HF58KQ5, 0TWTS88TWN, 076JGP6R3T, 073E4XC016, 0RXD6EZYBK, 04CPJ6AF00, 0Z4BWARC38, 027KDW2K72, 0Q9EZS90GY]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_polynomial
    locator: Properties
---

## Proof

We write $t I - P^{-1} A P$ as a conjugate of $t I - A$ and then use the product rule for determinants.

1. Let $Q = P^{-1}$, so that $Q P = P Q = I_n$.
2. The ring $K$ is a subring of the [[polynomial ring|0Q9EZS90GY]] $K[t]$, which is commutative.
   So we may view $A$, $P$ and $Q$ as matrices over $K[t]$, and the products $QP$ and $PQ$ do not change.
3. The scalar $t$ commutes with every entry, so by the definition of the [[matrix product|076JGP6R3T]],
$$Q (t I_n) P = t\, (Q P) = t I_n.$$
4. By [[distributivity|0RXD6EZYBK]] and [[associativity|073E4XC016]] of the matrix product and step 3,
$$Q (t I_n - A) P = Q (t I_n) P - Q A P = t I_n - Q A P.$$
5. By the definition of the [[characteristic polynomial|039HF58KQ5]] and step 4, $p_{QAP}(t) = \det\big(Q (t I_n - A) P\big)$, a determinant over $K[t]$.
6. The [[product rule|04CPJ6AF00]] holds over the commutative ring $K[t]$, so
$$\det\big(Q (t I_n - A) P\big) = \det Q \cdot \det(t I_n - A) \cdot \det P.$$
7. The ring $K[t]$ is commutative, so we may move $\det P$ next to $\det Q$, and the product rule again gives $\det Q \det P = \det(QP) = \det I_n$.
8. The [[determinant of the identity|0Z4BWARC38]] is $1$, so $p_{P^{-1} A P}(t) = \det(t I_n - A) = p_A(t)$.
9. If $B$ is [[similar|027KDW2K72]] to $A$, then $B = P^{-1} A P$ for some invertible $P$, and step 8 gives $p_B = p_A$.

## Idea

The matrix $t I$ commutes with everything, so conjugating $t I - A$ by $P$ gives $t I - P^{-1} A P$.
When we take determinants, the factors $\det P^{-1}$ and $\det P$ cancel, and what is left is $\det(tI - A)$.
The one thing to watch is that the product rule is used over $K[t]$, not over $K$, and it holds there because $K[t]$ is commutative.

## Variants

When $K$ is a field, one can avoid the polynomial ring.
For each scalar $\lambda$ the same computation gives $\det(\lambda I - P^{-1}AP) = \det(\lambda I - A)$, so the two polynomials agree at every $\lambda \in K$.
This proves that they are equal when $K$ has more than $n$ elements, since the difference of the two polynomials has degree less than $n$ and more than $n$ roots.
Over a field with at most $n$ elements the pointwise argument is not enough, and the proof above is needed.
