---
tag: CWKNRTVERF
kind: definition
name: Karoubi envelope
msc: [18A05, "18E05"]
defines: S2GBXQ26QM
uses: [A2DE66937D, 0N5NJZKKN3, DXJH3DGXBC]
sources:
  - url: https://en.wikipedia.org/wiki/Karoubi_envelope
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]].
An endomorphism $e \colon A \to A$ is *idempotent* if $e \circ e = e$.
The *Karoubi envelope* $\mathrm{Kar}(\mathcal{C})$ is the category with these parts.

1. Its objects are pairs $(A, e)$ with $A$ an object of $\mathcal{C}$ and $e$ an idempotent endomorphism of $A$.
2. A morphism $f \colon (A, e) \to (B, e')$ is a morphism $f \colon A \to B$ of $\mathcal{C}$ with $e' \circ f \circ e = f$.
3. Composition is that of $\mathcal{C}$, and the identity of $(A, e)$ is $e$.

## Remarks

The condition in clause 2 is equivalent to $f \circ e = f$ and $e' \circ f = f$.
The functor $\mathcal{C} \to \mathrm{Kar}(\mathcal{C})$ with $A \mapsto (A, \id_A)$ is fully faithful.
Every idempotent of $\mathrm{Kar}(\mathcal{C})$ splits.
For example, an idempotent $e$ of $(A, \id_A)$ is the composite of the [[retraction|DXJH3DGXBC]] $e \colon (A, \id_A) \to (A, e)$ and the section $e \colon (A, e) \to (A, \id_A)$.
Other names are idempotent completion and Cauchy completion.

Example: let $\mathcal{C}$ have one object $*$ and morphisms $1$ and $e$, with $e \circ e = e$.
Then $\mathrm{Kar}(\mathcal{C})$ has the objects $(*, 1)$ and $(*, e)$.
The morphisms $(*, e) \to (*, e)$ are the $f$ with $e f e = f$, and only $f = e$ qualifies, so $(*, e)$ has only its identity $e$.

Non-example: with the same $\mathcal{C}$, the morphism $1 \colon (*, e) \to (*, e)$ is not a morphism of $\mathrm{Kar}(\mathcal{C})$.
Indeed $e \circ 1 \circ e = e \ne 1$, so clause 2 fails.
