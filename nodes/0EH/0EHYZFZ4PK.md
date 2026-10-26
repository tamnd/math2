---
tag: 0EHYZFZ4PK
kind: definition
name: P-value
msc: [62F03]
defines: 0GGKJGZF6D
uses: [087P03NEND, 036756NFD6, 0WGDPYR30Q]
sources:
  - url: https://en.wikipedia.org/wiki/P-value
    locator: Definition
---

## Definition

Consider a [[hypothesis test|087P03NEND]] of a null hypothesis $H_0 \colon \theta \in \Theta_0$ with a test statistic $T(X)$, where large values of $T$ are evidence against $H_0$. Let $t$ be the observed value of $T(X)$.
The p-value of the observation is
$$p(t) = \sup_{\theta \in \Theta_0} P_\theta\big(T(X) \ge t\big).$$
If $H_0$ is simple, $\Theta_0 = \{\theta_0\}$, then $p(t) = P_{\theta_0}(T(X) \ge t)$.

## Remarks

For a two-sided test with a statistic that is symmetric about $0$ under $H_0$, one uses $P_{\theta_0}(|T(X)| \ge |t|)$.
The test that rejects $H_0$ when $p \le \alpha$ has significance level $\alpha$.
If $H_0$ is simple and $T(X)$ has a continuous law under $H_0$, then the random p-value $p(T(X))$ has the [[uniform distribution|0WGDPYR30Q]] on $[0, 1]$ under $H_0$.
The p-value is not the probability that $H_0$ is true.

## Explanations

### L1 human

The p-value tells how surprising your data would be if the null hypothesis were true.
Example: a coin shows $14$ heads in $20$ tosses. If the coin is fair, the probability of at least $14$ heads is about $0.058$. This is the one-sided p-value.
