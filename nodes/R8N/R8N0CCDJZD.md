---
tag: R8N0CCDJZD
kind: definition
name: Likelihood-ratio test
msc: [62F03, 62F05]
defines: YM1BNA80RC
uses: [05FSTXM92W, 087P03NEND, 0FREPFKNS7]
sources:
  - url: https://en.wikipedia.org/wiki/Likelihood-ratio_test
---

## Definition

Let $X$ be data with [[likelihood function|05FSTXM92W]] $L(\theta \mid x)$ for $\theta$ in a parameter set $\Theta$, and let $\Theta_0 \subset \Theta$.
For data $x$ with $\sup_{\theta \in \Theta} L(\theta \mid x) > 0$, the *likelihood-ratio statistic* is
$$\lambda(x) = \frac{\sup_{\theta \in \Theta_0} L(\theta \mid x)}{\sup_{\theta \in \Theta} L(\theta \mid x)}.$$
The *likelihood-ratio test* of $H_0 \colon \theta \in \Theta_0$ against $H_1 \colon \theta \in \Theta \setminus \Theta_0$ rejects $H_0$ when $\lambda(x) \le c$.
The constant $c \in [0, 1]$ is chosen so that $\sup_{\theta \in \Theta_0} P_\theta(\lambda(X) \le c) \le \alpha$, for a given level $\alpha$.

## Remarks

Since $\Theta_0 \subset \Theta$, one has $0 \le \lambda(x) \le 1$.
The two suprema are the likelihoods at the restricted and the unrestricted [[maximum likelihood estimates|0FREPFKNS7]], when these exist.
One often uses $-2 \log \lambda(X)$, which is large when $\lambda$ is small.
Example: for $X_1, \dots, X_n$ i.i.d. $\mathcal{N}(\mu, 1)$ and $\Theta_0 = \set{0}$, one finds $-2 \log \lambda = n \bar X^2$.
So the test rejects when $\abs{\sqrt{n}\, \bar X}$ is large, which is the usual two-sided z-test.
For two simple hypotheses, the test is the most powerful test of the [[Neyman–Pearson lemma|0EE19CFEEF]].
