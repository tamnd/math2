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

We use the rank-nullity theorem to compare the kernel and the image.

1. Let $n = \dim V$. By [[rank-nullity|0W4FSW1TVB]], $\dim \im T + \dim \ker T = n$. Here $\im T$ is the [[image|0WSFKKT6FF]] and $\ker T$ the [[kernel|0S23E6YE83]].
2. A subspace of [[dimension|03GSZ8RTZJ]] $0$ has the empty family as [[basis|0KCQ9Y3QKA]]. So it equals $\{0\}$. Conversely, $\{0\}$ has dimension $0$.
3. (1 implies 2.) Let $T$ be injective. By the [[kernel test|0BJBYCGMWE]], $\ker T = \{0\}$, so $\dim \ker T = 0$.
4. By step 1, $\dim \im T = n = \dim V$.
5. $\im T$ is a subspace of $V$ of full dimension. By [[the full-dimension lemma|0WGAXEK99E]], $\im T = V$. So $T$ is surjective.
6. (2 implies 1.) Let $T$ be surjective. Then $\im T = V$, so $\dim \im T = n$.
7. By step 1, $\dim \ker T = 0$. By step 2, $\ker T = \{0\}$. By the kernel test, $T$ is injective.
8. (3 is equivalent to 1.) By definition, a map is bijective when it is injective and surjective.
9. If $T$ is bijective, then condition 1 holds. If condition 1 holds, then condition 2 holds by step 5. So $T$ is bijective.
10. By steps 3 to 9, the three conditions are equivalent.

## Idea

Rank-nullity says that the dimensions of the kernel and the image add up to $\dim V$.
A trivial kernel forces the image to have full dimension.
A full image forces the kernel to be trivial.
This trade-off needs finite dimension: the [[right shift|~834be223]] on sequences is injective but not surjective.

## Variants

- A proof with bases avoids rank-nullity. Let $(b_1, \dots, b_n)$ be a basis of $V$ and let $T$ be injective. Then $(T b_1, \dots, T b_n)$ is independent. Each independent family of $n$ vectors in an $n$-dimensional space is a basis. So $\im T$ contains a basis, and $\im T = V$.
- With a matrix $A$ of $T$ in some basis, the theorem becomes: $A$ has rank $n$ if and only if its columns are independent, if and only if they span $F^n$.
- The same argument proves the result for $T \colon V \to W$ with $\dim V = \dim W < \infty$. Step 5 then uses $\dim \im T = \dim W$.
