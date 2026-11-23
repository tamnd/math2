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

Let $\mathrm{RT}^1_2$ be the [[infinite pigeonhole principle|0FS3RHF6KE]] for two colors, as a sentence of $L_2$.
It says: for every function $c \colon \mathbb{N} \to \{0, 1\}$ there are $i < 2$ and an infinite set $H$ with $c(m) = i$ for all $m \in H$.
Here "$H$ is infinite" is the formula $\forall n \, \exists m > n \, (m \in H)$.
We check that [[RCA0|DNXCKXZZ08]] proves $\mathrm{RT}^1_2$.

1. Fix $c$.
   By the law of excluded middle, either (a) $\forall n \, \exists m > n \, c(m) = 0$, or (b) $\exists n \, \forall m > n \, c(m) = 1$.
2. In case (a), the formula $c(m) = 0$ is $\Sigma^0_0$ in the parameter $c$, so $\Delta^0_1$ comprehension gives $H = \{ m : c(m) = 0 \}$.
   By (a), $H$ is infinite, and $c(m) = 0$ for all $m \in H$.
3. In case (b), fix such an $n$.
   $\Delta^0_1$ comprehension gives $H = \{ m : m > n \}$, which is infinite since $m + 1 > m$ for every $m$.
   By (b), $c(m) = 1$ for all $m \in H$.
4. In both cases the conclusion holds, and the proof used no induction at all.

## Remarks

The result is a classification at the lowest level: no set existence beyond $\Delta^0_1$ comprehension is needed.
For a computable coloring, the set $H$ is computable in both cases, so it lies in the $\omega$-model of the computable sets.

The proof is not uniform.
It does not compute the color $i$ from $c$, because deciding between (a) and (b) asks a $\Pi^0_2$ question about $c$.
For the coloring with $c(m) = 1$ for $m \ge 10$ and $c(m) = 0$ below, case (b) holds with $n = 9$, but no finite part of $c$ reveals that it never turns back to $0$.

What changes with more colors?
The same proof works for each fixed number $k$ of colors, by an induction on $k$ outside the formal system.
The statement $\forall k \, \mathrm{RT}^1_k$, with $k$ a variable, is not provable in $\mathsf{RCA}_0$.
Hirst showed that it is equivalent over $\mathsf{RCA}_0$ to the bounding scheme $\mathrm{B}\Sigma^0_2$.
With pairs in place of single numbers, the principle becomes [[Ramsey's theorem for pairs|ZT5KV6KJ3E]], which is far stronger.

## Explanations

### L1 human

Color each natural number red or blue.
Either red occurs again and again, or from some point on all numbers are blue.
In both cases there is an infinite set of numbers of one color: all the red numbers, or all the numbers after the last red one.
These sets have simple descriptions, so the weak base system proves that they exist.

### L2 human

The choice between the cases uses classical logic, not a computation.
That is allowed: $\mathsf{RCA}_0$ is a classical theory, and it only restricts which sets exist.

Watch out: a tempting proof uses the set of all $n$ such that some $m > n$ has $c(m) = 0$.
That set is defined by a $\Sigma^0_1$ formula, and $\mathsf{RCA}_0$ does not prove that every such set exists.
The proof above avoids it, and uses only sets that $c$ decides directly.
