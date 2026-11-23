---
tag: R3WCA35JKD
kind: example
name: An infinite path of p-worlds as a greatest fixed point
msc: ["03B45", "03B70"]
topics: [SPQVNPZDTB]
audience: research
instance_of: [MZ0M2KR9S0]
uses: [MZ0M2KR9S0, 5BXYE8REDN]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_%CE%BC-calculus
    locator: Examples
---

## Example

Let $\mathfrak{M} = (W, R, V)$ with $W = \{0, 1, 2, 3, 4\}$ and $V(p) = \{0, 1, 2, 3\}$, where the relation is the following.
$$R = \{(0, 1), (1, 0), (0, 2), (2, 3), (3, 4), (4, 4)\}$$
We compute $\|\nu X . (p \wedge \lozenge X)\|$ in the [[modal mu-calculus|MZ0M2KR9S0]], the set of worlds where an infinite path through $p$-worlds starts.
Write $\mathrm{pre}(T) = \{ w : w R v \text{ for some } v \in T \}$ and $g(T) = V(p) \cap \mathrm{pre}(T)$.
By the [[definition|5BXYE8REDN]], the formula denotes the greatest fixed point of $g$, and on a finite model we reach it by iterating from $W$.

1. Start with $T_0 = W$.
2. Every world has a successor, so $\mathrm{pre}(W) = W$ and $T_1 = V(p) = \{0, 1, 2, 3\}$.
3. Worlds $0$, $1$ and $2$ have successors in $T_1$, through $0 R 1$, $1 R 0$ and $2 R 3$.
   Worlds $3$ and $4$ do not, since their only successor is $4$.
   So $T_2 = \{0, 1, 2\}$.
4. Worlds $0$ and $1$ still have successors in $T_2$, but the only successor of $2$ is $3 \notin T_2$.
   So $T_3 = \{0, 1\}$.
5. Since $0 R 1$ and $1 R 0$, we get $T_4 = \{0, 1\} = T_3$, a fixed point.
6. It is the greatest one.
   If $T = g(T)$, then $T \subseteq W = T_0$, and monotonicity of $g$ gives $T = g(T) \subseteq g(T_k) = T_{k+1}$ for each $k$, so $T \subseteq T_3$.

So the formula holds exactly at $0$ and $1$:
$$\|\nu X . (p \wedge \lozenge X)\| = \{0, 1\}.$$
Check: the path $0, 1, 0, 1, \dots$ stays among $p$-worlds forever, and so does $1, 0, 1, 0, \dots$.

## Remarks

World $2$ starts the $p$-path $2, 3$, but every continuation of it goes to $4$, where $p$ is false.
World $3$ has the infinite path $3, 4, 4, \dots$, but that path leaves the $p$-worlds at once.
So the greatest fixed point asks for two things together: the path must be infinite, and it must stay inside $p$.

The choice of $\nu$ is what makes the formula speak about infinite behavior.
The least fixed point of the same map is empty, because $g(\emptyset) = \emptyset$: no world has a successor in the empty set.
The answer is also fragile.
If we remove the pair $(1, 0)$ from $R$, world $1$ has no successor, and the iteration gives $T_1 = \{0, 2, 3\}$, then $T_2 = \{0, 2\}$, then $T_3 = \{0\}$, then $T_4 = \emptyset$, since no world has the successor $0$ any more.

## Explanations

### L1 human

Read $p$ as "the machine is safe", and the arrows as the possible next steps.
The formula asks for a way to run forever and stay safe at every step.
From worlds $0$ and $1$ the machine can go back and forth between them forever, and both are safe.
From world $2$ every run reaches world $4$, which is unsafe.

### L2 human

For a greatest fixed point there is a short way to prove membership without the whole iteration.
By the definition, $\|\nu X . \varphi\|$ is the union of all post-fixed points, the sets $T$ with $T \subseteq g(T)$.
So it is enough to find one such $T$ that contains the world.
Try $T = \{0, 1\}$.
World $0$ satisfies $p$ and has the successor $1 \in T$, so $0 \in g(T)$.
World $1$ satisfies $p$ and has the successor $0 \in T$, so $1 \in g(T)$.
Hence $T \subseteq g(T)$, and both worlds lie in the greatest fixed point.
Watch out: this shortcut only proves membership, and to show that world $2$ is outside you still need the iteration or another argument.
The typical use of this formula is the property "on some path, always $p$", written $\mathrm{EG}\, p$ in computation tree logic.
