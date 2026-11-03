---
tag: Z2ED2TA87E
kind: statement
role: theorem
name: Principle of maximum entropy
msc: [94A17, 82B03, 62B10]
uses: [1SFZNN31JW, GYNMZ9201M, PQBW43X5RE, 0DVDCMA2DK]
about: [1SFZNN31JW, GYNMZ9201M]
sources:
  - url: https://en.wikipedia.org/wiki/Principle_of_maximum_entropy
same_as:
  wikidata: Q1417473
  wikipedia: Principle of maximum entropy
---

## Statement

Let $\Omega$ be a finite set, let $f_1, \dots, f_m \colon \Omega \to \R$ be functions and let $c_1, \dots, c_m \in \R$.
Let $\mathcal{P}$ be the set of [[probability distributions|0DVDCMA2DK]] $p$ on $\Omega$ with $\sum_{\omega} p(\omega) f_k(\omega) = c_k$ for $k = 1, \dots, m$.
Let $H(p) = -\sum_{\omega} p(\omega) \ln p(\omega)$ be the entropy, with $0 \ln 0 = 0$.
Suppose there are $\lambda_1, \dots, \lambda_m \in \R$ such that the distribution
$$p^*(\omega) = \frac{1}{Z(\lambda)} \exp\Big(-\sum_{k=1}^m \lambda_k f_k(\omega)\Big), \qquad Z(\lambda) = \sum_{\omega \in \Omega} \exp\Big(-\sum_{k=1}^m \lambda_k f_k(\omega)\Big),$$
lies in $\mathcal{P}$.
Then $H(p) \le H(p^*)$ for every $p \in \mathcal{P}$, with equality only for $p = p^*$.

## Remarks

Proof idea: for $p \in \mathcal{P}$, a direct computation with the constraints gives $H(p^*) - H(p) = D(p \,\|\, p^*)$.
Here $D$ is the [[Kullback–Leibler divergence|PQBW43X5RE]], which is nonnegative and vanishes only for $p = p^*$.
Example: with one constraint, the mean energy $\sum_\omega p(\omega) E(\omega) = U$, the maximizer is the [[Boltzmann distribution|GYNMZ9201M]] $e^{-\beta E} / Z$, with $\beta$ chosen to match $U$.
With no constraint at all, the maximizer is the uniform distribution, with entropy $\ln \abs{\Omega}$.
The existence hypothesis matters: if $f_1 = E$ and $c_1 = \min E$ with a unique minimizer, no exponential family member with finite $\lambda$ matches, and the maximizer is a point mass.

## Explanations

### L1 human

Suppose all you know about a random system is a few averages, such as its mean energy.
The principle says: pick the distribution that matches these averages and is otherwise as uncertain as possible, that is, has the largest entropy.
This avoids building in information you do not have.
The answer always has an exponential form, which is why Boltzmann factors appear everywhere in physics.

### L2 human

As a theorem, it says that exponential families are the entropy maximizers under linear constraints.
As a principle of inference, proposed by E. T. Jaynes in 1957, it says that one should use these maximizers as the probability assignments.
In statistical mechanics it rederives the canonical ensemble from a mean-energy constraint and the grand canonical ensemble from mean energy and mean particle number.
The multipliers $\lambda_k$ are found from $c_k = -\partial \ln Z / \partial \lambda_k$, and they play the role of inverse temperature and of $-\beta \mu$.
