---
tag: GTBMW9QXST
kind: definition
name: Linear discriminant analysis
msc: [62H30]
defines: ZATS7NV9WD
uses: [0XN3K7RSZY, 0KX66CZMBB, 0V7G6WMFK0]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_discriminant_analysis
---

## Definition

Let $K \ge 2$ be the number of classes.
For $k = 1, \ldots, K$ let $\pi_k > 0$ be prior probabilities with $\pi_1 + \cdots + \pi_K = 1$, and let $\mu_k \in \R^p$ be class means.
Let $\Sigma$ be a [[positive definite|0KX66CZMBB]] $p \times p$ matrix, the common [[covariance matrix|0V7G6WMFK0]].
The *linear discriminant functions* are
$$\delta_k(x) = x^T \Sigma^{-1} \mu_k - \tfrac{1}{2} \mu_k^T \Sigma^{-1} \mu_k + \log \pi_k, \qquad x \in \R^p.$$
*Linear discriminant analysis* assigns $x$ to a class $k$ for which $\delta_k(x)$ is largest.
In practice the parameters are estimated from a labelled training sample.
One uses the class proportions for $\pi_k$, the class sample means for $\mu_k$ and the pooled sample covariance matrix for $\Sigma$.

## Remarks

If the class $k$ has the distribution $N_p(\mu_k, \Sigma)$ and prior probability $\pi_k$, this rule is the Bayes rule.
Indeed, $\delta_k(x)$ differs from $\log(\pi_k f_k(x))$ by a term that does not depend on $k$, where $f_k$ is the density of class $k$.
Each $\delta_k$ is affine in $x$, so the boundary between two classes is a hyperplane.
For two classes, $x$ goes to class $1$ when
$$(\mu_1 - \mu_2)^T \Sigma^{-1} x - \tfrac{1}{2} (\mu_1 - \mu_2)^T \Sigma^{-1} (\mu_1 + \mu_2) > \log(\pi_2 / \pi_1).$$
Example: with $p = 1$, $\mu_1 = 1$, $\mu_2 = -1$, $\Sigma = 1$ and $\pi_1 = \pi_2$, the condition is $2x > 0$, so $x$ goes to class $1$ when $x > 0$.
Non-example: if the normal classes have different covariance matrices $\Sigma_k$, the Bayes rule has quadratic boundaries.
This rule is quadratic discriminant analysis, not a linear rule.
