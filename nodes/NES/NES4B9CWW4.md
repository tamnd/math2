---
tag: NES4B9CWW4
kind: concept
name: Categorical logic
msc: [03G30, 18C10, 18B25]
sources:
  - url: https://en.wikipedia.org/wiki/Categorical_logic
same_as:
  wikidata: Q5051813
  wikipedia: Categorical logic
---

## Summary

Categorical logic is the branch of mathematics that studies logic with the tools of [[category theory|Q1RZT7DV0F]].
A logical theory is matched with a category built from its syntax.
A model of the theory is then a structure-preserving [[functor|28NQ0KRHD3]] from that category to another category, such as the category of sets.
Typical correspondences match the simply typed [[lambda calculus|BD756KR8FM]] with [[Cartesian closed categories|BFBNQ36QS8]], and higher-order [[intuitionistic logic|Q11N8X99FK]] with [[toposes|6837RS7N82]].
These correspondences let one transfer results between logic, algebra, geometry and the semantics of programming languages.

## Explanations

### L1 human

In ordinary logic one writes formulas and proofs, and then interprets them in sets.
Categorical logic allows the interpretation to take place in any suitable category, not only in sets.
Types become objects, terms become morphisms, and logical connectives become operations such as products and exponentials.
For example, a proof that $A$ and $B$ together give $C$ becomes a morphism $A \times B \to C$, and the rule "from $A$ and $B$ infer $A$" becomes the projection $A \times B \to A$.
