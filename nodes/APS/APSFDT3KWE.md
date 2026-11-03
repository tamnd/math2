---
tag: APSFDT3KWE
kind: statement
role: theorem
name: Slepian–Wolf theorem
msc: [94A29, 94A24, 94A15]
uses: [VKETGMSX5H, DZWEWHZ20N, F3ZNDD6GG7, 00MRN0FARV, E3A9MPV1QY, GW25TGD33J]
about: [VKETGMSX5H]
sources:
  - url: https://en.wikipedia.org/wiki/Slepian%E2%80%93Wolf_coding
---

## Statement

Let $(X_1, Y_1), (X_2, Y_2), \dots$ be [[i.i.d.|00MRN0FARV]] pairs of random variables with values in finite sets $\mathcal{X} \times \mathcal{Y}$, and let $(X, Y)$ have their common law.
Let $H(X, Y)$ be the [[joint entropy|DZWEWHZ20N]] and $H(X \mid Y)$, $H(Y \mid X)$ the [[conditional entropies|F3ZNDD6GG7]], in bits.
Consider [[distributed source codes|VKETGMSX5H]] with separate encoders for $X^n$ and $Y^n$ and one joint decoder.

1. If $R_1 > H(X \mid Y)$, $R_2 > H(Y \mid X)$ and $R_1 + R_2 > H(X, Y)$, then the rate pair $(R_1, R_2)$ is achievable.
2. If $(R_1, R_2)$ is achievable, then $R_1 \ge H(X \mid Y)$, $R_2 \ge H(Y \mid X)$ and $R_1 + R_2 \ge H(X, Y)$.

## Remarks

The achievability proof uses random binning: each encoder assigns its sequences to $2^{nR_i}$ bins at random and sends the bin index.
The decoder looks for the unique jointly typical pair in the two received bins; the rate conditions make wrong pairs unlikely.
The converse follows from [[Fano's inequality|E3A9MPV1QY]], as for a single source.

Example: let $X$ be a uniform bit and $Y = X \oplus Z$, where $Z$ is a bit independent of $X$ with $\Pr(Z = 1) = q$.
Then $H(Y) = 1$ and $H(X \mid Y) = h(q)$, with $h$ the [[binary entropy function|GW25TGD33J]].
So $Y$ can be sent at rate just above $1$ and $X$ at rate just above $h(q)$, which can be much less than $1$.
The encoder of $X$ achieves this without seeing $Y$.

## Explanations

### L1 human

Two correlated data streams are compressed by two encoders that do not communicate.
The theorem says that the total rate needed is the joint entropy, exactly as if one encoder compressed both streams together.
Separation of the encoders costs nothing, as long as the decoder works jointly.

### L2 human

The rate region is a polygon bounded by the lines $R_1 = H(X \mid Y)$, $R_2 = H(Y \mid X)$ and $R_1 + R_2 = H(X, Y)$.
Its corner point $(H(X \mid Y), H(Y))$ is coding with side information: $Y$ is compressed alone, and $X$ is compressed as if the decoder already knew $Y$.
The theorem was proved by David Slepian and Jack Wolf in 1973, and it extends to any finite number of sources.
Its lossy analogue with side information at the decoder is the Wyner–Ziv problem.
