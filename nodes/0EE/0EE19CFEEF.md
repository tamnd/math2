---
tag: 0EE19CFEEF
kind: statement
role: lemma
name: Neyman–Pearson lemma
aliases: [neyman-pearson-lemma]
msc: [62F03]
uses: [087P03NEND, 05FSTXM92W, 0R41PVFA39]
sources:
  - url: https://en.wikipedia.org/wiki/Neyman–Pearson_lemma
    locator: Statement
same_as:
  wikidata: Q1375989
  wikipedia: Neyman–Pearson lemma
---

## Statement

Consider a [[hypothesis test|087P03NEND]] of the simple null hypothesis $H_0 \colon \theta = \theta_0$ against the simple alternative $H_1 \colon \theta = \theta_1$. Let $L(\theta \mid x)$ be the [[likelihood|05FSTXM92W]] of the data $x$.
For $\eta > 0$, let the test reject $H_0$ when
$$\Lambda(x) = \frac{L(\theta_0 \mid x)}{L(\theta_1 \mid x)} \le \eta,$$
and let $\alpha = P_{\theta_0}(\Lambda(X) \le \eta)$ be its size.
Then this likelihood-ratio test is a most powerful test of size $\alpha$. Each other test with size at most $\alpha$ has at most the same power at $\theta_1$.

## Remarks

Consider all tests with a probability of a [[type I error|0R41PVFA39]] at most $\alpha$. Among them, the likelihood-ratio test has the smallest probability of a type II error.
For a discrete law, an exact size $\alpha$ can need a randomized test on the boundary $\Lambda(x) = \eta$.
Example: for an i.i.d. $\mathcal{N}(\mu, 1)$ sample and $\mu_1 > \mu_0$, the test rejects $H_0$ when $\bar{x}$ is large.

## History

Jerzy Neyman and Egon Pearson introduced the lemma in a paper in 1933.

## Explanations

### L1 human

To choose between two exact hypotheses, the best test compares how well each hypothesis explains the data.
If the alternative explains the data much better than the null hypothesis, reject the null hypothesis. No other test with the same false-alarm rate finds more true effects.
