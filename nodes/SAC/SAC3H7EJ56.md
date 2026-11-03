---
tag: SAC3H7EJ56
kind: definition
name: Phylogenetic network
msc: [92D15, 05C90]
defines: Z0MGB0NG6B
uses: [00C0BR7D7H, RK58WSHJSG]
sources:
  - url: https://en.wikipedia.org/wiki/Phylogenetic_network
---

## Definition

Let $X$ be a finite set of taxa.
A *rooted phylogenetic network* on $X$ is a finite directed acyclic [[graph|00C0BR7D7H]] $N$ such that:

1. $N$ has exactly one vertex of in-degree $0$, the *root*, and it has out-degree at least $2$;
2. the vertices of out-degree $0$, the *leaves*, have in-degree $1$ and are labelled bijectively by $X$;
3. every other vertex is a *tree vertex* (in-degree $1$, out-degree at least $2$) or a *reticulation vertex* (in-degree at least $2$, out-degree $1$).

## Remarks

Conventions differ in details; many authors require the network to be binary, with root out-degree $2$, tree vertices of out-degree $2$ and reticulations of in-degree $2$.
Example: on $X = \set{a, b, c}$, take a root $\rho$ with children $u$ and $w$.
Let $u$ have children $a$ and $r$, let $w$ have children $r$ and $c$, and let $r$ have the single child $b$.
Then $r$ is a reticulation vertex, and the network says that $b$ descends from a lineage formed by merging the lineages of $u$ and $w$.
A network with no reticulation vertex is a rooted [[phylogenetic tree|RK58WSHJSG]].
Non-example: a directed graph containing a directed cycle fails the acyclicity requirement, since no taxon can be its own ancestor.
Unrooted phylogenetic networks, such as split networks, are also used, mainly to display conflicting signals in data rather than explicit evolutionary histories.
