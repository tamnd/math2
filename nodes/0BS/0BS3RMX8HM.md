---
tag: 0BS3RMX8HM
kind: statement
role: proposition
name: Multiplication rule
aliases: [chain-rule-of-probability, general-product-rule]
msc: [60A05]
uses: [0FJB06AD2P]
sources:
  - url: https://en.wikipedia.org/wiki/Chain_rule_(probability)
    locator: Chain rule for events
same_as:
  wikidata: Q17004731
  wikipedia: Chain rule (probability)
---

## Statement

Let $(\Omega, \mathcal{F}, P)$ be a probability space and let $A_1, \dots, A_n \in \mathcal{F}$ with $n \ge 2$ and $P(A_1 \cap \dots \cap A_{n-1}) > 0$.
Then
$$P(A_1 \cap \dots \cap A_n) = P(A_1) \, P(A_2 \mid A_1) \, P(A_3 \mid A_1 \cap A_2) \cdots P(A_n \mid A_1 \cap \dots \cap A_{n-1}).$$
Here $P(\cdot \mid \cdot)$ is the [[conditional probability|0FJB06AD2P]].

## Remarks

The case $n = 2$ is $P(A \cap B) = P(A) \, P(B \mid A)$ for $P(A) > 0$. It is the definition of $P(B \mid A)$ multiplied by $P(A)$.
The hypothesis makes each conditional probability in the formula defined, because each conditioning event contains $A_1 \cap \dots \cap A_{n-1}$.
Example: draw two cards from a deck without replacement. The probability of two aces is $\frac{4}{52} \cdot \frac{3}{51} = \frac{1}{221}$.

## Explanations

### L1 human

To find the chance that several things all happen, take them one at a time.
Multiply the chance of the first by the chance of the second given the first.
Then multiply by the chance of the third given the first two, and so on.
