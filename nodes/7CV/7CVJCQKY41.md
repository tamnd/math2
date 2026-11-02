---
tag: 7CVJCQKY41
kind: concept
name: Arithmetical hierarchy
msc: [03D55, 03F30]
sources:
  - url: https://en.wikipedia.org/wiki/Arithmetical_hierarchy
same_as:
  wikidata: Q669094
  wikipedia: Arithmetical hierarchy
---

## Summary

The arithmetical hierarchy classifies sets of natural numbers by the number of alternating blocks of unbounded quantifiers needed to define them in first-order arithmetic.
Its levels are the classes $\Sigma^0_n$, $\Pi^0_n$ and $\Delta^0_n$ for $n \in \N$.
The first levels are familiar: $\Delta^0_1$ sets are the [[computable sets|PPGD5KW8JC]] and $\Sigma^0_1$ sets are the [[computably enumerable sets|TN9G24VABN]].
[[Post's theorem|NYJX5QXX1T]] links each level to computability relative to iterated [[Turing jumps|60P2XWY5QX]].

## Explanations

### L1 human

Some properties of a number $e$ can be checked by a search that ends when a witness is found: "there is a $c$ such that ...".
These are the $\Sigma^0_1$ properties, for example "program $e$ halts on input $e$".
Other properties need two alternating quantifiers.
An example is "for every $x$ there is a $c$ such that program $e$ halts on $x$ within $c$ steps", which says that program $e$ is total.
Each extra alternation of "there is" and "for all" can define strictly more sets.
The hierarchy measures how unsolvable a problem is.
