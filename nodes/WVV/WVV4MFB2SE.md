---
tag: WVV4MFB2SE
kind: statement
role: theorem
name: Riesz–Fischer theorem
msc: ["46E30", 28A25]
uses: [SASP14MA1Z, P15VQS5DJ9, 06GZ956657]
about: [SASP14MA1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Riesz%E2%80%93Fischer_theorem
same_as:
  wikidata: Q643513
  wikipedia: Riesz–Fischer theorem
---

## Statement

Let $(X, \Sigma, \mu)$ be a [[measure space|P15VQS5DJ9]] and let $1 \le p \le \infty$.
Then the space [[$L^p(\mu)$|SASP14MA1Z]] with the norm $\norm{\cdot}_p$ is complete.
So $L^p(\mu)$ is a [[Banach space|06GZ956657]].

## Remarks

The proof for $p < \infty$ starts from a Cauchy sequence $(f_n)$ and picks a subsequence with $\norm{f_{n_{k+1}} - f_{n_k}}_p < 2^{-k}$.
The function $g = \abs{f_{n_1}} + \sum_k \abs{f_{n_{k+1}} - f_{n_k}}$ lies in $L^p$ by Minkowski's inequality and the [[monotone convergence theorem|G2S6H789RG]].
So the subsequence converges [[almost everywhere|RARTMA0ZEC]] to a function $f$, and [[Fatou's lemma|S95TR54TCG]] shows that $f \in L^p$ and $f_n \to f$ in $L^p$.
A by-product: for $p < \infty$, every sequence that converges in $L^p$ has a subsequence that converges almost everywhere.
The case $p = \infty$ is a direct argument with uniform convergence outside a null set.

The original form concerns $p = 2$.
If $(\varphi_n)$ is an orthonormal sequence in $L^2(\mu)$ and $(c_n)$ is a sequence of scalars with $\sum_n \abs{c_n}^2 < \infty$, then there is $f \in L^2(\mu)$ with $\ip{f}{\varphi_n} = c_n$ for all $n$.
For the trigonometric system on $[0, 2\pi]$, every square-summable sequence is the sequence of Fourier coefficients of some square-integrable function.

The Lebesgue integral is essential here.
The continuous functions on $[0, 1]$ with the norm $\int_0^1 \abs{f}\, dx$ do not form a complete space.

## Explanations

### L1 human

The theorem says that the spaces $L^p$ have no holes.
If the functions of a sequence get closer and closer to each other in the $L^p$ distance, then they get close to an actual function of the space.
This is the same property that the real numbers have and the rational numbers lack.
It is the main reason why analysts use the Lebesgue integral and not the Riemann integral.

### L2 human

Completeness makes the tools of Banach space theory available on $L^p$: the Baire category theorem, the open mapping theorem and the uniform boundedness principle.
For $p = 2$ it makes $L^2(\mu)$ a Hilbert space, which is the setting of Fourier series and of quantum mechanics.
The proof also gives the useful fact that $L^p$ convergence implies almost everywhere convergence along a subsequence, but not for the whole sequence.
The "typewriter" sequence of indicator functions of shrinking intervals that sweep across $[0, 1]$ converges to $0$ in $L^1$ but at no point.
