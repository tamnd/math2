---
tag: VEBDNCJJTN
kind: concept
name: Bayes risk
msc: [62C10]
sources:
  - url: https://en.wikipedia.org/wiki/Bayes_estimator
---

## Summary

The Bayes risk of a decision rule is its [[risk function|N26TSVRH2S]] averaged over a [[prior distribution|00NBBSXRQS]] on the parameter.
It reduces the comparison of rules to the comparison of single numbers.
The smallest Bayes risk over all rules is the Bayes risk of the prior, and a rule attaining it is a [[Bayes estimator|PP1A0JB47Q]].

## Explanations

### L1 human

The risk of a rule depends on the unknown truth, so it is a whole curve rather than one number.
If one has an opinion about which values of the truth are likely, one can average the curve with those weights.
That weighted average is the Bayes risk.
For example, estimating a coin's heads probability $\theta$ by the proportion of heads in $n$ tosses has risk $\theta(1-\theta)/n$, and its average over a uniform prior is $1/(6n)$.
