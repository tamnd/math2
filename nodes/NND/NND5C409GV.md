---
tag: NND5C409GV
kind: definition
name: Fermi liquid theory
msc: [82D35, 81V74, 82B10]
defines: FW27X1KB37
uses: [GK3SVTXXKX, 663MJA8NAC, FM6XWC4BST]
sources:
  - url: https://en.wikipedia.org/wiki/Fermi_liquid_theory
---

## Definition

Consider a translation-invariant system of interacting spin-$1/2$ fermions in $\R^3$ at density $n$, in a large volume $\mathcal{V}$, with units where $\hbar = 1$.
The system is a *Landau Fermi liquid* if its low-energy states are described as follows.

1. (Adiabatic continuity) The low-energy excited states are labelled by occupation numbers $n_{p\sigma} \in \set{0, 1}$ of quasiparticles of momentum $p$ and spin $\sigma$. This labelling is as for the free [[Fermi gas|663MJA8NAC]], with the same Fermi momentum $k_F = (3\pi^2 n)^{1/3}$.
2. (Energy functional) Let $\delta n_{p\sigma}$ be small deviations from the ground state. The energy is
$$E = E_0 + \sum_{p,\sigma} \varepsilon_p \, \delta n_{p\sigma} + \frac{1}{2\mathcal{V}} \sum_{p,\sigma,p',\sigma'} f_{p\sigma, p'\sigma'} \, \delta n_{p\sigma} \, \delta n_{p'\sigma'},$$
where near the [[Fermi surface|GK3SVTXXKX]] $\varepsilon_p - \mu \approx v_F(\abs{p} - k_F)$ with Fermi velocity $v_F = k_F / m^*$, which defines the effective mass $m^*$.
3. (Long life) A quasiparticle of energy $\varepsilon$ above the chemical potential $\mu$ has a decay rate of order $(\varepsilon - \mu)^2$, small compared with $\varepsilon - \mu$.

The function $f$ is the Landau interaction function, and its angular averages are the Landau parameters.

## Remarks

Microscopically, the momentum distribution of the particles has a jump of size $Z \in (0, 1]$ at $\abs{p} = k_F$, the quasiparticle residue; for the free gas $Z = 1$.

Example: the free Fermi gas is a Fermi liquid with $f = 0$, $m^* = m$ and infinite lifetime.
In general the low-temperature heat capacity per volume is $C/\mathcal{V} = \tfrac13 m^* k_F k_B^2 T$, the free-gas value with $m$ replaced by $m^*$.

Non-example: interacting fermions in one dimension form a [[Luttinger liquid|AS696NEAGP]] instead.
There the jump of the momentum distribution vanishes, $Z = 0$, and clause 1 fails: the low-energy excitations are collective sound modes, not quasiparticles.
