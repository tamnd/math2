---
tag: 24D1EGHP4G
kind: statement
role: proposition
name: Expansion of iterated differences in shifts
msc: [39A70, 05A10]
uses: [E38801KVJ1, 91QMF4R1CY, 092GEF38YD]
about: [3039GWNHWS]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_difference
---

## Statement

Let $M$ be an additive commutative monoid, let $G$ be an additive abelian group, let $h \in M$, and let $f \colon M \to G$ be a function.
Let $\Delta_h^n f$ be the [[$n$-th forward difference|E38801KVJ1]] of $f$ with step $h$.
Then for every $n \in \N$ and every $x \in M$,
$$\Delta_h^n f(x) = \sum_{k=0}^{n} (-1)^{n-k} \binom{n}{k} f(x + kh),$$
where $\binom{n}{k}$ is the [[binomial coefficient|092GEF38YD]].

## Remarks

Write $\Delta_h = E_h - I$, where $E_h$ is the [[shift operator|91QMF4R1CY]] and $I$ is the identity.
The operators $E_h$ and $I$ commute, so the [[binomial theorem|0EHWPWGHB2]] gives $(E_h - I)^n = \sum_k \binom{n}{k} (-1)^{n-k} E_h^k$, and $E_h^k f(x) = f(x + kh)$.
A direct proof is an induction on $n$ with Pascal's rule.
Example: for $n = 3$ the formula reads $\Delta_h^3 f(x) = f(x + 3h) - 3f(x + 2h) + 3f(x + h) - f(x)$.
With $f(x) = x^3$, $h = 1$ and $x = 0$ this gives $27 - 24 + 3 - 0 = 6 = 3!$.

## Explanations

### L1 human

The $n$-th difference of a function can be computed in one step from $n + 1$ equally spaced values.
The weights are the binomial coefficients with alternating signs, as in a row of Pascal's triangle.
For example, the second difference is $f(x + 2h) - 2f(x + h) + f(x)$.

### L2 human

The formula is the inverse of [[Newton's forward difference formula|DDHCMKHD2T]], which writes shifted values in terms of differences.
Together the two formulas say that the sequences $(f(x + kh))_k$ and $(\Delta_h^k f(x))_k$ are each other's binomial transform.
The second difference $f(x + h) - 2f(x) + f(x - h)$, divided by $h^2$, is the standard finite difference approximation of $f''(x)$.
Combined with the fact that [[differences of polynomials vanish beyond the degree|EFYGR426DF]], it gives identities.
An example is $\sum_{k=0}^n (-1)^k \binom{n}{k} k^m = 0$ for $0 \le m < n$.
