---
tag: TFYJQJERA4
kind: definition
name: Chemical reaction network theory
msc: ["92E20", 80A30, 37N25]
defines: KCGE92DJ1W
uses: [0KFYGSHHF5, 00YC1D652K, 03GSZ8RTZJ, 0JG9W3KA6B, 0NT64JV96A]
sources:
  - url: https://en.wikipedia.org/wiki/Chemical_reaction_network_theory
---

## Definition

Let $\mathcal{S} = \set{X_1, \dots, X_m}$ be a finite set of *species*.
A *chemical reaction network* is a pair $(\mathcal{C}, \mathcal{R})$ with the following properties.

1. The set of *complexes* $\mathcal{C}$ is a finite subset of $\Z_{\ge 0}^m$; the complex $y$ stands for $y_1 X_1 + \cdots + y_m X_m$.
2. The set of *reactions* $\mathcal{R}$ is a subset of $\set{(y, y') \in \mathcal{C} \times \mathcal{C} : y \ne y'}$, and a reaction $(y, y')$ is written $y \to y'$.
3. Each complex is the source or the target of at least one reaction.

So $(\mathcal{C}, \mathcal{R})$ is a [[directed graph|0KFYGSHHF5]], the *reaction graph*.
Its main invariants are these.

1. The *stoichiometric subspace* is the [[linear subspace|00YC1D652K]] $S = \operatorname{span}\set{y' - y : y \to y' \in \mathcal{R}}$ of $\R^m$, and $s = \dim S$ is its [[dimension|03GSZ8RTZJ]].
2. The *linkage classes* are the [[connected components|0JG9W3KA6B]] of the reaction graph with directions ignored, and $\ell$ is their number.
3. The network is *weakly reversible* if each linkage class is strongly connected: for each reaction $y \to y'$ there is a directed path from $y'$ to $y$.
4. The *deficiency* is $\delta = n - \ell - s$, where $n = \abs{\mathcal{C}}$.

A *mass-action system* is a network together with *rate constants* $k_{y \to y'} > 0$, one for each reaction.
Its equation is the [[ordinary differential equation|0NT64JV96A]]
$$\frac{dx}{dt} = \sum_{y \to y' \in \mathcal{R}} k_{y \to y'}\, x^{y} (y' - y), \qquad x \in \R_{\ge 0}^m,$$
where $x^y = x_1^{y_1} \cdots x_m^{y_m}$, with $0^0 = 1$.
For $x_0 \in \R_{>0}^m$, the *positive stoichiometric compatibility class* of $x_0$ is $(x_0 + S) \cap \R_{>0}^m$.

## Remarks

Example: the network $X_1 \rightleftharpoons 2X_2$ has complexes $(1,0)$ and $(0,2)$, so $n = 2$.
It has one linkage class, $\ell = 1$, and $S$ is spanned by $(-1, 2)$, so $s = 1$ and $\delta = 2 - 1 - 1 = 0$.
It is weakly reversible, and its equation is $\dot x_1 = -k_1 x_1 + k_2 x_2^2$, $\dot x_2 = 2k_1 x_1 - 2k_2 x_2^2$.
Non-example of weak reversibility: in $X_1 \to X_2$ there is no path from $X_2$ back to $X_1$.
The deficiency is always $\ge 0$, since it is the dimension of a subspace of the kernel of a linear map.
Every solution that starts in $\R_{\ge 0}^m$ stays in $\R_{\ge 0}^m$ and in its class $x_0 + S$, since $\dot x$ always lies in $S$.
