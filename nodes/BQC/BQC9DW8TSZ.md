---
tag: BQC9DW8TSZ
kind: definition
name: Generator
msc: [18A05, 18A20]
defines: CK08JW32WB
uses: [A2DE66937D, 859F0TFVA3, VJXS8AK67E, GRG8WEBSH5, 082GHNPJ53]
sources:
  - url: https://en.wikipedia.org/wiki/Generator_(category_theory)
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]].
An object $G$ of $\mathcal{C}$ is a *generator* (or *separator*) if it has the following property.
For all [[morphisms|859F0TFVA3]] $f, g \colon X \to Y$ with $f \neq g$, there is a morphism $h \colon G \to X$ with $f \circ h \neq g \circ h$.
More generally, a set $\mathcal{G}$ of objects is a *generating family* if for all $f \neq g \colon X \to Y$ there are $G \in \mathcal{G}$ and $h \colon G \to X$ with $f \circ h \neq g \circ h$.

## Remarks

When $\mathcal{C}$ is locally small, $G$ is a generator exactly when the [[hom functor|VJXS8AK67E]] $\Hom(G, -) \colon \mathcal{C} \to \mathbf{Set}$ is [[faithful|GRG8WEBSH5]].
The dual notion is a cogenerator (or coseparator): an object $C$ such that $f \neq g \colon X \to Y$ implies $k \circ f \neq k \circ g$ for some $k \colon Y \to C$.

Example: in the category of [[abelian groups|082GHNPJ53]], $\Z$ is a generator.
If $f \neq g \colon A \to B$, pick $a \in A$ with $f(a) \neq g(a)$ and let $h \colon \Z \to A$ be $n \mapsto na$; then $(f \circ h)(1) = f(a) \neq g(a) = (g \circ h)(1)$.

Non-example: in the same category, the trivial group $0$ is not a generator.
The identity and the zero map of $\Z/2\Z$ differ, but the only morphism $h \colon 0 \to \Z/2\Z$ is zero, and both composites with $h$ are zero.
