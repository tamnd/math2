---
tag: SVGN0QKE2C
kind: definition
name: Homogeneous and inhomogeneous linear recurrences
msc: [39A06, 39A05]
defines: 8Y28JQB0Q5
uses: [07TZV87Y0T, 0G9EKM0E15]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_recurrence_with_constant_coefficients
---

## Definition

Let $K$ be a field and let $d \ge 1$ be an integer.
Let $a_0, \dots, a_{d-1} \colon \N \to K$ and $g \colon \N \to K$ be [[sequences|0G9EKM0E15]].
A linear recurrence of order $d$ is the [[recurrence relation|07TZV87Y0T]]
$$u_{n+d} + a_{d-1}(n)\, u_{n+d-1} + \cdots + a_0(n)\, u_n = g(n) \qquad (n \in \N)$$
for a sequence $u \colon \N \to K$.
The sequence $g$ is its right-hand side.

1. The recurrence is *homogeneous* if $g(n) = 0$ for all $n$.
2. The recurrence is *inhomogeneous* if $g(n) \ne 0$ for some $n$.
3. The *associated homogeneous recurrence* is the one with the same $a_0, \dots, a_{d-1}$ and with $g$ replaced by $0$.

## Remarks

Example: $u_{n+1} - 2 u_n = 1$ is inhomogeneous of order $1$, with $a_0(n) = -2$ and $g(n) = 1$.
Its associated homogeneous recurrence is $u_{n+1} - 2 u_n = 0$, whose solutions are $c\, 2^n$.
Non-example: $u_{n+1} = u_n^2 + 1$ is not a linear recurrence at all, since the term $u_n^2$ is not linear in $u_n$; so it is neither homogeneous nor inhomogeneous in this sense.
When all $a_i$ are constant, the homogeneous case is a [[linear recurrence with constant coefficients|081THG13JZ]].
Other names are homogeneous and nonhomogeneous linear difference equations.
The difference of two solutions of the inhomogeneous recurrence solves the associated homogeneous one.
