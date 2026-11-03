---
tag: CTZC8VE91H
kind: definition
name: Bauschinger effect
msc: [74C05]
defines: H5DB86NRGS
uses: [K8BBMTN0KV, CWWCEXZ8BH, XD47SRCJJF]
sources:
  - url: https://en.wikipedia.org/wiki/Bauschinger_effect
---

## Definition

Consider a uniaxial test of a material with initial yield stress $\sigma_y > 0$, the same in tension and compression.
Load it in tension past yield, up to a flow stress $\sigma_f > \sigma_y$, then unload and load in compression.
Let $\sigma_r > 0$ be the size of the compressive stress at which plastic flow starts again.
The material shows the *Bauschinger effect* if $\sigma_r < \sigma_f$.
So prior plastic flow in one direction lowers the reverse yield stress below the current flow stress.

## Remarks

Example: one-dimensional linear kinematic hardening has the yield condition $\abs{\sigma - \alpha} \le \sigma_y$ with back stress $\alpha = H \varepsilon^p$ for a constant $H > 0$.
After loading to $\sigma_f = \sigma_y + \alpha$, reverse yield starts at $\sigma = \alpha - \sigma_y = \sigma_f - 2\sigma_y$.
Its size $\abs{\sigma_f - 2\sigma_y}$ is less than $\sigma_f$ because $\sigma_f > \sigma_y$, and when $\sigma_f > 2\sigma_y$ reverse yielding even starts while the stress is still tensile.
Non-example: linear isotropic hardening has the yield condition $\abs{\sigma} \le \sigma_y + H \varepsilon^p_{\mathrm{acc}}$, where $\varepsilon^p_{\mathrm{acc}}$ is the accumulated plastic strain.
Its elastic range grows symmetrically, so reverse yield starts at $\sigma_r = \sigma_f$ and there is no Bauschinger effect.
In several dimensions kinematic hardening uses a yield function $f(\sigma - \alpha) \le 0$ with a back stress tensor $\alpha$, so that the [[yield surface|CWWCEXZ8BH]] translates in stress space.
