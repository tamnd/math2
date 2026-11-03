---
tag: PZV5HW9BT7
kind: example
name: Repetition code
msc: [94B05, 94B25]
instance_of: [E85KREWV60]
uses: [8TXKFC5PRD, M2X88AXM17, 94K1WWWGF6]
sources:
  - url: https://en.wikipedia.org/wiki/Repetition_code
same_as:
  wikidata: Q369367
  wikipedia: Repetition code
---

## Example

Let $q$ be a prime power and $n \ge 1$.
The *repetition code* of length $n$ over $\F_q$ is
$$C = \set{(a, a, \dots, a) : a \in \F_q} \subseteq \F_q^n.$$
It is a [[linear code|E85KREWV60]]: it is the span of the all-ones word $(1, \dots, 1)$, which is a [[generator matrix|8TXKFC5PRD]] with one row.
So it has dimension $1$ and $q$ codewords.
Two different codewords $(a, \dots, a)$ and $(b, \dots, b)$ differ in all $n$ positions, so its [[minimum distance|M2X88AXM17]] is $n$, and it is an $[n, 1, n]$ code.
It therefore corrects $\floor{(n - 1)/2}$ errors, by a majority vote over the $n$ received symbols.

## Remarks

The binary repetition code of odd length $n = 2t + 1$ is a [[perfect code|94K1WWWGF6]].
Indeed every word of $\F_2^n$ has at most $t$ ones or at most $t$ zeros, but not both.
So it lies within distance $t$ of exactly one of $0 \cdots 0$ and $1 \cdots 1$.
Its rate $1/n$ tends to $0$, so it is a poor code for long messages.
The dual of the binary repetition code is the even-weight code, the code of all words with an even number of ones.

## Explanations

### L1 human

To protect a bit, send it several times: $00000$ for $0$ and $11111$ for $1$.
The receiver takes a majority vote, so the bit is still right if fewer than half of the copies were flipped.
This is the simplest error-correcting code, and it shows the price of protection: five times as much is sent for the same information.
