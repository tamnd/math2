---
tag: FZJWSX2C8J
kind: proof
name: Proof that an injective endomorphism of a finite-dimensional space is surjective
msc: [15A04]
proves: 0912EEEVCT
uses: [0W4FSW1TVB, 0BJBYCGMWE, 0WGAXEK99E, 0S23E6YE83, 0WSFKKT6FF, 03GSZ8RTZJ, 0KCQ9Y3QKA]
sources:
  - url: https://dec41.user.srcf.net/notes/IB_M/linear_algebra_thm_proof.pdf
    locator: Section 2.3
---

## Proof

We use the rank–nullity theorem to compare the kernel and the image.

1. Let $n = \dim V$. By the [[rank–nullity theorem|0W4FSW1TVB]], $\dim \im T + \dim \ker T = n$, where $\im T$ is the [[image|0WSFKKT6FF]] and $\ker T$ the [[kernel|0S23E6YE83]].
2. A subspace of [[dimension|03GSZ8RTZJ]] $0$ has the empty family as [[basis|0KCQ9Y3QKA]], so it equals $\{0\}$. Conversely $\{0\}$ has dimension $0$.
3. (1 implies 2.) Suppose $T$ is injective. By [[the kernel criterion|0BJBYCGMWE]], $\ker T = \{0\}$, so $\dim \ker T = 0$.
4. By step 1, $\dim \im T = n = \dim V$. Since $\im T$ is a subspace of $V$, [[a subspace of full dimension is the whole space|0WGAXEK99E]] gives $\im T = V$. So $T$ is surjective.
5. (2 implies 1.) Suppose $T$ is surjective. Then $\im T = V$, so $\dim \im T = n$.
6. By step 1, $\dim \ker T = 0$, so $\ker T = \{0\}$ by step 2. By the kernel criterion, $T$ is injective.
7. (3 is equivalent to 1 and 2.) A map is bijective exactly when it is injective and surjective.
8. If $T$ is bijective, it is injective, so condition 1 holds. If condition 1 holds, then condition 2 holds by step 4, so $T$ is bijective.
9. By steps 3 to 8, the three conditions are equivalent.

## Idea

Rank–nullity says that the dimensions of the kernel and the image add up to $\dim V$. A trivial kernel forces the image to have full dimension, and a full image forces the kernel to be trivial. This trade-off needs finite dimension: the shift on sequences is injective but not surjective.
