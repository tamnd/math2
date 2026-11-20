---
tag: ~e8f0dab0
kind: example
name: The logic of paradox is not an adaptive logic
msc: ["03B53", "03B60"]
topics: [NJB94B39QK]
audience: grad
not_instance_of:
  - target: ~132437fd
    note: LP rejects disjunctive syllogism for consistent premises too, so it does not adapt to the premises
uses: [~132437fd, ~655488d6, ~66b4811f, 6EFJF9NAYX]
sources:
  - url: https://plato.stanford.edu/entries/logic-paraconsistent/
    locator: Paraconsistent Logic (SEP entry), sections 3.4 and 3.6
---

## Example

Take the consistent premises $\Gamma = \set{p, \neg p \lor q}$ from the [[adaptive example|~66b4811f]].
In the [[logic of paradox|~655488d6]], let $v(p) = \tfrac12$ and $v(q) = 0$.

1. $v(p) = \tfrac12$ is designated.
2. $v(\neg p \lor q) = \max(\tfrac12, 0) = \tfrac12$ is designated.
3. $v(q) = 0$ is not designated.

So $p, \neg p \lor q \nvDash_{\mathrm{LP}} q$, even though $\Gamma$ is classically consistent.
The adaptive logic derives $q$ from $\Gamma$.
LP is a fixed, monotonic consequence relation that rejects [[disjunctive syllogism|6EFJF9NAYX]] for all premise sets.
So it is not an [[adaptive logic|~132437fd]].

## Remarks

The counterexample valuation makes $p$ a glut, although nothing in $\Gamma$ forces that.
An adaptive logic built on LP as lower limit logic would read $\Gamma$ "as consistently as possible" and discard such valuations.
LP is monotonic, while the adaptive logic of the example is nonmonotonic: adding $\neg p$ to $\Gamma$ removes the conclusion $q$.

## Explanations

### L1 human

LP treats every statement as possibly contradictory, all the time.
So from "$p$" and "not $p$ or $q$" it does not conclude $q$, even when nothing is contradictory.
An adaptive logic would conclude $q$ here.

### L2 human

The test is a consistent premise set where disjunctive syllogism applies.
An adaptive logic gives the classical answer; LP does not.
A trap is to think that every paraconsistent logic is adaptive; most paraconsistent logics are monotonic and do not adapt to the premises.
