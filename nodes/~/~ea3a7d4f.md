---
tag: ~ea3a7d4f
kind: statement
role: theorem
name: Third isomorphism theorem for rings
msc: [16D25]
uses: [~fcc6d7c6, ~41b74bde]
sources:
  - url: https://en.wikipedia.org/wiki/Isomorphism_theorems
    locator: Theorem C (rings)
---

## Statement

Let $R$ be a [[ring|~447242bf]] and let $I \subseteq J$ be two-sided ideals of $R$.
Then $J/I = \{a + I : a \in J\}$ is a two-sided ideal of the [[quotient ring|~fcc6d7c6]] $R/I$.
The map $(R/I)/(J/I) \to R/J$, $(a + I) + J/I \mapsto a + J$, is a [[ring isomorphism|~41b74bde]].

## Remarks

The proof applies the [[first isomorphism theorem|~88fdaac0]] to the map $R/I \to R/J$, $a + I \mapsto a + J$. It is surjective, and its kernel is $J/I$.
For example, $6\mathbb{Z} \subseteq 2\mathbb{Z}$, and $(\mathbb{Z}/6\mathbb{Z})/(2\mathbb{Z}/6\mathbb{Z}) \cong \mathbb{Z}/2\mathbb{Z}$.

## Explanations

### L1 human

You can make a quotient in two steps or in one step.
Dividing first by $I$ and then by the image of $J$ gives the same ring as dividing directly by $J$.
