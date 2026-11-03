---
tag: W767YTWAJE
kind: definition
name: Distance measures in cosmology
msc: ["83F05"]
defines: YDWH956TJA
uses: [ECJMS4VDTF, J70F32P86W, 8K69WPX4GS, PPHFS2P4G4]
sources:
  - url: https://en.wikipedia.org/wiki/Distance_measure
---

## Definition

Let $g = -dt^2 + a(t)^2 \left( d\chi^2 + S_k(\chi)^2 \, d\Omega^2 \right)$ be a [[Friedmann–Lemaître–Robertson–Walker metric|ECJMS4VDTF]] in units with $c = 1$.
Here $a$ is the [[scale factor|J70F32P86W]], normalized by $a(t_0) = 1$ at the time $t_0$ of observation.
The form $d\Omega^2$ is the round metric on the unit sphere.
The function $S_k(\chi)$ is $\sin(\sqrt{k}\chi)/\sqrt{k}$, $\chi$ or $\sinh(\sqrt{-k}\chi)/\sqrt{-k}$ according as $k > 0$, $k = 0$ or $k < 0$.
Let a comoving source emit light at time $t_e < t_0$ that reaches a comoving observer at $\chi = 0$ at time $t_0$.
Let $z$ be its [[cosmological redshift|8K69WPX4GS]].

1. The *comoving distance* is $D_C = \int_{t_e}^{t_0} \frac{dt}{a(t)}$, which is the comoving coordinate $\chi$ of the source.
2. The *transverse comoving distance* is $D_M = S_k(D_C)$.
3. The *angular diameter distance* is $D_A = D_M / (1 + z)$.
4. The *luminosity distance* is $D_L = (1 + z)\, D_M$.

## Remarks

When the Hubble parameter is known as a function of redshift, $D_C = \int_0^z \frac{dz'}{H(z')}$, with $H(z)$ given by the [[Friedmann equations|PPHFS2P4G4]].
An object of proper size $\ell$ at the source, perpendicular to the line of sight, subtends the small angle $\ell / D_A$; a source of power $L$ gives the observed flux $L / (4\pi D_L^2)$.
These two facts are the reasons for the definitions of $D_A$ and $D_L$, and together they give the reciprocity relation $D_L = (1 + z)^2 D_A$.
Example: in the Einstein–de Sitter model, $k = 0$ and $H(z) = H_0 (1 + z)^{3/2}$, so $D_M = D_C = \frac{2}{H_0}\left( 1 - (1 + z)^{-1/2} \right)$.
At small $z$ all four distances agree to first order with $z / H_0$.
The angular diameter distance is not monotone in $z$ in general: in the Einstein–de Sitter model it is largest at $z = 5/4$.
