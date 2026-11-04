---
tag: Y9JFGK2BX8
kind: proof
name: Proof that finite-dimensional spaces are isomorphic iff they have equal dimension
msc: [15A03]
proves: 0VJBSK15SN
uses: [0B8T10CE7N, 0BJBYCGMWE, 0R8X9XA83A, 01VG2A0BHW, 0KCQ9Y3QKA, 0CRMGPAH83, 088RYKAWK9, 03GSZ8RTZJ, 0WK0Y8RH1M]
sources:
  - url: https://dec41.user.srcf.net/notes/IB_M/linear_algebra_thm_proof.pdf
    locator: Sections 2.1 and 2.2
---

## Proof

We show that an isomorphism sends a basis to a basis, and that a bijection between bases extends to an isomorphism.

1. Suppose $V$ and $W$ are [[isomorphic|0B8T10CE7N]], and let $T \colon V \to W$ be a linear isomorphism. Let $n = \dim V$, the [[dimension|03GSZ8RTZJ]], and let $(b_1, \dots, b_n)$ be a [[basis|0KCQ9Y3QKA]] of $V$.
2. The family $(T(b_1), \dots, T(b_n))$ is [[linearly independent|0CRMGPAH83]]. Suppose $\sum_i a_i T(b_i) = 0$ with $a_i \in F$. Then $T\left(\sum_i a_i b_i\right) = 0$ by linearity.
3. $T$ is injective, so its kernel is $\{0\}$ by [[the kernel criterion|0BJBYCGMWE]]. Hence $\sum_i a_i b_i = 0$, and all $a_i = 0$ because $(b_i)$ is linearly independent.
4. The family $(T(b_1), \dots, T(b_n))$ [[spans|088RYKAWK9]] $W$. Let $w \in W$. Since $T$ is surjective, $w = T(v)$ for some $v = \sum_i a_i b_i$, and then $w = \sum_i a_i T(b_i)$.
5. So $(T(b_1), \dots, T(b_n))$ is a basis of $W$ with $n$ vectors. By the [[dimension theorem|0WK0Y8RH1M]], $\dim W = n = \dim V$.
6. Conversely, suppose $\dim V = \dim W = n$. Let $(b_1, \dots, b_n)$ be a basis of $V$ and $(c_1, \dots, c_n)$ a basis of $W$.
7. By [[the extension of values on a basis|0R8X9XA83A]], there is a linear map $S \colon V \to W$ with $S(b_i) = c_i$ for all $i$. There is also a linear map $R \colon W \to V$ with $R(c_i) = b_i$ for all $i$.
8. The composite $R \circ S \colon V \to V$ is linear, since $R(S(u + av)) = R(S(u)) + a R(S(v))$ for $u, v \in V$ and $a \in F$. It sends each $b_i$ to $R(c_i) = b_i$.
9. The identity map of $V$ also sends each $b_i$ to $b_i$. By the uniqueness part of [[the same result|0R8X9XA83A]], $R \circ S = \mathrm{id}_V$.
10. In the same way, $S \circ R \colon W \to W$ fixes each $c_i$, so $S \circ R = \mathrm{id}_W$.
11. By [[the two-sided inverse criterion|01VG2A0BHW]], $S$ is bijective. So $S$ is a linear isomorphism, and $V$ and $W$ are isomorphic.

## Idea

An isomorphism carries a basis to a basis, so it preserves the number of basis vectors. Conversely, if two spaces have bases of the same size, matching the basis vectors one to one defines a linear map in each direction. The two maps undo each other.
