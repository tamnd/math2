---
tag: ESTN2VX79E
kind: definition
name: Theory of island biogeography
msc: [92D40]
defines: CZAD9RNTEX
uses: [0P97V20RW7, 0G4X36AE0X]
sources:
  - url: https://en.wikipedia.org/wiki/Insular_biogeography
---

## Definition

Let $P \ge 1$ be the number of species in the mainland species pool.
Let $S(t) \in [0, P]$ be the number of species present on an island at time $t$.
Let $I \colon [0, P] \to [0, \infty)$ be the immigration rate and $E \colon [0, P] \to [0, \infty)$ the extinction rate, as functions of the number of resident species.
The *equilibrium model of island biogeography* assumes the following.

1. $I$ is strictly decreasing with $I(P) = 0$.
2. $E$ is strictly increasing with $E(0) = 0$.
3. $S$ obeys the [[ordinary differential equation|0P97V20RW7]] $S'(t) = I(S(t)) - E(S(t))$.

The *equilibrium species number* is the value $\hat{S}$ with $I(\hat{S}) = E(\hat{S})$.
The *theory of island biogeography* is the study of species numbers on islands, and on habitat patches, through this balance.

## Remarks

Under clauses 1 and 2, if $I(0) > 0$ and $I$, $E$ are continuous, the function $I - E$ is strictly decreasing, positive at $0$ and nonpositive at $P$.
So there is exactly one $\hat{S}$, and it is a stable [[equilibrium point|0G4X36AE0X]].

Example: take $I(S) = i \, (1 - S/P)$ and $E(S) = e \, S/P$ with constants $i, e > 0$.
Both clauses hold, and $I(\hat{S}) = E(\hat{S})$ gives $\hat{S} = P \, i / (i + e)$.
For $P = 100$, $i = 3$ and $e = 1$, one gets $\hat{S} = 75$.

Non-example: if the extinction rate were constant and positive, clause 2 would fail, since $E(0) > 0$ would mean an empty island loses species.

In the theory, larger islands have lower extinction rates, and islands closer to the mainland have higher immigration rates.
This fits the empirical species–area relation $S = c A^{z}$, where $A$ is the island area and $c, z > 0$ are constants.
