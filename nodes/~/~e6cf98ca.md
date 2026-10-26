---
tag: ~e6cf98ca
kind: definition
name: Law of a random variable
msc: ["60E05"]
defines: ~4f22bdfe
uses: [~89528024, ~11dac529]
sources:
  - url: https://en.wikipedia.org/wiki/Probability_distribution
    locator: General probability definition
---

## Definition

Let $(\Omega, \mathcal{F}, P)$ be a probability space, let $(E, \mathcal{E})$ be a set with a σ-algebra, and let $X \colon \Omega \to E$ be a [[random variable|~89528024]].
The law of $X$, also called the distribution of $X$, is the function $P_X \colon \mathcal{E} \to [0, 1]$ with
$$P_X(B) = P(X^{-1}(B)) = P(X \in B) \quad \text{for } B \in \mathcal{E}.$$

## Remarks

$P_X$ is a [[probability distribution|~11dac529]] on $(E, \mathcal{E})$. It is the image measure, or pushforward, of $P$ under $X$, and one also writes $P \circ X^{-1}$ or $X_* P$.
Notation: $X \sim \mu$ means that the law of $X$ is $\mu$.
Two random variables can have the same law but be different functions. For a fair coin toss, the indicator of heads and the indicator of tails both have the Bernoulli law with parameter $1/2$.

## Explanations

### L1 human

The law of $X$ forgets the sample space and keeps only the chances of the values of $X$.
For the sum of two dice, the law says that $7$ has probability $6/36$, $2$ has probability $1/36$, and so on.
