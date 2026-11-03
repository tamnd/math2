---
tag: SG5K6GE0YB
kind: statement
role: theorem
name: Amenability of abelian and solvable groups
msc: ["43A07", "20F16"]
uses: [082GHNPJ53, 0FXJ7YFMMX, CEAT9BESKK, MF4N3VGGFV, H9AFGFG4RB]
about: [CEAT9BESKK]
sources:
  - url: https://en.wikipedia.org/wiki/Amenable_group
---

## Statement

Let $G$ be a group, with no topology.

1. If $G$ is [[abelian|082GHNPJ53]], then $G$ is [[amenable|CEAT9BESKK]].
2. If $G$ is [[solvable|0FXJ7YFMMX]], then $G$ is amenable.

## Remarks

For part 1, the means on $\ell^\infty(G)$ form a nonempty weak-$*$ compact convex set, and each $g \in G$ acts on it by the continuous affine map $m \mapsto (f \mapsto m(g^{-1} \cdot f))$.
These maps commute because $G$ is abelian, so the [[Markov–Kakutani fixed-point theorem|H9AFGFG4RB]] gives a common fixed point, which is an invariant mean.
For part 2, amenability passes to [[extensions|MF4N3VGGFV]]: if $N$ is a normal subgroup with $N$ and $G/N$ amenable, then $G$ is amenable.
A solvable group has a finite series $\set{1} = G_k \le \cdots \le G_0 = G$ with each $G_{i+1}$ normal in $G_i$ and $G_i/G_{i+1}$ abelian, so induction on $k$ gives part 2.

Example: the group of upper triangular $2 \times 2$ real matrices with determinant $1$ is solvable, hence amenable as a discrete group.
In contrast, $\mathrm{SL}(2, \Z)$ is not amenable, since it contains a free group of rank $2$.

The same statements hold for locally compact groups: every abelian and every solvable locally compact group is amenable.

## Explanations

### L1 human

Abelian groups, and groups built from abelian groups in finitely many layers, always admit a fair translation-invariant way to average bounded functions.
For the integers, one can think of such an average as a limit of averages over longer and longer intervals.
The proof uses a fixed point theorem instead of an explicit formula.

### L2 human

This result, together with the amenability of finite groups and stability under subgroups, quotients, extensions and directed unions, generates the class of [[elementary amenable groups|N8RM4Q6W4S]].
It contrasts with the [[non-amenability of free groups|XXT7T7VM05]].
By the Tits alternative, a finitely generated linear group is either virtually solvable, hence amenable, or contains a free group of rank $2$.
