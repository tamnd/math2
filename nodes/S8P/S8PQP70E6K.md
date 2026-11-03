---
tag: S8PQP70E6K
kind: statement
role: fact
name: Båth's law
msc: [86A15, 62P12]
uses: [F8YBKFKFMX, 8QWGDVEH46, 9ZEBGCR93V]
about: [7XSYER25YA, 9ZEBGCR93V]
sources:
  - url: https://en.wikipedia.org/wiki/Aftershock
    locator: Båth's law
---

## Statement

Consider an earthquake sequence with a mainshock of [[magnitude|8QWGDVEH46]] $M_m$, and let $M_a$ be the magnitude of the largest aftershock of the sequence.
Then, empirically and on average over many sequences,
$$M_m - M_a \approx 1.2,$$
and this average difference does not depend on the size of the mainshock.

## Remarks

The law is an observed regularity of earthquake catalogues, not a theorem, and it is named after the Swedish seismologist Markus Båth.
Single sequences scatter widely around the value $1.2$.
A standard heuristic explanation combines two other laws.
The magnitudes of aftershocks follow the [[Gutenberg–Richter law|9ZEBGCR93V]] with the same $b$-value as other earthquakes.
If the total number of aftershocks above a fixed magnitude grows like $10^{b M_m}$, then the expected largest of them lies a fixed amount below $M_m$, which gives a constant difference.
Example: a mainshock of magnitude $7.0$ is expected to have a largest aftershock of magnitude about $5.8$.
Together with [[Omori's law|7XSYER25YA]] for the decay of the aftershock rate in time, the law is used to forecast the hazard after a large earthquake.

## Explanations

### L1 human

After a large earthquake many smaller ones follow, called aftershocks.
Båth's law says that the biggest aftershock is usually about $1.2$ magnitude units smaller than the main earthquake.
Since magnitude is logarithmic, this means the largest aftershock releases only a few percent of the energy of the mainshock.

### L2 human

Båth's law is one of three classical statistical laws of aftershocks, next to the Gutenberg–Richter law for sizes and Omori's law for times.
It is often explained by self-similar statistics.
When aftershock productivity and the magnitude distribution both scale exponentially with magnitude, the gap between the mainshock and the largest aftershock no longer depends on the mainshock.
In forecasting it gives a quick estimate of how strong the largest aftershock may be.
