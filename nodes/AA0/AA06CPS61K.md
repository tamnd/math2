---
tag: AA06CPS61K
kind: definition
name: Renormalization
msc: [81T15, 81T17]
defines: 1X0W3AEBEJ
uses: [BS6HVNMTWC, HVGDXMPB29, 033WGN00BF]
sources:
  - url: https://en.wikipedia.org/wiki/Renormalization
---

## Definition

Consider a family of quantum field theories with a regulator $\Lambda$, a cutoff that makes every [[Feynman diagram|BS6HVNMTWC]] finite.
The theory has bare parameters $g_0 = (g_{0,1}, \dots, g_{0,k})$ and a field $\phi_0$, with correlation functions $G_n(x_1, \dots, x_n; g_0, \Lambda)$.
These are [[formal power series|033WGN00BF]] in the bare couplings.
A *renormalization* of the theory is a choice of the following data.

1. Renormalized parameters $g$, and bare parameters $g_0 = g_0(g, \Lambda)$ given as formal power series in $g$.
2. A field strength factor $Z = Z(g, \Lambda)$, also a formal power series, with renormalized field $\phi = Z^{-1/2}\phi_0$.
3. The condition: for every $n$, the renormalized correlation function $Z^{-n/2} G_n(x; g_0(g, \Lambda), \Lambda)$ has a finite limit as $\Lambda \to \infty$, coefficient by coefficient in $g$.

The differences $g_0 - g$ and $Z - 1$ are the counterterms.
The theory is *renormalizable* if this is possible with counterterms of the same form as the terms already in the Lagrangian.

## Remarks

Example: the [[quartic interaction|HVGDXMPB29]] in four dimensions is renormalizable.
Counterterms for the mass, the coupling $\lambda$ and the field strength make all correlation functions finite at every order.
The divergent subdiagrams have at most four external legs, and their divergent parts are polynomials of degree at most $2$ in momenta.

Non-example: the $\phi^6$ interaction in four dimensions is not renormalizable.
Its coupling has negative mass dimension, so diagrams with more and more external legs diverge.
Removing their divergences needs new counterterms such as $\phi^8$ and $\phi^{10}$, without end.

The finite limits are not unique: they depend on a renormalization scheme, such as conditions at a chosen momentum scale.
Different schemes are related by a finite change of the renormalized parameters.
