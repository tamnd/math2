---
tag: JS88E3DQ2P
kind: definition
name: Fell topology
msc: ["22D10", "22D25", "43A40"]
defines: SV5YRK473H
uses: [AHV05ZBCYW, 95Q8WZMN0W, JKANN4VBYH, 74BPYJNZTM, WFFGB4RK60]
sources:
  - url: https://en.wikipedia.org/wiki/Unitary_representation
---

## Definition

Let $G$ be a [[locally compact group|AHV05ZBCYW]] with [[unitary dual|95Q8WZMN0W]] $\widehat{G}$, and let $C^*(G)$ be its [[group C\*-algebra|JKANN4VBYH]].
Each irreducible [[unitary representation|74BPYJNZTM]] $\pi$ of $G$ extends to an irreducible representation of $C^*(G)$, with kernel $\ker \pi \subseteq C^*(G)$ depending only on the class of $\pi$.
For a subset $S \subseteq \widehat{G}$, let
$$\overline{S} = \Bigl\{ \pi \in \widehat{G} : \ker \pi \supseteq \bigcap_{\sigma \in S} \ker \sigma \Bigr\},$$
with $\overline{\emptyset} = \emptyset$.
The *Fell topology* on $\widehat{G}$ is the topology whose closed sets are the sets $S$ with $\overline{S} = S$.

## Remarks

The operation $S \mapsto \overline{S}$ is a closure operator, so this defines a topology; it is the pull-back of the [[Jacobson topology|WFFGB4RK60]] on the primitive ideals of $C^*(G)$.
Fell showed an equivalent form: $\pi \in \overline{S}$ exactly when $\pi$ is weakly contained in $S$.
This means that every function $x \mapsto \ip{\pi(x)\xi}{\xi}$ is a limit, uniformly on compact subsets of $G$, of finite sums of functions $x \mapsto \ip{\sigma(x)\eta}{\eta}$ with $\sigma \in S$.

Example: let $G = \Z$, so $\widehat{G}$ is the set of characters $\chi_\theta(n) = e^{in\theta}$, $\theta \in \R/2\pi\Z$.
If $\theta_k \to \theta$, then $\chi_{\theta_k} \to \chi_\theta$ uniformly on finite sets, so $\chi_\theta$ lies in the closure of $\set{\chi_{\theta_k}}$.
In general, for an abelian group the Fell topology is the compact-open topology of the [[Pontryagin dual|FMW57WNPDB]].

Non-example: in $\widehat{\Z}$, the trivial character $\chi_0$ is not in the closure of $\set{\chi_\pi}$, where $\chi_\pi(n) = (-1)^n$.
The positive-type functions of $\chi_\pi$ and their sums are the functions $c(-1)^n$ with $c \ge 0$.
To approach $\chi_0$ one would need $c \to 1$ at $n = 0$ and $-c \to 1$ at $n = 1$, which is impossible.

For a compact group the Fell topology is discrete.
The Fell topology is $T_1$ for many groups but not always Hausdorff.
