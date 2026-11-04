---
tag: 93WSVFTZPJ
kind: proof
name: Proof that the inner automorphism group is isomorphic to G modulo its centre
msc: [20F28]
proves: 05HYGWFG63
uses: [0H47DMFN3S, 0S7Y9Q990Q, 0CWXCWP0Y0, 0HV9Y7WG5R, 01VG2A0BHW, 0D9NDGE9KP, 0Z424HK8CQ, 0CXXJNG5B6]
sources:
  - url: https://proofwiki.org/wiki/Inner_Automorphism_Group_is_Isomorphic_to_Quotient_Group_with_Center
---

## Proof

We apply the first isomorphism theorem to the map $g \mapsto c_g$.

1. Let $G$ be a group with identity $e$. For $g \in G$, let $c_g \colon G \to G$, $c_g(x) = gxg^{-1}$, be the [[inner automorphism|0H47DMFN3S]] given by $g$.
2. For $g, h \in G$, $(gh)(h^{-1}g^{-1}) = e$. By the [[uniqueness of inverses|0D9NDGE9KP]], $(gh)^{-1} = h^{-1}g^{-1}$.
3. For $g, h, x \in G$, step 2 gives $c_g(c_h(x)) = ghxh^{-1}g^{-1} = (gh)x(gh)^{-1} = c_{gh}(x)$. So $c_g \circ c_h = c_{gh}$.
4. The map $c_e$ is the identity of $G$. By step 3, $c_g \circ c_{g^{-1}} = c_{g^{-1}} \circ c_g = c_e$, so $c_g$ is [[bijective|01VG2A0BHW]].
5. For $x, y \in G$, $c_g(x) c_g(y) = gxg^{-1}gyg^{-1} = gxyg^{-1} = c_g(xy)$. So $c_g$ is a [[group homomorphism|0HV9Y7WG5R]].
6. By steps 4 and 5, each $c_g$ lies in the [[automorphism group|0CWXCWP0Y0]] $\operatorname{Aut}(G)$, whose operation is composition.
7. By step 3, the map $c \colon G \to \operatorname{Aut}(G)$, $g \mapsto c_g$, is a group homomorphism. Its image is the set $\operatorname{Inn}(G)$ of all inner automorphisms.
8. The identity of $\operatorname{Aut}(G)$ is $c_e$, the identity map. So $g$ lies in the [[kernel|0Z424HK8CQ]] of $c$ exactly when $gxg^{-1} = x$ for all $x \in G$.
9. Multiplying on the right by $g$ or by $g^{-1}$ shows that $gxg^{-1} = x$ holds exactly when $gx = xg$.
10. By steps 8 and 9, $\ker c = \{g \in G : gx = xg \text{ for all } x \in G\}$. This is the [[centre|0S7Y9Q990Q]] $Z(G)$.
11. By the [[first isomorphism theorem|0CXXJNG5B6]], the map $gZ(G) \mapsto c_g$ is an isomorphism from $G/Z(G)$ onto $\operatorname{im} c = \operatorname{Inn}(G)$.

## Idea

Conjugation turns each element $g$ into an automorphism $c_g$, and $c_g c_h = c_{gh}$, so this is a homomorphism onto $\operatorname{Inn}(G)$. The elements that give the trivial conjugation are those that commute with everything, which is the centre. Dividing out the kernel gives the isomorphism.
