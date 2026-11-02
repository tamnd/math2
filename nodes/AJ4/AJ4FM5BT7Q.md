---
tag: AJ4FM5BT7Q
kind: definition
name: Periodic sequence
msc: [39A23, 11B83]
defines: Q3B6K9HYRG
uses: [0G9EKM0E15]
sources:
  - url: https://en.wikipedia.org/wiki/Periodic_sequence
---

## Definition

Let $S$ be a set and let $(x_n)_{n \ge 0}$ be a [[sequence|0G9EKM0E15]] of elements of $S$.
The sequence is *periodic* if there is an integer $p \ge 1$ such that
$$x_{n+p} = x_n \quad \text{for all } n \ge 0.$$
Such a $p$ is a *period* of the sequence, and the smallest such $p$ is its *least period*.

## Remarks

Example: $x_n = (-1)^n$ in $\R$ satisfies $x_{n+2} = (-1)^n (-1)^2 = x_n$ for all $n$, so it is periodic, with least period $2$ since $x_1 \ne x_0$.

Non-example: $x_n = n$ is not periodic, since $x_{n+p} = n + p \ne x_n$ for every $p \ge 1$.

The sequence is *eventually periodic* if the condition holds for all $n \ge n_0$ for some $n_0$; for example $0, 1, 1, 1, \dots$ is eventually periodic but not periodic.
Every period is a multiple of the least period.
The same definition applies to two-sided sequences $(x_n)_{n \in \Z}$, with the condition required for all $n \in \Z$.
