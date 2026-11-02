---
tag: T6Q7NST7JA
kind: definition
name: Topological modular forms
msc: [55N34, 55P43, 11F11]
defines: JN73KE96YB
uses: [XH68V2BP4K, BAW0T68GWK, T78YG90VVT, SJ2BVG9F4W, M8NA9X8BTV]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_modular_forms
---

## Definition

Let $\mathcal{M}_{\mathrm{ell}}$ be the moduli stack of [[elliptic curves|SJ2BVG9F4W]] and $\overline{\mathcal{M}}_{\mathrm{ell}}$ its compactification by generalized elliptic curves.
An $E_\infty$ [[ring spectrum|BAW0T68GWK]] is a ring spectrum with an action of an [[$E_\infty$ operad|T78YG90VVT]].
By the Goerss–Hopkins–Miller theorem there is a sheaf $\mathcal{O}^{\mathrm{top}}$ of $E_\infty$ ring spectra on the étale site of $\overline{\mathcal{M}}_{\mathrm{ell}}$ with the following property.
For each étale map $\operatorname{Spec} R \to \mathcal{M}_{\mathrm{ell}}$, which classifies an elliptic curve $C$ over $R$, the spectrum $\mathcal{O}^{\mathrm{top}}(\operatorname{Spec} R)$ is an [[elliptic cohomology|XH68V2BP4K]] theory for $C$.
From this sheaf one defines three spectra.

1. $\mathrm{Tmf} = \mathcal{O}^{\mathrm{top}}(\overline{\mathcal{M}}_{\mathrm{ell}})$ is the spectrum of global sections.
2. *Topological modular forms* $\mathrm{tmf}$ is the connective cover $\tau_{\ge 0} \mathrm{Tmf}$.
3. Periodic topological modular forms $\mathrm{TMF} = \mathcal{O}^{\mathrm{top}}(\mathcal{M}_{\mathrm{ell}})$ is the spectrum of sections over the open substack of smooth curves.

## Remarks

There is a ring map $\pi_{2k} \mathrm{tmf} \to MF_k$ to the ring of integral [[modular forms|M8NA9X8BTV]] of weight $k$, $MF_* = \Z[c_4, c_6, \Delta]/(c_4^3 - c_6^2 - 1728 \Delta)$.
It becomes an isomorphism after tensoring with $\Q$, so $\pi_* \mathrm{tmf} \otimes \Q \cong \Q[c_4, c_6]$ with $c_4$ in degree $8$ and $c_6$ in degree $12$.
The spectrum $\mathrm{TMF}$ is $576$-periodic: $\Delta^{24}$ lifts to a unit in $\pi_{576} \mathrm{TMF}$.

Example: in degree $8$, $\pi_8 \mathrm{tmf} \otimes \Q \cong \Q$, and the map to modular forms sends a generator to a nonzero multiple of $c_4$, the Eisenstein series of weight $4$; this agrees with $\dim_\Q MF_4 \otimes \Q = 1$.

Non-example: $\pi_* \mathrm{tmf}$ is not the ring $MF_*$ of modular forms.
The group $\pi_3 \mathrm{tmf} \cong \Z/24$ is torsion in odd degree, while $MF_*$ is zero in odd degrees.
