---
tag: WGY75H4VWW
kind: statement
role: theorem
name: Titchmarsh convolution theorem
msc: [44A35, 42A85]
uses: [FCKX8KFVGN]
about: [FCKX8KFVGN]
sources:
  - url: https://en.wikipedia.org/wiki/Titchmarsh_convolution_theorem
same_as:
  wikidata: Q7809920
  wikipedia: Titchmarsh convolution theorem
---

## Statement

Let $T > 0$, and let $\varphi, \psi \colon [0, T] \to \C$ be Lebesgue integrable.
Suppose that the [[convolution|FCKX8KFVGN]]
$$(\varphi * \psi)(x) = \int_0^x \varphi(t) \, \psi(x - t) \, dt$$
is $0$ for almost every $x \in (0, T)$.
Then there are $\lambda \ge 0$ and $\mu \ge 0$ with $\lambda + \mu \ge T$ such that $\varphi = 0$ almost everywhere on $(0, \lambda)$ and $\psi = 0$ almost everywhere on $(0, \mu)$.

## Remarks

Equivalently, write $\lambda(\varphi)$ for the largest $\lambda$ such that $\varphi$ vanishes almost everywhere on $(0, \lambda)$.
Then for integrable $\varphi, \psi$ on $[0, T]$ one has $\lambda(\varphi * \psi) = \lambda(\varphi) + \lambda(\psi)$ whenever the right side is less than $T$.
A standard form concerns functions or distributions with compact support on $\R$.
It says that the convex hull of the support of $\varphi * \psi$ is the sum of the convex hulls of the supports of $\varphi$ and $\psi$.
The classical proof uses complex analysis: the Laplace or Fourier transforms of such functions are entire functions of exponential type, and the theorem reduces to growth estimates for them.
Real-variable proofs are also known.

Example: with $T = 2$ and $\varphi = \psi = \mathbf{1}_{(1, 2)}$, the convolution vanishes on $(0, 2)$, and the conclusion holds with $\lambda = \mu = 1$, so $\lambda + \mu = T$ exactly.

The easy direction is the converse: if $\varphi = 0$ on $(0, \lambda)$ and $\psi = 0$ on $(0, \mu)$, then each product $\varphi(t) \psi(x - t)$ with $x < \lambda + \mu$ vanishes, so $\varphi * \psi = 0$ on $(0, \lambda + \mu)$.

## Explanations

### L1 human

Convolving two signals that start at time $0$ can only produce silence for as long as the first signal waits plus the second signal waits.
There is no way for the two signals to cancel each other out early.
So if the convolution is zero for a long time, at least one of the signals must have been silent for a correspondingly long time.

### L2 human

Letting $T \to \infty$ gives the corollary that the [[convolution ring of continuous functions on the half-line has no zero divisors|E9QNNPQD2P]].
This is the algebraic foundation of the [[Mikusiński operational calculus|TD5XK5AHNV]], which builds the field of fractions of that ring.
The support form of the theorem is used in the theory of distributions and in the uniqueness theory of partial differential equations.
