---
tag: D07MBM0S3V
kind: statement
role: theorem
name: Conley's fundamental theorem of dynamical systems
msc: [37B35, 37B25, 37B20]
uses: [0TVJZYB6SH, 0VKD1TP7F3, BBZP1R872N, 6MX5R482KJ, 01REYCJ371, 0VQYCCQVJ5]
about: [6MX5R482KJ, 01REYCJ371]
sources:
  - url: https://en.wikipedia.org/wiki/Conley%27s_fundamental_theorem_of_dynamical_systems
same_as:
  wikidata: Q122143261
  wikipedia: Conley's fundamental theorem of dynamical systems
---

## Statement

Let $(X, d)$ be a [[compact|0TVJZYB6SH]] [[metric space|0VKD1TP7F3]] and let $\varphi \colon \R \times X \to X$, $(t, x) \mapsto \varphi_t(x)$, be a continuous [[flow|BBZP1R872N]].
Let $\mathcal{R}(\varphi)$ be its [[chain recurrent set|6MX5R482KJ]].
Call $x, y \in \mathcal{R}(\varphi)$ chain equivalent if for all $\varepsilon > 0$ and $T > 0$ there are $(\varepsilon, T)$-chains from $x$ to $y$ and from $y$ to $x$.
The classes of this relation are the chain components.
Then there is a continuous function $V \colon X \to \R$, a complete [[Lyapunov function|01REYCJ371]] for $\varphi$, such that:

1. $V(\varphi_t(x)) < V(x)$ for every $x \notin \mathcal{R}(\varphi)$ and every $t > 0$.
2. For $x, y \in \mathcal{R}(\varphi)$, $V(x) = V(y)$ if and only if $x$ and $y$ lie in the same chain component.
3. The set $V(\mathcal{R}(\varphi))$ is a compact [[nowhere dense|0VQYCCQVJ5]] subset of $\R$.

## Remarks

The proof uses attractor–repeller pairs $(A, A^\ast)$.
For each such pair, Conley builds a continuous function equal to $0$ on $A$ and to $1$ on $A^\ast$ that strictly decreases along orbits between them.
A compact metric space carries only countably many attractors $A_1, A_2, \ldots$, and $V = \sum_n 3^{-n} V_n$ combines the corresponding functions.
The key fact is that $\mathcal{R}(\varphi)$ is the intersection of the sets $A \cup A^\ast$ over all attractor–repeller pairs.
Example: let $f$ be a Morse function on a compact Riemannian manifold with pairwise distinct critical values.
For the flow of $-\nabla f$, the chain recurrent set is the set of critical points, and $V = f$ satisfies the three conditions.
Compactness is needed for the countability of attractors and for the existence of the attractor–repeller decomposition used in the proof.

## Explanations

### L1 human

The theorem splits every continuous flow on a compact metric space into two parts.
One part is the chain recurrent set, where the motion can come back to itself up to tiny errors.
On the rest, the motion runs steadily downhill for some height function, as water flows down a landscape.
So every flow on a compact space looks like a gradient flow once the recurrent pieces are collapsed to points.

### L2 human

The function $V$ orders the chain components like levels of a landscape and shows that orbits outside $\mathcal{R}(\varphi)$ go from higher components to lower ones.
This is why the result is sometimes called the fundamental theorem of dynamical systems: the chain components are the indecomposable pieces, and between them there is only gradient-like motion.
The statement is the starting point for Morse decompositions and for the Conley index.
Versions for continuous maps of compact metric spaces, with $\varepsilon$-chains in place of $(\varepsilon, T)$-chains, also hold.
