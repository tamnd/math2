---
tag: X0J9RZTSYW
kind: problem
name: Vehicle routing problem
msc: [90B06, 90C27, 90B10]
uses: [FJPER80BJC, XJRHJX2241, MHA48AWBXN]
about: [FJPER80BJC]
sources:
  - url: https://en.wikipedia.org/wiki/Vehicle_routing_problem
same_as:
  wikidata: Q944041
  wikipedia: Vehicle routing problem
history:
  posed_by: "George Dantzig and John Ramser"
  first_stated: "1959"
  notes: "Dantzig and Ramser called it the truck dispatching problem."
---

## Problem

Let $0$ be a depot and $1, \dots, n$ be customers.
Customer $i$ has a demand $q_i > 0$, and the cost of travel from $i$ to $j$ is $c_{ij} \ge 0$, for $i, j \in \set{0, \dots, n}$.
There are $K$ vehicles, each of capacity $Q \ge \max_i q_i$.
A *route* is a cycle that starts and ends at the depot and visits some customers once each.
Its load is the sum of the demands of its customers, and its cost is the sum of the costs $c_{ij}$ of its legs.
The *capacitated vehicle routing problem* asks for at most $K$ routes of least total cost with two conditions.
Each customer lies on exactly one route, and each route has load at most $Q$.

## Remarks

With one vehicle and $Q \ge \sum_i q_i$, the problem is the [[travelling salesman problem|XJRHJX2241]] on the depot and the customers.
So the vehicle routing problem is [[NP-hard|MHA48AWBXN]].
In practice it is attacked by heuristics, such as the savings method of Clarke and Wright, and by exact branch-and-cut and branch-and-price methods for moderate sizes.
Many variants exist.
Customers may have time windows, vehicles may differ, goods may be picked up and delivered, or demands may be random.

## Explanations

### L1 human

A delivery company has a warehouse, a fleet of trucks of limited size, and a list of shops with orders.
It must plan a round trip for each truck so that every shop gets its goods and the total driving is as small as possible.
For example, if one truck can carry $10$ units and four shops each order $5$ units, at least two trucks are needed, each serving two shops.
The question is which shops to group together and in which order to visit them.
This is the travelling salesman problem with the extra choice of splitting the customers among several trucks.
