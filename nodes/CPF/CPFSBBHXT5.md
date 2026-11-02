---
tag: CPFSBBHXT5
kind: concept
name: Statistical decision theory
msc: [62C05, 62A01]
sources:
  - url: https://en.wikipedia.org/wiki/Decision_theory
---

## Summary

Statistical decision theory treats statistical problems as decisions under uncertainty.
A statistician observes data from a model with an unknown parameter and chooses an action by a decision rule.
The statistician then pays a [[loss|3BTG6VVCGZ]] that depends on the action and the true parameter.
Rules are compared through their [[risk functions|N26TSVRH2S]], which gives a common frame for estimation, testing and prediction.

## Explanations

### L1 human

Estimating a number, testing a hypothesis or predicting a value are all ways of making a decision from data.
Decision theory asks the user to say how costly each kind of mistake is, and then looks for the rule with the smallest average cost.
Usually no rule is best for every possible truth at once, so one needs a criterion.
Common criteria are to protect against the worst case (minimax), to average over a prior (Bayes), or at least to discard rules that are beaten everywhere (admissibility).
