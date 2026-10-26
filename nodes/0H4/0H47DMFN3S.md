---
tag: 0H47DMFN3S
kind: definition
name: Inner automorphism
aliases: [conjugation-automorphism]
msc: [20F28]
defines: 0RN00NTM3S
uses: [0CWXCWP0Y0, 0D1VWQGZZ7]
sources:
  - url: https://en.wikipedia.org/wiki/Inner_automorphism
    locator: Definition
---

## Definition

Let $G$ be a [[group|G5S1M9]] and let $g \in G$.
The inner automorphism given by $g$ is the map $c_g \colon G \to G$, $c_g(x) = gxg^{-1}$.
The set of all inner automorphisms of $G$ is written $\operatorname{Inn}(G)$.

## Remarks

Each $c_g$ is an [[automorphism|0K1SCPBNKJ]] of $G$, with inverse $c_{g^{-1}}$.
Since $c_g \circ c_h = c_{gh}$, the map $g \mapsto c_g$ is a homomorphism from $G$ to $\operatorname{Aut}(G)$, and $\operatorname{Inn}(G)$ is its image.
The subgroup $\operatorname{Inn}(G)$ is normal in $\operatorname{Aut}(G)$, because $\alpha \circ c_g \circ \alpha^{-1} = c_{\alpha(g)}$ for each automorphism $\alpha$.
In an [[abelian group|082GHNPJ53]], each inner automorphism is the identity map.

## Explanations

### L1 human

Each element of a group gives a symmetry of the group: conjugate everything by this element.
These symmetries are called inner, because they come from inside the group.
In a group where all elements commute, conjugation changes nothing.
