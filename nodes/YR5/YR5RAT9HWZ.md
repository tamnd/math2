---
tag: YR5RAT9HWZ
kind: statement
role: axiom
name: Likelihood principle
msc: [62A01]
uses: [05FSTXM92W, JZ6R7J36K5]
about: [0VW9E4QXR6]
sources:
  - url: https://en.wikipedia.org/wiki/Likelihood_principle
same_as:
  wikidata: Q13200161
  wikipedia: Likelihood principle
---

## Statement

Let $E_1$ and $E_2$ be two experiments about the same unknown parameter $\theta \in \Theta$, each given by a [[statistical model|JZ6R7J36K5]] with densities or mass functions.
Let $x_1$ be an outcome of $E_1$ and $x_2$ an outcome of $E_2$, with [[likelihood functions|05FSTXM92W]] $L_1(\theta \mid x_1)$ and $L_2(\theta \mid x_2)$.
Suppose there is a constant $c > 0$, not depending on $\theta$, such that $L_1(\theta \mid x_1) = c \, L_2(\theta \mid x_2)$ for all $\theta \in \Theta$.
The likelihood principle asserts that the outcomes $(E_1, x_1)$ and $(E_2, x_2)$ carry the same evidence about $\theta$.
So every inference about $\theta$ should be the same in both cases.

## Remarks

This is a principle of inference, not a theorem: it is a requirement that a method of inference may satisfy or violate.
Birnbaum showed that it is implied by the sufficiency principle together with the conditionality principle; this argument and its reading are still debated.
Example: one experiment tosses a coin $12$ times and sees $3$ heads; another tosses until the $3$rd head, which comes at toss $12$.
The likelihoods are $\binom{12}{3} p^3 (1 - p)^9$ and $\binom{11}{2} p^3 (1 - p)^9$, which are proportional, so the principle demands the same conclusion about $p$.
Bayesian inference with a fixed prior obeys the principle, since the posterior depends on the data only through the likelihood.
Many frequentist procedures violate it: in the example, the two p-values for the hypothesis $p = 1/2$ differ, because they depend on outcomes that could have occurred but did not.

## Explanations

### L1 human

The likelihood function tells how well each parameter value explains the data that were actually seen.
The likelihood principle says that this function is all that matters for learning about the parameter.
In particular, how the experimenter planned to stop, or which other results could have occurred, should not change the conclusion.

### L2 human

The principle separates the two main schools of statistics.
A Bayesian posterior is proportional to prior times likelihood, so it respects the principle automatically, and so does a comparison of likelihood values.
P-values, confidence levels and unbiasedness are defined by averaging over all possible data sets of the experiment, so they depend on the sampling design and usually violate the principle.
The binomial versus negative binomial example above, with a stopping rule, is the standard illustration of this conflict.
