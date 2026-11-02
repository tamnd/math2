---
tag: HK8339ECNN
kind: statement
role: theorem
name: Shannon–McMillan–Breiman theorem
msc: [37A35, 28D20, 94A17]
uses: [0NFPJVJJHX, 556WBDAHNP, AZRPHS478B, X1D1C7VH6P, RARTMA0ZEC, 08QMKTWF9T]
about: [X1D1C7VH6P]
sources:
  - url: https://en.wikipedia.org/wiki/Asymptotic_equipartition_property
---

## Statement

Let $(X, \mathcal{B}, \mu)$ be a [[probability space|0NFPJVJJHX]] and let $T \colon X \to X$ be an [[ergodic|AZRPHS478B]] [[measure-preserving transformation|556WBDAHNP]].
Let $\mathcal{P}$ be a finite measurable [[partition|08QMKTWF9T]] of $X$.
Let $h(T, \mathcal{P})$ be the entropy of $T$ with respect to $\mathcal{P}$, as in the definition of the [[Kolmogorov–Sinai entropy|X1D1C7VH6P]].
For $n \ge 1$ and $x \in X$, let $\mathcal{P}_n(x)$ be the set of the partition $\bigvee_{i=0}^{n-1} T^{-i}\mathcal{P}$ that contains $x$.
Then
$$\lim_{n \to \infty} -\frac{1}{n} \log \mu(\mathcal{P}_n(x)) = h(T, \mathcal{P})$$
for [[almost every|RARTMA0ZEC]] $x \in X$, and also in $L^1(\mu)$.

## Remarks

The set $\mathcal{P}_n(x)$ consists of the points whose first $n$ positions $x, Tx, \dots, T^{n-1}x$ lie in the same sets of $\mathcal{P}$ as those of $x$.
The function $-\log \mu(\mathcal{P}_n(x))$ is the information carried by these $n$ symbols, and its integral is $H(\bigvee_{i=0}^{n-1} T^{-i}\mathcal{P})$.
So the convergence in $L^1$ refines the definition of $h(T, \mathcal{P})$, and the theorem says that the information per symbol is almost surely constant.
The proof writes the information as a Birkhoff sum of conditional information functions, plus an error, and applies Birkhoff's ergodic theorem together with the martingale convergence theorem.
Shannon proved convergence in probability for ergodic Markov sources, McMillan proved $L^1$ convergence for stationary ergodic sources, and Breiman proved almost sure convergence.
Example: for the Bernoulli scheme $B(p_1, \dots, p_k)$ with the partition by the zeroth coordinate, $\mu(\mathcal{P}_n(x)) = p_{x_0} \cdots p_{x_{n-1}}$, and the theorem is the strong law of large numbers for the i.i.d. variables $-\log p_{x_i}$, whose mean is $-\sum p_i \log p_i$.
Without ergodicity the limit still exists almost everywhere, but it is an invariant function whose integral is $h(T, \mathcal{P})$.

## Explanations

### L1 human

Watch a long stretch of output of a stationary random source, such as a long English text.
The theorem says that almost every long stretch of $n$ symbols has probability close to $e^{-nh}$, where $h$ is the entropy of the source.
So the likely messages all have about the same probability, and there are about $e^{nh}$ of them.

### L2 human

This is the asymptotic equipartition property, the basis of data compression: about $nh$ nats, or $nh / \log 2$ bits, suffice to encode a typical message of length $n$.
In ergodic theory it gives a local, pointwise meaning to the [[Kolmogorov–Sinai entropy|X1D1C7VH6P]].
It is a key tool in the proofs of the Ornstein isomorphism theorem and of Sinai's factor theorem, and it has analogues for actions of amenable groups.
