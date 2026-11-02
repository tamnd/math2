---
tag: GFZD5Z7PT2
kind: definition
name: Latent variable model
msc: [62H25, 62H05]
defines: C63RVH96TF
uses: [K3AMMSY8DD, 0DR81R1F2B, 0MXT6PRZZ6, 0THJ7416DX]
sources:
  - url: https://en.wikipedia.org/wiki/Latent_variable_model
---

## Definition

Let $\Theta$ be a parameter set.
Let $(X, Z)$ be a pair of random vectors, where $X$ is observed and $Z$ is not.
A *latent variable model* is a family $\set{P_\theta : \theta \in \Theta}$ of [[joint distributions|0DR81R1F2B]] of $(X, Z)$.
The variables $Z$ are the *latent variables*.
The [[statistical model|K3AMMSY8DD]] for the data is the family of [[marginal distributions|0MXT6PRZZ6]] of $X$ under $P_\theta$.
When $P_\theta$ has a density $p_\theta(x, z)$ with respect to a product measure $\mu \otimes \nu$, the observed density is
$$p_\theta(x) = \int p_\theta(x, z) \, d\nu(z).$$

## Remarks

Often the components $X_1, \ldots, X_m$ of $X$ are assumed [[conditionally independent|0THJ7416DX]] given $Z$, the assumption of local independence.
Example: let $Z$ be standard normal and, given $Z$, let $X_1, X_2$ be independent with distribution $N(Z, 1)$.
Then $(X_1, X_2)$ is bivariate normal with variances $2$ and covariance $1$; the dependence of $X_1$ and $X_2$ comes only from $Z$.
Non-example: a regression model of $Y$ given a measured covariate $x$ is not a latent variable model, since all of its variables are observed.
The models are classified by the type of the variables.
Factor analysis has continuous latent and observed variables.
Latent class and mixture models have discrete latent variables.
Item response models have continuous latent and discrete observed variables.
