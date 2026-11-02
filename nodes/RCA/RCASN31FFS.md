---
tag: RCASN31FFS
kind: statement
role: theorem
name: Karlin–Rubin theorem
msc: [62F03]
uses: [4Z73AFN7WT, QRAPTPVH8C, 4RJSN0QARD, 036756NFD6]
about: [QRAPTPVH8C, 4Z73AFN7WT]
sources:
  - url: https://en.wikipedia.org/wiki/Uniformly_most_powerful_test
---

## Statement

Let $\Theta \subseteq \R$, let $X$ have a density $f_\theta$ with $\theta \in \Theta$, and assume the family has a [[monotone likelihood ratio|4Z73AFN7WT]] in a [[statistic|036756NFD6]] $T(X)$.
Let $\theta_0 \in \Theta$ and $\alpha \in (0, 1)$.
For constants $c \in \R$ and $\gamma \in [0, 1]$, let $\varphi(x) = 1$ if $T(x) > c$, $\varphi(x) = \gamma$ if $T(x) = c$, and $\varphi(x) = 0$ if $T(x) < c$.
Then $c$ and $\gamma$ can be chosen so that $E_{\theta_0}[\varphi(X)] = \alpha$.
With this choice, $\varphi$ is a [[uniformly most powerful test|QRAPTPVH8C]] at level $\alpha$ of $H_0 \colon \theta \le \theta_0$ against $H_1 \colon \theta > \theta_0$.

## Remarks

Proof idea: fix $\theta_1 > \theta_0$.
By the monotone likelihood ratio, $\varphi$ rejects exactly when $f_{\theta_1}/f_{\theta_0}$ is large, so it is the most powerful test of $\theta_0$ against $\theta_1$ by the [[Neyman–Pearson lemma|0EE19CFEEF]].
This test does not depend on $\theta_1$.
One then shows that its [[power function|4RJSN0QARD]] is nondecreasing in $\theta$, so its type I error is at most $\alpha$ on all of $\set{\theta \le \theta_0}$.
Example: for $X$ binomial with parameters $n$ and $p$, the UMP test of $p \le p_0$ against $p > p_0$ rejects for a large number of successes, with randomization at the boundary value.
The theorem is about one-sided hypotheses; for $H_1 \colon \theta \ne \theta_0$ a UMP test usually does not exist.

## Explanations

### L1 human

When larger values of a statistic always point towards larger parameters, the best one-sided test is the obvious one.
It rejects "the parameter is at most $\theta_0$" when the statistic is large.
The theorem says that this simple test is the best possible against every larger parameter at once.

### L2 human

The Karlin–Rubin theorem extends the Neyman–Pearson lemma from a simple alternative to a one-sided composite alternative.
The key is that the most powerful test against one alternative is the same for all alternatives on one side.
It applies to one-parameter exponential families, such as binomial, Poisson and normal models with one unknown parameter.
For two-sided problems, one restricts to unbiased tests to get an optimal test.
For discrete data, the randomization $\gamma$ is needed to reach the exact level $\alpha$.
