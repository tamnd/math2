---
tag: YAVW1XHNFH
kind: concept
name: Decision problem
msc: [68Q01, 03D35]
sources:
  - url: https://en.wikipedia.org/wiki/Decision_problem
same_as:
  wikidata: Q3262192
  wikipedia: Decision problem
---

## Summary

A decision problem is a question with a yes or no answer for each of infinitely many inputs, such as "is the number $n$ prime?".
Once inputs are written as strings, a decision problem is the same as a [[formal language|5MFZ4VNY6D]]: the set of inputs whose answer is yes.
Decision problems are the main objects of [[computability theory|X14Y880PN5]] and complexity theory.
A problem is decidable when an algorithm answers it correctly on every input, and the [[halting problem|Z7TN2B35B0]] is the standard example of an undecidable one.

## Explanations

### L1 human

A decision problem is a family of yes or no questions, one for each input.
"Is this number even?" and "does this graph have a cycle?" are decision problems.
A single question such as "is $7$ prime?" is not one; the problem is the whole family over all inputs.
The interesting question is whether one method answers all the questions of the family correctly.
To feed the inputs to a machine, one writes them as strings with an [[encoding|EV03FVHX37]].
