---
tag: ES4MC30ZES
kind: concept
name: Missing data mechanisms
msc: [62D10]
sources:
  - url: https://en.wikipedia.org/wiki/Missing_data
---

## Summary

A missing data mechanism is the probability law that decides which entries of a data set are not observed.
The standard classification has three classes: missing completely at random (MCAR), missing at random (MAR) and missing not at random (MNAR).
The class decides which analyses stay valid.
Under MAR, if the mechanism has its own separate parameters, likelihood and Bayesian inference can ignore it.
Under MNAR the mechanism must be modelled.

## Explanations

### L1 human

Data are often incomplete: people skip survey questions, sensors fail, patients leave a study.
The key question is whether the fact that a value is missing is linked to the values themselves.
If a lab machine breaks at random times, the missing values are MCAR, and the rest of the data is still a fair sample.
If older people skip an income question more often and age is recorded, the data are MAR.
If people with high incomes skip the income question because their income is high, the data are MNAR, and a naive average of the answers is too low.
