---
tag: M4VHXJSCD5
kind: proof
name: Proof that a linear map is injective iff its kernel is trivial
msc: [15A04]
proves: 0BJBYCGMWE
uses: [0NRYHJPQG2, 0S23E6YE83]
sources:
  - url: https://en.wikipedia.org/wiki/Kernel_(linear_algebra)
    locator: Properties
---

## Proof

1. Let $T \colon V \to W$ be a [[linear map|0NRYHJPQG2]]. First, $T(0) = 0$. Indeed, $T(0) = T(0 + 0) = T(0) + T(0)$, and subtracting $T(0)$ gives $T(0) = 0$.
2. So $0$ lies in the [[kernel|0S23E6YE83]] $\ker T$, and $\{0\} \subseteq \ker T$ always holds.
3. For $u, v \in V$, linearity gives $T(u) - T(v) = T(u - v)$. So $T(u) = T(v)$ if and only if $u - v \in \ker T$.
4. Suppose $T$ is injective, and let $v \in \ker T$. Then $T(v) = 0 = T(0)$ by step 1, so $v = 0$ by injectivity. Hence $\ker T = \{0\}$.
5. Suppose $\ker T = \{0\}$, and let $u, v \in V$ with $T(u) = T(v)$. By step 3, $u - v \in \ker T$, so $u - v = 0$ and $u = v$. Hence $T$ is injective.
6. By steps 4 and 5, $T$ is injective if and only if $\ker T = \{0\}$.

## Idea

Two vectors have the same image exactly when their difference lies in the kernel. So the map can only merge vectors if the kernel holds a nonzero vector.
