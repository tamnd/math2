---
tag: 1CF72TCVD2
kind: definition
name: Graph of an operator
msc: [47A05]
defines: 3RCAY97W1E
uses: [KRJX5RA0PW, 0JBJYT69ZV, 00YC1D652K]
sources:
  - url: https://en.wikipedia.org/wiki/Unbounded_operator
    locator: Definitions and basic properties
---

## Definition

Let $X$ and $Y$ be normed spaces, and let $T$ be an [[unbounded operator|KRJX5RA0PW]] from $X$ to $Y$ with domain $D(T)$.
The *graph* of $T$ is the set
$$\Gamma(T) = \set{(x, Tx) : x \in D(T)} \subseteq X \times Y.$$
The product $X \times Y$ carries the norm $\norm{(x, y)} = \norm{x} + \norm{y}$, or any equivalent norm.

## Remarks

It is the [[graph|0JBJYT69ZV]] of the function $T \colon D(T) \to Y$.
Since $T$ is linear, $\Gamma(T)$ is a [[linear subspace|00YC1D652K]] of $X \times Y$.

Example: for $X = Y = \R$ and $Tx = 3x$ with $D(T) = \R$, the graph is the line $\set{(x, 3x) : x \in \R}$.

Non-example: the subspace $\set{(0, y) : y \in \R}$ of $\R \times \R$ is not the graph of any operator, since it contains $(0, 1)$, while every graph contains only $(0, 0)$ above $x = 0$.

A linear subspace $G$ of $X \times Y$ is the graph of an operator if and only if $(0, y) \in G$ implies $y = 0$.
Then $D(T)$ is the projection of $G$ onto $X$, and $Tx$ is the unique $y$ with $(x, y) \in G$.
In this way $S \subseteq T$ holds exactly when $\Gamma(S) \subseteq \Gamma(T)$.
