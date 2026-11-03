---
tag: TC7SQFTN3A
kind: concept
name: f-divergence
msc: [94A17, 62B10, "60E05"]
sources:
  - url: https://en.wikipedia.org/wiki/F-divergence
same_as:
  wikidata: Q5423634
  wikipedia: F-divergence
---

## Summary

An $f$-divergence measures how different a probability measure $P$ is from a probability measure $Q$.
It averages $f(dP/dQ)$ over $Q$ for a [[convex function|07Q7CNM5WF]] $f$ with $f(1) = 0$.
One family contains many classical quantities: the [[Kullback–Leibler divergence|PQBW43X5RE]], the [[total variation distance|3SZESKX3N5]], the $\chi^2$-divergence and the squared Hellinger distance.
Every $f$-divergence is non-negative and does not increase when both measures are pushed through the same Markov kernel, a form of the [[data processing inequality|BGH1T3HKPV]].
The notion was studied independently by Csiszár, by Morimoto, and by Ali and Silvey in the 1960s.

## Explanations

### L1 human

There are many ways to say how far apart two probability laws are.
An $f$-divergence looks at the ratio $t = P(x) / Q(x)$ at each point, applies a convex penalty $f(t)$ that is $0$ when $t = 1$, and averages the penalty over $Q$.
If the two laws agree, every ratio is $1$ and the divergence is $0$.
Choosing $f(t) = t \log t$ gives the Kullback–Leibler divergence, and $f(t) = \frac12 \abs{t - 1}$ gives the total variation distance.
For example, for a fair coin $P$ and a coin $Q$ with heads probability $\frac14$, the ratios are $2$ and $\frac23$, and with $f(t) = (t - 1)^2$ the divergence is $\frac14 \cdot 1 + \frac34 \cdot \frac19 = \frac13$.
