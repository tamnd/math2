---
tag: 0912EEEVCT
kind: statement
role: theorem
name: An injective endomorphism of a finite-dimensional space is surjective
msc: [15A04]
uses: [0W4FSW1TVB]
sources:
  - url: https://en.wikipedia.org/wiki/Rank–nullity_theorem
    locator: Reformulations and generalizations
---

## Statement

Let $F$ be a field, let $V$ be a finite-dimensional vector space over $F$, and let $T \colon V \to V$ be a linear map.
Then these conditions are equivalent:

1. $T$ is injective.
2. $T$ is surjective.
3. $T$ is bijective.

## Remarks

The proof uses the [[rank–nullity theorem|0W4FSW1TVB]]: $\ker T = 0$ if and only if $\dim \im T = \dim V$.
It fails in infinite dimensions: on $F[x]$, multiplication by $x$ is injective and not surjective.
In characteristic $0$, the derivative on $F[x]$ is surjective and not injective.
For square matrices, this is the statement that $Ax = 0$ has only the trivial solution if and only if $Ax = b$ has a solution for each $b$.

## Explanations

### L1 human

For a linear map from a finite-dimensional space to itself, one to one and onto are the same thing.
If no information is lost, then nothing in the target can be missed, because the dimensions match.
This is like a map from a finite set to itself.
