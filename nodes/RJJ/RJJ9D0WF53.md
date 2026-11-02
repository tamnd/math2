---
tag: RJJ9D0WF53
kind: concept
name: Unification
msc: [68V15, 03B35, 08B05]
sources:
  - url: https://en.wikipedia.org/wiki/Unification_(computer_science)
same_as:
  wikidata: Q609057
  wikipedia: Unification (computer science)
---

## Summary

Unification is the problem of finding a [[substitution|NCDZ969V7X]] that makes two terms equal.
Such a substitution is a unifier.
When two terms have a unifier, they have a most general one, from which every other unifier is obtained by a further substitution.
Robinson's unification algorithm computes it, and unification is at the core of resolution theorem proving, logic programming and type inference.

## Explanations

### L1 human

Two expressions with blanks are given, and the task is to fill in the blanks so that the two become the same expression.
For example, $f(x, b)$ and $f(a, y)$ become the same once $x$ is replaced by $a$ and $y$ by $b$.
The expressions $f(x)$ and $g(y)$ can never be made equal, because their outer symbols differ.
Neither can $x$ and $f(x)$, because $x$ would have to contain itself.
