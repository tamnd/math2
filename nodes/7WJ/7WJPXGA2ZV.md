---
tag: 7WJPXGA2ZV
kind: example
name: The recursive sequence h with h(n + 1) = 2h(n) + 1
msc: ["00A35", "11B37"]
topics: [EEH2F76CYQ]
audience: school
instance_of: [AM4GQQMZ3C]
uses: [AM4GQQMZ3C, 0ASJVEFA9J, 0DSHAVH45F]
sources:
  - url: https://en.wikipedia.org/wiki/Tower_of_Hanoi
    locator: Recursive solution
  - url: https://en.wikipedia.org/wiki/Recursive_definition
    locator: Form of recursive definitions
---

## Example

Define a sequence $(h_n)_{n \ge 0}$ of natural numbers by a [[recursive definition|AM4GQQMZ3C]]:
$$h_0 = 0, \qquad h_{n+1} = 2 h_n + 1 \quad \text{for } n \ge 0.$$
The base gives one value, and the rule uses only the value just before, so one start value is enough.
By the recursion theorem, which underlies [[definition by recursion|0DSHAVH45F]], exactly one sequence satisfies these two equations.

We compute the first terms from the rule and compare them with the powers of $2$.

| $n$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ |
|---|---|---|---|---|---|---|---|
| $h_n$ | $0$ | $1$ | $3$ | $7$ | $15$ | $31$ | $63$ |
| $2^n - 1$ | $0$ | $1$ | $3$ | $7$ | $15$ | $31$ | $63$ |

For example, $h_3 = 2 h_2 + 1 = 2 \cdot 3 + 1 = 7$ and $h_4 = 2 \cdot 7 + 1 = 15$.
The table suggests the closed form $h_n = 2^n - 1$, and we prove it by [[mathematical induction|0ASJVEFA9J]] on $n$.

1. Let $P(n)$ be the statement "$h_n = 2^n - 1$".
2. Base case: $h_0 = 0$ by the definition, and $2^0 - 1 = 1 - 1 = 0$.
   So $P(0)$ holds.
3. Induction step: let $n \ge 0$, and assume $P(n)$, that is, $h_n = 2^n - 1$.
4. The rule of the definition and the assumption give
   $$h_{n+1} = 2 h_n + 1 = 2(2^n - 1) + 1 = 2^{n+1} - 2 + 1 = 2^{n+1} - 1.$$
5. So $P(n + 1)$ holds.
6. By induction, $h_n = 2^n - 1$ for each natural number $n$.

## Remarks

The sequence counts the minimum number of moves in the [[Tower of Hanoi|0906Z03EMN]] with $n$ discs.
The rule comes from the largest disc: move the $n$ smaller discs away, move the largest disc, and move the $n$ smaller discs back, for $h_n + 1 + h_n$ moves.

The proof has the same shape as the definition.
Its base case uses the base of the definition, and its induction step uses the rule.
This match is typical of proofs about recursively defined sequences.

Change the start value to $h_0 = c$, and the same rule gives $h_n = 2^n (c + 1) - 1$.
The step is the same calculation:
$$2\big(2^n(c + 1) - 1\big) + 1 = 2^{n+1}(c + 1) - 1.$$
Check: for $n = 0$ the formula gives $(c + 1) - 1 = c$.
Change the rule to $h_{n+1} = 2 h_n$ instead, and the start $h_0 = 0$ gives the zero sequence, so the added $1$ is what makes the sequence grow.

## Explanations

### L1 human

Start with $0$, and to get the next number, double the last one and add $1$.
This gives $0$, $1$, $3$, $7$, $15$, $31$.
Each of these is one less than a power of $2$: $1 - 1$, $2 - 1$, $4 - 1$, $8 - 1$, and so on.
Induction shows that this pattern never breaks.
If a number is one less than a power of $2$, then doubling it and adding $1$ gives one less than the next power of $2$.

### L2 human

Let us guess and prove a closed form for a related recursion, $g_0 = 1$ and $g_{n+1} = 3 g_n - 2$.
The first terms are $g_0 = 1$, $g_1 = 3 - 2 = 1$ and $g_2 = 1$, so the sequence looks constant.
The claim $g_n = 1$ has the base $g_0 = 1$, and the step: if $g_n = 1$, then $g_{n+1} = 3 \cdot 1 - 2 = 1$.
So $g_n = 1$ for each $n$, by induction.

With the start value $g_0 = 2$ instead, the terms are $2, 4, 10, 28$, and the closed form is $g_n = 3^n + 1$.
The step is
$$3(3^n + 1) - 2 = 3^{n+1} + 1.$$
That is the typical use of a recursive definition: compute some terms, guess a closed form, and prove it by induction.
Watch out: a table of finitely many values never proves a formula for all $n$, so the proof is not optional.
