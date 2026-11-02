---
tag: T4EPFGAQ8C
kind: definition
name: Topological data analysis
msc: [62R40, 55N31]
defines: FETY7R4X86
uses: [0VKD1TP7F3, V8GZ0W1ZZ5, S8SNBHVPSP]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_data_analysis
---

## Definition

*Topological data analysis* is the analysis of data by topological invariants computed through the following steps.

1. The data are a finite set $X = \set{x_1, \dots, x_n}$ in a [[metric space|0VKD1TP7F3]] $(M, d)$.
2. A filtration of [[simplicial complexes|V8GZ0W1ZZ5]] $(K_r)_{r \ge 0}$ is built on $X$, with $K_r \subseteq K_s$ for $r \le s$.
   A standard choice is the Vietoris–Rips complex: its simplices at scale $r$ are the nonempty subsets of $X$ of diameter at most $r$.
3. The [[persistent homology|S8SNBHVPSP]] of the filtration, in each degree $k$ with coefficients in a field, is computed and summarised by a barcode or persistence diagram.
4. Statistical conclusions are drawn from these summaries, for example by comparing them with the bottleneck distance.

## Remarks

The stability theorem gives the summaries a statistical meaning.
For two finite metric spaces, the persistence diagrams of their Vietoris–Rips filtrations are at bottleneck distance at most twice their Gromov–Hausdorff distance.

Example: let $X$ be the $n \ge 4$ vertices of a regular $n$-gon in $\R^2$, with side length $a$ and with length $b > a$ of the diagonals that skip one vertex.
For $a \le r < b$, the Vietoris–Rips complex $K_r$ has an edge between consecutive vertices only, and no triangle, since any three vertices include two that are not consecutive.
So $K_r$ is the $n$-cycle graph, a circle, and its first homology has rank $1$; the bar in degree $1$ that is born at $a$ detects the circle.

Non-example: computing the mean and covariance of $X$ is not topological data analysis, since it uses no filtration and no topological invariant.
