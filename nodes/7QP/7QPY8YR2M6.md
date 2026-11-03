---
tag: 7QPY8YR2M6
kind: statement
role: theorem
name: Dirty paper coding theorem
msc: [94A40, 94A24]
uses: [RYFPT7P01J, J7MZ2XQP9M, A83CYGDXFG, 05AQE0QR0D]
about: [J7MZ2XQP9M]
sources:
  - url: https://en.wikipedia.org/wiki/Dirty_paper_coding
---

## Statement

Let $P, Q, N > 0$.
Consider the channel $Y_i = X_i + S_i + Z_i$ for $i = 1, \dots, n$.
Here $S_1, \dots, S_n$ are independent with the [[normal distribution|05AQE0QR0D]] $N(0, Q)$, and $Z_1, \dots, Z_n$ are independent with distribution $N(0, N)$.
The $S_i$ and $Z_i$ are independent of each other and of the message.
The whole interference sequence $S^n = (S_1, \dots, S_n)$ is known to the encoder before transmission, but not to the decoder.
The codeword $x^n$ may depend on the message and on $S^n$, and it must satisfy $\frac1n \sum_{i=1}^n x_i^2 \le P$.
Then the [[capacity|J7MZ2XQP9M]] of this channel is
$$C = \frac12 \log_2\!\left(1 + \frac{P}{N}\right),$$
the same as the capacity of the [[AWGN channel|RYFPT7P01J]] without interference.

## Remarks

The idea of the proof: consider a channel with a state known non-causally at the encoder.
For it, the Gelfand–Pinsker theorem gives the capacity $\max [I(U; Y) - I(U; S)]$ over auxiliary variables $U$, where $I$ is [[mutual information|A83CYGDXFG]].
Costa chose $X \sim N(0, P)$ independent of $S$ and $U = X + \alpha S$ with $\alpha = P / (P + N)$.
A direct computation shows that $I(U; Y) - I(U; S) = \frac12 \log_2(1 + P/N)$.
This value cannot be beaten, because even a decoder that knows $S$ could not do better than the AWGN channel.

The hypothesis that the encoder knows $S^n$ in advance is essential.
If neither side knows $S$, the interference acts as extra noise and the capacity drops to $\frac12 \log_2\big(1 + P/(Q + N)\big)$.
The result does not depend on $Q$, so the interference can be arbitrarily strong.

## Explanations

### L1 human

Imagine writing a message on a sheet of paper that already has dirt on it.
You can see the dirt, but the reader cannot tell dirt from ink.
The theorem says that, if you plan your writing around the dirt, the reader can get as much information as from a clean sheet.
Known interference costs nothing, even though the receiver does not know it.

### L2 human

Max Costa proved the theorem in 1983 in a paper titled "Writing on dirty paper", which gave the technique its name.
It is a special case of channels with state information at the transmitter, studied by Gelfand and Pinsker.
Its main use is in the Gaussian broadcast channel with several antennas: the transmitter encodes users one after another and treats the signals of earlier users as known interference.
This scheme achieves the capacity region of the multiple-antenna Gaussian broadcast channel.
Practical versions use lattice codes and modulo arithmetic to cancel the known interference.
