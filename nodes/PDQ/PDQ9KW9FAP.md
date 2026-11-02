---
tag: PDQ9KW9FAP
kind: object
name: Unit ball in C^n
msc: [32A10, 32M15]
instance_of: [0YE5868HZB]
sources:
  - url: https://en.wikipedia.org/wiki/Unit_sphere
---

## Description

Let $n \ge 1$.
The *unit ball* of $\C^n$ is
$$\mathbb{B}^n = \set{z \in \C^n : \abs{z_1}^2 + \cdots + \abs{z_n}^2 < 1}.$$
It is the [[open ball|0YE5868HZB]] of radius $1$ about $0$ for the norm $\abs{z} = (\sum_j \abs{z_j}^2)^{1/2}$.
Writing $z_j = x_j + i y_j$, the condition becomes $\sum_j (x_j^2 + y_j^2) < 1$, so $\mathbb{B}^n$ is the Euclidean unit ball of $\R^{2n}$.

## Remarks

Its boundary is the unit sphere $S^{2n-1} = \set{z : \abs{z} = 1}$.
It is a [[Reinhardt domain|WA0SE56FVH]]: if $z \in \mathbb{B}^n$ and $\theta_j \in \R$, then $(e^{i\theta_1} z_1, \dots, e^{i\theta_n} z_n)$ has the same norm, so it lies in $\mathbb{B}^n$.
Every unitary map $U$ of $\C^n$ preserves the norm, so it maps $\mathbb{B}^n$ onto itself.
For $n = 1$ it is the unit disc, and for $n \ge 2$ it is not biholomorphic to the unit [[polydisc|DJBWP7D3M8]], by [[Poincaré's theorem|1NF8T07H9X]].

## Explanations

### L1 human

The unit ball of $\C^n$ is the set of points at distance less than $1$ from the origin.
As a set it is just the round ball of $\R^{2n}$; what is new is that one studies the holomorphic functions on it.
In $\C^2$, the point $(1/2, 1/2)$ is in the ball, since $1/4 + 1/4 < 1$, while $(0.9, 0.9)$ is not.
The ball is very symmetric: its holomorphic automorphisms can move any point of it to the origin.
