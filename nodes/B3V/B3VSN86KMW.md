---
tag: B3VSN86KMW
kind: statement
role: fact
name: Zipf's law
msc: [91F20, 62P25]
uses: [0NANDX7V02, 1XWBY4N0VT]
sources:
  - url: https://en.wikipedia.org/wiki/Zipf's_law
same_as:
  wikidata: Q205472
  wikipedia: Zipf's law
---

## Statement

Let a large text corpus have $N$ distinct words, ranked $r = 1, \dots, N$ by decreasing number of occurrences.
Let $f(r)$ be the relative frequency of the word of rank $r$.
*Zipf's law* is the empirical regularity that, for natural languages,
$$f(r) \approx \frac{r^{-s}}{H_{N,s}}, \qquad H_{N,s} = \sum_{k=1}^{N} k^{-s},$$
with an exponent $s$ close to $1$; so $r \, f(r)$ is roughly constant.

## Remarks

This is an observed approximation, not a theorem, and it is least accurate for the highest and lowest ranks.
For $s = 1$ the normalising constant $H_{N,1}$ is the [[harmonic number|0NANDX7V02]] $H_N \approx \ln N + 0.5772$.
For $s > 1$ and $N = \infty$ the constant is the [[Riemann zeta function|1XWBY4N0VT]] value $\zeta(s)$, which gives the zeta distribution.
Example: with $s = 1$, the second most common word occurs about half as often as the most common one, and the third about a third as often.
On a log-log plot of frequency against rank, Zipf's law appears as a straight line of slope $-s$.
Similar rank-size rules are reported for city populations and firm sizes.

## Explanations

### L1 human

In English text, "the" is the most common word, and the next most common words appear about half as often, a third as often, and so on.
In general, the word in place $r$ appears about $1/r$ times as often as the top word.
A few words are used all the time, and a huge number of words are rare.

### L2 human

The law is named after the linguist George Kingsley Zipf, who studied it widely.
Rank-frequency laws of this kind are equivalent to power-law tails for the distribution of frequencies, related to the Pareto distribution.
Several mechanisms produce it, such as preferential attachment and random typing models, so a good fit says little about the cause.
