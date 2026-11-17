---
tag: XYK4DFM5WC
kind: proof
name: Proof of the subgroup criterion
msc: ["20A05"]
topics: [BAVE5RN4EE]
audience: ug1
proves: 05N4TQKPH0
uses: [G5S1M9, 0X1JXT47GA, 0D9NDGE9KP, 00DRK90Z6K, 0VSNX4P2Q0]
methods: [0NTF6DMVAP]
sources:
  - url: https://proofwiki.org/wiki/One-Step_Subgroup_Test
  - url: https://en.wikipedia.org/wiki/Subgroup
    locator: Subgroup tests
---

## Proof

Let $G$ be a [[group|G5S1M9]] with identity $e$, and let $H \subseteq G$.
A [[subgroup|0X1JXT47GA]] is a subset that contains $e$ and is closed under products and inverses.

Part 2, the two-step test.

1. Suppose $H$ is a subgroup. Then $e \in H$, so $H \neq \emptyset$. Closure under products and inverses holds by the definition.
2. Conversely, suppose $H \neq \emptyset$ and $H$ is closed under products and inverses. Choose $a \in H$.
3. By closure under inverses, $a^{-1} \in H$. By closure under products, $e = aa^{-1} \in H$.
4. So $H$ contains $e$ and is closed under products and inverses. Thus $H$ is a subgroup.

Part 1, the one-step test.

5. Suppose $H$ is a subgroup, and let $a, b \in H$. Then $b^{-1} \in H$, and $ab^{-1} \in H$ by closure under products. Also $H \neq \emptyset$ by step 1.
6. Conversely, suppose $H \neq \emptyset$ and $ab^{-1} \in H$ for all $a, b \in H$. Choose $a \in H$.
7. The pair $(a, a)$ gives $e = aa^{-1} \in H$.
8. Let $b \in H$. The pair $(e, b)$ gives $eb^{-1} = b^{-1} \in H$. So $H$ is closed under inverses.
9. Let $a, b \in H$. By step 8, $b^{-1} \in H$. The pair $(a, b^{-1})$ gives $a(b^{-1})^{-1} \in H$.
10. By the [[uniqueness of inverses|0D9NDGE9KP]], $(b^{-1})^{-1} = b$, because $b^{-1} b = e$. So $ab \in H$, and $H$ is closed under products.
11. By steps 6 to 10, $H$ is nonempty and closed under products and inverses. By part 2, $H$ is a subgroup.

Part 3, the finite test.

12. Suppose $H$ is a subgroup. Then $H$ is closed under products by the definition.
13. Conversely, suppose $H$ is finite, $H \neq \emptyset$, and $ab \in H$ for all $a, b \in H$. Let $a \in H$.
14. By closure and induction on $k$, the power $a^k$ lies in $H$ for each integer $k \geq 1$: $a^1 = a$, and $a^{k+1} = a^k a$.
15. The powers $a^1, a^2, \ldots$ form an infinite list of elements of the finite set $H$. So there are integers $1 \leq i < j$ with $a^i = a^j$.
16. By the [[laws of exponents|00DRK90Z6K]], $a^j = a^i a^{j-i}$. So $a^i a^{j-i} = a^i e$, and the [[cancellation law|0VSNX4P2Q0]] gives $a^{j-i} = e$.
17. Put $m = j - i$, so $m \geq 1$ and $a^m = e$. By step 14, $e = a^m \in H$.
18. If $m = 1$, then $a = e$ and $a^{-1} = e \in H$. If $m \geq 2$, then $a \cdot a^{m-1} = a^m = e$, so $a^{-1} = a^{m-1}$ by the uniqueness of inverses. This power lies in $H$ by step 14, since $m - 1 \geq 1$.
19. So $H$ is nonempty and closed under products and inverses. By part 2, $H$ is a subgroup.

This proves the three tests.
$\blacksquare$

## Idea

The two-step test only drops the identity condition, because $e = aa^{-1}$ for any $a \in H$.
The one-step condition $ab^{-1} \in H$ contains the three conditions: use it with $a = b$ to get $e$, with $a = e$ to get inverses, and with $b^{-1}$ in place of $b$ to get products.
In the finite test, the powers of an element must repeat, so some positive power $a^m$ is $e$, and then $a^{-1} = a^{m-1}$ is a positive power that closure provides.

## Variants

The finite test can also be proved with a counting argument.
For $a \in H$, the map $x \mapsto ax$ from $H$ to $H$ is injective by cancellation, so it is surjective because $H$ is finite.
So $ax = a$ for some $x \in H$, which gives $x = e \in H$, and $ay = e$ for some $y \in H$, which gives $y = a^{-1} \in H$.
