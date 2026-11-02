---
tag: 8JV9PPFRG4
kind: concept
name: Minimum description length
msc: [62B10, 94A17, 68Q30]
sources:
  - url: https://en.wikipedia.org/wiki/Minimum_description_length
same_as:
  wikidata: Q1417790
  wikipedia: Minimum description length
---

## Summary

The minimum description length (MDL) principle selects the model that gives the shortest description of the data.
The description counts the bits to state the model and the bits to encode the data with the help of the model.
It turns model selection into data compression: a good model captures regularities and so compresses the data.
It is a computable relative of [[Kolmogorov complexity|8PY3K6NCKF]], and Jorma Rissanen introduced it.

## Explanations

### L1 human

To send a long list of numbers to a friend, you may first send a rule, such as "a straight line plus small errors", and then the errors.
A simple rule is short to send but may leave large errors, which are long to send.
A very complex rule leaves tiny errors but is itself long.
MDL chooses the rule for which the total message is shortest.
