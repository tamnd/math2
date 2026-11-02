---
tag: FHKGR7MD1A
kind: definition
name: Harish-Chandra character
msc: ["22E46", "22E45", "22E50"]
defines: F2E3317P78
uses: [SZV8Y806Y7, 42ZCE14AD2, VY0HXD3GC4, Z2CP530WDE, RMWMYBY8TC, 0V33BNKZ9S]
sources:
  - url: https://en.wikipedia.org/wiki/Harish-Chandra_character
---

## Definition

Let $G$ be a [[real reductive Lie group|42ZCE14AD2]] with a [[Haar measure|VY0HXD3GC4]] $dg$.
Let $\pi$ be an [[admissible representation|SZV8Y806Y7]] of $G$ of finite length on a Hilbert space $H$.
For a [[smooth function|0V33BNKZ9S]] $f \colon G \to \C$ with compact support, let
$$\pi(f) = \int_G f(g) \, \pi(g) \, dg,$$
a bounded operator on $H$.
Harish-Chandra proved that each $\pi(f)$ is a [[trace class operator|Z2CP530WDE]].
The *Harish-Chandra character* of $\pi$ is the distribution
$$\Theta_\pi(f) = \operatorname{tr} \pi(f), \qquad f \in C_c^\infty(G).$$

## Remarks

Example: if $\dim H < \infty$, then $\operatorname{tr} \pi(f) = \int_G f(g) \operatorname{tr} \pi(g) \, dg$ by linearity of the trace.
So $\Theta_\pi$ is the distribution given by the ordinary [[character|RMWMYBY8TC]] $g \mapsto \operatorname{tr} \pi(g)$.

Non-example: for $\dim H = \infty$, the operator $\pi(e) = \id_H$ is not trace class.
So the naive rule $g \mapsto \operatorname{tr} \pi(g)$ does not define a function, and the smearing by $f$ is necessary.

The character $\Theta_\pi$ is invariant under conjugation: $\Theta_\pi(f^x) = \Theta_\pi(f)$ for $f^x(g) = f(x g x^{-1})$.
Two irreducible admissible representations have the same character if and only if they are infinitesimally equivalent.
By [[Harish-Chandra's regularity theorem|M9X7Y3GZZD]], $\Theta_\pi$ is given by a locally integrable function.
The same definition works for $G(F)$ with $F$ a non-archimedean local field, with $f$ locally constant of compact support.
