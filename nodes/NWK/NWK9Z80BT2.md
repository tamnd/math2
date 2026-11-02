---
tag: NWK9Z80BT2
kind: statement
role: theorem
name: Browder–Minty theorem
msc: [47H05, 47J05]
uses: [06GZ956657, NN8RWPC8WG, 4A82S5FVRT, Y1M03JQKKR]
about: [Y1M03JQKKR]
sources:
  - url: https://en.wikipedia.org/wiki/Browder–Minty_theorem
same_as:
  wikidata: Q25303622
  wikipedia: Browder–Minty theorem
---

## Statement

Let $X$ be a real separable [[reflexive|NN8RWPC8WG]] [[Banach space|06GZ956657]] with norm $\norm{\cdot}$, and let $X^*$ be its [[continuous dual space|4A82S5FVRT]].
Write $\langle g, u \rangle$ for the value of $g \in X^*$ at $u \in X$.
Let $T \colon X \to X^*$ be a map with these three properties.

1. $T$ is [[monotone|Y1M03JQKKR]]: $\langle T(u) - T(v), u - v \rangle \ge 0$ for all $u, v \in X$.
2. $T$ is hemicontinuous: for all $u, v, w \in X$, the map $t \mapsto \langle T(u + t v), w \rangle$ is continuous on $[0, 1]$.
3. $T$ is coercive: $\langle T(u), u \rangle / \norm{u} \to +\infty$ as $\norm{u} \to \infty$.

Then for every $g \in X^*$ the equation $T(u) = g$ has a solution $u \in X$.
If moreover $\langle T(u) - T(v), u - v \rangle > 0$ for all $u \ne v$, then the solution is unique.

## Remarks

A standard proof uses the Galerkin method.
On an increasing sequence of finite-dimensional subspaces whose union is dense, the Brouwer fixed point theorem gives approximate solutions.
Coercivity bounds them, reflexivity gives a weakly convergent subsequence, and Minty's trick passes to the limit.
The trick: for a monotone hemicontinuous $T$, if $\langle g - T(v), u - v \rangle \ge 0$ for all $v \in X$, then $T(u) = g$.
For $X = \R$ the theorem says that a nondecreasing continuous function $T$ with $T(u) \to \pm\infty$ as $u \to \pm\infty$ takes every real value.
Coercivity cannot be dropped: $T(u) = \arctan u$ on $\R$ is monotone and continuous but never takes the value $2$.

## Explanations

### L1 human

The theorem solves equations $T(u) = g$ where $T$ is a nonlinear operator that "never goes backwards" and grows fast enough at infinity.
On the real line this is the intermediate value theorem for an increasing function that runs from $-\infty$ to $+\infty$.
The theorem carries this simple picture to infinite-dimensional spaces of functions.

### L2 human

The theorem is the nonlinear analogue of the Lax–Milgram theorem.
A bounded linear operator given by a coercive bilinear form is a special case of a coercive monotone operator.
Its main use is in quasilinear elliptic equations such as $-\operatorname{div}(\abs{\nabla u}^{p-2} \nabla u) = f$, whose weak form defines a monotone coercive operator from the Sobolev space $W_0^{1,p}$ to its dual for $1 < p < \infty$.
