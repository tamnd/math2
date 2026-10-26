---
tag: ~bf3fa33b
kind: definition
name: Union
msc: ["03E20"]
defines: ~e292d972
uses: [~bd92ceee, ~6dec28e3, ~4f3617aa]
sources:
  - url: https://en.wikipedia.org/wiki/Union_(set_theory)
    locator: lead section
---

## Definition

Let $A$ and $B$ be [[sets|~bd92ceee]].
The union of $A$ and $B$ is the set
$$A \cup B = \{x \mid x \in A \lor x \in B\}.$$
So an object $x$ is an [[element|~6dec28e3]] of $A \cup B$ when $x \in A$ or $x \in B$, or both.

## Remarks

Example: $\{1, 2\} \cup \{2, 3\} = \{1, 2, 3\}$.
Union is commutative and associative, and $A \cup \varnothing = A$.
The union of an arbitrary family of sets is in [[union of a family of sets|~f7777dd8]].

## Explanations

### L1 human

To form $A \cup B$, put the elements of $A$ and the elements of $B$ together in one set.
An element of both sets appears only one time.
