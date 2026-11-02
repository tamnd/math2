---
tag: HA1KJ3B9DX
kind: concept
name: Cross-validation
msc: [62G09, 62J05]
sources:
  - url: https://en.wikipedia.org/wiki/Cross-validation_(statistics)
same_as:
  wikidata: Q541014
  wikipedia: Cross-validation (statistics)
---

## Summary

Cross-validation estimates how well a fitted model predicts new data by repeatedly fitting it on part of the data and testing it on the rest.
Each observation is used for testing exactly once, with a model that did not see it.
It is the standard tool to choose tuning parameters, such as a bandwidth or a penalty, and to compare predictive models.

## Explanations

### L1 human

Checking a model on the same data that built it is too optimistic, like grading students on questions they saw in advance.
Cross-validation hides a part of the data, fits the model on the rest, and checks the predictions on the hidden part.
In $5$-fold cross-validation, the data are cut into $5$ pieces and each piece is hidden once.
The average error over the $5$ rounds estimates the error on new data.
