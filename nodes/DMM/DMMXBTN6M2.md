---
tag: DMMXBTN6M2
kind: statement
role: theorem
name: Delta method
msc: ["62E20", "60F05"]
uses: [0JDAQHWA9N, 07RXBVTVZB, 0G558GJQMW, 0A61B60B5R, 0135XZZQ8M, 047NDTEPCV, 0EPZC4Z1FC, 0VEFSSKX18]
about: [0JDAQHWA9N]
sources:
  - url: https://en.wikipedia.org/wiki/Delta_method
same_as:
  wikidata: Q1132714
  wikipedia: Delta method
---

## Statement

Let $\theta \in \R$ and $\sigma^2 > 0$.
Let $(T_n)$ be a sequence of real random variables such that
$$\sqrt{n}\,(T_n - \theta) \xrightarrow{d} \mathcal{N}(0, \sigma^2),$$
where $\xrightarrow{d}$ is [[convergence in distribution|0JDAQHWA9N]] and $\mathcal{N}(0, \sigma^2)$ is the [[normal distribution|07RXBVTVZB]].
Let $g \colon \R \to \R$ be [[differentiable|0A61B60B5R]] at $\theta$.
Then
$$\sqrt{n}\,\big(g(T_n) - g(\theta)\big) \xrightarrow{d} \mathcal{N}\big(0, g'(\theta)^2 \sigma^2\big).$$

## Remarks

Idea of proof: by differentiability, $g(T_n) - g(\theta) = g'(\theta)(T_n - \theta) + r(T_n)(T_n - \theta)$ with $r(t) \to 0$ as $t \to \theta$.
Since $T_n \to \theta$ in probability, $r(T_n) \to 0$ in probability, and $\sqrt{n}(T_n - \theta)$ is bounded in probability.
So the remainder times $\sqrt{n}$ tends to $0$ in probability, and Slutsky's lemma gives the limit $g'(\theta)\,\mathcal{N}(0, \sigma^2)$.

Multivariate form: if $\sqrt{n}(T_n - \theta) \xrightarrow{d} \mathcal{N}_k(0, \Sigma)$ in $\R^k$, with a [[multivariate normal|0G558GJQMW]] limit, and $g \colon \R^k \to \R^m$ is [[differentiable|0135XZZQ8M]] at $\theta$ with [[Jacobian matrix|047NDTEPCV]] $J$, then $\sqrt{n}(g(T_n) - g(\theta)) \xrightarrow{d} \mathcal{N}_m(0, J \Sigma J^T)$.

Example: for i.i.d. [[Poisson|0VEFSSKX18]] variables with mean $\lambda > 0$, the [[central limit theorem|0EPZC4Z1FC]] gives $\sqrt{n}(\bar{X}_n - \lambda) \xrightarrow{d} \mathcal{N}(0, \lambda)$.
With $g(t) = 2\sqrt{\abs{t}}$, $g'(\lambda) = 1/\sqrt{\lambda}$, so $\sqrt{n}\big(2\sqrt{\bar{X}_n} - 2\sqrt{\lambda}\big) \xrightarrow{d} \mathcal{N}(0, 1)$.
The limit variance no longer depends on $\lambda$: the square root is a variance-stabilizing transformation for Poisson data.

If $g'(\theta) = 0$, the limit is the point mass at $0$, and one needs a second-order expansion: if $g''(\theta) \ne 0$ exists, then $n(g(T_n) - g(\theta)) \xrightarrow{d} \frac{1}{2} g''(\theta) \sigma^2 \chi^2_1$.

## Explanations

### L1 human

If an estimate is approximately normal around the truth, then a smooth function of the estimate is also approximately normal around the function of the truth.
Near the true value, a smooth function looks like a straight line with slope $g'(\theta)$, and a straight line stretches the spread by that slope.
So the standard deviation is multiplied by $\abs{g'(\theta)}$.

### L2 human

The delta method turns the central limit theorem for averages into limit laws for smooth functions of averages: ratios, logarithms, correlation coefficients, odds ratios.
It gives approximate standard errors and confidence intervals for such quantities.
It is also the step that passes from the asymptotic normality of an estimator $\hat{\theta}$ to that of $g(\hat{\theta})$, for example for maximum likelihood estimators.
Variance-stabilizing transformations are chosen with it: one picks $g$ so that $g'(\theta)^2 \sigma^2(\theta)$ does not depend on $\theta$.
