---
tag: N26TSVRH2S
kind: concept
name: Risk function
msc: [62C05]
sources:
  - url: https://en.wikipedia.org/wiki/Loss_function
---

## Summary

The risk function of a decision rule gives, for each value of the unknown parameter, the expected [[loss|3BTG6VVCGZ]] of the rule.
The data are drawn from the model with that parameter.
It turns a random loss into a deterministic function of the parameter.
Decision rules are compared through their risk functions, which leads to the notions of admissible, minimax and Bayes rules.

## Explanations

### L1 human

A rule that turns data into a decision is sometimes lucky and sometimes unlucky.
The risk is its average loss over many repetitions of the experiment, for a fixed true parameter.
Because the true parameter is unknown, one looks at the whole curve $\theta \mapsto R(\theta, \delta)$.
For example, estimating a normal mean $\theta$ by the mean of $n$ observations with variance $1$ has risk $1/n$ under squared error, the same for every $\theta$.
