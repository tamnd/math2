---
tag: MDFT90XEQ8
kind: concept
name: Evaluation strategy
msc: [68N18, 03B40, 68Q55]
sources:
  - url: https://en.wikipedia.org/wiki/Evaluation_strategy
same_as:
  wikidata: Q2881121
  wikipedia: Evaluation strategy
---

## Summary

An evaluation strategy is a rule that decides which part of an expression to compute next.
In the [[lambda calculus|BD756KR8FM]] it chooses which redex to contract in each [[beta reduction|Y9B9CVY6SJ]] step.
The main strategies are normal order, which reduces the leftmost outermost redex, and applicative order, which reduces the leftmost innermost one.
Programming languages use the weak versions call-by-name, call-by-need and call-by-value, and the choice affects termination and efficiency.

## Explanations

### L1 human

To compute $f(2 + 3)$, one can first add and then call $f$ on $5$.
One can also pass the unevaluated $2 + 3$ to $f$ and add only when $f$ needs the value.
The first way is call-by-value, the second is call-by-name.
If $f$ ignores its argument and the argument is a computation that never ends, only the second way finishes.
On the other hand, call-by-name may compute the same argument many times, which call-by-need avoids by remembering the result.
