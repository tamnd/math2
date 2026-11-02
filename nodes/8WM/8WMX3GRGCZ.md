---
tag: 8WMX3GRGCZ
kind: example
name: Computed tomography as an inverse problem
msc: [44A12, 92C55, 65R32]
instance_of: [PCMW7KN5P4]
uses: [VJNZJ352PC, HN93ST5CBT]
sources:
  - url: https://en.wikipedia.org/wiki/Tomography
---

## Example

Let $\mu \colon \R^2 \to [0, \infty)$ be the X-ray attenuation coefficient of a slice of a body, a function with compact support.
An X-ray beam that crosses the slice along a [[line|0MP9BCF6DP]] $L$ enters with intensity $I_0$ and leaves with intensity $I$.
By the Beer–Lambert law of absorption, $I = I_0 \exp\left(-\int_L \mu \, ds\right)$, where $ds$ is arc length on $L$.
So each measurement gives the number
$$-\log \frac{I}{I_0} = \int_L \mu \, ds = (R\mu)(L),$$
the value of the [[Radon transform|VJNZJ352PC]] $R\mu$ at the line $L$.
A scanner measures $R\mu(L)$ for many lines $L$, and the task is to recover $\mu$ from these values.

This is an [[inverse problem|PCMW7KN5P4]]: the forward map $\mu \mapsto R\mu$ is known and linear, and one must invert it from data.
When $R\mu(L)$ is known for all lines, $\mu$ is determined, and the [[Radon inversion formula|HN93ST5CBT]] reconstructs it.
The inversion is unstable, because it involves a derivative, a "ramp filter" $\abs{\omega}$ in the Fourier variable.
So small errors at high frequencies in the data become large errors in $\mu$.
With data from only a limited range of directions the instability is much worse.

## Explanations

### L1 human

A CT scanner cannot look inside the body directly.
It only measures how much each X-ray beam is weakened, and that number is the total density along the beam.
From thousands of such totals along lines in many directions, a computer rebuilds the density at each point.
This "rebuild the cause from its effects" is a typical inverse problem.
Noise in the measurements is the main enemy, so practical reconstruction methods filter the data before they invert it.
