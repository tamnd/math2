---
tag: 5P7AA5QR7T
kind: statement
role: theorem
name: Asymptotic equipartition property
msc: [94A17, 94A29, 60F15]
uses: [00MRN0FARV, 0D6J4B671D, Y86E072V0V, 0DFWHQ839T, 0AAXWGT5TD]
about: [Y86E072V0V]
sources:
  - url: https://en.wikipedia.org/wiki/Asymptotic_equipartition_property
same_as:
  wikidata: Q4812181
  wikipedia: Asymptotic equipartition property
---

## Statement

Let $\mathcal{X}$ be a finite set, and let $p$ be a [[probability mass function|0D6J4B671D]] on $\mathcal{X}$.
Let $X_1, X_2, \dots$ be [[independent and identically distributed|00MRN0FARV]] random variables with law $p$, and let $H = -\sum_x p(x) \log p(x)$ be their [[Shannon entropy|Y86E072V0V]].
For $n \ge 1$ let $p(X_1, \dots, X_n) = p(X_1) \cdots p(X_n)$.
Then
$$-\frac1n \log p(X_1, \dots, X_n) \to H$$
[[almost surely|0AAXWGT5TD]] as $n \to \infty$, and hence also in probability.

## Remarks

Proof idea: $-\frac1n \log p(X_1, \dots, X_n) = \frac1n \sum_{i=1}^n (-\log p(X_i))$ is an average of independent copies of the random variable $-\log p(X_1)$.
This variable takes finitely many values, and its mean is $H$, so the [[strong law of large numbers|0DFWHQ839T]] applies.

Example: for a coin with $p(1) = \frac14$ and $p(0) = \frac34$, a typical sequence of length $n$ has about $n/4$ ones, so its probability is about $(\frac14)^{n/4} (\frac34)^{3n/4} = 2^{-n H}$ with $H = H_b(\frac14) \approx 0.811$ bits.

The independence can be weakened: the [[Shannon–McMillan–Breiman theorem|HK8339ECNN]] gives the same conclusion for stationary ergodic sources.
Without ergodicity it fails: if $X_1 = X_2 = \cdots$ is a single fair bit, then every block $(X_1, \dots, X_n)$ that occurs has probability $\frac12$.
So minus $\frac1n$ times the logarithm of its probability is $\frac1n \to 0$, while each $X_i$ has entropy $1$ bit.

## Explanations

### L1 human

Toss a biased coin many times.
Almost surely, the sequence you get has a probability close to $2^{-nH}$, where $H$ is the entropy per toss.
So the long sequences that actually occur are nearly equally likely, and there are about $2^{nH}$ of them.
This is where the name equipartition comes from.

### L2 human

The property says that a source of entropy $H$ behaves, for long blocks, like a uniform source on about $2^{nH}$ sequences, the [[typical set|6J90EN65VQ]].
Encoding only these sequences proves the achievability half of [[Shannon's source coding theorem|PC8ASRWARE]].
Its joint version, for pairs of sequences, is the main tool in the random coding proof of the [[noisy-channel coding theorem|PR3NJB0SKG]].
