---
tag: 7FCSM3Y3EA
kind: definition
name: Seismic tomography
msc: [86A22, 86A15, 65R32]
defines: JRN1693EHB
uses: [C54MFNX576, 20FVNS391E]
sources:
  - url: https://en.wikipedia.org/wiki/Seismic_tomography
---

## Definition

Let $\Omega$ be a region of the Earth.
Let $m$ be a model of a seismic property on $\Omega$, such as the P-wave or S-wave speed.
Let seismic waves from sources $s_1, \dots, s_J$ be recorded at receivers $r_1, \dots, r_K$.
Let $d$ be the vector of observations derived from the records, such as travel times or waveforms.
Let $G$ be the forward operator that predicts these observations from $m$ by seismic wave theory.
*Seismic tomography* is the [[geophysical inversion|C54MFNX576]] that estimates $m$ on $\Omega$ from $d$ and $G$.
Usually it seeks a perturbation $\delta m$ of a reference model $m_0$, such as a radial Earth model.
It solves the linearised equation $d - G(m_0) \approx DG(m_0)\, \delta m$ by regularised least squares.

## Remarks

Example: travel-time tomography, where $d$ are arrival times and $DG(m_0)$ integrates slowness perturbations along the rays of the reference model.
Non-example: locating earthquakes from arrival times in a fixed velocity model estimates the sources, not the medium, so it is not tomography; joint inversions do both.
The resolution depends on the coverage: a region crossed by few rays, or by rays in only one direction, is poorly resolved and smeared along the ray direction.
Resolution is often tested with synthetic models such as a checkerboard pattern.

## Explanations

### L1 human

Seismic tomography uses many recorded waves to estimate how wave speed varies inside the Earth.
It starts from a simple reference Earth and solves for the corrections that best explain the data.
