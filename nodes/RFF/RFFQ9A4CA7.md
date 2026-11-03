---
tag: RFFQ9A4CA7
kind: definition
name: Richter magnitude scale
msc: [86A15]
defines: F8YBKFKFMX
uses: [04DXAFN2ES]
sources:
  - url: https://en.wikipedia.org/wiki/Richter_scale
---

## Definition

Let an earthquake be recorded at epicentral distance $\delta$, within local distances of a few hundred kilometres, by a standard Wood–Anderson torsion seismograph.
Let $A$ be the maximum trace amplitude of the record, in millimetres.
Let $A_0(\delta)$ be the empirical calibration function of distance, fixed so that an earthquake with $A = 1$ mm at $\delta = 100$ km has magnitude $3$.
The *local* or *Richter magnitude* of the earthquake is
$$M_L = \log_{10} A - \log_{10} A_0(\delta).$$

## Remarks

Equivalently, a magnitude $0$ earthquake produces an amplitude of $0.001$ mm at $100$ km.
Example: an earthquake recorded at $100$ km with $A = 10$ mm has $M_L = \log_{10} 10 - \log_{10} 10^{-3} = 1 + 3 = 4$.
Non-example: the peak amplitude of an earthquake $5000$ km away is not covered, since $A_0$ is defined only at local distances; teleseismic events use other scales.
The value of $M_L$ is the average over several stations, each corrected by $A_0$.
For large earthquakes the peak amplitude at the short periods of the instrument grows little with size, so $M_L$ saturates at about $7$.
The logarithm is decimal, $\log_{10} x = \ln x / \ln 10$, with $\ln$ the [[natural logarithm|04DXAFN2ES]].
