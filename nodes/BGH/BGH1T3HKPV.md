---
tag: BGH1T3HKPV
kind: statement
role: theorem
name: Data processing inequality
msc: [94A17, 94A15]
uses: [0X2J0VY6DN, 0THJ7416DX, 0G48PYM96Q, A83CYGDXFG, PW6PXZ2WV4]
about: [A83CYGDXFG]
sources:
  - url: https://en.wikipedia.org/wiki/Data_processing_inequality
same_as:
  wikidata: Q20707568
  wikipedia: Data processing inequality
---

## Statement

Let $X$, $Y$ and $Z$ be [[discrete random variables|0X2J0VY6DN]] on a common probability space.
Assume that $X$ and $Z$ are [[conditionally independent|0THJ7416DX]] given $Y$, that is, $X \to Y \to Z$ is a [[Markov chain|0G48PYM96Q]].
Then
$$I(X; Z) \le I(X; Y),$$
where $I$ denotes the [[mutual information|A83CYGDXFG]].

## Remarks

Proof idea: expand $I(X; Y, Z)$ by the chain rule in two ways, $I(X; Y, Z) = I(X; Z) + I(X; Y \mid Z) = I(X; Y) + I(X; Z \mid Y)$.
The Markov condition gives $I(X; Z \mid Y) = 0$, and the [[conditional mutual information|PW6PXZ2WV4]] $I(X; Y \mid Z)$ is non-negative.
If $I(X; Y)$ is finite, equality holds exactly when $I(X; Y \mid Z) = 0$, that is, when $X \to Z \to Y$ is also a Markov chain.

Example: if $Z = g(Y)$ for a function $g$, the Markov condition holds, so $I(X; g(Y)) \le I(X; Y)$.
Thus no processing of an observation $Y$, deterministic or random, can increase the information it carries about $X$.

The Markov hypothesis is needed: for independent fair bits $X$ and $Y$ and $Z = X$, one has $I(X; Y) = 0$ but $I(X; Z) = 1$ bit.
Here $Z$ depends on $X$ directly and not only through $Y$.
The same inequality holds for general random variables, with mutual information defined through the Kullback–Leibler divergence.

## Explanations

### L1 human

If $Z$ is computed from $Y$ alone, possibly with some extra randomness, then $Z$ can not know more about $X$ than $Y$ does.
Post-processing never creates information.
A blurred copy of a photograph tells at most as much about the scene as the photograph itself.

### L2 human

The inequality is used in every converse proof of information theory: an estimate $\hat{X}$ made from a channel output satisfies $I(X; \hat{X}) \le I(X; Y)$, and this is combined with [[Fano's inequality|E3A9MPV1QY]].
The analogue for divergences states $D(PK \,\|\, QK) \le D(P \,\|\, Q)$ for a Markov kernel $K$, and it holds for every [[f-divergence|TC7SQFTN3A]].
