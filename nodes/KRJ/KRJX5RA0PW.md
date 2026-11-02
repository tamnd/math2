---
tag: KRJX5RA0PW
kind: concept
name: Unbounded operator
msc: [47A05, 47B25]
sources:
  - url: https://en.wikipedia.org/wiki/Unbounded_operator
same_as:
  wikidata: Q5108738
  wikipedia: Unbounded operator
---

## Summary

An unbounded operator is a linear map defined on a linear subspace of a normed space, its domain, with values in another normed space.
Despite the name, it need not be unbounded: the term means that boundedness is not assumed.
Differential operators such as $f \mapsto f'$ and the position and momentum operators of quantum mechanics are the main examples.
The domain is part of the data, and two operators with the same formula but different domains are different.

## Explanations

### L1 human

Differentiation is a linear operation on functions, but it cannot be applied to every square-integrable function, and it can turn a small function into a huge one.
For example, $\sin(nx)/n$ is small on $[0, \pi]$, but its derivative $\cos(nx)$ is not small.
An unbounded operator handles this by fixing a domain, a subspace of functions where the operation is defined.
On this domain the map is linear, but no bound $\norm{Tx} \le C \norm{x}$ needs to hold.
