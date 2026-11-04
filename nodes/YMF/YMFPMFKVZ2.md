---
kind: concept
name: Convexity of an open set with respect to a class of functions
msc: ["32E05"]
sources:
  - url: https://github.com/jirilebl/scv/blob/78d7d41554695c389552c301398803d4633b9208/scv.tex#L7799
    locator: scv.tex:7799
tag: YMFPMFKVZ2
uses: ["01ZQQDCERP", "0R6EWFKRCF"]
---

## Summary

Let $U \subseteq \mathbb{R}^n$ be an [[open set|01ZQQDCERP]]. Let $\mathcal{F}$ be a class of functions on $U$ with values in the extended reals $\mathbb{R} \cup \{-\infty, \infty\}$.

For a subset $K \subseteq U$, the hull of $K$ with respect to $\mathcal{F}$ is the set $\widehat{K}$ of all points $x \in U$ such that $f(x) \le \sup_{y \in K} f(y)$ for every $f \in \mathcal{F}$.

The set $U$ is convex with respect to $\mathcal{F}$ if the hull $\widehat{K}$ is relatively compact in $U$ for every relatively compact subset $K$ of $U$. Here relatively compact in $U$ means that the closure taken inside $U$ is a [[compact set|0R6EWFKRCF]].

Always $K \subseteq \widehat{K}$. A larger class $\mathcal{F}$ gives smaller hulls, so it is easier for $U$ to be convex with respect to it.
