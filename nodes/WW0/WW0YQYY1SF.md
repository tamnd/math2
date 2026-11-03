---
tag: WW0YQYY1SF
kind: definition
name: Scattering theory
msc: [81U99, 47A40, 35P25]
defines: CSHWP5PK4P
uses: [HM2HHE3J51, 0NEGN5CRSC, MM0EJ2GDE4, VXDEQB46GV]
sources:
  - url: https://en.wikipedia.org/wiki/Scattering
---

## Definition

Let $\mathcal{H}$ be a complex [[Hilbert space|HM2HHE3J51]], and let $H_0$ and $H$ be [[self-adjoint operators|0NEGN5CRSC]] on $\mathcal{H}$, the free and the full [[Hamiltonian|VXDEQB46GV]].
Let $P_{ac}(H_0)$ be the orthogonal projection onto the absolutely continuous subspace of $H_0$.
The *wave operators* of the pair $(H, H_0)$ are the strong limits
$$W_\pm = \operatorname*{s-lim}_{t \to \pm\infty} e^{itH} e^{-itH_0} P_{ac}(H_0),$$
when they exist.
*Scattering theory* is the study of these limits and of the following properties.

1. Existence: both limits $W_+$ and $W_-$ exist.
2. Asymptotic completeness: the ranges of $W_+$ and $W_-$ are both equal to the absolutely continuous subspace of $H$.
3. Scattering operator: when $W_\pm$ exist, $S = W_+^* W_-$ maps the free state that describes the system as $t \to -\infty$ to the free state that describes it as $t \to +\infty$.

## Remarks

When they exist, $W_\pm$ are partial isometries from the absolutely continuous subspace of $H_0$ onto their ranges, and they satisfy $e^{isH} W_\pm = W_\pm e^{isH_0}$ for all $s \in \R$.
Some authors use the opposite sign convention, with $W_\pm$ defined by the limit $t \to \mp\infty$.
Example: $\mathcal{H} = L^2(\R^3)$, $H_0 = -\Delta$ and $H = -\Delta + V$ with $V$ real and $\abs{V(x)} \le C(1 + \abs{x})^{-1-\varepsilon}$ for some $C, \varepsilon > 0$; then the wave operators exist and are asymptotically complete.
Non-example: for the Coulomb potential $V(x) = c/\abs{x}$ with $c \ne 0$, the limits in clause 1 do not exist.
One needs modified wave operators, introduced by Dollard, which correct the free dynamics by a logarithmic phase.
The [[unitary|MM0EJ2GDE4]] groups $e^{-itH}$ and $e^{-itH_0}$ are the solutions of the time-dependent Schrödinger equations of $H$ and $H_0$.
