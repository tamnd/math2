---
tag: 0AJN7WHBJZ
kind: definition
name: Independent and identically distributed random variables
msc: [60A05]
defines: 00MRN0FARV
uses: [0XCE070V8B, 01X8YSDTBW]
sources:
  - url: https://en.wikipedia.org/wiki/Independent_and_identically_distributed_random_variables
    locator: Definition for more than two random variables
---

## Definition

Let $(X_i)_{i \in I}$ be a family of random variables on one probability space, all with values in the same measurable space $(E, \mathcal{E})$.
The family is independent and identically distributed (i.i.d.) if both of these conditions hold:
1. The family $(X_i)_{i \in I}$ is [[independent|0XCE070V8B]].
2. The random variables $X_i$ are [[identically distributed|01X8YSDTBW]]: all $X_i$ have the same law $\mu$.

## Remarks

One also says that $X_1, X_2, \dots$ is an i.i.d. sequence with common law $\mu$, or a random sample from $\mu$.
The results of repeated tosses of one coin form an i.i.d. sequence of Bernoulli random variables.
The law of large numbers and the central limit theorem are first proved for i.i.d. sequences.

## Explanations

### L1 human

I.i.d. variables are the results of the same experiment, repeated under the same conditions, with no influence between the repetitions.
Each one follows the same law, and none of them gives information about the others.
