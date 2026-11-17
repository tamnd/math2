---
tag: 9EB4DXQMWK
kind: example
name: The infinite pigeonhole principle for two colors is provable in RCA0
msc: ["03B30", "05D10"]
topics: [BY8AAFN7C5]
audience: grad
instance_of: [7SQS69T17R, XQENB067R3]
uses: [7SQS69T17R, DNXCKXZZ08, 0FS3RHF6KE]
sources:
  - url: https://en.wikipedia.org/wiki/Pigeonhole_principle
    locator: Infinite sets
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Base system RCA0
---

## Example

Let $\mathrm{RT}^1_2$ be the [[infinite pigeonhole principle|0FS3RHF6KE]] for two colors, as a sentence of $L_2$: for every function $c \colon \N \to \set{0, 1}$ there are $i < 2$ and a set $H$ with $\forall n\, \exists m > n\, (m \in H)$ and $c(m) = i$ for all $m \in H$.
We check that [[RCA0|DNXCKXZZ08]] proves $\mathrm{RT}^1_2$.

1. Fix $c$. By the law of excluded middle, either (a) $\forall n\, \exists m > n\, c(m) = 0$, or (b) $\exists n\, \forall m > n\, c(m) = 1$.
2. Case (a). The formula $c(m) = 0$ is $\Sigma^0_0$ in the parameter $c$, so $\Delta^0_1$ comprehension gives $H = \set{m : c(m) = 0}$.
3. By (a), $H$ is infinite, and $c(m) = 0$ for all $m \in H$.
4. Case (b). Fix such an $n$. $\Delta^0_1$ comprehension gives $H = \set{m : m > n}$.
5. $H$ is infinite, since $m + 1 > m$ for all $m$, and $c(m) = 1$ for all $m \in H$ by (b).
6. In both cases the conclusion holds, and no induction was used.

## Remarks

The result is a reverse mathematics classification at the lowest level: no set existence beyond $\Delta^0_1$ comprehension is needed.
The proof is not uniform: it does not compute the color $i$ from $c$.
The same proof works for each fixed number $k$ of colors, by induction on $k$ outside the formal system.
The statement $\forall k\, \mathrm{RT}^1_k$, with $k$ a variable, is not provable in $\mathsf{RCA}_0$; Hirst showed that it is equivalent over $\mathsf{RCA}_0$ to the bounding scheme $\mathrm{B}\Sigma^0_2$.

## Explanations

### L1 human

Color each natural number red or blue.
Either red occurs again and again, or from some point on all numbers are blue.
In both cases there is an infinite set of numbers with one color.
The set is described simply, so the weak base system proves that it exists.

### L2 human

The choice between the cases uses classical logic, not a computation.
For a computable coloring, the set $H$ is computable in both cases, so it exists in the $\omega$-model of the computable sets.
A trap is to use the set of all $n$ such that some $m > n$ has $c(m) = 0$: this set is $\Sigma^0_1$, and $\mathsf{RCA}_0$ does not prove that it exists.
