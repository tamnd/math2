---
tag: FZJWSX2C8J
kind: proof
name: Proof that an injective endomorphism of a finite-dimensional space is surjective
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
proves: 0912EEEVCT
methods: [TFQ1845T84, 0NTF6DMVAP]
uses: [0W4FSW1TVB, 0BJBYCGMWE, 0WGAXEK99E, 0S23E6YE83, 0WSFKKT6FF, 03GSZ8RTZJ, 0KCQ9Y3QKA]
sources:
  - url: https://dec41.user.srcf.net/notes/IB_M/linear_algebra_thm_proof.pdf
    locator: Section 2.3
---

## Proof

We use the rank-nullity theorem to trade the dimension of the kernel against the dimension of the image.

1. Let $n = \dim V$; by [[rank-nullity|0W4FSW1TVB]], $\dim \im T + \dim \ker T = n$, where $\im T$ is the [[image|0WSFKKT6FF]] and $\ker T$ the [[kernel|0S23E6YE83]].
2. A subspace of [[dimension|03GSZ8RTZJ]] $0$ has the empty family as [[basis|0KCQ9Y3QKA]], so it equals $\{0\}$, and conversely $\{0\}$ has dimension $0$.
3. To show that 1 implies 2, let $T$ be injective; by the [[kernel test|0BJBYCGMWE]], $\ker T = \{0\}$, so $\dim \ker T = 0$.
4. By step 1, $\dim \im T = n = \dim V$.
5. So $\im T$ is a subspace of $V$ of full dimension, and [[the full-dimension lemma|0WGAXEK99E]] gives $\im T = V$, so $T$ is surjective.
6. To show that 2 implies 1, let $T$ be surjective; then $\im T = V$, so $\dim \im T = n$.
7. By step 1, $\dim \ker T = 0$, so $\ker T = \{0\}$ by step 2, and $T$ is injective by the kernel test.
8. A map is bijective when it is injective and surjective, so condition 3 implies condition 1.
9. If condition 1 holds, then condition 2 holds by step 5, so $T$ is bijective, and condition 1 implies condition 3.
10. By steps 3 to 9, the three conditions are equivalent.

## Idea

Rank-nullity says that the dimensions of the kernel and the image add up to $\dim V$.
A trivial kernel forces the image to have full dimension, and a full image forces the kernel to be trivial.
This trade needs finite dimension, since the [[right shift|N1G1WQW59J]] on sequences is injective but not surjective.

## Variants

A proof with bases avoids rank-nullity.
Let $(b_1, \dots, b_n)$ be a basis of $V$ and let $T$ be injective, so that $(T b_1, \dots, T b_n)$ is independent.
Each independent family of $n$ vectors in an $n$-dimensional space is a basis, so $\im T$ contains a basis and $\im T = V$.

With a matrix $A$ of $T$ in some basis, the theorem says that the columns of $A$ are independent exactly when they span $F^n$, and both mean $\rank A = n$.
The same argument proves the result for $T \colon V \to W$ with $\dim V = \dim W < \infty$, where step 5 uses $\dim \im T = \dim W$.
