---
tag: 5BNBYZVECW
kind: definition
name: Opposite category
msc: [18A05]
defines: DAMK8XE1FR
uses: [A2DE66937D, 859F0TFVA3, 0VABYWJWH9]
sources:
  - url: https://en.wikipedia.org/wiki/Opposite_category
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]].
The *opposite category* $\mathcal{C}^{\mathrm{op}}$ is the category defined as follows:

1. its objects are the objects of $\mathcal{C}$;
2. for objects $A$, $B$, its [[morphisms|859F0TFVA3]] are $\Hom_{\mathcal{C}^{\mathrm{op}}}(A, B) = \Hom_{\mathcal{C}}(B, A)$; a morphism $f \colon B \to A$ of $\mathcal{C}$ is written $f^{\mathrm{op}} \colon A \to B$ when seen in $\mathcal{C}^{\mathrm{op}}$;
3. the composite is $g^{\mathrm{op}} \circ f^{\mathrm{op}} = (f \circ g)^{\mathrm{op}}$, and the identity of $A$ is $1_A^{\mathrm{op}}$.

## Remarks

The category axioms for $\mathcal{C}^{\mathrm{op}}$ follow from those of $\mathcal{C}$ read backwards, and $(\mathcal{C}^{\mathrm{op}})^{\mathrm{op}} = \mathcal{C}$.
Example: let $(P, \le)$ be a [[preorder|0VABYWJWH9]], seen as a category with one morphism $a \to b$ when $a \le b$.
Its opposite has one morphism $a \to b$ when $b \le a$, so it is the preorder $(P, \ge)$.
Non-example: the rule "keep the arrows as they are and only reverse the order of composition" does not give a category in general.
For $f \colon A \to B$ and $g \colon B \to C$, the expression $f \circ g$ has no meaning in $\mathcal{C}$ unless $C = A$.
A morphism $f$ is a monomorphism in $\mathcal{C}$ exactly when $f^{\mathrm{op}}$ is an epimorphism in $\mathcal{C}^{\mathrm{op}}$.
