---
tag: FGD9THSJ04
kind: proof
name: Proof of von Dyck's theorem
msc: [20F05]
proves: 0QPYHHNRXC
uses: [0QZCY9PE3Q, 0CDWKDYWN6, 0GJ83E78A5, 0Z424HK8CQ, 0C9ZKYSPYR, 0HV9Y7WG5R]
sources:
  - url: https://en.wikipedia.org/wiki/Presentation_of_a_group
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Free_group
    locator: Universal property
---

## Proof

1. By the definition of a [[presentation|0QZCY9PE3Q]], $G = F_S/N$, where $N$ is the smallest normal subgroup of $F_S$ that contains $R$. Let $\pi \colon F_S \to G$ be the projection $\pi(w) = wN$.
2. The homomorphism $\varphi$ exists and is unique, by the [[universal property of the free group|0CDWKDYWN6]].
3. By hypothesis, $\varphi(r) = e$ for each $r \in R$. So $R \subseteq \ker \varphi$, the [[kernel|0Z424HK8CQ]] of $\varphi$.
4. Since [[the kernel is a normal subgroup|0C9ZKYSPYR]], $\ker \varphi$ is a normal subgroup of $F_S$ that contains $R$. Since $N$ is the smallest one, $N \subseteq \ker \varphi$.
5. By the [[universal property of the quotient group|0GJ83E78A5]], there is a [[group homomorphism|0HV9Y7WG5R]] $\psi \colon G \to H$ with $\psi(wN) = \varphi(w)$ for each $w \in F_S$.
6. In particular, $\psi(sN) = \varphi(s) = f(s)$ for each $s \in S$. This proves existence.
7. For uniqueness, let $\psi' \colon G \to H$ be a homomorphism with $\psi'(sN) = f(s)$ for each $s \in S$.
8. Then $\psi' \circ \pi \colon F_S \to H$ is a homomorphism with $(\psi' \circ \pi)(s) = f(s)$ for each $s \in S$.
9. By the uniqueness part of the universal property of the free group, $\psi' \circ \pi = \varphi$.
10. So $\psi'(wN) = \varphi(w) = \psi(wN)$ for each $w \in F_S$. Every element of $G$ has the form $wN$, so $\psi' = \psi$.

## Idea

The homomorphism $\varphi$ kills every relator, so it kills the normal subgroup they generate. Hence $\varphi$ factors through the quotient $F_S/N = G$. Uniqueness follows from uniqueness for free groups. Two homomorphisms that agree on the cosets $sN$ give the same map on $F_S$, so they agree on $G$.
