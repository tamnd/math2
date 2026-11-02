---
tag: MSN9TFS59W
kind: definition
name: Uniformly most powerful test
msc: [62F03]
defines: QRAPTPVH8C
uses: [087P03NEND, 4RJSN0QARD]
sources:
  - url: https://en.wikipedia.org/wiki/Uniformly_most_powerful_test
---

## Definition

Let $X$ be data whose law $P_\theta$ depends on $\theta \in \Theta$, let $\Theta_0$ and $\Theta_1$ be disjoint subsets of $\Theta$, and let $\alpha \in (0, 1)$.
A (possibly randomized) test $\varphi$ of $H_0 \colon \theta \in \Theta_0$ against $H_1 \colon \theta \in \Theta_1$ has level $\alpha$ if $E_\theta[\varphi(X)] \le \alpha$ for every $\theta \in \Theta_0$.
A test $\varphi^*$ is *uniformly most powerful* (UMP) at level $\alpha$ if:

1. $\varphi^*$ has level $\alpha$;
2. for every test $\varphi$ of level $\alpha$ and every $\theta \in \Theta_1$, $E_\theta[\varphi^*(X)] \ge E_\theta[\varphi(X)]$.

## Remarks

Here $E_\theta[\varphi(X)]$ is the [[power function|4RJSN0QARD]] of $\varphi$.
Example: let $X_1, \dots, X_n$ be i.i.d. $\mathcal{N}(\theta, 1)$, $H_0 \colon \theta \le 0$, $H_1 \colon \theta > 0$.
The test that rejects when $\sqrt{n}\, \bar X > z_{1 - \alpha}$, the $1 - \alpha$ quantile of $\mathcal{N}(0, 1)$, is UMP at level $\alpha$.
For each $\theta_1 > 0$ it is the most powerful test of $\theta = 0$ against $\theta = \theta_1$, by the [[Neyman–Pearson lemma|0EE19CFEEF]], and its power function is increasing.
Non-example: for $H_0 \colon \theta = 0$ against $H_1 \colon \theta \ne 0$ in the same model, no test satisfies clause 2.
The one-sided test above is most powerful against each $\theta_1 > 0$, but at each $\theta_1 < 0$ the mirror one-sided test has strictly more power.
