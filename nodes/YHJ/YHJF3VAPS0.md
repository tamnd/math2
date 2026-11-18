---
tag: YHJF3VAPS0
kind: example
name: Reachability as a least fixed point
msc: ["03B45", "03B70"]
topics: [SPQVNPZDTB]
audience: research
instance_of: [MZ0M2KR9S0]
uses: [MZ0M2KR9S0, 5BXYE8REDN, DBD64TH52D]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_%CE%BC-calculus
    locator: Examples
---

## Example

Let $\mathfrak{M} = (W, R, V)$ with $W = \{0, 1, 2, 3\}$, $R = \{(0, 1), (1, 2), (3, 3)\}$ and $V(p) = \{2\}$.
We compute $\|\mu X . (p \vee \lozenge X)\|$ in the [[modal mu-calculus|MZ0M2KR9S0]].
Write $f(T) = V(p) \cup \mathrm{pre}(T)$, where $\mathrm{pre}(T) = \set{w : w R v \text{ for some } v \in T}$.
By the [[definition|5BXYE8REDN]], $f(T) = \|p \vee \lozenge X\|_{[X \mapsto T]}$, and the formula denotes the [[least fixed point|DBD64TH52D]] of $f$.

1. $T_0 = \emptyset$.
2. $T_1 = f(\emptyset) = \{2\} \cup \emptyset = \{2\}$, since no world has a successor in $\emptyset$.
3. $T_2 = f(\{2\}) = \{2\} \cup \{1\} = \{1, 2\}$, since $1 R 2$ and no other world has the successor $2$.
4. $T_3 = f(\{1, 2\}) = \{2\} \cup \{0, 1\} = \{0, 1, 2\}$, since $0 R 1$ and $1 R 2$.
5. $T_4 = f(\{0, 1, 2\}) = \{2\} \cup \{0, 1\} = \{0, 1, 2\}$. World $3$ has only the successor $3$, and world $2$ has no successor.
6. $T_4 = T_3$, so $T_3 = \{0, 1, 2\}$ is a fixed point of $f$.
7. It is the least one: every $T$ with $f(T) \subseteq T$ contains $V(p) = \{2\}$, then $1$ (a predecessor of $2$), then $0$ (a predecessor of $1$).

So $\|\mu X . (p \vee \lozenge X)\| = \{0, 1, 2\}$, the set of worlds from which a finite path reaches a $p$-world.

## Remarks

World $3$ is not in the set, although it has an infinite path: the path $3 R 3 R 3 \cdots$ never meets $p$.
If we replace $\mu$ by $\nu$, the iteration starts from $W$, and $3$ stays in the set, since $3 \in \mathrm{pre}(W)$ and then $3 \in \mathrm{pre}(T)$ for every $T$ that contains $3$.
So $\|\nu X . (p \vee \lozenge X)\| = W$: the greatest fixed point also accepts an infinite path that never reaches $p$.
If we add $p$ at $3$, the least fixed point becomes $\{0, 1, 2, 3\}$.

## Explanations

### L1 human

Think of the worlds as rooms and the arrows as one-way doors.
Room $2$ is the goal.
Room $1$ has a door to room $2$, and room $0$ has a door to room $1$, so both can reach the goal.
Room $3$ only has a door back to itself, so it can never reach the goal.

### L2 human

We check the fixed-point equation for the result $T = \{0, 1, 2\}$ world by world.

1. World $0$: $p$ is false, but $0 R 1$ and $1 \in T$, so $0 \in f(T)$.
2. World $1$: $p$ is false, but $1 R 2$ and $2 \in T$, so $1 \in f(T)$.
3. World $2$: $p$ is true, so $2 \in f(T)$.
4. World $3$: $p$ is false, and its only successor $3$ is not in $T$, so $3 \notin f(T)$.

So $f(T) = T$.
The typical use of this formula is the property "eventually $p$ on some path", written $\mathrm{EF}\, p$ in computation tree logic.
A trap: the greatest fixed point of the same map is $W$ here, so choosing $\nu$ by mistake changes the answer at world $3$.
