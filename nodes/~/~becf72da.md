---
tag: ~becf72da
kind: concept
name: Chi-squared test
aliases: [chi-square-test, pearsons-chi-squared-test]
msc: [62H17, 62G10]
uses: [~8ce83e63, ~3aae6fc8, ~a4c66ec3]
sources:
  - url: https://en.wikipedia.org/wiki/Chi-squared_test
    locator: Pearson's chi-squared test
  - url: https://en.wikipedia.org/wiki/Chi-squared_test
    locator: Example chi-squared test for categorical data
same_as:
  wikidata: Q1071004
  wikipedia: Chi-squared test
---

## Summary

A chi-squared test is a [[hypothesis test|~8ce83e63]] whose test statistic has approximately a [[chi-squared distribution|~3aae6fc8]] under the null hypothesis. The main example is Pearson's chi-squared test for counts in categories.
For observed counts $O_1, \dots, O_k$ and expected counts $E_1, \dots, E_k$ under $H_0$, Pearson's statistic is
$$\chi^2 = \sum_{i=1}^{k} \frac{(O_i - E_i)^2}{E_i}.$$
One rejects $H_0$ when $\chi^2$ is large.

## Remarks

In the goodness-of-fit test, $H_0$ fixes the probabilities of the $k$ categories. For a large sample, $\chi^2$ has approximately the law $\chi^2_{k - 1}$ under $H_0$.
In the test of independence for an $r \times c$ contingency table, $H_0$ states that the two categorical variables are [[independent|~a4c66ec3]]. Then $E_{ij}$ is (row total $\times$ column total) / $n$, and the law is approximately $\chi^2_{(r-1)(c-1)}$.
The approximation is poor when expected counts are small. A common rule asks for $E_i \ge 5$ in each cell. For small tables, Fisher's exact test is an alternative.
Karl Pearson introduced the test in 1900.

## Explanations

### L1 human

The chi-squared test compares the counts that you observe with the counts that a hypothesis predicts.
If the squared differences, scaled by the predictions, add up to a large number, the hypothesis does not fit the data.
