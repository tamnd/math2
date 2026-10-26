---
tag: 0C4YEQ9H5E
kind: statement
role: theorem
name: Inclusion–exclusion for two sets
msc: [05A05]
uses: [05099E1NMJ, 0EE2V3CHFK]
sources:
  - url: https://en.wikipedia.org/wiki/Inclusion–exclusion_principle
    locator: Formula
---

## Statement

Let $A$ and $B$ be finite sets.
Then
$$|A \cup B| + |A \cap B| = |A| + |B|.$$
Equivalently, $|A \cup B| = |A| + |B| - |A \cap B|$.

## Remarks

If $A \cap B = \varnothing$, this is the [[rule of sum|0EE2V3CHFK]].
For three sets: $|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|$.
The [[inclusion–exclusion principle|0FF7726C7P]] is the version for $n$ sets.

## Explanations

### L1 human

When you add the sizes of $A$ and $B$, you count the elements of both sets twice.
Subtract the size of $A \cap B$ once to correct this. For example, $12$ students play football, $8$ play chess, and $3$ do both, so $17$ students do at least one.
