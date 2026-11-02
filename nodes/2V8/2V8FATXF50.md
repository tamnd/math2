---
tag: 2V8FATXF50
kind: definition
name: Contravariant functor
msc: [18A05, 18A22]
defines: RECR96V97B
uses: [28NQ0KRHD3, DAMK8XE1FR, 00E0YZCERH, 07JBSZE0V4]
sources:
  - url: https://en.wikipedia.org/wiki/Functor
---

## Definition

Let $\mathcal{C}$ and $\mathcal{D}$ be categories.
A *contravariant functor* $F$ from $\mathcal{C}$ to $\mathcal{D}$ consists of:

1. for each object $A$ of $\mathcal{C}$, an object $F(A)$ of $\mathcal{D}$;
2. for each morphism $f \colon A \to B$ of $\mathcal{C}$, a morphism $F(f) \colon F(B) \to F(A)$ of $\mathcal{D}$;

such that:

1. $F(1_A) = 1_{F(A)}$ for every object $A$;
2. $F(g \circ f) = F(f) \circ F(g)$ for all $f \colon A \to B$ and $g \colon B \to C$.

## Remarks

A contravariant functor from $\mathcal{C}$ to $\mathcal{D}$ is the same as a [[functor|28NQ0KRHD3]] $\mathcal{C}^{\mathrm{op}} \to \mathcal{D}$ from the [[opposite category|DAMK8XE1FR]], via $f^{\mathrm{op}} \mapsto F(f)$.
Example: the [[power set|00E0YZCERH]] with preimages, $A \mapsto \mathcal{P}(A)$ and $f \mapsto f^{-1}$, is a contravariant functor from sets to sets.
Here $f^{-1} \colon \mathcal{P}(B) \to \mathcal{P}(A)$, and $(g \circ f)^{-1}(S) = f^{-1}(g^{-1}(S))$ gives clause 2.
Another example is the [[dual space|07JBSZE0V4]] functor $V \mapsto V^*$, $f \mapsto f^*$ on vector spaces over a field, where $(g \circ f)^* = f^* \circ g^*$.
Non-example: the power set with direct images, $f \mapsto (S \mapsto f(S))$, is not contravariant, because $f(\cdot)$ goes from $\mathcal{P}(A)$ to $\mathcal{P}(B)$, so clause 2 of the data fails; it is a covariant functor.
