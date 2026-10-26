---
tag: 0A7KGAYHGV
kind: statement
role: theorem
name: Baire category theorem
msc: ["54E52"]
uses: [08EWT7J0SC, 0D5KR33H7X]
sources:
  - url: https://en.wikipedia.org/wiki/Baire_category_theorem
    locator: Statement
same_as:
  wikidata: Q1052678
  wikipedia: Baire category theorem
---

## Statement

Each [[complete metric space|08EWT7J0SC]] is a [[Baire space|0D5KR33H7X]].

## Remarks

Explicitly: if $X$ is a complete metric space and $(U_n)_{n \in \mathbb{N}}$ is a sequence of open dense subsets of $X$, then $\bigcap_n U_n$ is dense in $X$.
The proof builds a nested sequence of closed balls with radii tending to $0$, and uses completeness to find a point in all of them.
A second form of the theorem says that each locally compact Hausdorff space is a Baire space.
A consequence: $\mathbb{R}$ is not a countable union of nowhere dense sets, and thus $\mathbb{R}$ is uncountable.

## Explanations

### L1 human

A complete metric space cannot be covered by countably many thin sets.
For example, you cannot write the real line as a countable union of sets like $\mathbb{Z}$ or the Cantor set.
