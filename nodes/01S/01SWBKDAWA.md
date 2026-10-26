---
tag: 01SWBKDAWA
kind: definition
name: Composition of relations
msc: ["03E20"]
defines: 0PYSR20HGF
uses: [08EJC6Q25H, 0JW2FHW7G3]
sources:
  - url: https://en.wikipedia.org/wiki/Composition_of_relations
    locator: lead section
---

## Definition

Let $A$, $B$ and $C$ be sets, let $R \subseteq A \times B$ and let $S \subseteq B \times C$ be [[binary relations|08EJC6Q25H]].
The composition of $R$ and $S$ is the relation from $A$ to $C$
$$R \mathbin{;} S = \{(a, c) \in A \times C \mid \exists b \in B, \, a \mathrel{R} b \text{ and } b \mathrel{S} c\}.$$

## Remarks

Many authors write $S \circ R$ for $R \mathbin{;} S$. This order agrees with [[function composition|07HF9YCWPP]].
Composition of relations is associative.
A relation $R$ on a set is [[transitive|0CYRECG2YQ]] exactly when $R \mathbin{;} R \subseteq R$.

## Explanations

### L1 human

Let $R$ be "is a parent of" and let $S$ be "is a parent of" again.
Then $R \mathbin{;} S$ is "is a grandparent of": you go from a person to a child, then from the child to a grandchild.
