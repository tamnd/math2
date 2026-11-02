---
tag: WKD2S2XA9C
kind: definition
name: Coherent analytic sheaf
msc: [32C35]
defines: DSJET02WPR
uses: [HXSZA44J5J, S33B2H3MYD]
sources:
  - url: https://en.wikipedia.org/wiki/Coherent_sheaf
---

## Definition

Let $(X, \mathcal{O}_X)$ be a [[complex analytic space|HXSZA44J5J]] and let $\mathcal{F}$ be a [[sheaf of $\mathcal{O}_X$-modules|S33B2H3MYD]].
The sheaf $\mathcal{F}$ is of *finite type* if each point of $X$ has an open neighbourhood $U$ with a surjective morphism $\mathcal{O}_U^p \to \mathcal{F}|_U$ for some $p \ge 0$.
The sheaf $\mathcal{F}$ is a *coherent analytic sheaf* if:

1. $\mathcal{F}$ is of finite type;
2. for every open $U \subseteq X$, every integer $q \ge 0$ and every morphism $\varphi \colon \mathcal{O}_U^q \to \mathcal{F}|_U$ of sheaves of modules, the kernel of $\varphi$ is of finite type.

## Remarks

Example: the sheaf $\mathcal{O}_X^p$ is coherent for every complex space $X$; for $X = \C^n$ this is the Oka coherence theorem, and the general case follows from it.
Given it, a sheaf is coherent if and only if it has, locally, a presentation $\mathcal{O}_U^q \to \mathcal{O}_U^p \to \mathcal{F}|_U \to 0$.

Non-example: let $X = \C$, $U = \C \setminus \set{0}$, and let $\mathcal{F}$ be the sheaf of holomorphic functions on $U$ extended by zero to $\C$.
Its stalk at $0$ is $0$ and its stalks at other points are $\mathcal{O}_{\C,x}$.
A section of $\mathcal{F}$ on a connected open set $V \ni 0$ is a holomorphic function on $V \setminus \set{0}$ that vanishes near $0$, so it is zero by the identity theorem.
So no finite set of sections over a neighbourhood of $0$ generates the nonzero stalks near $0$, and clause 1 fails.
