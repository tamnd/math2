---
tag: 7FVQMAZ5C6
kind: definition
name: Extensive-form game
msc: [91A18]
defines: 4Y8AF9H9HA
uses: [0Y0JGC2K9T, 0DVDCMA2DK, 5MZTZRC3CZ]
sources:
  - url: https://en.wikipedia.org/wiki/Extensive-form_game
---

## Definition

A *finite extensive-form game* with player set $N = \set{1, \dots, n}$ consists of the following.

1. A finite [[rooted tree|0Y0JGC2K9T]]; its leaves are the *terminal nodes*, and its other nodes are *decision nodes*. Each edge from a decision node to a child is labelled by an *action*. Different children of one node have different actions.
2. A *player function* that assigns to each decision node either a player in $N$ or *chance*.
3. For each chance node, a [[probability distribution|0DVDCMA2DK]] on its outgoing actions.
4. For each player $i$, a partition of the decision nodes of $i$ into *information sets*. All nodes of one information set have the same set of actions.
5. For each player $i$, a payoff function $u_i$ from the set of terminal nodes to $\R$.

A *pure strategy* of player $i$ is a function that picks one action at each information set of $i$.
The game has *perfect information* if every information set has a single node.
Some authors also require that there be no chance nodes.

## Remarks

Each pure strategy profile determines a probability distribution on terminal nodes, and so an expected payoff for each player; this gives the *induced* [[normal-form game|5MZTZRC3CZ]].
Example: in the entry game, player 1 chooses Out, ending with payoffs $(0, 2)$, or In; after In, player 2 chooses Fight with payoffs $(-1, -1)$ or Accommodate with payoffs $(1, 1)$.
The tree has two decision nodes, each an information set by itself, so it is a game of perfect information.
Non-example: let two nodes of player 2 lie in one information set, with actions $\set{L, R}$ at one and $\set{L, M, R}$ at the other.
Then clause 4 fails; indeed player 2 could tell the two nodes apart by the actions offered.
A player has *perfect recall* if she never forgets what she knew or did before; many results, such as Kuhn's theorem on behavior strategies, assume it.
