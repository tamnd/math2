---
tag: AT76ZBC9ZM
kind: proof
name: Proof that a ring homomorphism is injective iff its kernel is zero
msc: [16B99]
proves: 0MMCB8RXGA
uses: [0GGE0Z0JQ1, 0AAHE7GEW6, 0PVG1CRAJN]
sources:
  - url: https://proofwiki.org/wiki/Kernel_is_Trivial_iff_Monomorphism/Ring
---

## Proof

1. Let $f \colon R \to S$ be a [[ring homomorphism|0GGE0Z0JQ1]] with [[kernel|0AAHE7GEW6]] $\ker f = \set{a \in R : f(a) = 0}$.
2. We have $f(0) = f(0 + 0) = f(0) + f(0)$. Subtracting $f(0)$ gives $f(0) = 0$. So $0 \in \ker f$.
3. For $a \in R$, $f(a) + f(-a) = f(a + (-a)) = f(0) = 0$. So $f(-a) = -f(a)$.
4. Hence $f(a - b) = f(a) + f(-b) = f(a) - f(b)$ for all $a, b \in R$.
5. Suppose that $f$ is [[injective|0PVG1CRAJN]], and let $a \in \ker f$. Then $f(a) = 0 = f(0)$, so $a = 0$. With step 2, $\ker f = \set{0}$.
6. Conversely, suppose that $\ker f = \set{0}$. Let $a, b \in R$ with $f(a) = f(b)$.
7. By step 4, $f(a - b) = f(a) - f(b) = 0$. So $a - b \in \ker f$, and $a - b = 0$.
8. Thus $a = b$, and $f$ is injective.

## Idea

Two elements have the same image exactly when their difference lies in the kernel. If only $0$ lies in the kernel, the difference is $0$ and the elements are equal. The argument uses only that $f$ preserves addition.
