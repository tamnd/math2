---
tag: R7VKRV8AGQ
kind: statement
role: theorem
name: Cartan's theorem B
msc: ["32E10", 32C35]
uses: [Z4AMJS5KA6, DSJET02WPR, PQ6Q143ARJ]
about: [Z4AMJS5KA6, DSJET02WPR]
sources:
  - url: https://en.wikipedia.org/wiki/Cartan%27s_theorems_A_and_B
---

## Statement

Let $X$ be a [[Stein space|Z4AMJS5KA6]] and let $\mathcal{F}$ be a [[coherent analytic sheaf|DSJET02WPR]] on $X$.
Then the [[sheaf cohomology|PQ6Q143ARJ]] groups vanish in positive degree:
$$H^q(X, \mathcal{F}) = 0 \quad \text{for all } q \ge 1.$$

## Remarks

The converse holds: a complex space on which $H^1(X, \mathcal{F}) = 0$ for every coherent analytic sheaf $\mathcal{F}$ is Stein, so theorem B characterizes Stein spaces.
The proof first treats compact polydiscs and analytic polyhedra.
There, vanishing follows from Cousin-type gluing and from the local theory of coherent sheaves.
Then it passes to the limit over an exhaustion of $X$ by holomorphically convex compact sets, using approximation to control the inverse limit.
Example: on a Stein manifold, $H^1(X, \mathcal{O}) = 0$, so the first Cousin problem is always solvable.
Example: for an analytic subset $Y$ with ideal sheaf $\mathcal{I}$, the exact sequence $0 \to \mathcal{I} \to \mathcal{O}_X \to \mathcal{O}_X / \mathcal{I} \to 0$ and $H^1(X, \mathcal{I}) = 0$ show that every holomorphic function on $Y$ extends to a holomorphic function on $X$.
The Stein hypothesis is needed: on the projective line, $H^1(\mathbb{P}^1, \mathcal{O}(-2)) \cong \C$ is not zero; and on $\C^2 \setminus \set{0}$, the group $H^1(X, \mathcal{O})$ is infinite-dimensional.

## Explanations

### L1 human

Many problems in complex analysis ask to glue local holomorphic solutions into a global one.
The obstruction to such gluing lies in a cohomology group.
Theorem B says that on a Stein space these obstructions vanish, for all problems described by coherent sheaves.
So on Stein spaces, whatever can be solved locally can be solved globally.

### L2 human

Theorem B, with the exponential sequence, solves the Cousin problems: the additive one always, and the multiplicative one exactly when a topological obstruction in $H^2(X, \Z)$ vanishes.
It gives extension of holomorphic functions from closed analytic subsets, interpolation on discrete sets, and the embedding of Stein manifolds into $\C^N$.
It is the analytic analogue of Serre's vanishing theorem for quasi-coherent sheaves on affine schemes.
