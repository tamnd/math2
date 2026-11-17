---
tag: RW1ZF04CRF
kind: proof
name: Proof of the uniqueness of identity and inverses
msc: [20A05]
topics: [BAZT8JJ70S]
audience: ug1
proves: 0D9NDGE9KP
uses: [G5S1M9, 07WYQPB8E3, 0ZNZH0EXFX, 0K8F7PVDMX]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Group_(mathematics)
    locator: Uniqueness of inverses
  - book: isbn:9780471433347
    locator: Section 1.1
---

## Proof

Let $G$ be a [[group|G5S1M9]] with [[identity|07WYQPB8E3]] $e$, and let $a, b \in G$.
We use the group axioms in the form $ex = x = xe$ and $x x^{-1} = e = x^{-1} x$ for all $x \in G$.

Part 1.

1. Let $f \in G$ with $fx = x$ for all $x$. Put $x = e$: then $fe = e$. Reason: hypothesis on $f$.
2. Also $fe = f$. Reason: $e$ is an identity.
3. By steps 1 and 2, $f = fe = e$.
4. Let $f \in G$ with $xf = x$ for all $x$. Put $x = e$: then $ef = e$. Since $e$ is an identity, also $ef = f$. So $f = ef = e$.

Part 2.

5. Suppose that $ab = e$. We have $b = eb = (a^{-1} a) b$. Reason: $e$ is an identity, and $a^{-1} a = e$.
6. We have $(a^{-1} a) b = a^{-1} (ab)$. Reason: [[associativity|0K8F7PVDMX]].
7. We have $a^{-1} (ab) = a^{-1} e = a^{-1}$. Reason: $ab = e$, and $e$ is an identity.
8. By steps 5 to 7, $b = a^{-1}$.
9. We have $a = ae = a (b b^{-1})$. Reason: $e$ is an identity, and $b b^{-1} = e$.
10. We have $a (b b^{-1}) = (ab) b^{-1} = e b^{-1} = b^{-1}$. Reason: associativity, $ab = e$, and $e$ is an identity.
11. By steps 9 and 10, $a = b^{-1}$.
12. If $b$ and $c$ are both [[inverses|0ZNZH0EXFX]] of $a$, then $ab = e$ and $ac = e$. By step 8, $b = a^{-1}$ and $c = a^{-1}$, so $b = c$. Thus $a$ has exactly one inverse.

Part 3.

13. We have $a^{-1} a = e$. Reason: definition of $a^{-1}$.
14. Apply part 2 to the pair $a^{-1}$, $a$ in place of $a$, $b$. It gives $a = (a^{-1})^{-1}$.

Part 4.

15. We have $(ab)(b^{-1} a^{-1}) = a(b(b^{-1} a^{-1}))$. Reason: associativity, with the three elements $a$, $b$ and $b^{-1} a^{-1}$.
16. We have $b(b^{-1} a^{-1}) = (b b^{-1}) a^{-1} = e a^{-1} = a^{-1}$. Reason: associativity, $b b^{-1} = e$, and $e$ is an identity.
17. By steps 15 and 16, $(ab)(b^{-1} a^{-1}) = a a^{-1} = e$.
18. Apply part 2 to the pair $ab$, $b^{-1} a^{-1}$. It gives $b^{-1} a^{-1} = (ab)^{-1}$. $\blacksquare$

## Idea

Two identities $f$ and $e$ meet in the product $fe$, which equals both of them.
For inverses, we multiply $ab = e$ on the left by $a^{-1}$ and use associativity to isolate $b$.
Parts 3 and 4 then follow from part 2: we only need to show one product equal to $e$.
