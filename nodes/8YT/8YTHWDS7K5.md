---
tag: 8YTHWDS7K5
kind: definition
name: Lambda-CDM model
msc: ["83F05", "83C56"]
defines: QFXF8R1K8B
uses: [ECJMS4VDTF, J70F32P86W, PPHFS2P4G4, WVKKDY9V61, H4FNPG6ZY1, 6A915X05CK]
sources:
  - url: https://en.wikipedia.org/wiki/Lambda-CDM_model
---

## Definition

Use units with $c = 1$.
The background of the *Lambda-CDM model* is the [[Friedmann–Lemaître–Robertson–Walker metric|ECJMS4VDTF]] with spatial curvature $k = 0$.
Its matter content is the sum of two separately conserved [[perfect fluids|H4FNPG6ZY1]] and a [[cosmological constant|WVKKDY9V61]]:

1. matter (cold dark matter and baryons) with [[equation of state|6A915X05CK]] $w = 0$;
2. radiation (photons and relativistic neutrinos) with $w = 1/3$;
3. a cosmological constant $\Lambda > 0$, equivalent to a fluid with $w = -1$.

Normalize the [[scale factor|J70F32P86W]] by $a(t_0) = 1$ today, and let $H_0$ be the present Hubble parameter.
Then the first [[Friedmann equation|PPHFS2P4G4]] becomes
$$H(a)^2 = H_0^2 \left( \Omega_r a^{-4} + \Omega_m a^{-3} + \Omega_\Lambda \right), \qquad \Omega_r + \Omega_m + \Omega_\Lambda = 1,$$
where $\Omega_m, \Omega_r, \Omega_\Lambda > 0$ are the present density parameters of matter, radiation and $\Lambda$, with $\Omega_\Lambda = \Lambda/(3H_0^2)$.

## Remarks

The full model also prescribes nearly scale-invariant, adiabatic, Gaussian initial perturbations, which are evolved by cosmological perturbation theory.
Example: neglecting radiation, $H^2 = H_0^2(\Omega_m a^{-3} + \Omega_\Lambda)$ has the explicit solution $a(t) = \left( \Omega_m / \Omega_\Lambda \right)^{1/3} \sinh^{2/3}\left( \tfrac{3}{2}\sqrt{\Omega_\Lambda}\, H_0 t \right)$.
At early times this behaves like the Einstein–de Sitter law $a \propto t^{2/3}$, and at late times like the de Sitter law $a \propto e^{\sqrt{\Omega_\Lambda} H_0 t}$.
Non-example: the Einstein–de Sitter universe has $\Omega_\Lambda = 0$, so it fails clause 3.
The deceleration parameter today is $q_0 = \Omega_r + \tfrac{1}{2}\Omega_m - \Omega_\Lambda$, which is negative for the observed values.
