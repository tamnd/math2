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
We compute $\|\mu X . (p \vee \lozenge X)\|$ in the [[modal mu-calculus|MZ0M2KR9S0]], the set of worlds from which some finite path reaches $p$.
Write $\mathrm{pre}(T) = \{ w : w R v \text{ for some } v \in T \}$ and $f(T) = V(p) \cup \mathrm{pre}(T)$.
By the [[definition|5BXYE8REDN]], $f(T) = \|p \vee \lozenge X\|_{[X \mapsto T]}$, and the formula denotes the [[least fixed point|DBD64TH52D]] of $f$.
On a finite model we find it by iterating $f$ from the empty set.

1. Start with $T_0 = \emptyset$.
2. No world has a successor in $\emptyset$, so $T_1 = f(\emptyset) = \{2\}$.
3. Only world $1$ has the successor $2$, so $T_2 = f(\{2\}) = \{2\} \cup \{1\} = \{1, 2\}$.
4. The predecessors of $\{1, 2\}$ are $0$ and $1$, so $T_3 = f(\{1, 2\}) = \{2\} \cup \{0, 1\} = \{0, 1, 2\}$.
5. The predecessors of $\{0, 1, 2\}$ are again $0$ and $1$.
   World $2$ has no successor, and world $3$ has only the successor $3$.
   So $T_4 = \{0, 1, 2\} = T_3$, and the iteration has stopped at a fixed point.
6. It is the least one.
   Every $T$ with $f(T) \subseteq T$ contains $V(p) = \{2\}$, then the predecessor $1$ of $2$, then the predecessor $0$ of $1$.

So the formula holds exactly at $0$, $1$ and $2$:
$$\|\mu X . (p \vee \lozenge X)\| = \{0, 1, 2\}.$$
Check: world $0$ reaches $p$ by the path $0, 1, 2$, and world $3$ can only loop at $3$.

## Remarks

World $3$ is left out although it has an infinite path, because the path $3, 3, 3, \dots$ never meets $p$.
A least fixed point only accepts what is reached after finitely many unfoldings, and no unfolding at $3$ ever reaches $p$.

Watch what happens if we replace $\mu$ by $\nu$.
The iteration then starts from $W$, and $3 \in \mathrm{pre}(T)$ for every $T$ that contains $3$, so world $3$ never drops out.
The greatest fixed point is all of $W$, which accepts a path that loops forever without reaching $p$.
If instead we make $p$ true at $3$, the least fixed point grows to $\{0, 1, 2, 3\}$.

## Explanations

### L1 human

Think of the worlds as rooms and the arrows as one-way doors.
Room $2$ is the goal.
Room $1$ has a door to room $2$, and room $0$ has a door to room $1$, so both can reach the goal.
Room $3$ only has a door back to itself, so it can never reach the goal.
The computation finds the goal first, then the rooms one door away, then two doors away.

### L2 human

We confirm that $T = \{0, 1, 2\}$ solves the equation $f(T) = T$, one world at a time.
At world $0$, $p$ is false, but $0 R 1$ with $1 \in T$, so $0 \in f(T)$.
At world $1$, $p$ is false, but $1 R 2$ with $2 \in T$, so $1 \in f(T)$.
At world $2$, $p$ is true, so $2 \in f(T)$.
At world $3$, $p$ is false and its only successor $3$ is not in $T$, so $3 \notin f(T)$.
Being a fixed point is not enough, since $W$ is a fixed point too; step 6 is what shows that $T$ is the least one.
The typical use of this formula is the property "on some path, eventually $p$", written $\mathrm{EF}\, p$ in computation tree logic.
