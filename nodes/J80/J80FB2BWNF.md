---
tag: J80FB2BWNF
kind: statement
role: lemma
name: Kac's lemma
msc: [37A05, 28D05, 60G10]
uses: [0NFPJVJJHX, 556WBDAHNP, AZRPHS478B, TVYJPBHD0S]
about: [556WBDAHNP]
sources:
  - url: https://en.wikipedia.org/wiki/Kac%27s_lemma
same_as:
  wikidata: Q97032821
  wikipedia: Kac's lemma
---

## Statement

Let $(X, \mathcal{B}, \mu)$ be a [[probability space|0NFPJVJJHX]] and let $T \colon X \to X$ be an [[ergodic|AZRPHS478B]] [[measure-preserving transformation|556WBDAHNP]].
Let $A \in \mathcal{B}$ with $\mu(A) > 0$, and for $x \in A$ let
$$r_A(x) = \min\set{n \ge 1 : T^n x \in A}$$
be the first return time of $x$ to $A$, which is finite for almost every $x \in A$.
Then
$$\int_A r_A \, d\mu = 1, \qquad \text{that is,} \qquad \frac{1}{\mu(A)} \int_A r_A \, d\mu = \frac{1}{\mu(A)}.$$

## Remarks

The return time is finite almost everywhere on $A$ by the [[Poincaré recurrence theorem|TVYJPBHD0S]].
For invertible $T$, let $A_n = \set{x \in A : r_A(x) = n}$.
The sets $T^j A_n$ with $n \ge 1$ and $0 \le j < n$ are pairwise disjoint, and their union is invariant up to a null set and contains $A$, so by ergodicity it has measure $1$.
Hence $1 = \sum_{n \ge 1} n \, \mu(A_n) = \int_A r_A \, d\mu$.
The non-invertible case follows by passing to the natural extension.
Example: for the rotation $x \mapsto x + 1/q \bmod 1$ on $\set{0, 1/q, \dots, (q-1)/q}$ with the uniform measure and $A$ a single point, the return time is $q$ and $\int_A r_A \, d\mu = q \cdot \frac{1}{q} = 1$.
Without ergodicity the integral equals the measure of the set of points whose orbit meets $A$, which can be less than $1$.
For the identity map, $r_A = 1$ on $A$ and $\int_A r_A \, d\mu = \mu(A)$.

## Explanations

### L1 human

The rarer a set of states, the longer it takes to come back to it, and the lemma gives the exact rate.
If a set has probability $\mu(A)$, then starting from that set, the average waiting time to return is $1/\mu(A)$.
For example, if a fair die is rolled again and again, a six comes back after $6$ rolls on average.

### L2 human

Kac's lemma explains why Poincaré recurrence does not contradict the second law of thermodynamics.
For a macroscopic system, the set of states near a given low-entropy state has astronomically small measure.
So the mean return time is astronomically long.
It is also the basis of the induced transformation $T_A(x) = T^{r_A(x)} x$ on $A$, which preserves the normalized measure on $A$ and is ergodic when $T$ is.
For an ergodic Markov chain started at a state $s$ with stationary probability $\pi(s) > 0$, it gives the classical formula $1/\pi(s)$ for the expected return time to $s$.
