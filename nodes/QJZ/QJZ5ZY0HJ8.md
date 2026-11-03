---
tag: QJZ5ZY0HJ8
kind: concept
name: ZPP
msc: [68Q15, 68Q10, 68W20]
specializes: [ESPYW94XGR]
sources:
  - url: https://en.wikipedia.org/wiki/ZPP_(complexity)
same_as:
  wikidata: Q136355
  wikipedia: ZPP (complexity)
---

## Summary

ZPP, for zero-error probabilistic polynomial time, is a [[complexity class|ESPYW94XGR]] of decision problems.
A problem is in ZPP when a [[probabilistic Turing machine|K99S0Q0814]] solves it without error, in expected polynomial time on every input.
Such algorithms are called Las Vegas algorithms.
ZPP equals $\mathrm{RP} \cap \text{co-RP}$, where [[RP|TPDMV6ZXN3]] is the class of one-sided error.
It satisfies $\mathrm{P} \subseteq \mathrm{ZPP} \subseteq$ [[BPP|PTD7E1PKV4]].

## Explanations

### L1 human

A ZPP algorithm always gives the right answer, but the time it takes depends on luck.
On average over its coin flips, it finishes in polynomial time on each input.
Quicksort with a random pivot is the classic picture of this behaviour, though it solves a sorting task rather than a decision problem.
If one stops the algorithm after a few times its expected time and answers "I don't know", one gets an algorithm that is fast always and gives up only rarely.
