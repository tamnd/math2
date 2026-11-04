---
tag: PZPPAXYD3G
kind: proof
name: Proof of Cayley's theorem by left multiplication
msc: [20B30]
proves: 0151VYVX27
uses: [0K5TWJAGPD, 0RJMNEN3BJ, 0HV9Y7WG5R, 0N0PXCTYA7, 085PND4KNT]
sources:
  - url: https://en.wikipedia.org/wiki/Cayley's_theorem
    locator: Proof of the theorem
---

## Proof

We use the [[action of $G$ on itself by left multiplication|0K5TWJAGPD]]. Let $e$ be the identity of $G$, and for $g \in G$ let $\ell_g \colon G \to G$, $\ell_g(x) = g x$.

1. For $g, h, x \in G$, associativity gives $\ell_g(\ell_h(x)) = g(hx) = (gh)x = \ell_{gh}(x)$. So $\ell_g \circ \ell_h = \ell_{gh}$.
2. Also $\ell_e(x) = ex = x$, so $\ell_e$ is the identity map of $G$.
3. By steps 1 and 2, $\ell_g \circ \ell_{g^{-1}} = \ell_e$ and $\ell_{g^{-1}} \circ \ell_g = \ell_e$. So $\ell_g$ is a bijection with inverse $\ell_{g^{-1}}$, and $\ell_g \in \operatorname{Sym}(G)$, the [[symmetric group|0RJMNEN3BJ]] of $G$.
4. Let $\varphi \colon G \to \operatorname{Sym}(G)$, $\varphi(g) = \ell_g$. The operation of $\operatorname{Sym}(G)$ is composition, so step 1 says $\varphi(gh) = \varphi(g) \circ \varphi(h)$. Thus $\varphi$ is a [[group homomorphism|0HV9Y7WG5R]].
5. If $\varphi(g) = \varphi(h)$, then $g = \ell_g(e) = \ell_h(e) = h$. So $\varphi$ is injective.
6. Let $K = \set{\ell_g : g \in G}$ be the image of $\varphi$. By steps 1 to 3, $K$ contains the identity $\ell_e$, is closed under composition, and contains the inverse $\ell_{g^{-1}}$ of each $\ell_g$. So $K$ is a [[subgroup|0N0PXCTYA7]] of $\operatorname{Sym}(G)$.
7. As a map $G \to K$, $\varphi$ is a homomorphism, injective by step 5 and onto by the definition of $K$. So it is an [[isomorphism|085PND4KNT]], and $G$ is isomorphic to the subgroup $K$ of $\operatorname{Sym}(G)$.

## Idea

Each element $g$ shuffles the elements of the group by $x \mapsto g x$. Composing two shuffles corresponds to multiplying the elements, and different elements give different shuffles because they send $e$ to different places. So the group sits faithfully inside the permutations of its own elements.
