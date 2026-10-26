---
tag: 04QNZZ4HHY
kind: definition
name: Dedekind cut
msc: [26A03]
defines: 0G3RRM41X9
uses: [09RFKMBQ63]
sources:
  - url: https://en.wikipedia.org/wiki/Dedekind_cut
    locator: Definition
---

## Definition

A Dedekind cut is a pair $(A, B)$ of subsets of the [[rational numbers|0NCJ5WXN6Z]] $\mathbb{Q}$ with these properties:

1. $A$ and $B$ are nonempty, $A \cap B = \emptyset$ and $A \cup B = \mathbb{Q}$;
2. if $a \in A$, $q \in \mathbb{Q}$ and $q < a$, then $q \in A$;
3. $A$ has no greatest element.

## Remarks

The set $A$ determines the cut, because $B = \mathbb{Q} \setminus A$. Thus some authors call $A$ itself the cut.
The cut with $A = \{q \in \mathbb{Q} : q < 0 \text{ or } q^2 < 2\}$ corresponds to $\sqrt{2}$. Here $B$ has no least element.
The set of all cuts, ordered by inclusion of the lower sets, is a [[complete ordered field|0A9E6X0S3E]] with suitable operations.

## Explanations

### L1 human

Cut the rational number line at one point. Put the numbers to the left in $A$ and the numbers to the right in $B$.
When the cut is at a gap of $\mathbb{Q}$, such as $\sqrt{2}$, the cut itself stands for the missing number.
