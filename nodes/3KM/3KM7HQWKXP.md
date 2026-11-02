---
tag: 3KM7HQWKXP
kind: definition
name: Truncation error
msc: [65G99, 65D25, 65L70]
defines: 4AKCQERM89
uses: [0CTV783HYT, 05M5SWSZZD]
sources:
  - url: https://en.wikipedia.org/wiki/Truncation_error
---

## Definition

Let $A$ be a real number defined as the [[limit|05M5SWSZZD]] of a [[real sequence|0CTV783HYT]] $(A_n)$, or of a family $A(h)$ as $h \to 0$.
Assume that each $A_n$ or $A(h)$ is computable by finitely many arithmetic operations.
The *truncation error* of the approximation $A_n$ is $A - A_n$, and that of $A(h)$ is $A - A(h)$.
Here $A_n$ and $A(h)$ are evaluated in exact arithmetic.

## Remarks

Example: let $f$ have a continuous second derivative and take the forward difference $A(h) = (f(x+h) - f(x))/h$, with limit $A = f'(x)$.
Taylor's theorem gives $A - A(h) = -\tfrac12 f''(\xi) h$ for some $\xi$ between $x$ and $x + h$, so the truncation error is of order $h$.
Example: for $A_n = \sum_{k=0}^{n} 1/k!$ and $A = e$, the truncation error is $\sum_{k > n} 1/k!$, which lies between $1/(n+1)!$ and $2/(n+1)!$ for $n \ge 1$.
Non-example: the difference between $1/3$ and its stored value $0.333$ in three-digit decimal arithmetic is a round-off error, since no limit process is cut off.
