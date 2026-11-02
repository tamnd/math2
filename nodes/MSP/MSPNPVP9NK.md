---
tag: MSPNPVP9NK
kind: statement
role: theorem
name: Compactness of families of harmonic functions
msc: [31B05]
uses: [0DEB0JMN0W, N76R7JWMNJ, 0381S8Z5P0, 0MW2WXTHMC, CQ7E0V6T2G, P15K8RKHDV, YNH832D50W]
about: [0DEB0JMN0W]
sources:
  - url: https://en.wikipedia.org/wiki/Harnack%27s_principle
---

## Statement

Let $U \subseteq \R^n$ be an open set and let $\mathcal{F}$ be a family of [[harmonic functions|0DEB0JMN0W]] on $U$.
Assume that $\mathcal{F}$ is uniformly bounded on each compact subset of $U$.
That is, for each compact $K \subseteq U$ there is $M_K$ with $\abs{u(x)} \le M_K$ for all $u \in \mathcal{F}$ and $x \in K$.
Then every sequence in $\mathcal{F}$ has a subsequence that converges uniformly on each compact subset of $U$, and the limit is harmonic on $U$.

## Remarks

Proof idea: the [[gradient estimates|N76R7JWMNJ]] bound $\abs{\nabla u}$ on each compact set, uniformly for $u \in \mathcal{F}$, so the family is [[equicontinuous|0MW2WXTHMC]] on compact sets.
The [[Arzelà–Ascoli theorem|0381S8Z5P0]] on an exhaustion of $U$ by compact sets, with a diagonal argument, gives a subsequence converging uniformly on compact sets.
The limit is continuous and inherits the mean value property, so it is harmonic by the [[converse of the mean value property|CQ7E0V6T2G]].
The derivatives of all orders then converge uniformly on compact sets as well.
For nonnegative harmonic functions on a connected $U$, it is enough that the family is bounded at a single point, by [[Harnack's inequality|YNH832D50W]]; this is closely related to [[Harnack's principle|P15K8RKHDV]].
The boundedness hypothesis is needed: the constants $u_k = k$ have no convergent subsequence.
Example: the family $\set{e^{t x} \cos(t y) : \abs{t} \le 1}$ on $\R^2$ is uniformly bounded on compact sets, so every sequence in it has a locally uniformly convergent subsequence.

## Explanations

### L1 human

A collection of harmonic functions that stays within fixed bounds on each bounded region cannot oscillate wildly.
From any sequence in it, one can extract a subsequence that settles down to a limit, and that limit is again harmonic.

### L2 human

This is the harmonic analogue of Montel's theorem on normal families of holomorphic functions.
It is the compactness tool behind existence proofs in potential theory, such as the construction of Green's functions by exhaustion and of extremal harmonic functions.
On a connected domain, Harnack's inequality upgrades boundedness at one point to local boundedness for positive families.
So the positive harmonic functions with $u(x_0) = 1$ form a compact set, and this compactness underlies the Martin boundary.
