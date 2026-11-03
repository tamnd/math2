---
tag: Z7SSS8G8G9
kind: concept
name: Data envelopment analysis
msc: [90C08, 90B50, 90C05]
sources:
  - url: https://en.wikipedia.org/wiki/Data_envelopment_analysis
same_as:
  wikidata: Q647974
  wikipedia: Data envelopment analysis
---

## Summary

Data envelopment analysis (DEA) measures the relative efficiency of comparable units, such as bank branches or hospitals, that turn several inputs into several outputs.
Each unit gets a score between $0$ and $1$, computed by a [[linear program|VNMXB0J2KA]].
The program chooses the weights of inputs and outputs most favourable to that unit.
A unit with score $1$ lies on the best-practice frontier, which "envelops" the data of all units.
The basic model is the CCR model of Charnes, Cooper and Rhodes, a [[linear-fractional program|XVBF9EJY10]] turned into a linear program.

## Explanations

### L1 human

Imagine comparing schools that use teachers and money to produce graduates and test results.
There is no agreed price that says how much a teacher is worth compared with a graduate.
DEA lets each school choose the prices that make it look as good as possible, under the rule that with those prices no school scores above $1$.
A school that still cannot reach $1$ is inefficient by any fair choice of prices.
With one input and one output, the score is just the output per input of the school divided by the best output per input among all schools.
