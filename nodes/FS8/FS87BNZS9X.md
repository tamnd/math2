---
tag: FS87BNZS9X
kind: concept
name: Information content
msc: [94A17]
sources:
  - url: https://en.wikipedia.org/wiki/Information_content
same_as:
  wikidata: Q735075
  wikipedia: Information content
---

## Summary

The information content, or self-information, or surprisal, of an outcome $x$ of probability $p(x) > 0$ is $I(x) = -\log p(x)$.
It measures how surprising the outcome is: certain outcomes carry no information, and rare outcomes carry much.
It is additive for independent events, and its average over the outcomes of a random variable is the [[Shannon entropy|Y86E072V0V]].

## Explanations

### L1 human

The less likely an event is, the more one learns when it happens.
Information content turns this into a number by taking minus the logarithm of the probability.
A fair coin landing heads has probability $\frac12$ and carries $1$ bit.
Rolling a six with a fair die carries $\log_2 6 \approx 2.58$ bits, and an event of probability $\frac{1}{1024}$ carries $10$ bits.
For two independent events the probabilities multiply, so the information contents add.
