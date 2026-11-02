---
tag: A2WHCVP6JN
kind: definition
name: Germ of an analytic set
msc: [32B10, 32B05]
defines: Q9B74BYZ8C
uses: [VMDTGTMN9P, Y98MD3WVTG, 0ZCY0Z80B6, 2TGPZ8VW2D]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_analytic_variety
---

## Definition

Let $a \in \C^n$.
Consider pairs $(U, A)$ where $U$ is an open [[neighbourhood|0ZCY0Z80B6]] of $a$ in $\C^n$ and $A$ is an [[analytic subset|VMDTGTMN9P]] of $U$.
Two pairs $(U, A)$ and $(V, B)$ are equivalent if there is an open neighbourhood $W \subseteq U \cap V$ of $a$ with $A \cap W = B \cap W$.
A *germ of an analytic set* at $a$ is an equivalence class for this relation; the class of $(U, A)$ is written $A_a$.

## Remarks

This is the notion of [[germ|Y98MD3WVTG]] applied to analytic sets.
Inclusion, finite union and finite intersection of germs are defined through representatives on a common neighbourhood.
To a germ $A_a$ one attaches the ideal $\mathcal{I}(A_a)$ of all [[holomorphic germs|2TGPZ8VW2D]] $f_a \in \mathcal{O}_{n,a}$ that have a representative vanishing on a representative of $A_a$; it is a radical ideal.
Conversely, an ideal $I \subseteq \mathcal{O}_{n,a}$ with generators $f_{1,a}, \dots, f_{k,a}$ defines the germ $V(I)$ of the common zero set of representatives $f_1, \dots, f_k$.
Example: the sets $\set{z_1 z_2 = 0}$ and $\set{z_1 z_2 (z_1 - 1) = 0}$ in $\C^2$ have the same germ at $0$, since they agree on the ball of radius $1$ about $0$.
Non-example: the sets $\set{z_1 = 0}$ and $\set{z_1 = z_2^2}$ have different germs at $0$.
Indeed, every neighbourhood of $0$ contains a point $(0, t)$ with $t \ne 0$, which lies in the first set but not the second.
The germ of $A$ at a point $a \notin A$ is the empty germ.
