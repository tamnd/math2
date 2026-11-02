---
tag: E0ZMRTA42A
kind: definition
name: Complexification of a Lie group
msc: ["22E15", "22E10"]
defines: DRYYK2WX0M
uses: [7JBRGCVJRB]
sources:
  - url: https://en.wikipedia.org/wiki/Complexification_(Lie_group)
---

## Definition

Let $G$ be a real [[Lie group|7JBRGCVJRB]].
A *complexification* (or universal complexification) of $G$ is a pair $(G_\C, \gamma)$ with two properties.

1. $G_\C$ is a complex Lie group and $\gamma \colon G \to G_\C$ is a continuous homomorphism.
2. For each complex Lie group $H$ and each continuous homomorphism $\varphi \colon G \to H$, there is exactly one holomorphic homomorphism $\psi \colon G_\C \to H$ with $\varphi = \psi \circ \gamma$.

## Remarks

By the universal property, a complexification is unique up to a unique isomorphism compatible with $\gamma$; it always exists.

Example: $G = \R$ with $G_\C = \C$ and $\gamma$ the inclusion.
A continuous homomorphism $\varphi \colon \R \to H$ is $\varphi(t) = \exp(tX)$ for some $X$ in the Lie algebra of $H$.
Then $\psi(z) = \exp(zX)$ is a holomorphic homomorphism extending $\varphi$.
It is the only one, since two holomorphic maps on $\C$ that agree on $\R$ are equal.

Non-example: $G = \R$ with $G_\C = \C^\times$ and $\gamma(t) = e^t$ fails clause 2.
Take $H = \C$ and $\varphi(t) = t$.
For a holomorphic homomorphism $\psi \colon \C^\times \to \C$, the map $z \mapsto \psi(e^z)$ is a holomorphic homomorphism $\C \to \C$, so $\psi(e^z) = cz$ for a constant $c$, and $c \cdot 2\pi i = \psi(1) = 0$ gives $\psi = 0$, so $\psi \circ \gamma \ne \varphi$.

The map $\gamma$ need not be injective.
For the universal cover $\widetilde{\mathrm{SL}}_2(\R)$, the complexification is $\mathrm{SL}_2(\C)$, and $\gamma$ is the covering map onto $\mathrm{SL}_2(\R)$, with infinite kernel.
For a compact Lie group $G$, the map $\gamma$ is injective, and $G$ is a maximal compact subgroup of $G_\C$.
