---
tag: C0AKF92CWH
kind: definition
name: Error of best approximation
msc: [41A50, 41A25, 41A10]
defines: YDN0T4MEX0
uses: [03J5RAKB30, 04KFTA34C5, 7N4988HN3P, 1G0B73WPX8]
sources:
  - url: https://en.wikipedia.org/wiki/Approximation_theory
---

## Definition

Let $X$ be a [[normed vector space|03J5RAKB30]], let $A \subseteq X$ be nonempty, and let $x \in X$.
The *error of best approximation* of $x$ from $A$ is the [[infimum|04KFTA34C5]]
$$E(x, A) = \inf_{a \in A} \norm{x - a}.$$
In particular, for a continuous $f \colon [a, b] \to \R$ with the supremum norm and the set $\mathcal{P}_n$ of real [[polynomial functions|1G0B73WPX8]] of degree at most $n$,
$$E_n(f) = \inf_{p \in \mathcal{P}_n} \max_{a \le x \le b} \abs{f(x) - p(x)}.$$

## Remarks

Example: for $f(x) = x^2$ on $[0, 1]$ one has $E_1(f) = 1/8$.
The line $p(x) = x - 1/8$ gives $\abs{x^2 - x + 1/8} \le 1/8$ on $[0, 1]$, and no line does better, because the error of $p$ takes the values $1/8, -1/8, 1/8$ at $0, 1/2, 1$.

Non-example: the error of a particular approximation is in general larger.
The line $x$ has error $\max_{[0, 1]} \abs{x^2 - x} = 1/4$, which is not $E_1(f)$.

$E(x, A) = 0$ if and only if $x$ lies in the closure of $A$.
The infimum equals $\norm{x - a^*}$ when $a^*$ is a [[best approximation|7N4988HN3P]].
Since $\mathcal{P}_0 \subseteq \mathcal{P}_1 \subseteq \cdots$, the sequence $E_n(f)$ is nonincreasing.
