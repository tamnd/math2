---
tag: ~0d2debcb
kind: statement
role: theorem
name: Sequential characterization of limits
aliases: [heine-definition-of-limit]
msc: [26A03]
uses: [~d578d124, ~23896e76]
sources:
  - url: https://en.wikipedia.org/wiki/Limit_of_a_function
    locator: In terms of sequences
---

## Statement

Let $D \subseteq \mathbb{R}$, let $f \colon D \to \mathbb{R}$, let $a$ be a limit point of $D$, and let $L$ be a real number.
Then $\lim_{x \to a} f(x) = L$ if and only if the following holds.
For each sequence $(x_n)$ in $D \setminus \{a\}$ with $x_n \to a$, we have $f(x_n) \to L$.

## Remarks

This turns facts about [[limits of sequences|~23896e76]] into facts about limits of functions. Examples are the limit laws for sums, products, and quotients.
It is also a tool to show that a limit does not exist. Find two sequences tending to $a$ whose images have different limits.
Mathlib states a general form as `tendsto_nhds_iff_seq_tendsto`.

## Explanations

### L1 human

The function has limit $L$ at $a$ exactly when it sends every sequence approaching $a$ to a sequence approaching $L$.
So limits of functions reduce to limits of sequences.
