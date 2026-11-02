---
tag: JN1PJ5AJJS
kind: concept
name: Logistic regression
msc: [62J12]
specializes: [K6C48KMRKC]
sources:
  - url: https://en.wikipedia.org/wiki/Logistic_regression
same_as:
  wikidata: Q1132755
  wikipedia: Logistic regression
---

## Summary

Logistic regression models the probability of a binary outcome as the logistic function of a linear combination of regressors.
Equivalently, the log-odds of the outcome is linear in the regressors.
So each coefficient is the change in log-odds for a unit change of its regressor.
It is the [[generalized linear model|K6C48KMRKC]] for [[Bernoulli|0386Y0Z7Y7]] responses with the canonical logit link, and it is fitted by [[maximum likelihood|0FREPFKNS7]].
It is one of the most used models in medicine, the social sciences and machine learning, where it is a basic linear classifier.

## Explanations

### L1 human

Many questions have a yes/no answer: does a patient recover, does a customer buy.
A straight line can predict values below $0$ or above $1$, which make no sense as probabilities.
Logistic regression bends the line into an S-shaped curve that always stays between $0$ and $1$.
If the model says $\log(p / (1 - p)) = -2 + 0.5 x$, then at $x = 4$ the odds are $e^0 = 1$, so the probability is $1/2$.
Each extra unit of $x$ multiplies the odds by $e^{0.5} \approx 1.65$.
