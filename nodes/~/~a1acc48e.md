---
tag: ~a1acc48e
kind: statement
role: theorem
name: Distributive laws for sets
aliases: [distributivity-of-union-and-intersection]
msc: ["03E20"]
uses: [~bf3fa33b, ~71f1e924]
sources:
  - url: https://en.wikipedia.org/wiki/Algebra_of_sets
    locator: lead section
same_as:
  wikidata: Q10565797
  wikipedia: Algebra of sets
---

## Statement

Let $A$, $B$ and $C$ be [[sets|~bd92ceee]].
Then intersection distributes over union, and union distributes over intersection:
$$A \cap (B \cup C) = (A \cap B) \cup (A \cap C),$$
$$A \cup (B \cap C) = (A \cup B) \cap (A \cup C).$$

## Remarks

The laws follow from the distributive laws of logic for $\land$ and $\lor$.
The second law has no analogue for numbers: $a + bc$ is not $(a + b)(a + c)$ in general.

## Explanations

### L1 human

To prove the first law, take $x$ in the left side. Then $x \in A$, and $x \in B$ or $x \in C$.
In the first case $x \in A \cap B$, and in the second case $x \in A \cap C$.
The other inclusion is similar.
