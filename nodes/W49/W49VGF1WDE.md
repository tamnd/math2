---
tag: W49VGF1WDE
kind: statement
role: theorem
name: Jakobson's theorem
msc: ["37E05", "37C40", "37D25"]
uses: [QN9X9BNKTX, P0P21KDV6E, B232EZ1FMB, 2Z2QVWZ262, NJ1FJSNK6A, Y2DKZH3CCT]
about: [QN9X9BNKTX]
sources:
  - url: https://en.wikipedia.org/wiki/Logistic_map
---

## Statement

For $r \in [0, 4]$ let $f_r(x) = r x (1 - x)$ be the [[logistic map|QN9X9BNKTX]] on $[0, 1]$.
Let $A$ be the set of parameters $r \in [0, 4]$ for which $f_r$ has an [[invariant|B232EZ1FMB]] probability measure that is [[absolutely continuous|P0P21KDV6E]] with respect to [[Lebesgue measure|2Z2QVWZ262]].
Then $A$ has positive Lebesgue measure.
Moreover, $4$ is a one-sided Lebesgue density point of $A$:
$$\lim_{\varepsilon \to 0^+} \frac{\lambda(A \cap [4 - \varepsilon, 4])}{\varepsilon} = 1,$$
where $\lambda$ is Lebesgue measure on $\R$.

## Remarks

Michael Jakobson proved the theorem in 1981.
The proof is a parameter exclusion argument.
Near $r = 4$, one follows the orbit of the critical point $1/2$ and removes the parameters for which this orbit comes too close to $1/2$ too early.
For the remaining parameters the derivative along the critical orbit grows exponentially, and this growth gives the absolutely continuous invariant measure; the removed set is shown to be small.
Benedicks and Carleson later gave another proof of this kind, which they extended to the Hénon maps.

Example: $r = 4$ itself is in $A$: the measure with density $\frac{1}{\pi \sqrt{x (1 - x)}}$ on $(0, 1)$ is invariant for $f_4$.

For parameters in $A$ the measure is ergodic and has a positive [[Lyapunov exponent|NJ1FJSNK6A]], so the dynamics is chaotic in a measurable sense.
This is in contrast with parameters where $f_r$ has an attracting periodic orbit; by [[Singer's theorem|Y2DKZH3CCT]] there is at most one, and then almost every orbit converges to it.
Such parameters form an open and dense subset of $[0, 4]$, but by Jakobson's theorem they do not have full measure.
Lyubich showed in 2002 that almost every parameter $r$ is of one of these two kinds.

## Explanations

### L1 human

In the logistic family, some parameters give a stable cycle and others give chaos.
Stable cycles are robust: a small change of the parameter keeps the cycle, so these parameters form open intervals that are everywhere in the parameter line.
One might expect chaos to be rare then, like a set of measure zero.
Jakobson's theorem says no: chaotic parameters, with a smooth invariant density, fill a set of positive length, and near $r = 4$ almost all parameters are of this kind.

### L2 human

The theorem shows that the chaotic behaviour seen at $r = 4$ persists, in a measure-theoretic sense, for many nearby parameters.
This holds even though the topological picture changes at a dense set of parameters.
It became a model for the study of nonuniformly hyperbolic systems with critical points.
The tool of following the critical orbit and excluding bad parameters was later used for the Hénon family and other strange attractors.
