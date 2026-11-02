---
tag: 1VBRNS1EQJ
kind: definition
name: Functional data analysis
msc: [62R10, 62H25]
defines: KEARMKNZ1Q
uses: [HM2HHE3J51, SASP14MA1Z, 0QH5ENKZM1, 0WQNRCNY3M, 0KBFAWYRTE]
sources:
  - url: https://en.wikipedia.org/wiki/Functional_data_analysis
---

## Definition

Let $\mathcal T = [a, b]$ with $a < b$, and let $H = L^2(\mathcal T)$ be the [[Hilbert space|HM2HHE3J51]] of [[square-integrable|SASP14MA1Z]] real functions on $\mathcal T$, with inner product $\langle f, g \rangle = \int_{\mathcal T} f(t) g(t) \, dt$.
*Functional data analysis* is the statistical analysis of data $X_1, \dots, X_n$ that are realisations of a random element $X$ of $H$.
Such an $X$ is a [[stochastic process|0QH5ENKZM1]] $(X(t))_{t \in \mathcal T}$ with paths in $H$.
Its basic parameters, when $E\norm{X}^2 < \infty$, are:

1. the mean function $\mu(t) = E[X(t)]$, an [[expected value|0WQNRCNY3M]] for each $t$;
2. the [[covariance|0KBFAWYRTE]] function $C(s, t) = \operatorname{Cov}(X(s), X(t))$;
3. the covariance operator $\mathcal C \colon H \to H$, $(\mathcal C f)(t) = \int_{\mathcal T} C(s, t) f(s) \, ds$.

## Remarks

The operator $\mathcal C$ is compact, self-adjoint and positive semidefinite, so it has an orthonormal basis of eigenfunctions $\phi_k$ with eigenvalues $\lambda_1 \ge \lambda_2 \ge \dots \ge 0$.
Functional principal component analysis estimates these and writes $X = \mu + \sum_k \xi_k \phi_k$ with uncorrelated scores $\xi_k = \langle X - \mu, \phi_k \rangle$ of variance $\lambda_k$.
The sample versions are $\hat\mu = \frac1n \sum_i X_i$ and $\hat C(s, t) = \frac1n \sum_i (X_i(s) - \hat\mu(s))(X_i(t) - \hat\mu(t))$.

Example: let $X(t) = \xi \sqrt{2} \sin(\pi t)$ on $[0, 1]$, with $\xi$ a real random variable of mean $0$ and variance $1$.
Then $\mu = 0$ and $C(s, t) = 2 \sin(\pi s) \sin(\pi t)$, so $\mathcal C$ has the single nonzero eigenvalue $1$, with eigenfunction $\sqrt{2} \sin(\pi t)$ of norm $1$.

Non-example: a table of the heights of children measured once each, at a single age, is ordinary multivariate data, not functional data, since no observation is a function of $t$.
