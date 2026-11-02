---
tag: 5S1R5AVKZ6
kind: definition
name: Bicategory
msc: [18N10]
defines: TAHV24ED74
uses: [A2DE66937D, 28NQ0KRHD3, KYCPCC57FT, M3MSQ3NKAE, CQACXG10JZ]
sources:
  - url: https://en.wikipedia.org/wiki/2-category
---

## Definition

A *bicategory* $\mathcal{B}$ consists of:

1. a class of objects;
2. for each pair of objects $a, b$, a [[category|A2DE66937D]] $\mathcal{B}(a, b)$ of 1-morphisms $f \colon a \to b$ and 2-morphisms $\theta \colon f \Rightarrow g$;
3. for each triple $a, b, c$, a [[functor|28NQ0KRHD3]] $\circ \colon \mathcal{B}(b, c) \times \mathcal{B}(a, b) \to \mathcal{B}(a, c)$, called horizontal composition;
4. for each object $a$, an identity 1-morphism $1_a \in \mathcal{B}(a, a)$;
5. invertible 2-morphisms $\alpha_{h,g,f} \colon (h \circ g) \circ f \Rightarrow h \circ (g \circ f)$, $\lambda_f \colon 1_b \circ f \Rightarrow f$ and $\rho_f \colon f \circ 1_a \Rightarrow f$, [[natural|KYCPCC57FT]] in $f$, $g$, $h$.

These data satisfy, for all composable $f \colon a \to b$, $g \colon b \to c$, $h \colon c \to d$, $k \colon d \to e$:

1. pentagon: $(1_k \circ \alpha_{h,g,f}) \cdot \alpha_{k, h \circ g, f} \cdot (\alpha_{k,h,g} \circ 1_f) = \alpha_{k,h,g \circ f} \cdot \alpha_{k \circ h, g, f}$;
2. triangle: $(1_g \circ \lambda_f) \cdot \alpha_{g, 1_b, f} = \rho_g \circ 1_f$.

Here $\cdot$ is vertical composition in the hom-categories, and $1_f$ also denotes the identity 2-morphism of $f$.

## Remarks

Example: the bicategory $\mathbf{Bim}$ has rings as objects, $S$-$R$-bimodules as 1-morphisms $R \to S$, and bimodule maps as 2-morphisms.
Its horizontal composition is $N \circ M = N \otimes_S M$, its identity is $1_R = R$, and $\alpha$, $\lambda$, $\rho$ are the usual isomorphisms of tensor products.
The pentagon and triangle hold because, on elementary tensors, both sides of each identity give the same rebracketed tensor.
Non-example: in the same data, replace each identity $1_R$ by the zero bimodule; then $0 \otimes_R M = 0$, which is not isomorphic to a nonzero $M$, so no unitor $\lambda_M$ exists.
A one-object bicategory is the same as a [[monoidal category|M3MSQ3NKAE]], and a bicategory whose $\alpha$, $\lambda$, $\rho$ are identities is a [[2-category|CQACXG10JZ]].
