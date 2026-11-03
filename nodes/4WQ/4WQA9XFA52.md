---
tag: 4WQA9XFA52
kind: concept
name: Submodular set function
msc: [90C27, 05B35]
sources:
  - url: https://en.wikipedia.org/wiki/Submodular_set_function
same_as:
  wikidata: Q7631710
  wikipedia: Submodular set function
---

## Summary

A submodular set function assigns a real number to each subset of a finite set so that $f(A) + f(B) \ge f(A \cup B) + f(A \cap B)$.
Equivalently, adding an element helps a small set at least as much as a larger set that contains it, a property called diminishing returns.
Cut functions of graphs, [[rank functions|SYRCTH853H]] of [[matroids|PX31ZNYS3Z]] and coverage functions are submodular.
Submodularity plays for set functions a role similar to convexity for functions on $\R^n$: submodular functions can be minimized in polynomial time.

## Explanations

### L1 human

Think of $f(A)$ as the area covered by a set $A$ of lamps in a room.
A new lamp adds more new light to a dark room than to a room that already has many lamps, because its light overlaps with theirs.
This is the rule of diminishing returns, and functions with this rule are submodular.
For example, if lamp $1$ lights $2$ square metres, lamp $2$ lights $2$ square metres, and they overlap in $1$, then $f(\set{1}) + f(\set{2}) = 4 \ge f(\set{1, 2}) + f(\emptyset) = 3$.
Such functions appear in economics, in network design and in machine learning.
