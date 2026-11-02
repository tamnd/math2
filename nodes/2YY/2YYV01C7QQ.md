---
tag: 2YYV01C7QQ
kind: concept
name: Mean curvature flow
msc: ["53E10", 35K55]
sources:
  - url: https://en.wikipedia.org/wiki/Mean_curvature_flow
same_as:
  wikidata: Q6803617
  wikipedia: Mean curvature flow
---

## Summary

Mean curvature flow is the evolution of a hypersurface in which each point moves with velocity equal to the mean curvature vector.
It is the gradient flow of the area, so it decreases area as fast as possible.
The equation for the moving surface is a nonlinear, weakly parabolic system.
It plays for surfaces the role that the [[heat equation|VP2HN86VAG]] plays for functions.
It is a close relative of the [[inverse mean curvature flow|5XVEF5DKAG]] and of the [[Ricci flow|CR14D9YQTY]].

## Explanations

### L1 human

Imagine a soap film or a closed curve that tries to shorten itself.
Each point moves toward the inside of the bend, faster where the surface is more bent, as measured by its [[mean curvature|PA78NFEPCF]].
A round sphere of radius $R_0$ in $\R^{n+1}$ stays round and its radius shrinks as $\sqrt{R_0^2 - 2nt}$.
For curves in the plane the flow is called curve shortening flow, and every embedded closed curve becomes round before it shrinks to a point.
