---
tag: 8DZTNVTGY2
kind: concept
name: Projective hierarchy
msc: ["03E15", "54H05"]
sources:
  - url: https://en.wikipedia.org/wiki/Projective_hierarchy
same_as:
  wikidata: Q219448
  wikipedia: Projective hierarchy
---

## Summary

The projective hierarchy sorts the projective subsets of a [[Polish space|584GXXY73M]] into levels $\Sigma^1_n$, $\Pi^1_n$ and $\Delta^1_n$ for $n \ge 1$.
It starts with the [[analytic sets|3RWWZYPAFV]], and alternates two operations: taking complements and taking projections along the [[Baire space|P2WS16HKD7]].
The first level $\Delta^1_1$ consists exactly of the Borel sets, by [[Suslin's theorem|9418TGREZX]].
ZFC does not decide whether the higher levels behave well, for example whether all their sets are Lebesgue measurable.
They do under [[projective determinacy|2GY3131ZPS]], and they do not under the [[axiom of constructibility|4QKRPRCSXH]].

## Explanations

### L1 human

Start with the shadows of closed sets: these are the analytic sets.
Take complements of these, then their shadows, then complements again, and so on.
Each step gives a new level of complexity, and the sets reached after finitely many steps are the projective sets.
Most sets of real numbers that appear in ordinary mathematics are projective, often at a low level.
