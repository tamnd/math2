---
tag: JBVKKDXETM
kind: definition
name: Equivalence of categories
msc: [18A22, 18A05]
defines: K7A04ZBD92
uses: [28NQ0KRHD3, KYCPCC57FT, 000AYPA9AJ]
sources:
  - url: https://en.wikipedia.org/wiki/Equivalence_of_categories
---

## Definition

Let $\mathcal{C}$ and $\mathcal{D}$ be categories.
A [[functor|28NQ0KRHD3]] $F \colon \mathcal{C} \to \mathcal{D}$ is an *equivalence of categories* if there are a functor $G \colon \mathcal{D} \to \mathcal{C}$ and [[natural isomorphisms|KYCPCC57FT]] $\eta \colon 1_{\mathcal{C}} \Rightarrow G \circ F$ and $\varepsilon \colon F \circ G \Rightarrow 1_{\mathcal{D}}$.
Then $G$ is a *quasi-inverse* of $F$, and $\mathcal{C}$ and $\mathcal{D}$ are *equivalent*, written $\mathcal{C} \simeq \mathcal{D}$.

## Remarks

If moreover $G \circ F = 1_{\mathcal{C}}$ and $F \circ G = 1_{\mathcal{D}}$, then $F$ is an *isomorphism of categories*, a much stronger condition.
Example: let $K$ be a field and let $\mathbf{Mat}_K$ have the natural numbers as objects, the $n \times m$ matrices over $K$ as morphisms $m \to n$, and matrix multiplication as composition.
The functor $\mathbf{Mat}_K \to$ (finite-dimensional [[vector spaces|000AYPA9AJ]] over $K$) sending $n$ to $K^n$ and a matrix to its linear map is an equivalence.
A quasi-inverse chooses a basis of each space $V$ and sends $V$ to $\dim V$ and a linear map to its matrix in the chosen bases.
Non-example: let $\mathbf{1}$ have one object and one morphism, and let $\mathbf{2}$ have two objects and only identity morphisms.
No functor $F \colon \mathbf{1} \to \mathbf{2}$ is an equivalence.
Both objects $X$ of $\mathbf{2}$ would need an isomorphism $F(G(X)) \cong X$.
But $F(G(X))$ is the single object in the image of $F$, and the two objects of $\mathbf{2}$ are not isomorphic.
Equivalence of categories is reflexive, symmetric and transitive.
