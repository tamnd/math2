---
tag: SCYW8DVPKQ
kind: definition
name: Design of experiments
msc: [62K99, 62K05]
defines: 2TE42ZWJ3E
uses: [K3AMMSY8DD]
sources:
  - url: https://en.wikipedia.org/wiki/Design_of_experiments
---

## Definition

Let $T$ be a finite set of *treatments* and let $U$ be a finite set of $n$ *experimental units*.
An *experimental design* for $T$ on $U$ is a map $d \colon U \to T$, which assigns treatment $d(u)$ to unit $u$.
The number $r_t = \abs{d^{-1}(t)}$ is the *replication* of treatment $t$.
After the treatments are applied, a response $y_u$ is observed on each unit.
A [[statistical model|K3AMMSY8DD]] relates $y_u$ to the treatment $d(u)$ and to the unit $u$.
*Design of experiments* is the choice of $T$, $U$ and $d$, together with the plan of analysis, before the data are collected.

## Remarks

Example: two diets $T = \set{A, B}$ and four animals $U = \set{1, 2, 3, 4}$.
The map $d(1) = A$, $d(2) = B$, $d(3) = B$, $d(4) = A$ is a design with $r_A = r_B = 2$.

Non-example: in an observational study the units choose their own treatments, for example smokers and non-smokers.
The map $d$ is not chosen by the investigator, so this is not a designed experiment.
Differences in response may then come from other differences between the groups.

For experiments with a quantitative input $x$ in a region $\mathcal{X}$, a design is a choice of the input values $x_1, \dots, x_n \in \mathcal{X}$.
In the approximate theory, it is a probability measure on $\mathcal{X}$ with finite support.
