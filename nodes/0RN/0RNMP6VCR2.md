---
tag: 0RNMP6VCR2
kind: definition
name: Complement graph
msc: [05C76]
defines: 0MCYJ72VGA
uses: [0JD5C82QMB]
sources:
  - url: https://en.wikipedia.org/wiki/Complement_graph
    locator: Definitions
---

## Definition

Let $G = (V, E)$ be a [[graph|0JD5C82QMB]].
The complement of $G$ is the graph $\overline{G}$ with vertex set $V$.
Two distinct vertices are adjacent in $\overline{G}$ if and only if they are not adjacent in $G$.

## Remarks

The complement of the complement of $G$ is $G$.
The complement of the complete graph $K_n$ is the graph on $n$ vertices with no edges.
A [[clique|0G52BPNPKG]] of $G$ is an [[independent set|0KZJ82WEPP]] of $\overline{G}$. This links Ramsey numbers to colourings of $K_n$.

## Explanations

### L1 human

To get the complement, remove all edges of the graph and draw all the missing ones.
If $G$ records which people know each other, then $\overline{G}$ records which people are strangers.
