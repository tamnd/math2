---
tag: 4PF4DWH48K
kind: statement
role: theorem
name: Secrecy capacity of the wiretap channel
msc: [94A40, 94A60, 94A24]
uses: [B9C5RBFATB, A83CYGDXFG, J7MZ2XQP9M, GW25TGD33J, MTNV8Y8FDG]
about: [J7MZ2XQP9M]
sources:
  - url: https://en.wikipedia.org/wiki/Information-theoretic_security
---

## Statement

A discrete memoryless *wiretap channel* is given by finite sets $\mathcal X$, $\mathcal Y$, $\mathcal Z$ and conditional distributions $p(y, z \mid x)$, used independently at each time.
The sender's input is $X$, the legitimate receiver sees $Y$, and the eavesdropper sees $Z$.
Consider codes of block length $n$, with possibly random encoders and with at least $2^{nR}$ messages.
A rate $R$ is *achievable with secrecy* if there are such codes with the following properties for a uniform message $W$:

1. the legitimate receiver decodes $W$ from $Y^n$ with error probability tending to $0$, and
2. $\frac1n I(W; Z^n) \to 0$ as $n \to \infty$, where $I$ is the [[mutual information|A83CYGDXFG]].

The *secrecy capacity* $C_s$ is the supremum of these rates.
Then:

1. (Csiszár and Körner) $C_s = \max \big[ I(U; Y) - I(U; Z) \big]$, where the maximum runs over joint distributions of an auxiliary variable $U$ and $X$ such that $U \to X \to (Y, Z)$ is a Markov chain.
2. (Wyner) If the channel is degraded, that is, $X \to Y \to Z$ is a Markov chain, then $C_s = \max_{p(x)} \big[ I(X; Y) - I(X; Z) \big]$.

## Remarks

The idea of the proof of achievability is random binning.
The sender uses a codebook with about $2^{n I(X; Y)}$ codewords, split into bins of about $2^{n I(X; Z)}$ codewords each, one bin per message.
It sends a codeword chosen at random in the bin of the message.
The legitimate receiver can find the codeword, while the eavesdropper sees a bin that looks almost uniformly random to it.

Example: let $Y = X$ with $X \in \set{0, 1}$, and let $Z$ be $X$ sent through a binary symmetric channel with crossover probability $p$.
This channel is degraded, and $I(X; Y) - I(X; Z) = H(X) - H(Z) + h(p)$, where $h$ is the [[binary entropy function|GW25TGD33J]].
Since $H(Z) \ge H(X)$, this is at most $h(p)$, with equality for uniform $X$; so $C_s = h(p)$.

If the eavesdropper's channel is at least as good as the main channel, for example $Z = Y$, then $C_s = 0$.
Secrecy here is reached without any shared secret key, only by the advantage of the main channel over the eavesdropper's channel.

## Explanations

### L1 human

Alice talks to Bob over a noisy line, and Eve listens on a line that is even noisier.
The theorem gives the rate at which Alice can send messages that Bob understands and about which Eve learns essentially nothing.
In simple cases the answer is a difference: what Bob can learn minus what Eve can learn.

### L2 human

Wyner introduced the wiretap channel in 1975, and Csiszár and Körner extended the result to channels that are not degraded in 1978.
The auxiliary variable $U$ in part 1 is needed in general, and it acts as a prefix channel that the sender adds on purpose.
The secrecy measure in clause 2 is weak secrecy; it is known that the strong criterion $I(W; Z^n) \to 0$ gives the same capacity.
For Gaussian channels with noise variances $N_1 < N_2$ for Bob and Eve and power $P$, the secrecy capacity is $\frac12 \log_2(1 + P/N_1) - \frac12 \log_2(1 + P/N_2)$.
Compare [[Shannon's perfect secrecy theorem|MTNV8Y8FDG]], where secrecy needs a key as long as the message.
