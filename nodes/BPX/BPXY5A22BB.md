---
tag: BPXY5A22BB
kind: definition
name: Interior operator
msc: [06A15]
defines: Z7P561Y2JQ
uses: [011C29Q1S1]
sources:
  - url: https://en.wikipedia.org/wiki/Interior_algebra
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|011C29Q1S1]].
An *interior operator* on $P$ is a map $i \colon P \to P$ such that, for all $x, y \in P$:

1. $i(x) \le x$ (deflationary);
2. if $x \le y$, then $i(x) \le i(y)$ (monotone);
3. $i(i(x)) = i(x)$ (idempotent).

An element $x$ with $i(x) = x$ is *open*.

## Remarks

Let $X$ be a topological space and $P$ the set of subsets of $X$ ordered by inclusion.
The map sending $A$ to its [[interior|0C38S0KMJK]] is an interior operator: the interior lies in $A$, grows with $A$, and is open, so taking it twice changes nothing.
On $\R$, the map $i(x) = x - 1$ is deflationary and monotone but not idempotent, since $i(i(0)) = -2 \ne -1 = i(0)$.
A map $i$ is an interior operator on $P$ if and only if it is a [[closure operator|17FVAN6HXX]] on the [[dual|BS1RD4F5MD]] of $P$.
On a power set, $A \mapsto X \setminus c(X \setminus A)$ is an interior operator for each closure operator $c$.
Other names are kernel operator and dual closure operator.

## Explanations

### L1 human

An interior operator moves each element down to the nearest open element.
Open elements stay where they are.
