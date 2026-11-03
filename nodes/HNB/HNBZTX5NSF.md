---
tag: HNBZTX5NSF
kind: definition
name: Credibility theory
msc: [91G05, 62P05]
defines: KWYCW4P8RH
uses: [0WQNRCNY3M, 0PNRKMRC55]
sources:
  - url: https://en.wikipedia.org/wiki/Credibility_theory
---

## Definition

Let $X_1, \dots, X_n$ be the observed claim amounts of one insured risk, each a [[random variable|0PNRKMRC55]], and let $\bar{X} = (X_1 + \cdots + X_n)/n$ be their mean.
Let $\mu$ be the [[expected value|0WQNRCNY3M]] of a claim in the collective of similar risks, called the manual premium.
A *credibility premium* for the risk is an estimate of the form
$$P = Z \bar{X} + (1 - Z) \mu,$$
where the number $Z \in [0, 1]$ is the *credibility factor*.
*Credibility theory* is the study of such premiums and of rules that fix $Z$ from the data and the model.

## Remarks

In the [[Bühlmann model|BZJMY230YG]], $Z = n/(n + k)$ for a constant $k > 0$ that depends only on the collective.
With $n = 3$ and $k = 9$ this gives $Z = 0.25$, so the premium puts weight $1/4$ on the risk's own mean.
The value $Z = 0$ gives the manual premium and $Z = 1$ gives the pure experience premium $\bar{X}$.
A rule such as $P = 2\bar{X} - \mu$ is not a credibility premium, since it corresponds to $Z = 2 \notin [0, 1]$.
Limited fluctuation credibility chooses $Z = 1$ once $n$ is large enough that $\bar{X}$ is within a given relative error of its mean with a given probability.
Greatest accuracy credibility chooses $Z$ to minimise the mean squared error of $P$ as a predictor of the risk's true mean.
