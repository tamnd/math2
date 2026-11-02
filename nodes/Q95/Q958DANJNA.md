---
tag: Q958DANJNA
kind: example
name: Kempner series
msc: [40A05, 11A63]
instance_of: [0AF7X08PCR]
uses: [0CXTMAY5PX, 0E9M24KS9J]
sources:
  - url: https://en.wikipedia.org/wiki/Kempner_series
same_as:
  wikidata: Q928481
  wikipedia: Kempner series
---

## Example

The *Kempner series* is the sum of $1/n$ over the positive integers $n$ whose decimal expansion has no digit $9$:
$$\sum_{\substack{n \ge 1 \\ \text{no digit } 9}} \frac{1}{n} = 1 + \frac{1}{2} + \cdots + \frac{1}{8} + \frac{1}{10} + \cdots + \frac{1}{18} + \frac{1}{20} + \cdots.$$
It is a [[convergent series|0AF7X08PCR]], and its sum is less than $80$.

Check: a positive integer with exactly $k$ digits and no digit $9$ has a first digit in $\set{1, \ldots, 8}$ and $k - 1$ further digits in $\set{0, \ldots, 8}$.
So there are $8 \cdot 9^{k-1}$ such integers, and each is at least $10^{k-1}$.
Their reciprocals add up to at most $8 \cdot 9^{k-1} / 10^{k-1} = 8 \cdot (9/10)^{k-1}$.
Summing over $k \ge 1$ gives the bound $8 / (1 - 9/10) = 80$.
The terms are positive, so the partial sums are increasing and bounded, and the series converges.

## Remarks

The true sum is about $22.92$.
This contrasts with the [[harmonic series|0CXTMAY5PX]], which [[diverges|0E9M24KS9J]].
The same argument works for any digit and any base: removing every integer that contains a fixed digit string leaves a convergent series.
The series is named after A. J. Kempner, who proved its convergence in 1914.
Most large integers contain a $9$: the proportion of $k$-digit integers without one is $(8/9)(9/10)^{k-1}$, which tends to $0$.

## Explanations

### L1 human

The harmonic series $1 + 1/2 + 1/3 + \cdots$ grows without bound.
Throw away every term whose denominator has a $9$ somewhere in it.
This looks like a small change, but almost all large numbers contain a $9$, so most terms disappear, and what remains adds up to a finite number, about $22.92$.
