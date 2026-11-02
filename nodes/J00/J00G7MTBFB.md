---
tag: J00G7MTBFB
kind: definition
name: Order of a difference equation
msc: [39A05]
defines: SNRN446BHC
uses: [07TZV87Y0T]
sources:
  - url: https://en.wikipedia.org/wiki/Recurrence_relation
---

## Definition

Let $X$ be a set and let $(u_n)_{n \ge 0}$ denote an unknown sequence in $X$.
Consider a difference equation of the form
$$F(n, u_n, u_{n+1}, \dots, u_{n+k}) = 0 \qquad (n \ge 0),$$
where $k \ge 0$ is an integer and $F$ is a given function.
The equation has *order* $k$ if $F$ depends on both its second argument $u_n$ and its last argument $u_{n+k}$.
For a [[recurrence relation|07TZV87Y0T]] $u_{n+k} = f(n, u_n, \dots, u_{n+k-1})$ in which $f$ depends on $u_n$, the order is $k$.

## Remarks

Example: $u_{n+3} = u_{n+1} + 2u_n$ has order $3$.
The indices that occur are $n$, $n+1$ and $n+3$, and the largest minus the smallest is $3$.
Non-example: $u_{n+3} = 2u_{n+2}$ looks like order $3$, but $u_n$ does not occur.
After the substitution $v_n = u_{n+2}$ it reads $v_{n+1} = 2v_n$, which has order $1$.
For a linear equation $a_k(n) u_{n+k} + \dots + a_0(n) u_n = b(n)$ the order is $k$ when neither $a_k$ nor $a_0$ is the zero sequence.
