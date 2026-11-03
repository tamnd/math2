---
tag: JZAAZWMFK4
kind: problem
name: Pursuit–evasion game
msc: [49N75, 91A24, 91A23]
uses: [THSHGNJNPS, T3V6ZNAMDN]
about: [THSHGNJNPS, M0B618E2P6]
sources:
  - url: https://en.wikipedia.org/wiki/Pursuit%E2%80%93evasion
same_as:
  wikidata: Q7261573
  wikipedia: Pursuit–evasion
history:
  posed_by: "Richard Rado"
  first_stated: "1925"
  notes: "Rado posed the lion and man problem, an equal-speed pursuit in a disc, in 1925 according to Littlewood; the attribution is to this earliest known formulation. The general theory of pursuit and evasion as differential games was developed by Rufus Isaacs, whose book appeared in 1965."
---

## Problem

Let $n \ge 1$, let $R \subseteq \R^n$ be a closed set, and let $v_P > 0$, $v_E > 0$ and $\ell \ge 0$.
A pursuer at position $x_P(t) \in R$ and an evader at position $x_E(t) \in R$ move with $\abs{x_P'(t)} \le v_P$ and $\abs{x_E'(t)} \le v_E$, starting from given points $x_P(0)$ and $x_E(0)$.
Capture happens at the first time $T$ with $\abs{x_P(T) - x_E(T)} \le \ell$.
The pursuer wants to make $T$ as small as possible, and the evader wants to make it as large as possible, or infinite.
This is a two-player zero-sum [[differential game|THSHGNJNPS]].
The *pursuit–evasion problem* asks for which initial positions capture is certain, and for the value of the game and optimal strategies of both players.
Variants change the dynamics, the region $R$ or the information of each player.
In other variants the players move along the edges of a graph.

## Remarks

In the whole space $R = \R^n$ with $\ell = 0$ and $v_P > v_E$, the value is $T = d / (v_P - v_E)$, where $d = \abs{x_P(0) - x_E(0)}$.
If the pursuer always runs straight at the evader, the distance decreases at rate at least $v_P - v_E$, so capture happens by time $T$.
If the evader always runs straight away from the pursuer, the distance decreases at rate at most $v_P - v_E$, so capture takes at least time $T$.
If $v_P \le v_E$ and $d > 0$, the evader can avoid capture forever in $\R^n$.

The problem becomes hard when the region is bounded or the dynamics are constrained.
In the lion and man problem, $R$ is a closed disc and $v_P = v_E$; Besicovitch showed that the man (the evader) can avoid capture forever in continuous time.
The [[homicidal chauffeur problem|M0B618E2P6]] gives the pursuer a large speed but a bounded turning radius.
Isaacs developed his theory of [[differential games|THSHGNJNPS]] to study such games; it is linked to [[optimal control|T3V6ZNAMDN]] through the Hamilton–Jacobi–Isaacs equation for the value.
On graphs, the cops and robbers game asks how many pursuers are needed to catch an evader on a given graph.

## Explanations

### L1 human

One player chases and another player runs away, and both choose their moves as they go.
The questions are whether the chaser can always catch the runner, and how quickly.
In open space, a faster chaser simply runs at the runner and catches up at the speed difference.
Inside walls, or with a chaser that cannot turn sharply, the answer becomes subtle and needs real mathematics.
Such games model missiles and aircraft, robots searching a building, and police searching for a suspect.
