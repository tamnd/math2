---
tag: ~fccd21c4
kind: statement
role: proposition
name: Product of countable sets is countable
msc: ["03E10"]
uses: [~589c0629, ~2cf76fec, ~70e48eb2]
sources:
  - url: https://en.wikipedia.org/wiki/Countable_set
    locator: Formal overview
same_as:
  wikidata: Q66707394
  wikipedia: Countable set
---

## Statement

Let $A$ and $B$ be [[countable sets|~589c0629]].
Then the [[Cartesian product|~2cf76fec]] $A \times B$ is countable.

## Remarks

Proof: take injections $f \colon A \to \mathbb{N}$ and $g \colon B \to \mathbb{N}$. Then $(a, b) \mapsto \pi(f(a), g(b))$ is an injection to $\mathbb{N}$, where $\pi$ is the [[Cantor pairing function|~70e48eb2]].
By induction, a finite product $A_1 \times \dots \times A_n$ of countable sets is countable.
An infinite product need not be countable: the set of sequences of $0$ and $1$ is [[uncountable|~ae32fef7]].

## Explanations

### L1 human

The pairs of natural numbers fill an infinite grid, and the grid can be listed diagonal by diagonal.
So a product of two lists is again a list.
