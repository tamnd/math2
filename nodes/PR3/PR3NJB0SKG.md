---
tag: PR3NJB0SKG
kind: statement
role: theorem
name: Noisy-channel coding theorem
msc: [94A24, 94A40]
uses: [B9C5RBFATB, J7MZ2XQP9M, 5P7AA5QR7T]
about: [J7MZ2XQP9M]
sources:
  - url: https://en.wikipedia.org/wiki/Noisy-channel_coding_theorem
same_as:
  wikidata: Q2345282
  wikipedia: Noisy-channel coding theorem
---

## Statement

Let $(\mathcal{X}, W, \mathcal{Y})$ be a discrete memoryless [[channel|B9C5RBFATB]] with [[capacity|J7MZ2XQP9M]] $C$ in bits.
A *code* of length $n$ with $M$ messages is a pair of maps $e \colon \set{1, \dots, M} \to \mathcal{X}^n$ and $d \colon \mathcal{Y}^n \to \set{1, \dots, M}$.
For a message $m$, let $\lambda_m$ be the probability that $d(Y^n) \ne m$, where $Y^n$ has law $W^n(\cdot \mid e(m))$.

Let $0 \le R < C$ and $\varepsilon > 0$.
Then for every large enough $n$ there is a code of length $n$ with $M \ge 2^{nR}$ messages and $\max_m \lambda_m \le \varepsilon$.

## Remarks

Shannon's proof picks the codewords at random, each letter independently with a capacity-achieving law $p$.
The decoder looks for the unique codeword that is jointly typical with the received word, using the [[asymptotic equipartition property|5P7AA5QR7T]].
The average error over the random choice of code tends to $0$ when $R < C$, so some code has small average error.
Removing the worse half of its codewords gives a small maximal error, at the cost of one message bit.

Example: for the channel that flips each bit with probability $0.1$, the capacity is $1 - h(0.1) \approx 0.531$ bits.
So rate $1/2$ is achievable: one can send $n/2$ bits in $n$ channel uses with error probability tending to $0$.
The repetition of each bit, by contrast, only lowers the error by lowering the rate towards $0$.

## Explanations

### L1 human

Noise does not have to make communication unreliable.
As long as one sends information more slowly than the capacity, long enough codes make the chance of an error as small as one likes.
Shannon published this result in 1948, and it started the search for good error-correcting codes.

### L2 human

The theorem is an existence result: the random coding argument shows that good codes exist but does not construct them.
Explicit codes reaching capacity came much later, for example polar codes for binary-input symmetric channels.
The converse shows that rates above $C$ are not achievable, so $C$ is exactly the supremum of achievable rates.
For rates below $C$ the error probability can even be made to decrease exponentially in $n$.
