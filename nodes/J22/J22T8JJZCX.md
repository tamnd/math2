---
tag: J22T8JJZCX
kind: definition
name: Potential game
msc: [91A14]
defines: G5FRB9E3J1
uses: [5MZTZRC3CZ, 745WYP9YJ0]
sources:
  - url: https://en.wikipedia.org/wiki/Potential_game
---

## Definition

Let $G = (N, (S_i), (u_i))$ be a [[normal-form game|5MZTZRC3CZ]] with $S = S_1 \times \cdots \times S_n$.
A function $\Phi \colon S \to \R$ is an *exact potential* for $G$ if
$$u_i(t_i, s_{-i}) - u_i(s_i, s_{-i}) = \Phi(t_i, s_{-i}) - \Phi(s_i, s_{-i})$$
for every player $i$, every $s \in S$ and every $t_i \in S_i$.
$G$ is an *exact potential game* if it has an exact potential.
$\Phi$ is an *ordinal potential* if the two differences always have the same sign.

## Remarks

If $s$ maximises $\Phi$, then no player gains by a single deviation, so $s$ is a pure [[Nash equilibrium|745WYP9YJ0]].
Hence every finite potential game has a pure Nash equilibrium.
In a finite potential game every sequence of strict improvements by single players is finite, since $\Phi$ strictly increases.
Example: two players choose $L$ or $R$, each getting $1$ if they match and $0$ otherwise.
Take $\Phi(s) = 1$ if $s_1 = s_2$ and $0$ otherwise; then $\Phi = u_1 = u_2$, so the identity in the definition holds.
Non-example: matching pennies has no ordinal potential.
The cycle $(H,H) \to (H,T) \to (T,T) \to (T,H) \to (H,H)$ consists of strict improvements, so $\Phi$ would strictly increase around a cycle.
