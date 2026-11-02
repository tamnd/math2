---
tag: 40ATJEVR32
kind: concept
name: Bootstrap
msc: [62G09, 62F40]
sources:
  - url: https://en.wikipedia.org/wiki/Bootstrapping_(statistics)
same_as:
  wikidata: Q301990
  wikipedia: Bootstrapping (statistics)
---

## Summary

The bootstrap estimates the [[sampling distribution|656Y8FA3RY]] of a [[statistic|0Q5CG2NEQ8]] by resampling the observed data with replacement.
It treats the [[empirical distribution function|A05WR6TEK5]] of the sample as if it were the unknown true distribution.
It then recomputes the statistic on many simulated samples drawn from it.
From these replicates one gets standard errors, bias estimates and confidence intervals without explicit formulas.
Bradley Efron introduced it in 1979, and it is one of the most used tools of modern statistics.

## Explanations

### L1 human

You have one sample and want to know how much your estimate would vary if you could repeat the study.
You cannot repeat it, so you pretend that the sample is the whole population.
Draw a new sample of the same size from your data, with replacement, so that some points appear twice and some not at all.
Compute the estimate again, and repeat this a few thousand times.
The spread of these estimates approximates the spread you would see over real repetitions.
