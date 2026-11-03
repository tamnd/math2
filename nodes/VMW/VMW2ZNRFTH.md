---
tag: VMW2ZNRFTH
kind: definition
name: Reptation
msc: [82D60, 82C70]
defines: V0MDX6K1TN
uses: [M5WZKH7ZDV, 9HDQ094ADQ]
sources:
  - url: https://en.wikipedia.org/wiki/Reptation
---

## Definition

Consider a linear polymer chain of $N$ segments in a dense entangled system, such as a melt of long chains.
The *reptation model* describes its motion by the following assumptions.

1. The other chains confine the chain to a tube that follows its contour.
The centre line of the tube is an [[ideal chain|M5WZKH7ZDV]] of contour length $L$ proportional to $N$.
2. The chain moves only along the tube, as a one-dimensional [[diffusion|9HDQ094ADQ]] with curvilinear diffusion coefficient $D_c = D_1 / N$, where $D_1$ is a constant independent of $N$.
3. The ends of the chain explore new directions at random, so the part of the tube that the chain has left is forgotten.

The *reptation time*, or disengagement time, is the time $\tau_d$ that the chain needs to leave its initial tube completely.
Up to a constant factor it is $\tau_d \approx L^2 / D_c$.

## Remarks

From clauses 1 and 2, $\tau_d \propto N^2 \cdot N = N^3$.
In time $\tau_d$ the centre of mass moves by about the coil size $R$, and $R^2 \propto N$ by clause 1, so the self-diffusion coefficient scales as $D \approx R^2 / \tau_d \propto N / N^3 = N^{-2}$.
Example: in a polymer melt above the entanglement length, measured self-diffusion coefficients scale close to $N^{-2}$, as the model predicts.
Non-example: short unentangled chains do not move in a tube, so clause 1 fails; their dynamics is described instead by the Rouse model, with $D \propto N^{-1}$.
The model predicts a melt viscosity proportional to $N^3$, while experiments give an exponent close to $3.4$; tube length fluctuations and constraint release account for most of the difference.

## Explanations

### L1 human

The model replaces all the other chains by a tube around the chain.
Inside the tube the chain does an ordinary random walk back and forth along its length.
The scaling laws follow by counting how far the chain must go and how fast it diffuses.
