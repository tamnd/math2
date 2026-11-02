---
tag: 5MN8MX0JPA
kind: definition
name: Heegaard splitting
msc: [57K30]
defines: EDE9919B5R
uses: [R20TB2KEQQ, AP1KY4EHMA, VGJJVBZ1MQ, NJ787GZS1N]
sources:
  - url: https://en.wikipedia.org/wiki/Heegaard_splitting
---

## Definition

Let $\Gamma \subset \R^3$ be a connected finite graph with Euler characteristic $1 - g$.
A *handlebody of genus $g$* is a $3$-manifold homeomorphic to a closed regular neighbourhood of $\Gamma$ in $\R^3$.
Its boundary is a closed orientable surface of [[genus|NJ787GZS1N]] $g$.

Let $M$ be a closed connected orientable [[3-manifold|R20TB2KEQQ]].
A *Heegaard splitting* of $M$ is a pair $(V, W)$ of subsets of $M$ such that:

1. $M = V \cup W$;
2. $V$ and $W$ are [[handlebodies|AP1KY4EHMA]] of the same genus $g$;
3. $V \cap W = \partial V = \partial W$.

The closed [[surface|VGJJVBZ1MQ]] $\Sigma = V \cap W$ is the *Heegaard surface*, and $g$ is the genus of the splitting.

## Remarks

Every closed connected orientable $3$-manifold has a Heegaard splitting.
Take a triangulation and let $V$ be a regular neighbourhood of its $1$-skeleton.
The closure $W$ of the complement is a regular neighbourhood of the dual $1$-skeleton.
The *Heegaard genus* of $M$ is the least genus of a Heegaard splitting.

Example: $S^3 = \set{(z, w) \in \C^2 : \abs{z}^2 + \abs{w}^2 = 1}$ is the union of the solid tori $V = \set{\abs{z} \le \abs{w}}$ and $W = \set{\abs{z} \ge \abs{w}}$, which meet in the torus $\abs{z} = \abs{w} = 1/\sqrt{2}$; this is a splitting of genus $1$.
Lens spaces also have splittings of genus $1$.

Non-example: let $N$ be a closed tubular neighbourhood of a trefoil knot in $S^3$ and $E$ the closure of its complement.
Then $S^3 = N \cup E$ with $N \cap E = \partial N = \partial E$ a torus, and $N$ is a solid torus, but $E$ is not a handlebody.
Indeed the fundamental group of $E$ is $\langle x, y \mid x^2 = y^3 \rangle$, which is not free, while handlebodies have free fundamental groups.
So clause 2 fails.

## Explanations

### L1 human

The definition splits a closed $3$-dimensional space into two thickened graphs that share their whole boundary surface.
All the topology of the space is then in how the two boundary surfaces are glued.
