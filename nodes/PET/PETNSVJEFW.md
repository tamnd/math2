---
tag: PETNSVJEFW
kind: proof
name: Proof that a linear map is determined by its values on a basis
msc: [15A04]
proves: 0R8X9XA83A
uses: [0KCQ9Y3QKA, 0NRYHJPQG2, 0V8F3E48E6]
sources:
  - url: https://dec41.user.srcf.net/notes/IB_M/linear_algebra_thm_proof.pdf
    locator: Section 2.2
---

## Proof

We first prove uniqueness, then build the map from the coordinates of each vector.

1. Since $(b_i)_{i \in I}$ is a [[basis|0KCQ9Y3QKA]], each $v \in V$ is a [[linear combination|0V8F3E48E6]] $v = \sum_{i \in I} a_i b_i$ in exactly one way. Here $a_i \in F$, and $a_i = 0$ for all but finitely many $i$.
2. Let $S, T \colon V \to W$ be [[linear maps|0NRYHJPQG2]] with $S(b_i) = T(b_i)$ for all $i \in I$. Let $v \in V$ be written as in step 1.
3. The sum in step 1 has finitely many nonzero terms. Linearity, applied once for each term, gives $S(v) = \sum_{i \in I} a_i S(b_i)$ and $T(v) = \sum_{i \in I} a_i T(b_i)$.
4. The right sides of step 3 are equal term by term. So $S(v) = T(v)$ for all $v \in V$, and $S = T$.
5. Now let $(w_i)_{i \in I}$ be a family of vectors of $W$. For $v = \sum_{i \in I} a_i b_i$ as in step 1, define $T(v) = \sum_{i \in I} a_i w_i$.
6. This is a finite sum, since only finitely many $a_i$ are nonzero. The coefficients $a_i$ are unique, so $T(v)$ is well defined.
7. $T$ is additive. Let $v = \sum_i a_i b_i$ and $v' = \sum_i a'_i b_i$. Then $v + v' = \sum_i (a_i + a'_i) b_i$, and by uniqueness these are the coefficients of $v + v'$.
8. Hence $T(v + v') = \sum_i (a_i + a'_i) w_i = T(v) + T(v')$.
9. $T$ is homogeneous. For $c \in F$, $cv = \sum_i (c a_i) b_i$, and by uniqueness these are the coefficients of $cv$. Hence $T(cv) = \sum_i c a_i w_i = c\, T(v)$.
10. So $T$ is linear. For $j \in I$, the vector $b_j$ has coefficient $1$ at $j$ and $0$ elsewhere, by uniqueness. Hence $T(b_j) = w_j$.
11. If $T'$ is another linear map with $T'(b_j) = w_j$ for all $j \in I$, then $T'$ and $T$ agree on the basis. By step 4, $T' = T$.
12. So there is exactly one linear map $T \colon V \to W$ with $T(b_i) = w_i$ for all $i \in I$.

## Idea

Every vector is a unique combination of basis vectors, and a linear map must respect combinations. So the images of the basis vectors fix the map. Conversely, any choice of images defines a map by sending each combination to the same combination of the chosen images.
