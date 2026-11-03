---
tag: Z6MZG1FMD5
kind: definition
name: Komar mass
msc: ["83C40", "83C57"]
defines: 7V112F6KVB
uses: [D1SYF8F8RQ, PT9FSNP9T5, 45VSJ0RG2S, REDZ92MKXX]
sources:
  - url: https://en.wikipedia.org/wiki/Komar_mass
---

## Definition

Let $(M, g)$ be an oriented 4-dimensional [[Lorentzian manifold|D1SYF8F8RQ]] of signature $(-,+,+,+)$ with volume form $\epsilon_{abcd}$.
Let $\xi$ be a [[Killing vector field|PT9FSNP9T5]] that is timelike near infinity and normalised by $g(\xi, \xi) \to -1$ at infinity.
Let $S$ be a closed spacelike 2-surface in $M$.
In units with $G = 1$, the *Komar mass* of $S$ is
$$M_K(S) = -\frac{1}{8\pi} \int_S \epsilon_{abcd} \nabla^c \xi^d,$$
where $S$ is oriented as the boundary of a spacelike region that it encloses.
In the notation of forms, $M_K(S) = -\frac{1}{8\pi} \int_S \star d\xi^\flat$ up to the factor fixed by the convention for the [[Hodge star|45VSJ0RG2S]].

## Remarks

Assume that $S$ bounds a spacelike hypersurface $\Sigma$ with future unit normal $n$, and that the Einstein equations hold.
Then Stokes' theorem gives
$$M_K(S) = 2 \int_\Sigma \Bigl( T_{ab} - \tfrac12 T g_{ab} \Bigr) n^a \xi^b \, dV,$$
where $T_{ab}$ is the [[stress–energy tensor|REDZ92MKXX]] and $T$ its trace.
Hence $M_K(S)$ depends only on the matter enclosed, and it is the same for all surfaces $S$ that are homologous in a vacuum region.
Example: for the Schwarzschild metric with $\xi = \partial_t$, one has $\xi^\flat = -(1 - 2M/r) \, dt$ and $d\xi^\flat = (2M/r^2) \, dt \wedge dr$.
Integrating its dual over the sphere of radius $r$, of area $4\pi r^2$, gives $\pm 8\pi M$, and with the orientation above $M_K = M$.
Non-example: if $\xi$ is not a Killing field, the integral generally depends on the surface $S$, so it does not define a mass.

## Explanations

### L1 human

The Komar mass is a Gauss law for gravity in a stationary spacetime: a flux integral of the time-translation symmetry over a closed surface.
