---
tag: NZ8WECT409
kind: definition
name: Friedrichs extension
msc: [47B25, 47A20, 47A07]
defines: GTBXZXK146
uses: [HM2HHE3J51, BCJHNHKQFG, H971WGMV6C, 054YEQ0Y8M, 0NEGN5CRSC]
sources:
  - url: https://en.wikipedia.org/wiki/Friedrichs_extension
---

## Definition

Let $H$ be a complex [[Hilbert space|HM2HHE3J51]] with inner product $\ip{\cdot}{\cdot}$.
Let $T$ be a [[densely defined|BCJHNHKQFG]] [[symmetric operator|H971WGMV6C]] on $H$ with domain $D(T)$.
Assume that $T$ is bounded below: there is a real number $c$ with $\ip{Tx}{x} \ge c \norm{x}^2$ for all $x \in D(T)$.
On $D(T)$, put
$$\ip{x}{y}_T = \ip{Tx}{y} + (1 - c)\ip{x}{y}.$$
This is an inner product on $D(T)$, and its norm satisfies $\norm{x}_T \ge \norm{x}$.
Let $H_T$ be the completion of $D(T)$ for $\norm{\cdot}_T$.
The inclusion of $D(T)$ into $H$ extends to an injective map from $H_T$ into $H$, so $H_T$ is a subspace of $H$.
The *Friedrichs extension* of $T$ is the operator $T_F$ with domain
$$D(T_F) = \set{x \in H_T : \text{there is } z \in H \text{ with } \ip{x}{y}_T = \ip{z + (1 - c)x}{y} \text{ for all } y \in H_T},$$
given by $T_F x = z$.

## Remarks

The operator $T_F$ is a [[self-adjoint|0NEGN5CRSC]] extension of $T$, and $\ip{T_F x}{x} \ge c \norm{x}^2$ for all $x \in D(T_F)$.
An equivalent description is that $T_F$ is the restriction of the [[adjoint|86B7HF79PQ]] $T^*$ to $D(T^*) \cap H_T$.
The space $H_T$ is the form domain of $T_F$, and the [[sesquilinear form|054YEQ0Y8M]] $(x, y) \mapsto \ip{Tx}{y}$ extends to it.

Example: on $H = L^2(0, 1)$, let $T f = -f''$ on smooth functions with compact support in $(0, 1)$.
Integration by parts gives $\ip{Tf}{f} = \int_0^1 \abs{f'}^2 \, dx \ge 0$, so $c = 0$ works.
The space $H_T$ is the Sobolev space $H^1_0(0, 1)$, and $T_F f = -f''$ on $D(T_F) = H^2(0, 1) \cap H^1_0(0, 1)$, the Dirichlet Laplacian.

Non-example: on $L^2(0, \infty)$, let $S f = -i f'$ on smooth functions with compact support in $(0, \infty)$.
It is symmetric, but $\ip{Sf}{f}$ is not bounded below by any $c \norm{f}^2$, so the construction does not apply.
In fact the [[deficiency indices|G4GMSNAX8X]] of $S$ are unequal, so $S$ has no self-adjoint extension at all.
