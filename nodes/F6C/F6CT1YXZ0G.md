---
tag: F6CT1YXZ0G
kind: concept
name: Log-rank test
msc: [62N03, 62G10, 62P10]
sources:
  - url: https://en.wikipedia.org/wiki/Logrank_test
same_as:
  wikidata: Q6089397
  wikipedia: Logrank test
---

## Summary

The log-rank test is a nonparametric [[hypothesis test|087P03NEND]] that compares the survival distributions of two or more groups from right-[[censored|MY8ZZP84NP]] data.
At each event time it compares the observed number of events in a group with an expected number.
The expected number is computed as if all groups had the same [[hazard function|Y959NKQ3XW]].
Summing these differences and standardising gives a statistic that is approximately standard normal under the null hypothesis.
It is the standard test for comparing [[Kaplan–Meier|B7AJ8RWZRC]] curves, and it is most efficient when the hazards of the groups are proportional.

## Explanations

### L1 human

Two groups of patients get different treatments, and we record when each patient has a relapse.
Each time someone relapses, we look at how many patients of each group were still at risk.
From this we compute how many of these relapses we would expect in group 1 if the treatments were equally good.
The test adds up "observed minus expected" over all relapse times.
A large total, compared with its natural spread, suggests that the treatments really differ.
