---
tag: W7P6CCSMX7
kind: concept
name: Baum–Welch algorithm
msc: [62M05, 62F10]
sources:
  - url: https://en.wikipedia.org/wiki/Baum–Welch_algorithm
same_as:
  wikidata: Q811478
  wikipedia: Baum–Welch algorithm
---

## Summary

The Baum–Welch algorithm estimates the parameters of a [[hidden Markov model|HJVM390354]] from a sequence of observations alone.
It is the [[expectation–maximization algorithm|11N1AXSXYK]] for this model.
It alternates between computing the expected hidden path under the current parameters and re-estimating the parameters from those expectations.
The expectations are computed efficiently by the forward–backward recursions.
It is a standard tool in speech recognition and in biological sequence analysis.

## Explanations

### L1 human

Imagine a machine that switches between hidden moods and emits visible symbols, with each mood favouring different symbols.
You see only the symbols and want to learn how often the moods switch and what each mood emits.
Baum–Welch starts from a guess, works out for each time how likely each mood was, and then updates the guess using these soft counts.
Repeating this never lowers the likelihood of the observed data.
With only one mood, a single step gives the observed frequencies of the symbols.
