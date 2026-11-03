---
tag: 9ZEBGCR93V
kind: statement
role: fact
name: Gutenberg–Richter law
msc: [86A15, 62P12, 60G55]
uses: [F8YBKFKFMX, 8QWGDVEH46, 88YRH7XQDX, 0E99F51GVB, 5N3P64YHQR]
about: [8QWGDVEH46]
sources:
  - url: https://en.wikipedia.org/wiki/Gutenberg%E2%80%93Richter_law
same_as:
  wikidata: Q507905
  wikipedia: Gutenberg–Richter law
---

## Statement

Consider the earthquakes in a large region over a long time window.
Their magnitudes are measured on a fixed scale, such as the [[Richter|F8YBKFKFMX]] or the [[moment magnitude|8QWGDVEH46]] scale.
Let $M_c$ be the magnitude of completeness, above which all events are recorded.
Let $N(M)$ be the number of earthquakes with magnitude at least $M$.
Empirically there are constants $a$ and $b$ such that, for $M \ge M_c$,
$$\log_{10} N(M) = a - bM,$$
and $b$ is close to $1$ for tectonic earthquakes.

## Remarks

This is an observed regularity, not a theorem.
It holds over many orders of magnitude of $N$, with departures at the largest magnitudes because of small samples and finite fault size.
Equivalently, the magnitudes above $M_c$ follow an [[exponential distribution|0E99F51GVB]] with rate $\beta = b \ln 10$: the probability that $M \ge m$ is $10^{-b(m - M_c)}$.
Its maximum likelihood estimate from magnitudes $M_1, \dots, M_k$ is $\hat b = \log_{10} e / (\bar M - M_c)$, where $\bar M$ is their mean.
Example: with $b = 1$, each step of one unit in magnitude reduces the number of earthquakes tenfold.
A region with $1000$ events of magnitude at least $3$ per year has about $10$ of magnitude at least $5$.
Since $M_w = \frac23(\log_{10} M_0 - 9.1)$, the [[seismic moments|88YRH7XQDX]] then follow a [[Pareto distribution|5N3P64YHQR]]: $N(M_0) \propto M_0^{-2b/3}$.

## Explanations

### L1 human

Small earthquakes are common and large ones rare, in a very regular way.
In most regions, for every earthquake of magnitude $6$ there are about ten of magnitude $5$ and a hundred of magnitude $4$.
This lets seismologists estimate how often large earthquakes should happen from counts of small ones.

### L2 human

In the language of probability, magnitudes are exponentially distributed and moments are power-law distributed, which makes earthquake size scale-invariant.
The $b$-value is estimated from catalogues and is a basic input of probabilistic seismic hazard analysis.
Its variations in space and time are studied as possible signs of changes in stress.
Combined with Omori's law for aftershocks, it forms the core of statistical earthquake models such as the ETAS model.
