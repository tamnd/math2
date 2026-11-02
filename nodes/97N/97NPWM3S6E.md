---
tag: 97NPWM3S6E
kind: concept
name: Comonad
msc: [18C15]
sources:
  - url: https://en.wikipedia.org/wiki/Monad_(category_theory)
---

## Summary

A comonad on a category is the dual of a [[monad|FF6XXA6D1A]].
It is an endofunctor $G$ with a counit $\varepsilon \colon G \Rightarrow \mathrm{Id}$ and a comultiplication $\delta \colon G \Rightarrow G G$ that satisfy coassociativity and counit laws.
Every adjunction $F \dashv U$ gives a comonad $F U$ on the domain of $U$.
Comonads govern coalgebraic structure, descent theory and comonadic resolutions in homological algebra.

## Explanations

### L1 human

A monad builds things up, while a comonad unfolds things.
The counit extracts a value, and the comultiplication duplicates the context around it.
For a fixed set $A$, the functor $X \mapsto A \times X$ on sets is a comonad.
The counit forgets the label $a$ in $(a, x)$, and the comultiplication copies the label, giving $(a, (a, x))$.
