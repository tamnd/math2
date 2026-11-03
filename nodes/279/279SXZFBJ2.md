---
tag: 279SXZFBJ2
kind: definition
name: Left-invariant vector field
msc: ["22E60", "22E15"]
defines: SNA3DVPK0C
uses: [7JBRGCVJRB, 0299VCW1TH, 6P9PXQDSEN, 68FGQEBD6J, E7A5DHFT01]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_group
---

## Definition

Let $G$ be a [[Lie group|7JBRGCVJRB]] with identity $e$.
For $g \in G$, the *left translation* by $g$ is the diffeomorphism $L_g \colon G \to G$, $L_g(h) = gh$.
A [[vector field|0299VCW1TH]] $X$ on $G$ is *left-invariant* if
$$(dL_g)_h (X_h) = X_{gh} \quad \text{for all } g, h \in G,$$
where $(dL_g)_h$ is the [[differential|6P9PXQDSEN]] of $L_g$ at $h$.

## Remarks

Example: on $G = GL_n(\R)$, open in the space $M_n(\R)$ of matrices, fix $A \in M_n(\R)$ and put $X_g = gA$.
Left translation by $g$ is the linear map $h \mapsto gh$, so its differential is again $v \mapsto gv$, and $(dL_g)_h(X_h) = g h A = X_{gh}$.

Non-example: on the same group, the field $Y_g = Ag$ with $A \ne 0$ is not left-invariant in general.
For $n = 2$, $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $g = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}$, one gets $(dL_g)_e(Y_e) = gA \ne Ag = Y_g$.
It is right-invariant instead.

The map $X \mapsto X_e$ is a linear isomorphism from the space of left-invariant vector fields onto the [[tangent space|E7A5DHFT01]] $T_eG$; the inverse sends $v$ to the field $g \mapsto (dL_g)_e(v)$.
The [[Lie bracket|68FGQEBD6J]] of two left-invariant vector fields is left-invariant.
So $T_eG$ inherits a bracket, and with it becomes the [[Lie algebra|5JJYBJ6A8K]] of $G$, written $\mathfrak{g}$ or $\operatorname{Lie}(G)$.
Every left-invariant vector field is complete: its integral curves are defined on all of $\R$.
