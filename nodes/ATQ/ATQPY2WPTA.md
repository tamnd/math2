---
tag: ATQPY2WPTA
kind: concept
name: Point estimation
msc: [62F10]
sources:
  - url: https://en.wikipedia.org/wiki/Point_estimation
same_as:
  wikidata: Q1192065
  wikipedia: Point estimation
---

## Summary

Point estimation is the part of statistical inference that computes from data a single best guess of an unknown quantity.
A typical unknown quantity is a parameter of a statistical model.
The rule that turns data into the guess is an [[estimator|0SSS6ERQ0S]], and its value on the observed data is the estimate.
The theory compares estimators by bias, variance, mean squared error, consistency and efficiency.
It also gives general methods to build them, such as maximum likelihood and the method of moments.
It is contrasted with interval estimation, which gives a range of plausible values.

## Explanations

### L1 human

You flip a coin $100$ times and see $58$ heads; your guess for the probability of heads is $0.58$.
That single number is a point estimate, and the rule "number of heads divided by number of flips" is the estimator.
A different sample would give a different guess, so an estimator is itself random.
Point estimation studies which rules give guesses that are close to the truth most of the time.
