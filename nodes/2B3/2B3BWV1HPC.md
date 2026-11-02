---
tag: 2B3BWV1HPC
kind: definition
name: Adjoint representation of a Lie group
msc: ["22E60", "22E15"]
defines: P6ZP0TE07M
uses: [7JBRGCVJRB, 0RN00NTM3S, 6P9PXQDSEN, E7A5DHFT01, WYGRXCG2RN]
sources:
  - url: https://en.wikipedia.org/wiki/Adjoint_representation
---

## Definition

Let $G$ be a [[Lie group|7JBRGCVJRB]] with identity $e$ and Lie algebra $\mathfrak{g} = T_eG$, the [[tangent space|E7A5DHFT01]] at $e$.
For $g \in G$, let $C_g \colon G \to G$, $C_g(h) = g h g^{-1}$, be the [[inner automorphism|0RN00NTM3S]] given by $g$.
Since $C_g(e) = e$, its [[differential|6P9PXQDSEN]] at $e$ is a linear map $\operatorname{Ad}(g) = (dC_g)_e \colon \mathfrak{g} \to \mathfrak{g}$.
The *adjoint representation* of $G$ is the map
$$\operatorname{Ad} \colon G \to GL(\mathfrak{g}), \qquad g \mapsto \operatorname{Ad}(g).$$

## Remarks

From $C_{gh} = C_g \circ C_h$ and the chain rule, $\operatorname{Ad}(gh) = \operatorname{Ad}(g)\operatorname{Ad}(h)$, so $\operatorname{Ad}$ is a [[representation|WYGRXCG2RN]]; it is also smooth.

Example: for $G = GL_n(\R)$ and $\mathfrak{g} = M_n(\R)$, the map $C_g$ is the restriction of the linear map $X \mapsto g X g^{-1}$ of $M_n(\R)$.
So $\operatorname{Ad}(g)X = g X g^{-1}$.

Non-example: the map $g \mapsto (dL_g)_e$, with $L_g(h) = gh$, does not define a representation on $\mathfrak{g}$.
For $g \ne e$, $L_g$ does not fix $e$, so $(dL_g)_e$ sends $T_eG$ to $T_gG$, not to $\mathfrak{g}$.

The differential of $\operatorname{Ad}$ at $e$ is the adjoint representation $\operatorname{ad}$ of the Lie algebra $\mathfrak{g}$, given by $\operatorname{ad}(X)(Y) = [X, Y]$.
The two are related by $\operatorname{Ad}(\exp X) = e^{\operatorname{ad} X}$, and $g \exp(X) g^{-1} = \exp(\operatorname{Ad}(g)X)$.
