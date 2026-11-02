---
tag: 4CRH8NNFEF
kind: concept
name: Near-unanimity term
msc: [08B05, 08B10]
sources:
  - url: https://en.wikipedia.org/wiki/Majority_function
---

## Summary

A near-unanimity term is a term of arity at least $3$ that returns $x$ whenever all arguments but at most one equal $x$.
Having such a term is a [[Mal'cev condition|6R0CA4JWWY]] on a [[variety|AJNZJD8442]].
A variety with a near-unanimity term is congruence-distributive.
For a finite algebra, such a term makes the clone of term operations determined by a finite set of relations, as in the [[Baker–Pixley theorem|97SRYBF41G]].

## Explanations

### L1 human

Think of a vote among $n$ voters where at most one voter disagrees with the rest.
A near-unanimity term is an operation that always follows the large group in this situation.
In a lattice, the term $(x \wedge y) \vee (y \wedge z) \vee (x \wedge z)$ is such a term with three arguments.
For example, with $x = z$ it gives $(x \wedge y) \vee (y \wedge x) \vee x = x$.
When many voters disagree, the term may return anything; only the nearly unanimous inputs are fixed.
