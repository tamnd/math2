---
tag: ~ce2fcd9e
kind: statement
role: theorem
name: Rule of sum
aliases: [addition-principle, sum-rule]
msc: [05A05]
uses: [~b0941ec2]
sources:
  - url: https://en.wikipedia.org/wiki/Addition_principle
    locator: lead section
same_as:
  wikidata: Q2360148
  wikipedia: Addition principle
---

## Statement

Let $A$ and $B$ be finite sets with $A \cap B = \varnothing$.
Then $A \cup B$ is finite and $|A \cup B| = |A| + |B|$.

More generally, let $A_1, \dots, A_k$ be finite sets that are pairwise disjoint.
Then $|A_1 \cup \dots \cup A_k| = |A_1| + \dots + |A_k|$.

## Remarks

For the disjoint union $A \sqcup B$ of two arbitrary finite sets, the same formula $|A \sqcup B| = |A| + |B|$ holds.
If $A$ and $B$ are not disjoint, the formula fails. The [[inclusion-exclusion formula for two sets|~09a593d0]] gives the correct count.

## Explanations

### L1 human

If you choose one item from a first group or from a second group, and no item is in both groups, you add the sizes.
For example, with 3 soups and 4 salads on a menu, there are $3 + 4 = 7$ ways to choose one starter.
