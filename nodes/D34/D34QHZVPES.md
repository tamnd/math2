---
tag: D34QHZVPES
kind: statement
role: theorem
name: Adams–Novikov spectral sequence
msc: [55T15, 55N22, 55Q45]
uses: [5CZHFNY9F3, 1GHF4EKBXS, 4P7GBWJ4RR, DD4D0EKX74, 14CGGHA85T, S8S72AA9C8]
about: [5CZHFNY9F3]
sources:
  - url: https://en.wikipedia.org/wiki/Adams_spectral_sequence
---

## Statement

Let $MU$ be the [[complex cobordism|5CZHFNY9F3]] spectrum, with coefficient ring $MU_* = \pi_* MU$ and $MU_* MU = \pi_*(MU \wedge MU)$.
Then $(MU_*, MU_* MU)$ is a Hopf algebroid, and for every [[spectrum|1GHF4EKBXS]] $X$ the group $MU_* X$ is a comodule over it.
Let $X$ be a connective spectrum.
Then there is a spectral sequence $(E_r^{s,t}, d_r)_{r \ge 2}$.
Its differentials are $d_r \colon E_r^{s,t} \to E_r^{s+r, t+r-1}$, and its second page is
$$E_2^{s,t} = \operatorname{Ext}^{s,t}_{MU_* MU}(MU_*, MU_* X),$$
the [[Ext groups|4P7GBWJ4RR]] in the category of $MU_* MU$-comodules, and the spectral sequence converges to $\pi_{t-s}(X)$.

## Remarks

The construction is the same as for the [[Adams spectral sequence|DD4D0EKX74]], with the mod $p$ Eilenberg–MacLane spectrum replaced by $MU$.
Since $\pi_0 MU = \Z$ and $X$ is connective, the $MU$-based tower recovers $X$ itself, which gives convergence to $\pi_*(X)$ with no completion.
After localizing at a prime $p$, one may replace $MU$ by the [[Brown–Peterson spectrum|S8S72AA9C8]] $BP$, with $E_2^{s,t} = \operatorname{Ext}^{s,t}_{BP_* BP}(BP_*, BP_* X)$, which is smaller and easier to compute.

Example: for $X = S$, the [[sphere spectrum|14CGGHA85T]], the groups $MU_*$ and $MU_* MU$ are concentrated in even degrees, so $E_2^{s,t} = 0$ for odd $t$.
Also $E_2^{0,t}$ is $\Z$ for $t = 0$ and $0$ otherwise.

## Explanations

### L1 human

The Adams–Novikov spectral sequence is a machine for computing stable homotopy groups, like the Adams spectral sequence.
It replaces ordinary mod $p$ cohomology by complex cobordism, a richer cohomology theory built from complex manifolds.
The starting page is harder to compute, but far fewer corrections are needed afterwards.

### L2 human

Through Quillen's theorem, $MU_* MU$-comodules are related to formal group laws, so the $E_2$ term is a cohomology of the moduli of formal groups.
This links the stable homotopy groups of spheres to the height filtration of formal groups and to chromatic homotopy theory.
At odd primes the first differential in the $BP$ version that can be nonzero is $d_{2p-1}$, because the $E_2$ term is concentrated in internal degrees divisible by $2(p-1)$.
