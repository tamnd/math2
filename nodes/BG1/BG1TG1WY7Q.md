---
tag: BG1TG1WY7Q
kind: concept
name: Arithmetic coding
msc: [94A29, 68P30, 94A45]
sources:
  - url: https://en.wikipedia.org/wiki/Arithmetic_coding
same_as:
  wikidata: Q2651
  wikipedia: Arithmetic coding
---

## Summary

Arithmetic coding encodes a whole message as one number in the interval $[0, 1)$.
Each symbol shrinks the current interval in proportion to its probability, so the final interval has length equal to the probability of the message.
A few more bits than $\log_2$ of one over that probability identify the interval.
So the code length per symbol gets close to the entropy, without the loss of up to one bit per symbol of symbol-by-symbol codes.

## Explanations

### L1 human

Cut the interval $[0, 1)$ into pieces, one for each possible first letter, with lengths equal to the letter probabilities.
Inside the piece of the actual first letter, cut again for the second letter, and so on.
After the whole message one is left with a tiny interval, and any short binary fraction inside it names the message.
Likely messages give long intervals, which need few digits; rare messages give short intervals, which need many digits.
