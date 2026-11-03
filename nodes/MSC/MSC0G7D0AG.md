---
tag: MSC0G7D0AG
kind: definition
name: S-matrix
msc: [81U20, 47A40]
defines: YDC9XBJDE1
uses: [CSHWP5PK4P, HM2HHE3J51, 0NEGN5CRSC, MM0EJ2GDE4]
sources:
  - url: https://en.wikipedia.org/wiki/S-matrix
---

## Definition

Let $H_0$ and $H$ be [[self-adjoint operators|0NEGN5CRSC]] on a complex [[Hilbert space|HM2HHE3J51]] $\mathcal{H}$.
Assume that the wave operators $W_\pm = \operatorname*{s-lim}_{t \to \pm\infty} e^{itH} e^{-itH_0} P_{ac}(H_0)$ of [[scattering theory|CSHWP5PK4P]] exist, where $P_{ac}(H_0)$ is the projection onto the absolutely continuous subspace of $H_0$.
The *S-matrix*, or *scattering operator*, of the pair $(H, H_0)$ is the operator
$$S = W_+^* W_-.$$

## Remarks

The operator $S$ commutes with $H_0$, so it decomposes over the spectrum of $H_0$ into operators $S(E)$ on the energy shells, which are also called the scattering matrix.
If $\operatorname{Ran} W_+ = \operatorname{Ran} W_-$, then $S$ is a [[unitary operator|MM0EJ2GDE4]] on the absolutely continuous subspace of $H_0$; this holds under asymptotic completeness.
Example: if $H = H_0$, then $W_\pm = P_{ac}(H_0)$ and $S = P_{ac}(H_0)$, which is the identity there: no scattering.
Example: let $H = -\Delta + V$ on $L^2(\R^3)$ with $V$ spherically symmetric and short range.
Then $S(E)$ acts on the angular momentum $l$ component as multiplication by $e^{2i\delta_l(k)}$, with $k = \sqrt{E}$ and $\delta_l$ the phase shift.
Non-example: if $\operatorname{Ran} W_- \ne \operatorname{Ran} W_+$, then $S$ is not unitary on the absolutely continuous subspace of $H_0$.
Indeed, $S$ is an isometry there only if $\operatorname{Ran} W_- \subseteq \operatorname{Ran} W_+$, and a co-isometry only if the reverse inclusion holds.
With the opposite sign convention for $W_\pm$, the same operator is written $S = W_-^* W_+$.
