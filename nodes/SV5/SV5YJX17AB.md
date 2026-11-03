---
tag: SV5YJX17AB
kind: definition
name: Holling functional response
msc: [92D40, 92D25]
defines: KRBTBHGC5K
uses: [1YEMFQ1H32]
sources:
  - url: https://en.wikipedia.org/wiki/Functional_response
---

## Definition

In a predator–prey [[population model|1YEMFQ1H32]], the *functional response* is a function $f \colon [0, \infty) \to [0, \infty)$.
Its value $f(N)$ is the number of prey eaten per predator per unit of time when the prey density is $N$.
Let $a > 0$ be the attack rate and $h > 0$ the handling time per prey item.
The *Holling functional responses* are:

1. type I: $f(N) = a N$, often capped at a maximal value;
2. type II: $f(N) = \dfrac{a N}{1 + a h N}$;
3. type III: $f(N) = \dfrac{a N^2}{1 + a h N^2}$.

## Remarks

Example: the type II response with $a = 2$ and $h = 0.5$ is $f(N) = 2N/(1 + N)$; it is increasing, $f(0) = 0$, and $f(N) \to 1/h = 2$ as $N \to \infty$, so it saturates at the rate $1/h$.
Type II follows if a predator spends time $h$ handling each prey and searches at rate $a$ in the rest of its time.
It has the same form as the Michaelis–Menten law of enzyme kinetics.
Type III is sigmoid: $f(N) / N \to 0$ as $N \to 0$, so the risk for each prey is small when prey are rare.
Non-example: $f(N) = 2 - N$ is not a functional response on $[0, \infty)$, since it becomes negative for $N > 2$.
