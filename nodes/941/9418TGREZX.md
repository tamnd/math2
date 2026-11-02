---
tag: 9418TGREZX
kind: statement
role: theorem
name: Suslin's theorem
msc: ["03E15", "54H05", "28A05"]
uses: [584GXXY73M, 3RWWZYPAFV, 0WQXY32Q8D, 0RKF1ZT5JJ]
about: [3RWWZYPAFV, 0WQXY32Q8D]
sources:
  - url: https://en.wikipedia.org/wiki/Analytic_set
---

## Statement

Let $X$ be a [[Polish space|584GXXY73M]] and let $A \subseteq X$.
Then $A$ belongs to the [[Borel sigma-algebra|0WQXY32Q8D]] of $X$ if and only if both $A$ and its [[complement|0RKF1ZT5JJ]] $X \setminus A$ are [[analytic sets|3RWWZYPAFV]].

## Remarks

One direction is easy: every Borel set is analytic, and the complement of a Borel set is Borel.
For the other direction, the Lusin separation theorem says that two disjoint analytic sets $A$ and $B$ can be separated by a Borel set $C$, that is, $A \subseteq C$ and $C \cap B = \emptyset$.
Applied to $A$ and $X \setminus A$, it gives a Borel set $C$ with $A \subseteq C \subseteq A$, so $C = A$.

The hypothesis on the complement cannot be dropped.
Every uncountable Polish space contains an analytic set that is not Borel, and the complement of such a set is not analytic.

In the notation of the projective hierarchy, the theorem says $\boldsymbol{\Delta}^1_1 = \boldsymbol{\Sigma}^1_1 \cap \boldsymbol{\Pi}^1_1$ is exactly the class of Borel sets.

## Explanations

### L1 human

Analytic sets are the images of Borel sets under continuous maps, and they can be more complicated than Borel sets.
The theorem says when an analytic set is Borel after all: exactly when its complement is analytic too.
So "Borel" means "simple to describe from both sides".

### L2 human

The theorem is the standard way to prove that a set is Borel without writing it explicitly from open sets by countable unions and complements.
One shows that the set and its complement are both projections of Borel sets, and the theorem does the rest.
A common use is the result that a bijective Borel map between Polish spaces has a Borel inverse.
