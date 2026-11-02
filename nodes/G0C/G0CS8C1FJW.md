---
tag: G0CS8C1FJW
kind: definition
name: Minimum-variance unbiased estimator
msc: [62F10]
defines: ZCJX7THBNJ
uses: [0TTNRP5PFQ, 01BD2TFFP4, 007QED3E0Y, 0J97P5KZY0]
sources:
  - url: https://en.wikipedia.org/wiki/Minimum-variance_unbiased_estimator
---

## Definition

Let $\set{P_\theta : \theta \in \Theta}$ be a family of distributions of the data $X$, and let $g \colon \Theta \to \R$ be the quantity to estimate.
An [[estimator|0TTNRP5PFQ]] $T = T(X)$ is *unbiased* for $g$ if $E_\theta(T) = g(\theta)$ for every $\theta \in \Theta$, that is, its [[bias|01BD2TFFP4]] is zero.
Let $T$ be an unbiased estimator of $g$ with $\operatorname{Var}_\theta(T) < \infty$ for all $\theta$.
It is a *minimum-variance unbiased estimator*, or *uniformly minimum-variance unbiased estimator* (UMVUE), if
$$\operatorname{Var}_\theta(T) \le \operatorname{Var}_\theta(T')$$
for every unbiased estimator $T'$ of $g$ and every $\theta \in \Theta$.

## Remarks

Here $\operatorname{Var}_\theta$ is the [[variance|007QED3E0Y]] when $X \sim P_\theta$.

Example: let $X_1, \dots, X_n$ be i.i.d. [[Bernoulli|0J97P5KZY0]]($p$) with $\Theta = (0, 1)$.
The proportion $\bar{X}$ is unbiased with variance $p(1-p)/n$.
The Fisher information of the sample is $n/(p(1-p))$, so the Cramér–Rao bound for unbiased estimators of $p$ is $p(1-p)/n$.
The estimator $\bar{X}$ attains it at every $p$, so $\bar{X}$ is the UMVUE of $p$.

Non-example: for $n \ge 3$, $T' = (X_1 + X_2)/2$ is unbiased, but its variance $p(1-p)/2$ exceeds $p(1-p)/n$ for every $p$, so it fails the variance inequality.

The UMVUE need not exist, and an estimator that attains the Cramér–Rao bound need not exist even when the UMVUE does.
If $S$ is a complete sufficient statistic and $T$ is unbiased, then $E(T \mid S)$ is the UMVUE; this is the Lehmann–Scheffé theorem.
