---
tag: 0NMWG2PHJ0
kind: example
name: Birthday problem
aliases: [birthday-paradox]
msc: [60C05]
uses: [0AKNPYQ04R, 0PQEBTYDZM]
sources:
  - url: https://en.wikipedia.org/wiki/Birthday_problem
    locator: Calculating the probability
same_as:
  wikidata: Q339000
  wikipedia: Birthday problem
---

## Example

Assume that each person has a birthday on one of $365$ days, and that each day is equally likely.
Assume also that the birthdays of different people are independent.
Let $p(n)$ be the probability that among $n$ people, at least two have the same birthday.
By the [[rule for the complement|0PQEBTYDZM]], for $1 \le n \le 365$,
$$p(n) = 1 - \frac{365 \cdot 364 \cdots (365 - n + 1)}{365^n}.$$
Then $p(22) \approx 0.476$ and $p(23) \approx 0.507$. So $23$ people are enough for a probability above $1/2$.

## Remarks

The answer is surprising because there are many pairs: $23$ people form $\binom{23}{2} = 253$ pairs.
For $n$ much smaller than $365$, $p(n) \approx 1 - e^{-n(n-1)/730}$.
For $n = 70$, $p(n) > 0.999$. For $n \ge 366$, $p(n) = 1$ by the pigeonhole principle.

## Explanations

### L1 human

It is easier to compute the chance that all birthdays are different.
The second person must avoid $1$ day, the third person must avoid $2$ days, and so on. These small losses multiply quickly.
