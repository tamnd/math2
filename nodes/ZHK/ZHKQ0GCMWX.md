---
tag: ZHKQ0GCMWX
kind: proof
name: Proof of the universal property of the quotient ring
msc: [16D25]
proves: 0R74MZYNRB
uses: [0894J980RK, 0DDA6CY7GJ, 0VFW4Y69BT, 0GGE0Z0JQ1, 0AAHE7GEW6]
sources:
  - url: https://proofwiki.org/wiki/Universal_Property_of_Quotient_Ring
---

## Proof

1. Let $R$ be a [[ring|0894J980RK]], let $I$ be a [[two-sided ideal|0DDA6CY7GJ]] of $R$, and let $\pi \colon R \to R/I$, $\pi(a) = a + I$, be the quotient map to the [[quotient ring|0VFW4Y69BT]]. Let $f \colon R \to S$ be a [[ring homomorphism|0GGE0Z0JQ1]] with $I \subseteq \ker f$, where $\ker f$ is the [[kernel|0AAHE7GEW6]].
2. For $a, b \in R$, $a + I = b + I$ if and only if $a - b \in I$. Indeed, if $a + I = b + I$, then $a = a + 0 \in b + I$, so $a = b + x$ with $x \in I$. Conversely, if $a - b = x \in I$, then $a + y = b + (x + y)$ and $b + y = a + (y - x)$ for $y \in I$, so the two cosets are equal.
3. The map $f$ satisfies $f(0) = 0$, since $f(0) = f(0 + 0) = f(0) + f(0)$. It also satisfies $f(-a) = -f(a)$, since $f(a) + f(-a) = f(0) = 0$. So $f(a - b) = f(a) - f(b)$.
4. Define $\bar{f}(a + I) = f(a)$. This does not depend on the choice of $a$. Indeed, if $a + I = b + I$, then $a - b \in I \subseteq \ker f$ by step 2. So $f(a) - f(b) = f(a - b) = 0$ by step 3.
5. The map $\bar{f}$ preserves addition: $\bar{f}((a + I) + (b + I)) = \bar{f}((a + b) + I) = f(a + b) = f(a) + f(b)$.
6. The map $\bar{f}$ preserves multiplication: $\bar{f}((a + I)(b + I)) = \bar{f}(a b + I) = f(a b) = f(a) f(b)$.
7. The identity of $R/I$ is $1 + I$, and $\bar{f}(1 + I) = f(1) = 1$. So $\bar{f}$ is a ring homomorphism.
8. For $a \in R$, $\bar{f}(\pi(a)) = \bar{f}(a + I) = f(a)$. So $\bar{f} \circ \pi = f$. This proves existence.
9. For uniqueness, let $g \colon R/I \to S$ be a ring homomorphism with $g \circ \pi = f$. Every element of $R/I$ is $a + I = \pi(a)$ for some $a \in R$.
10. Then $g(a + I) = g(\pi(a)) = f(a) = \bar{f}(a + I)$. So $g = \bar{f}$.
11. Hence there is exactly one ring homomorphism $\bar{f} \colon R/I \to S$ with $\bar{f} \circ \pi = f$, and it is given by $\bar{f}(a + I) = f(a)$.

## Idea

A homomorphism that kills $I$ takes the same value at all elements of a coset $a + I$. So it gives a well defined map on cosets. That map inherits the homomorphism rules from $f$, and it is forced on every coset because $\pi$ is surjective.
