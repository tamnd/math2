---
tag: ~73adfcd7
kind: definition
name: Kernel of a homomorphism
aliases: [kernel-of-a-group-homomorphism]
msc: [20A05]
defines: ~695eca04
uses: [~f060c64f]
sources:
  - url: https://en.wikipedia.org/wiki/Kernel_(algebra)
    locator: Group homomorphisms
---

## Definition

Let $G$ and $H$ be [[groups|G5S1M9]], let $e_H$ be the identity element of $H$, and let $\varphi \colon G \to H$ be a [[group homomorphism|~c666c876]].
The kernel of $\varphi$ is the set $\ker \varphi = \{g \in G : \varphi(g) = e_H\}$.

## Remarks

The kernel is a [[normal subgroup|~ebf813cb]] of $G$.
The kernel of the map $\mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$, $k \mapsto k + n\mathbb{Z}$, is $n\mathbb{Z}$.
The kernel of the determinant map from $\mathrm{GL}_n(\mathbb{R})$ to $\mathbb{R}^\times$ is the special linear group $\mathrm{SL}_n(\mathbb{R})$.

## Explanations

### L1 human

The kernel is the part of the group that the homomorphism forgets: everything in it goes to the identity.
If the kernel is only the identity, the homomorphism forgets nothing, and it is injective.
For the map that sends an integer to its remainder modulo $3$, the kernel is the set of multiples of $3$.
