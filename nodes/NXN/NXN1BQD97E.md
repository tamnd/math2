---
tag: NXN1BQD97E
kind: statement
role: theorem
name: Channel polarization theorem
msc: [94A24, 94B05]
uses: [BV9X42B8KH, A83CYGDXFG, B9C5RBFATB, 0D0GBNDKDH, J7MZ2XQP9M, ESYMTB37YG, W773330RK7]
about: [SAVK6PAFQ5]
sources:
  - url: https://en.wikipedia.org/wiki/Polar_code_(coding_theory)
---

## Statement

Let $W$ be a binary-input discrete memoryless [[channel|B9C5RBFATB]].
Let $I(W)$ be its symmetric capacity, the [[mutual information|A83CYGDXFG]] between a uniform input bit and the output.
For $N = 2^n$ and $1 \le i \le N$, let $W_N^{(i)}$ be the synthetic channels of the [[polar code|SAVK6PAFQ5]] construction.
Then for every $\delta \in (0, 1)$,
$$\lim_{n \to \infty} \frac{\abs{\set{i : I(W_N^{(i)}) > 1 - \delta}}}{N} = I(W) \quad \text{and} \quad \lim_{n \to \infty} \frac{\abs{\set{i : I(W_N^{(i)}) < \delta}}}{N} = 1 - I(W).$$

## Remarks

One step of the construction turns two copies of a channel $V$ into $V^-$ and $V^+$ with $I(V^-) + I(V^+) = 2 I(V)$ and $I(V^-) \le I(V) \le I(V^+)$.
Choosing $-$ or $+$ at random at each of $n$ steps gives a random process $I_n$ that is a bounded [[martingale|0D0GBNDKDH]], so it converges almost surely.
At a limit point the step must no longer change the mutual information, which happens only for perfect or useless channels.
So the limit takes values in $\set{0, 1}$, and its mean is $I(W)$.

As a consequence, polar codes with successive cancellation decoding achieve the symmetric capacity: for every rate $R < I(W)$, the block error probability tends to $0$ as $N \to \infty$.
Arıkan and Telatar showed that it decays like $2^{-N^{\beta}}$ for every $\beta < 1/2$.
Example: for the [[binary erasure channel|ESYMTB37YG]] with erasure probability $\varepsilon$, $I(W) = 1 - \varepsilon$.
The erasure probabilities of the synthetic channels evolve by $\varepsilon \mapsto 2\varepsilon - \varepsilon^2$ or $\varepsilon \mapsto \varepsilon^2$.
A fraction tending to $1 - \varepsilon$ of them goes to $0$.

## Explanations

### L1 human

Mixing copies of a noisy channel in a clever recursive way produces new channels that are almost all either nearly noiseless or nearly pure noise.
The fraction of nearly noiseless ones is exactly the capacity of the original channel.
So one can send data on the good channels and ignore the bad ones, and in the limit this reaches capacity.

### L2 human

The theorem is the engine behind [[polar codes|SAVK6PAFQ5]], the first explicit family proved to achieve the symmetric capacity of all binary-input memoryless channels with an $O(N \log N)$ decoder.
For symmetric channels such as the [[binary symmetric channel|W773330RK7]] and the [[binary erasure channel|ESYMTB37YG]], the symmetric capacity equals the [[channel capacity|J7MZ2XQP9M]].
The proof is a martingale argument and is not constructive about the speed of polarization; the rate-of-polarization results of Arıkan and Telatar supply the error bounds needed for coding.
