---
tag: 2A9PYZ3F4H
kind: concept
name: Branch and price
msc: [90C57, 90C06, 90C10]
specializes: [ZZ7C50WN56]
sources:
  - url: https://en.wikipedia.org/wiki/Branch_and_price
same_as:
  wikidata: Q4956382
  wikipedia: Branch and price
---

## Summary

Branch and price is [[branch and bound|ZZ7C50WN56]] for [[integer programs|9GX3WH5EQF]] with a huge number of variables.
The [[linear programming relaxation|PYMHHM5Z6F]] at each node is solved by [[column generation|X8JZFMSYT1]].
Such formulations, often obtained from [[Dantzig–Wolfe decomposition|VE54BEPVKT]], have strong relaxations but too many columns to list.
The branching rule must be compatible with the pricing problem, so that the pricing problem keeps its structure deep in the tree.
It is a standard method for vehicle routing, crew scheduling and cutting problems.

## Explanations

### L1 human

Some planning problems are best written with one variable for each complete plan, such as each possible route of a delivery van.
There are far too many routes to list, so the routes are generated only when they look useful.
Branch and price uses this route-on-demand trick inside a branch and bound search for whole-number answers.
At each step of the search new routes may be generated again, because the conditions of that step change which routes are useful.
