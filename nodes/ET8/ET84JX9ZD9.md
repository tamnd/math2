---
tag: ET84JX9ZD9
kind: definition
name: Common midpoint stacking
msc: [86A22, 94A12]
defines: MKBZD2XY5G
uses: [8E7KGS4ZQH, 0477R9PYAE]
sources:
  - url: https://en.wikipedia.org/wiki/Reflection_seismology
---

## Definition

Let $d(s, r, t)$ be reflection traces for sources $s$ and receivers $r$ on a line.
The midpoint of a trace is $(s + r)/2$, and its offset is $x = \abs{r - s}$.
The *common midpoint gather* at a midpoint $y$ is the set of traces $d_k(t)$, $k = 1, \dots, N$, with midpoint $y$, of offsets $x_k$.
For a stacking velocity $v > 0$, the *common midpoint stack* at $y$ is
$$S_y(t_0) = \frac{1}{N} \sum_{k=1}^{N} d_k\Bigl(\sqrt{t_0^2 + x_k^2 / v^2}\Bigr),$$
the average of the gather after [[normal moveout|8E7KGS4ZQH]] correction.
*Common midpoint stacking* is the formation of $S_y$ for every midpoint $y$, which gives a stacked section with one trace per midpoint.

## Remarks

Example: suppose each trace is $d_k = a\, w + n_k$ after NMO correction, with a common reflection $a\, w$ and independent noises $n_k$ of [[variance|0477R9PYAE]] $\sigma^2$.
The stack is $a\, w + \frac{1}{N} \sum_k n_k$, whose noise has variance $\sigma^2 / N$; for $N = 4$ the noise standard deviation halves while the signal is unchanged.
Non-example: averaging the gather without the NMO correction sums reflections at different times, so the reflection is smeared and weakened; this fails the correction in the definition.
The number $N$ of traces in a gather is the fold of the survey.
Scanning $v$ and measuring the coherence of the corrected gather, for example by semblance, gives the stacking velocity analysis.

## Explanations

### L1 human

Group the traces by their midpoint, flatten each reflection with the moveout correction, and average.
Echoes add up and noise cancels.
