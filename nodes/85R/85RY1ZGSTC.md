---
tag: 85RY1ZGSTC
kind: statement
role: theorem
name: Nash's existence theorem
msc: [91A10, 91A06, 47H10]
uses: [5MZTZRC3CZ, P01KKHB155, QS6VCNJK60, 745WYP9YJ0, 1FSR0S8E45, 7V3HWGR32Z, N7AAJ2MW5T]
about: [745WYP9YJ0]
sources:
  - url: https://en.wikipedia.org/wiki/Nash_equilibrium
---

## Statement

Let $G$ be a finite [[normal-form game|5MZTZRC3CZ]], with finitely many players and finitely many pure strategies for each player.
Then $G$ has at least one [[Nash equilibrium|745WYP9YJ0]] in [[mixed strategies|P01KKHB155]].

## Remarks

Nash's first proof applies the [[Kakutani fixed-point theorem|7V3HWGR32Z]] to the [[best-response|QS6VCNJK60]] correspondence $\sigma \mapsto \prod_i \mathrm{BR}_i(\sigma_{-i})$ on the compact convex set $\prod_i \Delta(S_i)$.
Its values are nonempty and convex, and its graph is closed, because each $u_i$ is continuous and linear in $\sigma_i$.
His second proof builds a continuous map on the same set, which shifts weight toward pure strategies that do better than the current mix, and applies the [[Brouwer fixed-point theorem|N7AAJ2MW5T]].
A fixed point of either map is a Nash equilibrium.
Example: matching pennies has no pure Nash equilibrium, and the theorem gives the mixed one where both players play each side with probability $1/2$.
Finiteness matters: in the game where each of two players names a natural number and the larger number wins, there is no equilibrium at all.

## Explanations

### L1 human

Every game with finitely many players and choices has a stable outcome, provided players may randomise.
In such an outcome nobody wants to change her plan, given the plans of the others.
This is why Nash equilibrium can be used as a prediction in every finite game.

### L2 human

The proof is not constructive, since it rests on a fixed-point theorem.
For two players, the [[Lemke–Howson algorithm|1FSR0S8E45]] finds an equilibrium and gives a constructive proof.
In general, computing an equilibrium is believed to be hard: the problem is PPAD-complete.
For games with compact strategy sets and continuous payoffs, the Glicksberg extension gives existence in mixed strategies.
For two-player zero-sum games the theorem implies von Neumann's minimax theorem.
