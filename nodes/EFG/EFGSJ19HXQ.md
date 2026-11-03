---
tag: EFGSJ19HXQ
kind: problem
name: Facility location problem
msc: [90B80, 90B85, 90C27]
uses: [FJPER80BJC, XXRXVA6RBZ, MHA48AWBXN, 03HF5PMY5T, 4WEVBDQ8SR]
about: [FJPER80BJC]
sources:
  - url: https://en.wikipedia.org/wiki/Optimal_facility_location
same_as:
  wikidata: Q1305598
  wikipedia: Optimal facility location
history:
  posed_by: "A. A. Kuehn and M. J. Hamburger"
  first_stated: "1963"
  notes: "The discrete plant location problem was introduced independently in the early 1960s by Stollsteimer, Kuehn and Hamburger, Manne, and Balinski; the attribution is to the earliest well-documented journal formulation. The continuous version with one facility goes back to the Fermat–Weber problem."
---

## Problem

Let $F$ be a finite set of possible facilities and $C$ a finite set of clients.
Opening facility $i$ costs $f_i \ge 0$, and serving client $j$ from facility $i$ costs $c_{ij} \ge 0$.
The *uncapacitated facility location problem* asks for a nonempty set $S \subseteq F$ of open facilities that minimizes
$$\sum_{i \in S} f_i + \sum_{j \in C} \min_{i \in S} c_{ij}.$$
In the *metric* version, $F \cup C$ carries a metric $c$, so that the costs $c_{ij}$ satisfy the [[triangle inequality|03HF5PMY5T]].

## Remarks

The problem is [[NP-hard|MHA48AWBXN]], since it contains the [[set cover problem|XXRXVA6RBZ]].
Each set becomes a facility with opening cost $1$, and client $u$ costs $0$ to serve from a set containing $u$ and a very large amount otherwise.
Without the metric condition, the best possible approximation ratio in polynomial time is of order $\log \abs{C}$, as for set cover.
The metric version has constant-factor [[approximation algorithms|4WEVBDQ8SR]], based on linear programming rounding, primal-dual methods, greedy rules and local search.
Close variants fix the number $k$ of open facilities: the $k$-median problem minimizes the total service cost, and the $k$-center problem minimizes the largest service cost.
In the continuous version, facilities may be placed anywhere in the plane; with one facility and Euclidean distances, this is the [[Weber problem|6C31TY8W2Y]].

## Explanations

### L1 human

A chain wants to open warehouses to supply its shops.
Each warehouse has a building cost, and shipping to a shop costs more the farther away the warehouse is.
Opening many warehouses makes shipping cheap but building expensive, and opening few does the opposite.
The problem asks for the best balance.
For example, with two shops far apart and cheap buildings, one warehouse next to each shop is best; with very expensive buildings, a single warehouse is best.
