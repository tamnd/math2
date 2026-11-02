---
tag: D0A22MEB1F
kind: example
name: Tent map
msc: ["37E05", "37A05"]
instance_of: [5AA9AJEARJ]
uses: [5AA9AJEARJ, B232EZ1FMB, 2Z2QVWZ262, BDZYBXBFDE, NJ1FJSNK6A]
sources:
  - url: https://en.wikipedia.org/wiki/Tent_map
same_as:
  wikidata: Q11319849
  wikipedia: Tent map
---

## Example

For a parameter $\mu \in [0, 2]$, the *tent map* is
$$T_\mu \colon [0, 1] \to [0, 1], \qquad T_\mu(x) = \mu \min(x, 1 - x).$$
Its graph is a tent: it rises with slope $\mu$ on $[0, 1/2]$ and falls with slope $-\mu$ on $[1/2, 1]$.
Its top value is $\mu/2 \le 1$, so it maps $[0, 1]$ into itself and is a [[discrete-time dynamical system|5AA9AJEARJ]].

Check that [[Lebesgue measure|2Z2QVWZ262]] $\lambda$ is [[invariant|B232EZ1FMB]] for $\mu = 2$.
For $0 \le a < b \le 1$, the preimage $T_2^{-1}([a, b])$ is $[a/2, b/2] \cup [1 - b/2, 1 - a/2]$, two intervals of length $(b - a)/2$ each.
So $\lambda(T_2^{-1}[a, b]) = b - a = \lambda([a, b])$, and this extends from intervals to all Borel sets.

## Remarks

For $\mu = 2$ the map is ergodic for Lebesgue measure, has [[topological entropy|BDZYBXBFDE]] $\log 2$, and has [[Lyapunov exponent|NJ1FJSNK6A]] $\log 2$ at every point whose orbit avoids $1/2$, since $\abs{T_2'} = 2$.
For $0 \le \mu < 1$ every orbit tends to the fixed point $0$.
The map $T_2$ is conjugate to the logistic map $x \mapsto 4x(1 - x)$.

## Explanations

### L1 human

The tent map stretches the unit interval to twice its length and folds it back onto itself, like kneading dough.
Each step doubles small distances between nearby points, so tiny errors grow fast and long-term prediction fails.
Yet the stretching and folding is so even that a random starting point spends equal time in intervals of equal length.
