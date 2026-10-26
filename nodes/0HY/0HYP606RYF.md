---
tag: 0HYP606RYF
kind: concept
name: Student's t-test
aliases: [t-test, students-t-test, one-sample-t-test, two-sample-t-test]
msc: [62F03]
uses: [087P03NEND, 0NQ5798SB1, 0QNRBHWV35, 0JN9P4A944, 07RXBVTVZB]
sources:
  - url: https://en.wikipedia.org/wiki/Student's_t-test
    locator: Uses
  - url: https://en.wikipedia.org/wiki/Student's_t-test
    locator: Calculations
same_as:
  wikidata: Q309479
  wikipedia: Student's t-test
---

## Summary

A Student's t-test is a [[hypothesis test|087P03NEND]] whose test statistic has [[Student's t-distribution|0NQ5798SB1]] under the null hypothesis. It mostly tests hypotheses about the means of normal populations with unknown variance.
In the one-sample t-test, $X_1, \dots, X_n$ are i.i.d. $\mathcal{N}(\mu, \sigma^2)$ with unknown $\sigma$, and $H_0 \colon \mu = \mu_0$. The statistic is
$$t = \frac{\bar{X}_n - \mu_0}{S_n / \sqrt{n}},$$
with the [[sample mean|0QNRBHWV35]] $\bar{X}_n$ and the [[sample standard deviation|0JN9P4A944]] $S_n$. Under $H_0$, $t \sim t_{n - 1}$.

## Remarks

The two-sample t-test compares the means of two independent normal samples with sizes $n_1$, $n_2$ and equal variances. It uses the pooled standard deviation $s_p$ and $t = (\bar{X}_1 - \bar{X}_2) / \big(s_p \sqrt{1/n_1 + 1/n_2}\big)$, with $n_1 + n_2 - 2$ degrees of freedom.
For two samples with unequal variances, Welch's t-test uses an approximate number of degrees of freedom.
The paired t-test is the one-sample t-test applied to the differences of paired observations.
For large samples, the t-test gives almost the same results as a test with the normal law, because $t_\nu$ approaches $\mathcal{N}(0, 1)$.

## Explanations

### L1 human

A t-test checks whether an average differs from a given value, or whether two averages differ, more than chance alone can explain.
It divides the difference by its estimated standard error, and compares the result with the t-distribution.
