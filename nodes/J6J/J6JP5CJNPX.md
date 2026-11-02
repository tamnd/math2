---
tag: J6JP5CJNPX
kind: concept
name: Fisher's exact test
msc: [62H17, 62F03]
specializes: [087P03NEND]
sources:
  - url: https://en.wikipedia.org/wiki/Fisher%27s_exact_test
same_as:
  wikidata: Q41492
  wikipedia: Fisher's exact test
---

## Summary

Fisher's exact test is a test of independence of two binary factors in a $2 \times 2$ [[contingency table|PANSMHE0SW]].
It conditions on the row and column totals, and then the count in one cell has a [[hypergeometric distribution|0X3Y0ZSKNF]] under the null hypothesis.
The [[p-value|0GGKJGZF6D]] is computed exactly from this law, so the test is valid for small samples where the chi-squared approximation fails.

## Explanations

### L1 human

Ronald Fisher's lady tasting tea example illustrates the test.
A lady claims she can tell whether milk or tea was poured first, and she gets $8$ cups, $4$ of each kind.
If she is guessing, the chance that she picks the right $4$ cups is $1/\binom{8}{4} = 1/70$, about $0.014$.
So a fully correct answer is strong evidence against pure guessing.
