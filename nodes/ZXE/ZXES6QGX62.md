---
tag: ZXES6QGX62
kind: proof
name: Proof of the cancellation laws
msc: [20A05]
topics: [BAZT8JJ70S]
audience: ug1
proves: 0VSNX4P2Q0
uses: [G5S1M9, 0ZNZH0EXFX, 0K8F7PVDMX]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Group_(mathematics)
    locator: Division
---

## Proof

Let $G$ be a [[group|G5S1M9]] with identity $e$.

Part 1.

1. Let $a, b, c \in G$ with $ab = ac$. Multiply both sides on the left by the [[inverse|0ZNZH0EXFX]] $a^{-1}$. This gives $a^{-1}(ab) = a^{-1}(ac)$. Reason: equal elements have equal products with $a^{-1}$.
2. Then $(a^{-1} a) b = (a^{-1} a) c$. Reason: [[associativity|0K8F7PVDMX]].
3. Then $eb = ec$, so $b = c$. Reason: $a^{-1} a = e$, and $e$ is an identity.

Part 2.

4. Let $a, b, c \in G$ with $ba = ca$. Multiply both sides on the right by $a^{-1}$. This gives $(ba) a^{-1} = (ca) a^{-1}$.
5. Then $b(a a^{-1}) = c(a a^{-1})$, so $be = ce$ and $b = c$. Reason: associativity, $a a^{-1} = e$, and $e$ is an identity.

Part 3.

6. Let $a, b \in G$ and put $x = a^{-1} b$. Then $ax = a(a^{-1} b) = (a a^{-1}) b = eb = b$. Reason: associativity, $a a^{-1} = e$, and $e$ is an identity. So $x$ is a solution of $ax = b$.
7. Let $x'$ be any solution, so $ax' = b = ax$. By part 1, $x' = x$. So the solution is unique.
8. Put $y = b a^{-1}$. Then $ya = (b a^{-1}) a = b (a^{-1} a) = be = b$. Reason: associativity, $a^{-1} a = e$, and $e$ is an identity.
9. Let $y'$ be any solution, so $y' a = b = ya$. By part 2, $y' = y$. $\blacksquare$

## Idea

Multiply both sides of the equation by the inverse of the common factor, on the same side as that factor.
Associativity moves the inverse next to the factor, and the two cancel to $e$.
For the equation $ax = b$, the candidate $a^{-1} b$ works, and cancellation shows that no other element works.
