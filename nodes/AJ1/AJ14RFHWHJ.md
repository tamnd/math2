---
tag: AJ14RFHWHJ
kind: definition
name: Moment magnitude scale
msc: [86A15]
defines: 8QWGDVEH46
uses: [88YRH7XQDX, 04DXAFN2ES]
sources:
  - url: https://en.wikipedia.org/wiki/Moment_magnitude_scale
---

## Definition

Let an earthquake have [[seismic moment|88YRH7XQDX]] $M_0 > 0$, measured in newton metres.
Its *moment magnitude* is the dimensionless number
$$M_w = \frac23 \big(\log_{10} M_0 - 9.1\big).$$

## Remarks

Equivalently $M_0 = 10^{1.5 M_w + 9.1}$ N·m, so an increase of $M_w$ by $1$ multiplies $M_0$ by $10^{1.5} \approx 31.6$.
An older form, with $M_0$ in dyne centimetres, is $M_w = \frac23 \log_{10} M_0 - 10.7$; since $1$ N·m $= 10^7$ dyn·cm, the two forms differ by about $0.03$.
Example: $M_0 = 3 \times 10^{18}$ N·m gives $\log_{10} M_0 \approx 18.48$ and $M_w \approx \frac23 (18.48 - 9.1) \approx 6.25$.
Non-example: the local magnitude $M_L$ is computed from the peak amplitude on a seismogram, not from $M_0$.
So it is not a moment magnitude, even when the two numbers are close.
The logarithm here is the decimal one, $\log_{10} x = \ln x / \ln 10$, with $\ln$ the [[natural logarithm|04DXAFN2ES]].
