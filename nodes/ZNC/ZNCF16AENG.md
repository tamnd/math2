---
tag: ZNCF16AENG
kind: statement
role: theorem
name: Grauert's direct image theorem
msc: [32C35, 32H35]
uses: [HXSZA44J5J, DSJET02WPR, 15XEBGNGHC, PQ6Q143ARJ, MPNGD4V271, FE83QQS17S, VA2JEWWB61]
about: [DSJET02WPR, 15XEBGNGHC]
sources:
  - url: https://en.wikipedia.org/wiki/Coherent_sheaf
---

## Statement

Let $X$ and $Y$ be [[complex analytic spaces|HXSZA44J5J]], let $f \colon X \to Y$ be a [[proper|15XEBGNGHC]] holomorphic map and let $\mathcal{F}$ be a [[coherent analytic sheaf|DSJET02WPR]] on $X$.
For an integer $q \ge 0$, let $R^q f_* \mathcal{F}$ be the sheaf on $Y$ associated with the presheaf $V \mapsto H^q(f^{-1}(V), \mathcal{F})$ of [[sheaf cohomology|PQ6Q143ARJ]] groups.
Then $R^q f_* \mathcal{F}$ is a coherent analytic sheaf on $Y$ for every $q \ge 0$.

## Remarks

When $Y$ is a single point, $R^q f_* \mathcal{F}$ is the vector space $H^q(X, \mathcal{F})$ and $X$ is compact, so the theorem contains the [[Cartan–Serre finiteness theorem|MPNGD4V271]].
The case where $f$ is finite and $q = 0$ is easier and is proved with the [[Weierstrass division theorem|FE83QQS17S]].
The general case is much harder.
Grauert's original proof was long; a later proof by Kiehl and Verdier uses Čech cochains of Stein coverings and compact operators between Fréchet modules.

Example: if $A \subseteq X$ is an analytic subset with its reduced structure, then $f_* \mathcal{O}_A$ is coherent on $Y$, and its support is $f(A)$.
Since supports of coherent sheaves are analytic, this gives [[Remmert's proper mapping theorem|VA2JEWWB61]].

Properness is necessary.
Consider the inclusion $f \colon \C \setminus \set{0} \to \C$.
The stalk of $f_* \mathcal{O}$ at $0$ is the ring of holomorphic functions on punctured discs around $0$, modulo agreement near $0$.
It is not finitely generated over $\mathcal{O}_{\C,0}$.
Indeed it is nonzero and multiplication by $z$ is bijective on it, so Nakayama's lemma rules out finite generation.

## Explanations

### L1 human

Given a proper holomorphic map, one can push a coherent sheaf forward along it and take the cohomology along the fibres.
The theorem says that the result is again a coherent sheaf on the target.
So finiteness survives when one looks at a whole family of compact spaces at once, not only at one compact space.

### L2 human

The theorem is the basic finiteness result of relative complex analytic geometry.
It is used to study families of compact complex spaces, for example to prove semicontinuity of the dimensions of cohomology groups of fibres.
It is the analytic analogue of the coherence of higher direct images of coherent sheaves under proper morphisms of schemes.
