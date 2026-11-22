---
tag: WFAC541D0V
kind: example
name: A Boolean function of ten variables with no circuit of at most 71 gates
msc: ["68Q06", "68Q17", "00A35"]
topics: [GB14W4SYPK]
audience: ug1
instance_of: [1KVSS0KRZA]
uses: [1KVSS0KRZA, 0X05GS525E, SQXNFGVADX, 4PGX7PHJCK, 2R30KR3Z5G]
sources:
  - url: https://en.wikipedia.org/wiki/Circuit_complexity
    locator: lead section
---

## Example

A [[Boolean function|0X05GS525E]] of $n$ variables is a map $f \colon \{0, 1\}^n \to \{0, 1\}$.
A [[Boolean circuit|SQXNFGVADX]] computes such a function with gates of three types: AND and OR with two inputs, and NOT with one input.
We prove by a [[counting argument|1KVSS0KRZA]] that some Boolean function of $10$ variables has no circuit with at most $71$ gates.

1. Count the functions.
   The set $\{0, 1\}^{10}$ has $2^{10} = 1024$ elements, and each element has $2$ possible values, so there are $2^{1024}$ functions.
2. Describe a circuit with exactly $s$ gates $g_1, \ldots, g_s$.
   Its nodes are the $10$ inputs and the $s$ gates, so there are $10 + s$ nodes.
3. For each gate, give its type ($3$ choices) and two input nodes ($(10 + s)^2$ choices), where a NOT gate ignores its second input.
   Then give the output node ($10 + s$ choices).
4. So there are at most
   $$(10 + s) \cdot \big(3 (10 + s)^2\big)^s$$
   descriptions.
   Some descriptions are not valid circuits, for example those with a cycle of gates, and they only make the bound larger.
5. A circuit with fewer than $s$ gates computes the same function as a circuit with exactly $s$ gates: add unused NOT gates on $x_1$ until there are $s$ gates.
   So every function with a circuit of at most $s$ gates has a description with exactly $s$ gates.
6. With $s = 71$, the number of functions with a circuit of at most $71$ gates is at most $81 \cdot (3 \cdot 81^2)^{71}$.
7. Take base $2$ logarithms.
   Since $3 \cdot 81^2 = 3^9 = 19683$, we have $\log_2 81 \approx 6.340$ and $\log_2 19683 = 9 \log_2 3 \approx 14.265$, so
   $$\log_2\big(81 \cdot 19683^{71}\big) \approx 6.340 + 71 \cdot 14.265 \approx 1019.1.$$
8. Since $2^{1019.1} < 2^{1024}$, the circuits with at most $71$ gates compute fewer functions than exist.
   So some function of $10$ variables needs more than $71$ gates.

## Remarks

The count proves more than existence.
The bound $2^{1019.1}$ is below $2^{1020}$, so at most a fraction $2^{1020}/2^{1024} = 1/16$ of the functions have a circuit with at most $71$ gates.
So more than $15/16$ of the functions of $10$ variables need more than $71$ gates.

The bound stops at $71$.
For $s = 72$ the count is $82 \cdot (3 \cdot 82^2)^{72}$, with base $2$ logarithm about $6.358 + 72 \cdot 14.300 \approx 1036.0$, which is more than $1024$, and the argument gives nothing.
The general form, with circuit size of order $2^n/n$, is [[Shannon's counting argument|2R30KR3Z5G]].
The count also depends on the model: another set of gates changes the factor $3$ and the number of inputs per gate, and so changes the constant $71$.

The proof names no specific function of $10$ variables.
To find one and prove a bound on its [[circuit complexity|4PGX7PHJCK]] is a different and much harder problem.

## Explanations

### L1 human

A rule that takes $10$ yes-or-no answers and gives one yes-or-no answer is a Boolean function.
There are $2^{1024}$ such rules, a number with more than $300$ digits.
A small circuit is a short list of simple steps, and there are not so many short lists.
So the short lists cannot cover all the rules.
Some rule needs a long list of steps, even though nobody can point to it.

### L2 human

We repeat the count for $n = 2$ variables and circuits with at most $s = 1$ gate.
There are $2^{2^2} = 2^4 = 16$ functions of $2$ variables.
With $s = 1$ there are $2 + 1 = 3$ nodes, so the number of descriptions is at most
$$3 \cdot (3 \cdot 3^2)^1 = 81.$$
Since $81 > 16$, the count gives nothing here.
In fact only $6$ functions have a circuit with at most one gate: $x_1$, $x_2$, $\lnot x_1$, $\lnot x_2$, $x_1 \land x_2$ and $x_1 \lor x_2$.

So the crude count of $81$ descriptions is far above the true number $6$.
The method works for large $n$, where $2^{2^n}$ grows much faster than the number of small circuits.
Watch out: for small $n$ the count of descriptions can exceed the number of functions, and then it proves nothing.
