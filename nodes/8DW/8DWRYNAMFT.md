---
tag: 8DWRYNAMFT
kind: statement
role: theorem
name: Asymptotic normality of the maximum likelihood estimator
msc: [62F12, 62F10]
uses: [0FREPFKNS7, 54387XJ9QW, CP97GRVTQ0, G1Z3WSTE8Q, 0AJN7WHBJZ, 0JDAQHWA9N, 0G558GJQMW, 0C38S0KMJK, 0693Y2METT, 0EPZC4Z1FC]
about: [0FREPFKNS7]
sources:
  - url: https://en.wikipedia.org/wiki/Maximum_likelihood_estimation
---

## Statement

Let $\set{f(\cdot; \theta) : \theta \in \Theta}$ be a family of probability densities with respect to a measure $\nu$, with $\Theta \subseteq \R^k$, and let $X_1, X_2, \dots$ be [[i.i.d.|0AJN7WHBJZ]] with density $f(\cdot; \theta_0)$.
Assume:

1. $\theta_0$ lies in the [[interior|0C38S0KMJK]] of $\Theta$;
2. on a neighbourhood $N$ of $\theta_0$, $f(x; \theta) > 0$ and $\theta \mapsto f(x; \theta)$ is twice continuously differentiable, for every $x$;
3. $\int \sup_{\theta \in N} \norm{\nabla_\theta f(x; \theta)} \, d\nu(x) < \infty$ and $\int \sup_{\theta \in N} \norm{\nabla^2_\theta f(x; \theta)} \, d\nu(x) < \infty$;
4. the [[Fisher information|G1Z3WSTE8Q]] $I(\theta_0) = E_{\theta_0}\big[s(\theta_0; X_1)\, s(\theta_0; X_1)^T\big]$ exists and is nonsingular, where $s(\theta; x) = \nabla_\theta \log f(x; \theta)$ is the [[score|CP97GRVTQ0]];
5. $E_{\theta_0}\big[\sup_{\theta \in N} \norm{\nabla^2_\theta \log f(X_1; \theta)}\big] < \infty$.

Let $\hat{\theta}_n$ be a [[maximum likelihood estimator|0FREPFKNS7]] with $\hat{\theta}_n \to \theta_0$ in probability.
Then
$$\sqrt{n}\,(\hat{\theta}_n - \theta_0) \xrightarrow{d} \mathcal{N}_k\big(0, I(\theta_0)^{-1}\big),$$
where $\xrightarrow{d}$ is [[convergence in distribution|0JDAQHWA9N]] and $\mathcal{N}_k$ is the [[multivariate normal distribution|0G558GJQMW]].

## Remarks

Idea of proof: with probability tending to one, $\hat{\theta}_n$ is an interior maximizer, so the score equation $\sum_i s(\hat{\theta}_n; X_i) = 0$ holds.
A Taylor expansion around $\theta_0$ gives $0 = \sum_i s(\theta_0; X_i) + H_n (\hat{\theta}_n - \theta_0)$, where $H_n$ is the [[Hessian|0693Y2METT]] of the log-likelihood at intermediate points.
Conditions 2 and 3 allow differentiation under the integral, so the score has mean $0$ and covariance $I(\theta_0)$, and the [[central limit theorem|0EPZC4Z1FC]] gives $n^{-1/2}\sum_i s(\theta_0; X_i) \xrightarrow{d} \mathcal{N}_k(0, I(\theta_0))$.
Condition 5 and consistency give $H_n/n \to -I(\theta_0)$ in probability, and solving for $\sqrt{n}(\hat{\theta}_n - \theta_0)$ gives the result.
Consistency itself is provided, for example, by the [[consistency theorem|54387XJ9QW]].

Example: for i.i.d. Exponential($\lambda$) data, $\hat{\lambda}_n = 1/\bar{X}_n$ and $I(\lambda) = 1/\lambda^2$, so $\sqrt{n}(\hat{\lambda}_n - \lambda) \xrightarrow{d} \mathcal{N}(0, \lambda^2)$.

The interior condition is needed.
For $\mathcal{N}(\mu, 1)$ data with $\Theta = [0, \infty)$ and $\mu_0 = 0$, the MLE is $\max(\bar{X}_n, 0)$.
Then $\sqrt{n}\,\hat{\mu}_n$ converges to the law of $\max(Z, 0)$ with $Z$ standard normal, which is not normal.
Smoothness in $\theta$ with a fixed support is also needed: for Uniform$(0, \theta)$ data the MLE is $\max_i X_i$, and $n(\theta_0 - \hat{\theta}_n)$ has an exponential limit.

## Explanations

### L1 human

For large samples, the maximum likelihood estimate is approximately normally distributed around the true value.
Its spread shrinks like $1/\sqrt{n}$, and the constant is the inverse of the Fisher information, which measures how sharply the likelihood peaks.
This is the smallest spread allowed by the Cramér–Rao bound, so maximum likelihood is asymptotically efficient.

### L2 human

The theorem justifies the usual Wald confidence intervals $\hat{\theta}_n \pm 1.96\, (n\, I(\hat{\theta}_n))^{-1/2}$ and the Wald test.
Together with the delta method it gives limit laws for smooth functions of the MLE.
The same expansion of the log-likelihood leads to Wilks' theorem for the likelihood-ratio statistic and to the score test.
The modern view puts the result in the frame of local asymptotic normality, where the bound $I(\theta_0)^{-1}$ appears in the Hájek–Le Cam convolution theorem.
