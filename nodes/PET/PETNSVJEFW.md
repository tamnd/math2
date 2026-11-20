---
tag: PETNSVJEFW
kind: proof
name: Proof that a linear map is determined by its values on a basis
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
proves: 0R8X9XA83A
methods: [01XM7JEKHY, GQHHNV79PA, 0NTF6DMVAP]
uses: [0KCQ9Y3QKA, 0NRYHJPQG2, 0V8F3E48E6, 0VTQTPQGAV, 0RJF668P1T, STYEWH8R4E]
sources:
  - url: https://dec41.user.srcf.net/notes/IB_M/linear_algebra_thm_proof.pdf
    locator: Section 2.2
  - book: isbn:9783031410253
    locator: Chapter 3
---

## Proof

We first prove uniqueness, then build the map from the coordinates of each vector.

1. By the [[definition of a basis|0VTQTPQGAV]], each $v \in V$ is a [[linear combination|0V8F3E48E6]] $v = \sum_{i \in I} a_i b_i$ in exactly one way.
2. In step 1, $a_i \in F$, and $a_i = 0$ for all but finitely many $i$.
3. Let $S, T$ be [[linear maps|0RJF668P1T]] with $S(b_i) = T(b_i)$ for all $i$. Let $v$ be written as in step 1.
4. By the [[lemma on linear combinations|STYEWH8R4E]], $S(v) = \sum_i a_i S(b_i)$ and $T(v) = \sum_i a_i T(b_i)$.
5. The right sides of step 4 are equal term by term. So $S(v) = T(v)$ for all $v$, and $S = T$.
6. Now let $(w_i)_{i \in I}$ be a family in $W$. For $v = \sum_i a_i b_i$ as in step 1, define $T(v) = \sum_i a_i w_i$.
7. This is a finite sum by step 2. The coefficients $a_i$ are unique, so $T(v)$ is well defined.
8. Let $v = \sum_i a_i b_i$ and $v' = \sum_i a'_i b_i$. Then $v + v' = \sum_i (a_i + a'_i) b_i$.
9. By uniqueness, the $a_i + a'_i$ are the coefficients of $v + v'$. So $T(v + v') = \sum_i (a_i + a'_i) w_i = T(v) + T(v')$.
10. For $c \in F$, $cv = \sum_i (c a_i) b_i$, and these are the coefficients of $cv$. So $T(cv) = c\,T(v)$.
11. Steps 9 and 10 show that $T$ is linear.
12. For $j \in I$, the coefficients of $b_j$ are $1$ at $j$ and $0$ elsewhere, by uniqueness. So $T(b_j) = w_j$.
13. By step 5, any other linear map with these values equals $T$.

## Idea

Every vector is a unique combination of basis vectors, and a linear map must respect combinations.
So the images of the basis vectors fix the map.
Conversely, any choice of images defines a map: send each combination to the same combination of the chosen images.

## Variants

- In finite dimension, with $V = F^n$ and the standard basis, the map of step 6 is $x \mapsto Ax$, where $A$ has columns $w_1, \dots, w_n$.
- Existence can also be proved through coordinates: compose the coordinate isomorphism $V \to F^{(I)}$ with the map $F^{(I)} \to W$, $(a_i) \mapsto \sum_i a_i w_i$.
