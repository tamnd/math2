---
tag: 0FJB06AD2P
kind: definition
name: Conditional probability
msc: [60A05]
defines: 0990W5PN13
uses: [0ZYBZ34RT2, 00SQGJNRTB]
sources:
  - url: https://en.wikipedia.org/wiki/Conditional_probability
    locator: Kolmogorov definition
---

## Definition

Let $(\Omega, \mathcal{F}, P)$ be a [[probability space|0ZYBZ34RT2]] and let $A, B \in \mathcal{F}$ be [[events|00SQGJNRTB]] with $P(B) > 0$.
The conditional probability of $A$ given $B$ is
$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}.$$

## Remarks

For fixed $B$ with $P(B) > 0$, the map $A \mapsto P(A \mid B)$ is a [[probability measure|0VGMEBVW1M]] on $(\Omega, \mathcal{F})$. It gives all its mass to $B$.
For one roll of a fair die, $P(\{6\} \mid \text{even}) = (1/6) / (1/2) = 1/3$.
In general $P(A \mid B) \ne P(B \mid A)$. [[Bayes' theorem|0NM6E9VW04]] relates the two.
The definition does not apply when $P(B) = 0$. Conditioning on such events needs the [[conditional expectation|0YAMJRK04E]].

## Explanations

### L1 human

Once you know that $B$ happened, the outcomes outside $B$ are no longer possible.
So you keep only the part of $A$ inside $B$, and you rescale by $P(B)$ so that the total is $1$ again.
