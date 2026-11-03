---
tag: R6ZQ52NQMW
kind: statement
role: theorem
name: Entropy power inequality
msc: [94A17, "60E15"]
uses: [045D8P03E0, 0GQ938GDE0, B4PNYNYVKK, 0XN3K7RSZY, 0V7G6WMFK0]
about: [B4PNYNYVKK]
sources:
  - url: https://en.wikipedia.org/wiki/Entropy_power_inequality
same_as:
  wikidata: Q5380810
  wikipedia: Entropy power inequality
---

## Statement

Let $n \ge 1$, and let $X$ and $Y$ be [[independent|0GQ938GDE0]] random vectors in $\R^n$ with [[densities|045D8P03E0]] and finite second moments.
For such a random vector $Z$, let $h(Z) \in [-\infty, \infty)$ be its [[differential entropy|B4PNYNYVKK]] with natural logarithms, and let
$$N(Z) = \frac{1}{2 \pi e} \, e^{2 h(Z) / n}$$
be its *entropy power*, with $e^{-\infty} = 0$.
Then
$$N(X + Y) \ge N(X) + N(Y).$$
If moreover $h(X)$ and $h(Y)$ are finite, equality holds if and only if $X$ and $Y$ are [[Gaussian|0XN3K7RSZY]] with proportional [[covariance matrices|0V7G6WMFK0]].

## Remarks

The entropy power of a Gaussian vector with covariance matrix $\sigma^2 I_n$ is $\sigma^2$.
So $N(Z)$ is the variance per coordinate of the isotropic Gaussian vector that has the same entropy as $Z$.
For Gaussian vectors with covariances $\sigma^2 I_n$ and $\tau^2 I_n$ the sum has covariance $(\sigma^2 + \tau^2) I_n$, and equality holds.

The inequality was stated by Shannon in 1948; the first complete proofs are due to Stam and to Blachman.
The classical proof follows both vectors along the heat flow, adding independent Gaussian noise, and uses de Bruijn's identity, which links the derivative of the entropy to the Fisher information.
Another proof derives it from the sharp form of Young's inequality for convolutions.

Since $N(Y) \ge 0$, the inequality implies $h(X + Y) \ge h(X)$: adding independent noise does not decrease differential entropy.

## Explanations

### L1 human

When two independent random quantities are added, the sum is more spread out than either summand.
The entropy power inequality measures this spread with entropy and says that it grows at least as fast as for Gaussian quantities.
Gaussian vectors are the extreme case, where the inequality becomes an equality.

### L2 human

For variances, $\operatorname{Var}(X + Y) = \operatorname{Var}(X) + \operatorname{Var}(Y)$ always holds for independent $X$ and $Y$.
The entropy power inequality says that the "entropic variance" $N$ is superadditive, with Gaussians as the equality case.
It is used to bound the capacity of channels with non-Gaussian additive noise and in converse proofs for Gaussian broadcast channels.
In convex geometry it is an analogue of the Brunn–Minkowski inequality, with entropy power in the role of volume to the power $1/n$.
