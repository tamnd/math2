---
kind: concept
msc:
- 32A10
name: Holomorphic function of several variables (locally bounded, separately holomorphic form)
sources:
- url: https://github.com/jirilebl/scv/blob/78d7d41554695c389552c301398803d4633b9208/scv.tex#L1337
  locator: scv.tex:1337
tag: WKBASXP6HE
uses:
- 02BH3MCBQB
- 0NAHXR1FRH
---

## Summary

Let $U$ be an [[open set|02BH3MCBQB]] in $\C^n$. A function $f \colon U \to \C$ is holomorphic when two conditions hold.

First, $f$ is locally bounded. Every point of $U$ has a neighbourhood on which $f$ is bounded. Equivalently, $f$ is bounded on each compact subset of $U$.

Second, $f$ is holomorphic in each variable separately. If all other coordinates are fixed, the complex derivative in the $k$-th coordinate exists at every point of $U$, for each $k$ from $1$ to $n$. This is the notion of a [[holomorphic function|0NAHXR1FRH]] of one variable, applied one coordinate at a time.

The local bound is a convenience. By [[Hartogs's theorem on separate holomorphicity|ECJG25SAJR]] it can be dropped without changing the class of functions. With the bound, the definition agrees with the usual one by [[Osgood's lemma|NBFNXA2WFM]].

In the source, the plain words "differentiable" and "derivative" mean real differentiability. Complex differentiability is always named as such.
