---
tag: 0KJVQV3E0F
kind: statement
role: theorem
name: A polynomial over a field has at most as many roots as its degree
msc: ["12E05"]
uses: [0K3MWA7DMC, 0T233AZ1GE, 03XVP8Q4GY]
sources:
  - url: https://en.wikipedia.org/wiki/Polynomial
    locator: Solving equations
---

## Statement

Let $K$ be a [[field|0QA8CHH8MG]] and let $f \in K[x]$ be a nonzero polynomial of [[degree|0DPF6WRZW6]] $n$.
Then $f$ has at most $n$ roots in $K$.
More precisely, the sum of the [[multiplicities|03XVP8Q4GY]] of the roots of $f$ in $K$ is at most $n$.

## Remarks

The proof is an induction on $n$ with the [[factor theorem|0K3MWA7DMC]]: a root $c$ gives $f = (x - c) g$ with $\deg g = n - 1$.
The same statement holds over every [[integral domain|09S3PFBEPM]].
It fails without this hypothesis: in $\mathbb{Z}/8\mathbb{Z}$, the polynomial $x^2 - 1$ has the four roots $1, 3, 5, 7$.

## Explanations

### L1 human

A polynomial of degree $2$ over the real numbers has at most two roots.
In general, each root takes away one linear factor, and you can do this at most $n$ times.
Strange rings like $\mathbb{Z}/8\mathbb{Z}$ can break this rule, because they have zero divisors.
