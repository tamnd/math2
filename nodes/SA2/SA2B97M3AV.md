---
tag: SA2B97M3AV
kind: proof
name: Proof of the classification of cyclic groups
msc: ["20A05"]
topics: [BAVE5RN4EE]
audience: ug1
proves: 0736AXH2ME
uses: [0KVGH0J5B3, 08ABT85339, 0B85S2V2DR, 0WE2NHZJ7B, 031M8HX7DA, 00DRK90Z6K, 08MG7H8JW5, FB79N7AHZA, 02B1T50JD1]
methods: [0NTF6DMVAP, 0WCP0PVET6]
sources:
  - url: https://proofwiki.org/wiki/Cyclic_Groups_of_Same_Order_are_Isomorphic
  - url: https://kconrad.math.uconn.edu/blurbs/grouptheory/cyclicgp.pdf
    locator: Section 4
---

## Proof

We prove part 2 first, and then deduce part 1.

Part 2: cyclic groups of the same order are isomorphic.

1. Let $G = \langle g \rangle$ and $H = \langle h \rangle$ be [[cyclic groups|0KVGH0J5B3]] with $|G| = |H|$. Write $e$ for the identity of each group. So $G = \{g^k : k \in \mathbb{Z}\}$ and $H = \{h^k : k \in \mathbb{Z}\}$, by the definition of the [[cyclic subgroup|08ABT85339]].
2. By [[the theorem on the order of $\langle g \rangle$|031M8HX7DA]], the [[order|0B85S2V2DR]] of $G$ equals the [[order|0WE2NHZJ7B]] of $g$, and the order of $H$ equals the order of $h$.
3. So either $g$ and $h$ both have the same finite order $n$, or both have infinite order.
4. Claim: for all $a, b \in \mathbb{Z}$, $g^a = g^b$ if and only if $h^a = h^b$.
5. Proof of the claim in the finite case. By the same theorem, $g^a = g^b$ if and only if $n$ divides $a - b$, and $h^a = h^b$ if and only if $n$ divides $a - b$. So the two conditions agree.
6. Proof of the claim in the infinite case. By the same theorem, $g^a = g^b$ if and only if $a = b$, and $h^a = h^b$ if and only if $a = b$. So the two conditions agree.
7. Define $\varphi \colon G \to H$ by $\varphi(g^k) = h^k$. An element $x \in G$ can be $g^a$ and $g^b$ with $a \neq b$. Then $h^a = h^b$ by the claim, so $\varphi(x)$ does not depend on the choice of the exponent.
8. The map $\varphi$ is injective: if $h^a = h^b$, then $g^a = g^b$ by the claim.
9. The map $\varphi$ is surjective: each element of $H$ is $h^k = \varphi(g^k)$ for some $k$.
10. The map $\varphi$ preserves products: for $x = g^a$ and $y = g^b$, the [[laws of exponents|00DRK90Z6K]] give $\varphi(xy) = \varphi(g^{a+b}) = h^{a+b} = h^a h^b = \varphi(x)\varphi(y)$.
11. By steps 8 to 10, $\varphi$ is a [[group isomorphism|08MG7H8JW5]]. This proves part 2.

Part 1: each cyclic group is isomorphic to $\mathbb{Z}$ or to $\mathbb{Z}/n\mathbb{Z}$.

12. The group $(\mathbb{Z}, +)$ is [[cyclic with generator $1$|02B1T50JD1]], and it is infinite.
13. For $n \geq 1$, the group $(\mathbb{Z}/n\mathbb{Z}, +)$ is [[cyclic with generator $1$|FB79N7AHZA]], and it has order $n$.
14. Let $G$ be cyclic. If $G$ is infinite, then $G$ and $\mathbb{Z}$ are cyclic groups of the same order, so $G \cong \mathbb{Z}$ by part 2.
15. If $G$ has finite order $n$, then $G$ and $\mathbb{Z}/n\mathbb{Z}$ are cyclic groups of order $n$, so $G \cong \mathbb{Z}/n\mathbb{Z}$ by part 2. This proves part 1.
16. No two of the groups $\mathbb{Z}, \mathbb{Z}/1\mathbb{Z}, \mathbb{Z}/2\mathbb{Z}, \ldots$ are isomorphic, because an isomorphism is a bijection and these groups have different orders. $\blacksquare$

## Idea

Each element of a cyclic group is a power of the generator.
The only question is when two exponents give the same element, and the answer depends only on the order of the group.
So "send $g^k$ to $h^k$" is a well-defined bijection, and it preserves products because exponents add.
Part 1 then follows by comparing each cyclic group with the model $\mathbb{Z}$ or $\mathbb{Z}/n\mathbb{Z}$ of the same order.

## Variants

Part 1 has a direct proof with homomorphisms.
The map $\psi \colon \mathbb{Z} \to G$, $\psi(k) = g^k$, is a surjective [[group homomorphism|0JYTG5K9Y4]].
Its kernel is a subgroup of $\mathbb{Z}$, so it is $n\mathbb{Z}$ for one $n \geq 0$, by [[the classification of subgroups of the integers|0SRATCFF1W]].
The [[first isomorphism theorem|0CXXJNG5B6]] gives $G \cong \mathbb{Z}/n\mathbb{Z}$, which is $\mathbb{Z}$ when $n = 0$.
Part 2 then follows: two cyclic groups of the same order are both isomorphic to the same model, and a composite of isomorphisms is an isomorphism.
