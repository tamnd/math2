---
tag: CXPNXCC5Y8
kind: proof
name: Proof of the universal property of the quotient group
msc: [20A05]
proves: 0GJ83E78A5
uses: [0YYWCNTPWR, 0W77CVBCHQ, 05FD317V2W, 0HV9Y7WG5R, 0Z424HK8CQ]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_theorem_on_homomorphisms
    locator: Group-theoretic version
---

## Proof

We show that the formula $\bar{\varphi}(gN) = \varphi(g)$ is well defined, that it gives a homomorphism, and that no other homomorphism works.

1. Let $N$ be a [[normal subgroup|0W77CVBCHQ]] of $G$, and let $\varphi \colon G \to H$ be a [[group homomorphism|0HV9Y7WG5R]] with $N \subseteq \ker \varphi$. Let $e_G$ and $e_H$ be the identities.
2. The [[quotient group|0YYWCNTPWR]] $G/N$ is the set of [[left cosets|05FD317V2W]] $gN$, with $(aN)(bN) = (ab)N$. The projection is $\pi(g) = gN$.
3. Let $g, g' \in G$ with $gN = g'N$. Since $e_G \in N$, $g' = g' e_G \in g'N = gN$. So $g' = gn$ for some $n \in N$.
4. By step 1, $n \in \ker \varphi$, so $\varphi(n) = e_H$ by the definition of the [[kernel|0Z424HK8CQ]]. Hence $\varphi(g') = \varphi(g) \varphi(n) = \varphi(g)$.
5. By steps 3 and 4, the value $\varphi(g)$ depends only on the coset $gN$. So $\bar{\varphi}(gN) = \varphi(g)$ is a well defined map $\bar{\varphi} \colon G/N \to H$.
6. For $a, b \in G$, step 2 gives $\bar{\varphi}((aN)(bN)) = \bar{\varphi}((ab)N) = \varphi(ab) = \varphi(a) \varphi(b) = \bar{\varphi}(aN) \bar{\varphi}(bN)$. So $\bar{\varphi}$ is a group homomorphism.
7. For $g \in G$, $\bar{\varphi}(\pi(g)) = \bar{\varphi}(gN) = \varphi(g)$. So $\bar{\varphi} \circ \pi = \varphi$, and a homomorphism with this property exists.
8. Let $\psi \colon G/N \to H$ be any group homomorphism with $\psi \circ \pi = \varphi$. Each element of $G/N$ has the form $gN = \pi(g)$ for some $g \in G$.
9. For such an element, $\psi(gN) = \psi(\pi(g)) = \varphi(g) = \bar{\varphi}(gN)$. So $\psi = \bar{\varphi}$.
10. By steps 5 to 9, there is exactly one homomorphism $\bar{\varphi}$ with $\bar{\varphi} \circ \pi = \varphi$, and it is given by $\bar{\varphi}(gN) = \varphi(g)$.

## Idea

Two elements in the same coset differ by an element of $N$, and $\varphi$ sends that element to the identity. So $\varphi$ takes one value on each coset, which defines $\bar{\varphi}$. Uniqueness holds because $\pi$ is surjective: every coset is $\pi(g)$, so the value on it is forced to be $\varphi(g)$.
