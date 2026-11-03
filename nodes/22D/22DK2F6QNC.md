---
tag: 22DK2F6QNC
kind: definition
name: Strouhal number
msc: [76M55, 76D25]
defines: B7PKESV4CV
uses: [T3R5FWV91P]
sources:
  - url: https://en.wikipedia.org/wiki/Strouhal_number
---

## Definition

Consider an unsteady flow with a characteristic frequency $f$, a characteristic length $L$ and a characteristic speed $U$.
The *Strouhal number* is
$$\mathrm{St} = \frac{f L}{U}.$$
For vortex shedding behind a body, $f$ is the shedding frequency and $L$ is the width of the body.
The speed $U$ is that of the oncoming flow.

## Remarks

It is a [[dimensionless number|T3R5FWV91P]]: $[f L] = \mathsf{T}^{-1} \mathsf{L} = [U]$.
Example: a cylinder of diameter $L = 0.1\ \mathrm{m}$ in a flow at $U = 1\ \mathrm{m/s}$ that sheds vortices at $f = 2\ \mathrm{Hz}$ has $\mathrm{St} = 0.2$.
Non-example: $f / U$ is not a Strouhal number; it has dimension $\mathsf{L}^{-1}$.
When the equations of motion are made dimensionless with a time scale $1/f$, the Strouhal number multiplies the time-derivative term.
