---
tag: 7SWYFFHDBF
kind: definition
name: Censoring
msc: [62N01, 62N02]
defines: MY8ZZP84NP
uses: [0PNRKMRC55, 0GBJACNAP6]
sources:
  - url: https://en.wikipedia.org/wiki/Censoring_(statistics)
---

## Definition

Let $T$ be a real [[random variable|0PNRKMRC55]] of interest.
An observation of $T$ is *censored* if it reveals only that $T$ lies in a set, rather than the value of $T$.
The standard types are:

1. *Right censoring*: for a censoring time $C$, one observes $\tilde T = \min(T, C)$ and $\delta = \mathbf{1}\set{T \le C}$; when $\delta = 0$ one only learns $T > C$.
2. *Left censoring*: one only learns $T \le c$ for a known $c$.
3. *Interval censoring*: one only learns $L < T \le R$ for known $L < R$.

## Remarks

Right censoring is called *independent* when $T$ and $C$ are [[independent|0GBJACNAP6]]; most standard methods of survival analysis assume this or a closely related non-informative censoring condition.

Example: a patient enters a study at month $0$, the study closes at month $24$, and the patient has had no relapse by then.
With $T$ the relapse time and $C = 24$, the record is $\tilde T = 24$, $\delta = 0$, which says exactly that $T > 24$.

Non-example: truncation is different.
Suppose a study only includes people whose event time exceeds $5$.
Then those with $T \le 5$ never appear in the data, so nothing about them is observed, not even a bound.
