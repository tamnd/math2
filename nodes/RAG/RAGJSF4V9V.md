---
tag: RAGJSF4V9V
kind: concept
name: Monad in nonstandard topology
msc: [54J05, "26E35", "03H05"]
sources:
  - url: https://en.wikipedia.org/wiki/Monad_(nonstandard_analysis)
same_as:
  wikidata: Q6897850
  wikipedia: Monad (nonstandard analysis)
---

## Summary

Let $X$ be a topological space and ${}^*X$ its extension in nonstandard analysis.
The monad of a point $x$ of $X$ is the set of points of ${}^*X$ that are infinitely close to $x$.
It is the intersection of the nonstandard extensions of all open neighbourhoods of $x$.
Monads turn topological notions into simple statements about infinitely close points.
For example, a space is Hausdorff exactly when distinct points have disjoint monads.

## Explanations

### L1 human

In the hyperreal numbers there are infinitesimals, numbers smaller in size than every positive real number but not zero.
The monad of a real number $x$ is the cloud of hyperreal numbers $x + \varepsilon$ with $\varepsilon$ infinitesimal.
It is a picture of "all points that are infinitely near $x$".
For a general space, the open sets around $x$ take the place of distances, and the monad is what all of them have in common after the nonstandard extension.
Continuity then reads: points infinitely near $x$ go to points infinitely near $f(x)$.
