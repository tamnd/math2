---
tag: PTK8XCQ0GK
kind: definition
name: Bayesian hierarchical model
msc: [62F15]
defines: P944X6S117
uses: [Q0DXKAQXE1, 00NBBSXRQS, 0KJ7ZS8AJA, 0NM6E9VW04]
sources:
  - url: https://en.wikipedia.org/wiki/Bayesian_hierarchical_modeling
---

## Definition

A *Bayesian hierarchical model* (with two levels of prior) consists of the following.

1. A [[parametric model|Q0DXKAQXE1]] for the data: given a parameter $\theta \in \Theta$, the data $x$ have density $f(x \mid \theta)$.
2. A [[prior|00NBBSXRQS]] for $\theta$ that depends on a hyperparameter $\varphi \in \Phi$: given $\varphi$, the parameter $\theta$ has density $\pi(\theta \mid \varphi)$.
3. A hyperprior: a probability distribution on $\Phi$ with density $\pi(\varphi)$.

The joint density of $(x, \theta, \varphi)$ is $f(x \mid \theta)\,\pi(\theta \mid \varphi)\,\pi(\varphi)$, and the [[posterior|0KJ7ZS8AJA]] of $(\theta, \varphi)$ given $x$ is proportional to it, by [[Bayes' theorem|0NM6E9VW04]].

## Remarks

Models with more levels add further hyperpriors in the same way.
Example: data in $J$ groups with $X_{ij} \mid \theta_j \sim \mathcal{N}(\theta_j, \sigma^2)$, group means $\theta_j \mid \mu, \tau \sim \mathcal{N}(\mu, \tau^2)$ i.i.d., and a hyperprior on $(\mu, \tau)$.
All three clauses hold, with $\theta = (\theta_1, \dots, \theta_J)$ and $\varphi = (\mu, \tau)$.
Given $\mu$ and $\tau$, the posterior mean of each $\theta_j$ lies between the sample mean of group $j$ and the overall level $\mu$.
Non-example: the same model with $\mu$ and $\tau$ fixed numbers has no hyperprior, so clause 3 fails; it is an ordinary one-level Bayesian model.
Integrating out $\theta$ gives the marginal $\int f(x \mid \theta)\pi(\theta \mid \varphi)\,d\theta$; estimating $\varphi$ from it instead of using a hyperprior is the empirical Bayes approach.
