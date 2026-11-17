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
$$x \approx y \iff \lvert x - y \rvert \le 1.$$
So two real numbers are related when they are at distance at most $1$.
We run the three checks of [[proving a relation is an equivalence relation|RGNF33GVHX]] and find the one that fails.

1. Reflexivity holds. For each $x$, $\lvert x - x \rvert = 0 \le 1$, so $x \approx x$.
2. Symmetry holds. If $\lvert x - y \rvert \le 1$, then $\lvert y - x \rvert = \lvert x - y \rvert \le 1$, because $\lvert -t \rvert = \lvert t \rvert$ for each real $t$, by the definition of the [[absolute value|0FFXKTKKQC]].
3. Transitivity fails. A natural attempt uses the triangle inequality: $\lvert x - z \rvert \le \lvert x - y \rvert + \lvert y - z \rvert \le 1 + 1 = 2$. This bound is $2$, not $1$, so the attempt does not give $x \approx z$.
4. A [[counterexample|0ED72CTBNP]] shows that no other proof exists: take $x = 0$, $y = 1$ and $z = 2$.
5. Then $\lvert 0 - 1 \rvert = 1 \le 1$, so $0 \approx 1$, and $\lvert 1 - 2 \rvert = 1 \le 1$, so $1 \approx 2$.
6. But $\lvert 0 - 2 \rvert = 2 > 1$, so $0 \not\approx 2$.
7. So the relation is not [[transitive|0GJZW9JFZQ]], and it is not an [[equivalence relation|0G8VEZ3WTK]].

## Remarks

1. The example shows why transitivity must be checked, and not assumed from the name of a relation. A relation called "close", "near" or "similar" is often not transitive.
2. Step 3 shows a typical sign: the bound grows from $1$ to $2$ in one step, and after $k$ steps it grows to $k$.
3. Because transitivity fails, the "classes" overlap. The set of numbers related to $0$ is $[-1, 1]$, and the set related to $1$ is $[0, 2]$. These sets are neither equal nor disjoint.
4. If we change the bound $1$ to $0$, the relation becomes $\lvert x - y \rvert \le 0$, that is, $x = y$, and it is an equivalence relation.
5. The smallest equivalence relation that contains $\approx$ relates every two real numbers, because any two real numbers are joined by a chain of steps of length at most $1$.

## Explanations

### L1 human

Say that two towns are "close" when they are at most $1$ kilometre apart.
A town is close to itself, and if Ann's town is close to Ben's town, then Ben's town is close to Ann's town.
But Ann's town can be close to Ben's town and Ben's town close to Cara's town, while Ann's town is $2$ kilometres from Cara's town.
So "close" does not split the towns into separate groups, and it is not an equivalence relation.

### L2 human

We show the claim of Remark 5 for the numbers $0$ and $3.5$.

1. The chain $0, 1, 2, 3, 3.5$ has steps of length $1, 1, 1, 0.5$, each at most $1$.
2. So $0 \approx 1$, $1 \approx 2$, $2 \approx 3$ and $3 \approx 3.5$.
3. Any equivalence relation that contains $\approx$ is transitive, so it relates $0$ and $3.5$.
4. The same chain argument works for any two real numbers, so the smallest such equivalence relation has one class, the whole of $\mathbb{R}$.

The typical use of this non-example is a warning in measurement: "equal up to an error of $1$" is not transitive, so it cannot replace equality.
A trap is to prove transitivity with the triangle inequality and forget that the bound changes from $1$ to $2$.
