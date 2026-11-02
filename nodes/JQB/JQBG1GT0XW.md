---
tag: JQBG1GT0XW
kind: definition
name: Machine epsilon
msc: [65G50, 65Y04]
defines: JA3QXVF2B8
uses: [RTKRSC3KPH]
sources:
  - url: https://en.wikipedia.org/wiki/Machine_epsilon
---

## Definition

Consider a [[floating-point|RTKRSC3KPH]] system with base $\beta$ and precision $p$.
The *machine epsilon* is
$$\varepsilon_{\mathrm{mach}} = \beta^{1-p},$$
the distance from $1$ to the next larger floating-point number.
The *unit roundoff* of the system with rounding to nearest is
$$u = \tfrac12 \beta^{1-p}.$$
Some authors call $u$ the machine epsilon instead.

## Remarks

Example: in IEEE binary64, $\beta = 2$ and $p = 53$, so $\varepsilon_{\mathrm{mach}} = 2^{-52} \approx 2.22 \times 10^{-16}$ and $u = 2^{-53} \approx 1.11 \times 10^{-16}$.
Check: the floating-point numbers in $[1, 2)$ are $1 + k \, 2^{-52}$ for $k = 0, 1, \ldots, 2^{52} - 1$, so the successor of $1$ is $1 + 2^{-52}$.
Non-example: the smallest positive floating-point number, about $4.9 \times 10^{-324}$ in binary64, is not the machine epsilon; it measures the range, not the relative precision.
If $x$ lies in the range of normalized numbers and $\mathrm{fl}(x)$ is the nearest floating-point number, then $\mathrm{fl}(x) = x(1 + \delta)$ with $\abs{\delta} \le u$.
