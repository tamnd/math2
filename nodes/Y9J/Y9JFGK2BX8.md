---
tag: Y9JFGK2BX8
kind: proof
name: Proof that finite-dimensional spaces are isomorphic iff they have equal dimension
msc: ["15A03"]
topics: [9080WQTZ3M]
audience: ug1
proves: 0VJBSK15SN
methods: [TFQ1845T84, 01XM7JEKHY]
uses: [0B8T10CE7N, 0BJBYCGMWE, 0R8X9XA83A, 01VG2A0BHW, 0KCQ9Y3QKA, 03GSZ8RTZJ, 0WK0Y8RH1M, ~b1674adb, ~ed2e194c, 0V7ZD6P7RK]
sources:
  - url: https://dec41.user.srcf.net/notes/IB_M/linear_algebra_thm_proof.pdf
    locator: Sections 2.1 and 2.2
  - book: isbn:9783031410253
    locator: Chapter 3
---

## Proof

We show that an isomorphism sends a basis to a basis, and that a bijection between bases extends to an isomorphism.

1. Let $T \colon V \to W$ be a linear [[isomorphism|0B8T10CE7N]]. Let $n = \dim V$, and let $(b_1, \dots, b_n)$ be a [[basis|0KCQ9Y3QKA]] of $V$.
2. $T$ is injective, so $(T(b_1), \dots, T(b_n))$ is independent, by part 2 of the [[kernel test|0BJBYCGMWE]].
3. By the [[theorem on the image|~b1674adb]], the $T(b_i)$ span $\im T$. Since $T$ is surjective, $\im T = W$.
4. So $(T(b_1), \dots, T(b_n))$ is a basis of $W$ with $n$ vectors. By the [[dimension theorem|0WK0Y8RH1M]], $\dim W = n$.
5. Conversely, let $\dim V = \dim W = n$. Let $(b_1, \dots, b_n)$ be a basis of $V$ and $(c_1, \dots, c_n)$ a basis of $W$.
6. By the [[theorem on bases|0R8X9XA83A]], there are linear maps $S \colon V \to W$ with $S(b_i) = c_i$ and $R \colon W \to V$ with $R(c_i) = b_i$.
7. $R \circ S$ is linear, by the [[theorem on composites|~ed2e194c]], and $R(S(b_i)) = b_i$ for each $i$.
8. The identity of $V$ also fixes each $b_i$. By uniqueness in the theorem on bases, $R \circ S = \id_V$.
9. In the same way, $S \circ R$ fixes each $c_i$, so $S \circ R = \id_W$.
10. By the [[two-sided inverse criterion|01VG2A0BHW]], $S$ is bijective. So $V \cong W$, which proves part 1.
11. For part 2, take $W = F^n$ with the [[standard basis|0V7ZD6P7RK]] $(e_1, \dots, e_n)$ and $R(e_i) = b_i$.
12. By steps 6 to 10, $R$ is an isomorphism, and $R(a_1, \dots, a_n) = a_1 b_1 + \dots + a_n b_n$ by linearity.

## Idea

An isomorphism carries a basis to a basis, so it preserves the number of basis vectors.
Conversely, if two spaces have bases of the same size, matching the basis vectors one to one defines a linear map in each direction.
The two maps undo each other.

## Variants

- Steps 2 to 4 can be replaced by rank-nullity: $\dim V = \dim \ker T + \dim \im T = 0 + \dim W$.
- For infinite dimension, the same proof works with bases $(b_i)_{i \in I}$ and $(c_j)_{j \in J}$ and a bijection $I \to J$.
