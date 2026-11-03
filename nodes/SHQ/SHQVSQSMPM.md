---
tag: SHQVSQSMPM
kind: problem
name: Multiple comparisons problem
msc: [62J15, 62F03]
uses: [087P03NEND, 0GGKJGZF6D]
about: [GQCY1N8JZT, 087P03NEND]
sources:
  - url: https://en.wikipedia.org/wiki/Multiple_comparisons_problem
same_as:
  wikidata: Q1038757
  wikipedia: Multiple comparisons problem
history:
  posed_by: "unknown"
  first_stated: "unknown"
  notes: "The problem drew wide attention in the 1950s through the work of John Tukey and Henry Scheffé."
---

## Problem

Let $H_1, \dots, H_m$ be $m \ge 2$ null hypotheses about the same data, each with its own [[statistical hypothesis test|087P03NEND]].
Let $\alpha \in (0, 1)$ be a significance level.
Suppose each test rejects its hypothesis at level $\alpha$.
Then the probability of rejecting at least one true null hypothesis can be much larger than $\alpha$.
The problem is to find procedures that decide which $H_i$ to reject so that an overall error rate stays at most $\alpha$.
At the same time, the procedure should reject as many false hypotheses as possible.
The usual overall error rates are the [[family-wise error rate|GQCY1N8JZT]] and the [[false discovery rate|6CHHCTGQ18]].

## Remarks

Suppose that all $m$ null hypotheses are true and that the $m$ tests are independent, each of exact level $\alpha$.
Then the probability of at least one false rejection is $1 - (1 - \alpha)^m$.
For $m = 20$ and $\alpha = 0.05$ this is about $0.64$.
The [[Bonferroni correction|8GRD2TMJRR]] rejects $H_i$ when its [[p-value|0GGKJGZF6D]] $p_i$ satisfies $p_i \le \alpha / m$.
By the union bound, its family-wise error rate is at most $\alpha$, with no assumption on the dependence between the tests.
The price is a loss of power when $m$ is large.
The Benjamini–Hochberg procedure controls the weaker false discovery rate at level $\alpha$ when the tests are independent, and it usually rejects more hypotheses.
John Tukey wrote an influential manuscript titled "The Problem of Multiple Comparisons" in 1953.
There is no single best solution: the right error rate and procedure depend on the purpose of the study.

## Explanations

### L1 human

If you run one test at the 5% level on data where nothing is going on, a false alarm happens only one time in twenty.
If you run twenty such tests, you should expect about one false alarm.
The chance of at least one false alarm is close to two in three.
So a "significant" result found among many tries may be pure luck.
Multiple comparison methods make each test stricter, so that the whole set of tests keeps a small chance of error.
