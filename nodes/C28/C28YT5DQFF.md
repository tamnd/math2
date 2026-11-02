---
tag: C28YT5DQFF
kind: definition
name: Tauberian condition
msc: ["40E05"]
defines: 6ZDP261K7R
uses: [8X25Q4XYMN, 0JH4MN4K1C, 0CVVKY7GY2, 0S4EMDQS2F, 8SK3GQ4S0M]
sources:
  - url: https://en.wikipedia.org/wiki/Abelian_and_Tauberian_theorems
---

## Definition

Let $M$ be a [[summability method|8X25Q4XYMN]] that assigns a value to some [[series|0JH4MN4K1C]] $\sum a_n$ of real or complex numbers.
Let $P$ be a property of sequences $(a_n)_{n \ge 0}$.
The property $P$ is a *Tauberian condition* for $M$ if the following holds.
Every series $\sum a_n$ whose terms have property $P$ and which is $M$-summable to $s$ [[converges|0CVVKY7GY2]] with sum $s$.

## Remarks

Example: for Abel summation, the property $n a_n \to 0$ is a Tauberian condition.
This is [[Tauber's theorem|8SK3GQ4S0M]].
Stronger theorems allow weaker conditions; for example, $n a_n = O(1)$ is a Tauberian condition both for Cesàro summation and for Abel summation.

Non-example: the property $a_n \to 0$ is not a Tauberian condition for Cesàro summation.
Let the partial sums start at $-1$.
For $k = 1, 2, 3, \dots$ in turn, let them run up to $1$ in $k$ steps of size $2/k$ and then back down to $-1$ in $k$ such steps.
The terms are $\pm 2/k$, so $a_n \to 0$.
Over each full up-and-down run the partial sums add up to $0$.
The incomplete last run contributes at most $2k + 2$ in absolute value, while $n$ is at least of order $k^2$.
So the arithmetic means of the partial sums tend to $0$, but the partial sums reach $1$ and $-1$ infinitely often and do not converge.

A theorem whose hypothesis is a Tauberian condition is called a Tauberian theorem.
It is a partial converse of an Abelian theorem such as [[Abel's theorem|0S4EMDQS2F]].
