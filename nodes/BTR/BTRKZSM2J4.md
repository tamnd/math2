---
tag: BTRKZSM2J4
kind: statement
role: theorem
name: Tarski's theorem on paradoxical groups
msc: ["43A07", "03E25", "28C10"]
uses: [0WCY42EV9V, KFWQ24D9M6, XRCN826T16, CEAT9BESKK]
about: [XRCN826T16, CEAT9BESKK]
sources:
  - url: https://en.wikipedia.org/wiki/Amenable_group
---

## Statement

Let $G$ be a group acting on a set $X$, and let $E \subseteq X$.
Then exactly one of the following holds.

1. There is a [[finitely additive measure|KFWQ24D9M6]] $\mu$ on all subsets of $X$, with values in $[0, \infty]$, that is $G$-invariant, $\mu(gA) = \mu(A)$, and satisfies $\mu(E) = 1$.
2. $E$ has a [[paradoxical decomposition|XRCN826T16]] for the action of $G$.

In particular, a group $G$ is [[amenable|CEAT9BESKK]] if and only if it is not paradoxical for its action on itself by left multiplication.

## Remarks

That 1 and 2 cannot both hold is direct: the pieces of a paradoxical decomposition, chosen with $g_i A_i$ disjoint and $h_j B_j$ disjoint, would give $\mu(E) \ge 2\mu(E)$ with $\mu(E) = 1$.
The hard direction builds $\mu$ when $E$ is not paradoxical.
Tarski's proof studies the commutative semigroup of equidecomposability types and uses a cancellation law in it, with the Hahn–Banach theorem or a similar extension argument.
These arguments use the axiom of choice.

Example: the free group $F_2$ is paradoxical, so it carries no invariant finitely additive probability on its subsets.
The group $\Z$ is amenable, so it is not paradoxical.

## Explanations

### L1 human

Either a group has a fair, shift-invariant way to measure the size of every subset, or it has a paradoxical splitting.
In the second case, finitely many pieces of the group, after shifting, rebuild the group twice.
Tarski's theorem says that one of these two always happens, and never both.

### L2 human

The theorem explains why paradoxes like the [[Banach–Tarski paradox|FH250K068Z]] appear exactly for non-amenable groups.
In dimensions $1$ and $2$ the isometry groups are solvable, hence amenable, so no paradoxical decomposition of the interval or the disc by isometries exists.
In dimension $3$, the rotation group contains a free group of rank $2$, and the ball becomes paradoxical.
The minimal number of pieces in a paradoxical decomposition, the Tarski number, is a finer invariant of non-amenable groups.
