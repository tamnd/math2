---
tag: VMFWAPNN65
kind: definition
name: Thom–Mather stratified space
msc: [58A35, 57N80, 32S60]
defines: P9R3777ZJF
uses: [F45VQ47GPV, 0MXB4CKHFW, GTMT5ZFV00, 02BH3MCBQB]
sources:
  - url: https://en.wikipedia.org/wiki/Thom%E2%80%93Mather_stratified_space
---

## Definition

Let $V$ be a [[Hausdorff|0MXB4CKHFW]], locally compact topological space with a countable basis of open sets.
A *stratification* of $V$ is a locally finite partition $\mathcal{S}$ of $V$ into locally closed subsets, called strata.
Each stratum must be a [[smooth manifold|F45VQ47GPV]] in the subspace topology.
The frontier condition must hold: if $X, Y \in \mathcal{S}$ and $X \cap \overline{Y} \neq \emptyset$, then $X \subseteq \overline{Y}$.
One writes $X < Y$ when $X \ne Y$ and $X \subseteq \overline{Y}$.
*Control data* for $\mathcal{S}$ consist of three things for each stratum $X$.
They are an [[open|02BH3MCBQB]] neighbourhood $T_X$ of $X$ in $V$, a continuous retraction $\pi_X \colon T_X \to X$, and a continuous function $\rho_X \colon T_X \to [0, \infty)$ with $\rho_X^{-1}(0) = X$.
A *Thom–Mather stratified space* is a triple $(V, \mathcal{S}, \mathcal{J})$, where $\mathcal{J}$ is control data for $\mathcal{S}$, such that:

1. For all strata $X < Y$, the map $(\pi_X, \rho_X) \colon T_X \cap Y \to X \times (0, \infty)$ is a smooth [[submersion|GTMT5ZFV00]].
2. For all strata $X < Y$ and every stratum $Z$, the control conditions $\pi_X(\pi_Y(v)) = \pi_X(v)$ and $\rho_X(\pi_Y(v)) = \rho_X(v)$ hold for all $v \in T_X \cap T_Y \cap Z$ for which both sides are defined.

## Remarks

Example: let $V \subseteq \R^2$ be the union of the two coordinate axes, with strata $X = \set{0}$ and the four open half-axes.
Take $T_X = V$, $\pi_X(v) = 0$, and $\rho_X(v) = \abs{v}^2$.
On each half-axis, $\rho_X$ has non-zero derivative, so $(\pi_X, \rho_X)$ is a submersion onto $X \times (0, \infty)$.
For each half-axis $Y$ take $T_Y = Y$, $\pi_Y = \id_Y$ and $\rho_Y = 0$.
Then the only control conditions to check are $\pi_X(\pi_Y(v)) = 0 = \pi_X(v)$ and $\rho_X(\pi_Y(v)) = \rho_X(v)$ for $v \in Y$, which hold since $\pi_Y(v) = v$.


Non-example: give $V = \R$ the strata $X = \set{0}$ and $Y = \R \setminus \set{0}$, with $T_X = \R$ and $\pi_X = 0$.
Let $\rho_X(v) = \abs{v \sin(1/v)}$ for $v \ne 0$ and $\rho_X(0) = 0$; this function is continuous.
It vanishes at the points $v = 1/(k\pi)$ of $Y$ for every integer $k \ne 0$, so $\rho_X^{-1}(0) \ne X$ and these are not control data.

By a theorem of Mather, every closed subset of a smooth manifold with a Whitney stratification admits control data that make it a Thom–Mather stratified space.
