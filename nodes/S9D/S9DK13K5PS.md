---
tag: S9DK13K5PS
kind: concept
name: Kleene's T predicate
msc: [03D20]
sources:
  - url: https://en.wikipedia.org/wiki/Kleene's_T_predicate
same_as:
  wikidata: Q6420085
  wikipedia: Kleene's T predicate
---

## Summary

Kleene's T predicate is a [[primitive recursive|5NVA2JRHPV]] relation $T(e, x, c)$ about computations.
It says that $c$ codes a halting computation of the program with index $e$ on input $x$.
Together with a primitive recursive function $U$ that reads off the output, it gives Kleene's normal form theorem.
Every partial [[computable function|KZSB5E471K]] has the form $x \mapsto U(\mu c \, T(e, x, c))$ for some $e$.
So a single unbounded search is enough for any computation.

## Explanations

### L1 human

Checking that a given record of a computation is correct is easy: you go through it step by step.
The T predicate is exactly this check, done for every program and every input at once.
Finding a correct record may be impossible, because the program may never stop.
So every computation is "search for a valid record, then read the answer from it".
For instance, the halting set is the set of $e$ for which some $c$ satisfies $T(e, e, c)$.
