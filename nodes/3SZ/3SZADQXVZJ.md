---
tag: 3SZADQXVZJ
kind: object
name: Von Neumann universe
msc: ["03E30", "03E10"]
instance_of: [Y48FA69563]
uses: [0YSCSX5YZC, 0BC7KX51Z8, 0ZHQMQ2C1N, NFQ9FVCP31, NW4DREQ5DQ]
sources:
  - url: https://en.wikipedia.org/wiki/Von_Neumann_universe
same_as:
  wikidata: Q77887
  wikipedia: Von Neumann universe
---

## Description

The von Neumann universe $V$ is the [[class|Y48FA69563]] of all sets, arranged in stages indexed by the [[ordinal numbers|0YSCSX5YZC]].
The stages $V_\alpha$ are defined by [[transfinite recursion|0ZHQMQ2C1N]] on the ordinal $\alpha$:

1. $V_0 = \varnothing$.
2. $V_{\alpha + 1} = \mathcal{P}(V_\alpha)$, the [[power set|0BC7KX51Z8]] of $V_\alpha$.
3. $V_\lambda = \bigcup_{\beta < \lambda} V_\beta$ for each limit ordinal $\lambda$.

Then $V = \bigcup_{\alpha} V_\alpha$, the union over all ordinals.
The rank of a set $x$ in $V$ is the least ordinal $\alpha$ such that $x \subseteq V_\alpha$.

## Remarks

Each $V_\alpha$ is a transitive set, and $V_\beta \subseteq V_\alpha$ when $\beta \le \alpha$.
The first stages are $V_1 = \{\varnothing\}$ and $V_2 = \{\varnothing, \{\varnothing\}\}$, and in general $\abs{V_{n+1}} = 2^{\abs{V_n}}$ for finite $n$.
The stage $V_\omega$ is the set of hereditarily finite sets, and it is countable.
Over the other axioms of ZF, the [[axiom of regularity|NFQ9FVCP31]] is equivalent to the statement that every set lies in some $V_\alpha$.
If $\kappa$ is an [[inaccessible cardinal|NW4DREQ5DQ]], then $V_\kappa$ is a model of ZFC.

## Explanations

### L1 human

Start with nothing, the empty set.
At each step, form all sets whose elements were already built; at a limit step, collect everything built so far.
The von Neumann universe is everything that ever appears in this process, and in ZF this is every set.
For example, $\varnothing$ is an element of $V_1$, $\{\varnothing\}$ is an element of $V_2$, and $\{\{\varnothing\}\}$ is an element of $V_3$.
The picture is often drawn as a V-shaped cone that widens as the stages go up.
