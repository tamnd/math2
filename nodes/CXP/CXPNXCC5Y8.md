---
tag: CXPNXCC5Y8
kind: proof
name: Proof of the universal property of the quotient group
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug1
proves: 0GJ83E78A5
methods: [0NTF6DMVAP, 01XM7JEKHY]
uses: [0KYX2N69J0, 0CB0DX5BVV, 03DEH43F4H, 0JYTG5K9Y4, 0W88CEGQP1, 0S21GNW9ZB]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_theorem_on_homomorphisms
    locator: Proof
  - url: https://en.wikipedia.org/wiki/Quotient_group
    locator: Properties
---

## Proof

We show that the formula $\bar{\varphi}(gN) = \varphi(g)$ is well defined and gives a homomorphism, that no other homomorphism works, and then we find the image and the kernel of $\bar{\varphi}$.

1. Let $N$ be a [[normal subgroup|0CB0DX5BVV]] of $G$, and let $\varphi \colon G \to H$ be a [[group homomorphism|0JYTG5K9Y4]] with $N \subseteq \ker \varphi$. Let $e_G$ and $e_H$ be the identities of $G$ and $H$.
2. Because $N$ is normal, the [[quotient group|0KYX2N69J0]] $G/N$ exists. Its elements are the [[left cosets|03DEH43F4H]] $gN$, its product is $(aN)(bN) = (ab)N$, and its identity is $e_G N = N$. This step uses the hypothesis that $N$ is normal.
3. The projection $\pi(g) = gN$ is surjective, because each coset $gN$ is $\pi(g)$. It is a homomorphism, because $\pi(ab) = (ab)N = (aN)(bN) = \pi(a)\pi(b)$ by step 2.
4. Let $g, g' \in G$ with $gN = g'N$. Since $e_G \in N$, we get $g' = g' e_G \in g'N = gN$. So $g' = gn$ for some $n \in N$.
5. By the hypothesis $N \subseteq \ker \varphi$, the element $n$ is in the [[kernel|0W88CEGQP1]], so $\varphi(n) = e_H$. Because $\varphi$ is a homomorphism, $\varphi(g') = \varphi(gn) = \varphi(g)\varphi(n) = \varphi(g)$. This step uses the hypothesis that $N \subseteq \ker \varphi$.
6. By steps 4 and 5, the value $\varphi(g)$ depends only on the coset $gN$. So the formula $\bar{\varphi}(gN) = \varphi(g)$ defines a map $\bar{\varphi} \colon G/N \to H$.
7. For $a, b \in G$, step 2 gives $\bar{\varphi}((aN)(bN)) = \bar{\varphi}((ab)N) = \varphi(ab) = \varphi(a)\varphi(b) = \bar{\varphi}(aN)\,\bar{\varphi}(bN)$. So $\bar{\varphi}$ is a group homomorphism. This step uses the hypothesis that $\varphi$ is a homomorphism.
8. For $g \in G$, we get $\bar{\varphi}(\pi(g)) = \bar{\varphi}(gN) = \varphi(g)$. So $\bar{\varphi} \circ \pi = \varphi$.
9. Let $\psi \colon G/N \to H$ be a group homomorphism with $\psi \circ \pi = \varphi$. By step 3, each element of $G/N$ is $\pi(g)$ for some $g \in G$, and $\psi(\pi(g)) = \varphi(g) = \bar{\varphi}(\pi(g))$. So $\psi = \bar{\varphi}$.
10. By steps 6 to 9, $\bar{\varphi}$ is the only homomorphism with $\bar{\varphi} \circ \pi = \varphi$. This proves part 1.
11. The [[image|0S21GNW9ZB]] of $\bar{\varphi}$ is $\{\bar{\varphi}(gN) : g \in G\} = \{\varphi(g) : g \in G\}$, which is the image of $\varphi$. This proves part 2.
12. For $g \in G$, we have $\bar{\varphi}(gN) = e_H$ if and only if $\varphi(g) = e_H$, that is, if and only if $g \in \ker \varphi$. So the kernel of $\bar{\varphi}$ is $\{kN : k \in \ker \varphi\} = (\ker \varphi)/N$. This proves part 3.
13. Now we prove the last claim. Let $\psi \colon G/N \to H$ be a homomorphism. Then $\psi \circ \pi$ is a homomorphism, because $\psi(\pi(ab)) = \psi(\pi(a)\pi(b)) = \psi(\pi(a))\,\psi(\pi(b))$ by step 3.
14. For $n \in N$, we get $nN = N$, because $n \in N$ and $N$ is a subgroup. So $\psi(\pi(n)) = \psi(N) = e_H$, because a homomorphism sends the identity $N$ of $G/N$ to $e_H$. Thus $N \subseteq \ker(\psi \circ \pi)$, and the map $\psi \mapsto \psi \circ \pi$ goes into the given set.
15. The map $\psi \mapsto \psi \circ \pi$ is injective. If $\psi \circ \pi = \psi' \circ \pi$, then $\psi$ and $\psi'$ agree on each $\pi(g)$, and by step 3 these are all the elements of $G/N$.
16. The map $\psi \mapsto \psi \circ \pi$ is surjective. For each homomorphism $\varphi$ with $N \subseteq \ker \varphi$, step 8 gives $\varphi = \bar{\varphi} \circ \pi$.
17. By steps 13 to 16, the map $\psi \mapsto \psi \circ \pi$ is a bijection onto the homomorphisms $\varphi \colon G \to H$ with $N \subseteq \ker \varphi$.

This proves all parts of the theorem.

## Idea

Two elements in the same coset differ by an element of $N$, and $\varphi$ sends that element to the identity.
So $\varphi$ takes one value on each coset, and this value defines $\bar{\varphi}$.
Uniqueness holds because $\pi$ is surjective: every coset is $\pi(g)$, so the value on it must be $\varphi(g)$.
The image and the kernel of $\bar{\varphi}$ follow directly from the formula $\bar{\varphi}(gN) = \varphi(g)$.

## Variants

An equivalent check of well definedness uses the criterion $gN = g'N$ if and only if $g^{-1}g' \in N$.
Then $\varphi(g)^{-1}\varphi(g') = \varphi(g^{-1}g') = e_H$, so $\varphi(g) = \varphi(g')$.
