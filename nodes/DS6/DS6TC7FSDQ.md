---
tag: DS6TC7FSDQ
kind: definition
name: Kan extension
msc: [18A40]
defines: RN9D96ESWN
uses: [28NQ0KRHD3, KYCPCC57FT, 1X0WKFQX8K]
sources:
  - url: https://en.wikipedia.org/wiki/Kan_extension
---

## Definition

Let $K \colon \mathcal{A} \to \mathcal{B}$ and $F \colon \mathcal{A} \to \mathcal{C}$ be [[functors|28NQ0KRHD3]].
A *left Kan extension* of $F$ along $K$ is a functor $L \colon \mathcal{B} \to \mathcal{C}$ together with a [[natural transformation|KYCPCC57FT]] $\eta \colon F \Rightarrow L \circ K$ with this property.
For every functor $G \colon \mathcal{B} \to \mathcal{C}$ and every natural transformation $\alpha \colon F \Rightarrow G \circ K$, there is a unique natural transformation $\beta \colon L \Rightarrow G$ such that $\alpha = (\beta K) \circ \eta$.
Here $\beta K$ is the natural transformation with components $\beta_{K(a)}$ for $a$ in $\mathcal{A}$.

A *right Kan extension* of $F$ along $K$ is a functor $R \colon \mathcal{B} \to \mathcal{C}$ together with a natural transformation $\varepsilon \colon R \circ K \Rightarrow F$ with this property.
For every functor $G \colon \mathcal{B} \to \mathcal{C}$ and every natural transformation $\alpha \colon G \circ K \Rightarrow F$, there is a unique natural transformation $\beta \colon G \Rightarrow R$ such that $\alpha = \varepsilon \circ (\beta K)$.

## Remarks

The usual notation is $\mathrm{Lan}_K F$ for the left and $\mathrm{Ran}_K F$ for the right Kan extension.
Both are unique up to a unique natural isomorphism when they exist.
Suppose these extensions exist for all $F$.
Then, between the [[functor categories|1X0WKFQX8K]], $\mathrm{Lan}_K$ is left adjoint and $\mathrm{Ran}_K$ is right adjoint to the restriction $G \mapsto G \circ K$ from $[\mathcal{B}, \mathcal{C}]$ to $[\mathcal{A}, \mathcal{C}]$.

Example: let $\mathcal{B} = \mathbf{1}$ be the category with one object and one morphism, and $K$ the unique functor.
A functor $G \colon \mathbf{1} \to \mathcal{C}$ is an object $c$, and $G \circ K$ is the constant functor at $c$.
A natural transformation $F \Rightarrow G \circ K$ is then a cocone from $F$ to $c$.
So the clause of the definition says exactly that $\eta$ is a universal cocone, and $\mathrm{Lan}_K F$ is the colimit of $F$.

Non-example: let $\mathcal{A}$ be the empty category, $\mathcal{B} = \mathbf{1}$ and $\mathcal{C}$ the category of sets.
Then $F$ and $\eta$ are empty, and a left Kan extension is an initial object of $\mathcal{C}$, namely the empty set.
The constant functor $L$ at a one-point set is not a left Kan extension.
For $G$ the constant functor at the empty set there is no natural transformation $L \Rightarrow G$, so the existence part of the clause fails.
