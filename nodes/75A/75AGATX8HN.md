---
tag: 75AGATX8HN
kind: example
name: Closeness within 1 is not an equivalence relation
msc: ["00A35", "03E20"]
topics: [MEKKHHQTKB]
audience: ug1
not_instance_of:
  - target: RGNF33GVHX
    note: the relation is reflexive and symmetric, but the transitivity check fails, so it is not an equivalence relation
uses: [RGNF33GVHX, 0G8VEZ3WTK, 0GJZW9JFZQ, 0FFXKTKKQC, 0ED72CTBNP]
sources:
  - url: https://en.wikipedia.org/wiki/Equivalence_relation
    locator: Definition
---

## Example

On $\mathbb{R}$, define the relation
$$x \approx y \iff \lvert x - y \rvert \le 1,$$
so two real numbers are related when they are at distance at most $1$.
We run the three checks of [[proving a relation is an equivalence relation|RGNF33GVHX]] and find the one that fails.

1. Reflexivity holds, since $\lvert x - x \rvert = 0 \le 1$.
2. Symmetry holds, since $\lvert y - x \rvert = \lvert x - y \rvert$ by the definition of the [[absolute value|0FFXKTKKQC]].
3. Transitivity is where a proof attempt stalls.
   The triangle inequality gives
   $$\lvert x - z \rvert \le \lvert x - y \rvert + \lvert y - z \rvert \le 1 + 1 = 2,$$
   and the bound $2$ is too weak to give $x \approx z$.
4. A [[counterexample|0ED72CTBNP]] shows that no better proof exists.
   Take $x = 0$, $y = 1$ and $z = 2$, so $\lvert 0 - 1 \rvert = 1$ and $\lvert 1 - 2 \rvert = 1$, which gives $0 \approx 1$ and $1 \approx 2$.
5. But $\lvert 0 - 2 \rvert = 2 > 1$, so $0 \not\approx 2$.
   The relation is not [[transitive|0GJZW9JFZQ]], and so it is not an [[equivalence relation|0G8VEZ3WTK]].

## Remarks

Transitivity must be checked, not assumed from the name of the relation.
Relations called "close", "near" or "similar" are often not transitive, and step 3 shows the sign: each link of a chain adds up to $1$ to the bound, so after $k$ links the bound is $k$.

Because transitivity fails, the would-be classes overlap.
The numbers related to $0$ form $[-1, 1]$, and the numbers related to $1$ form $[0, 2]$; these sets are neither equal nor disjoint.
Change the bound $1$ to $0$ and the relation becomes $x = y$, an equivalence relation.
The smallest equivalence relation that contains $\approx$ relates every two real numbers, because a chain of steps of length at most $1$ joins any two of them.

## Explanations

### L1 human

Call two towns "close" when they are at most $1$ kilometer apart.
A town is close to itself, and if Ann's town is close to Ben's, then Ben's is close to Ann's.
But Ann's town can be close to Ben's and Ben's close to Cara's, while Ann's town is $2$ kilometers from Cara's.
So "close" does not split the towns into separate groups.

### L2 human

We check the last claim of the Remarks for $0$ and $3.5$.

1. The chain $0, 1, 2, 3, 3.5$ has steps of length $1, 1, 1, 0.5$, each at most $1$.
2. So $0 \approx 1$, $1 \approx 2$, $2 \approx 3$ and $3 \approx 3.5$.
3. An equivalence relation that contains $\approx$ is transitive, so it relates $0$ and $3.5$.
4. The same chain works for any two numbers, so that equivalence relation has one class, all of $\mathbb{R}$.

The example is a warning for measurement: "equal up to an error of $1$" is not transitive, so it cannot stand in for equality.
Watch out for the triangle inequality in step 3: it doubles the bound, and the doubled bound proves nothing.
