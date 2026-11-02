---
tag: ND1CBJS6V2
kind: definition
name: Holonomic sequence
msc: [39A06, 33F10, 05A15]
defines: NWKX329T01
uses: [K6QV4WSTXX, 0G9EKM0E15]
sources:
  - url: https://en.wikipedia.org/wiki/Holonomic_function
---

## Definition

Let $K$ be a field.
A [[sequence|0G9EKM0E15]] $u \colon \N \to K$ is *holonomic* (or *P-recursive*) if it satisfies some [[linear recurrence with polynomial coefficients|K6QV4WSTXX]].
That is, there are an integer $r \ge 0$ and polynomials $p_0, \dots, p_r \in K[n]$, not all zero, with
$$p_r(n)\, u_{n+r} + \cdots + p_0(n)\, u_n = 0 \quad \text{for all } n \in \N.$$

## Remarks

Example: the factorials $u_n = n!$ form a holonomic sequence over $\Q$, with $r = 1$, $p_1 = 1$ and $p_0 = -(n + 1)$, since $(n+1)! - (n+1) \cdot n! = 0$.
Non-example: $u_n = 2^{n^2}$ over $\Q$ is not holonomic.
Indeed, take a recurrence as above with $p_r \ne 0$ and the other $p_i$ of degree at most $f$.
It gives $\abs{u_{n+r}} \le C n^{f} \max_{i < r} \abs{u_{n+i}}$ for large $n$ and some constant $C$.
So $\log \abs{u_n}$ grows at most like a constant times $n \log n$, while $\log 2^{n^2} = n^2 \log 2$.
Over a field of characteristic $0$, $u$ is holonomic if and only if its generating function $\sum u_n x^n$ is a [[holonomic function|7H44JD9NQD]].
Every solution of a linear recurrence with constant coefficients is holonomic.
