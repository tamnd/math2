---
tag: 0X8HBKCSYB
kind: statement
role: proposition
name: Continuity of probability measures
aliases: [continuity-from-below, continuity-from-above]
msc: [60A10]
uses: [0ZYBZ34RT2, 0VGMEBVW1M]
sources:
  - url: https://en.wikipedia.org/wiki/Measure_(mathematics)
    locator: Continuity from below
---

## Statement

Let $(\Omega, \mathcal{F}, P)$ be a [[probability space|0ZYBZ34RT2]].
If $A_1 \subseteq A_2 \subseteq \cdots$ are events and $A = \bigcup_{n=1}^{\infty} A_n$, then $\lim_{n \to \infty} P(A_n) = P(A)$.
If $B_1 \supseteq B_2 \supseteq \cdots$ are events and $B = \bigcap_{n=1}^{\infty} B_n$, then $\lim_{n \to \infty} P(B_n) = P(B)$.

## Remarks

The first part is continuity from below. Its proof writes $A$ as the disjoint union of $A_1$ and the sets $A_{n+1} \setminus A_n$, and uses countable additivity.
The second part, continuity from above, follows from the first part with the complements $B_n^c$.
For a general measure $\mu$, continuity from above needs $\mu(B_1) < \infty$. A [[probability measure|0VGMEBVW1M]] is finite, so this holds.
For example, $P(X \le x + 1/n) \to P(X \le x)$ for a real random variable $X$. This gives the right continuity of the cumulative distribution function.

## Explanations

### L1 human

If events grow step by step, their probabilities grow toward the probability of the limit event.
For example, the chance that a fair coin shows heads at least once in the first $n$ tosses is $1 - 2^{-n}$. It tends to the chance $1$ of heads at some toss.
