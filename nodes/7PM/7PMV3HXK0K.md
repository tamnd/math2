---
tag: 7PMV3HXK0K
kind: example
name: Epsilon substitution for one critical formula
msc: ["03F05"]
topics: [R10RMQCJQX]
audience: grad
instance_of: [F5HTHB46SH]
uses: [TH5ZKCKN3W]
sources:
  - url: https://en.wikipedia.org/wiki/Epsilon_calculus
    locator: Epsilon substitution method
---

## Example

Let $A(x)$ be the equation $x + 1 = 3$ in the language of arithmetic, and let $e$ be the closed term $\varepsilon x\, A(x)$ of the [[epsilon calculus|TH5ZKCKN3W]].
Take the two critical formulas for $e$ with the term $t = 2$.

$$C_1 : \; 2 + 1 = 3 \to e + 1 = 3, \qquad C_2 : \; 2 + 1 = 3 \to \neg (2 < e).$$

We run the [[epsilon substitution method|F5HTHB46SH]].

1. The substitution $S_0$ gives $e$ the value $0$.
2. Under $S_0$, the premise $2 + 1 = 3$ is true. The conclusion of $C_1$ is $0 + 1 = 3$, which is false, so $C_1$ is false.
3. Under $S_0$, the conclusion of $C_2$ is $\neg(2 < 0)$, which is true, so $C_2$ is true.
4. $C_1$ is false, and its premise shows that $2$ is a witness for $A$. We test $m = 0, 1, 2$ in turn: $0 + 1 = 1$, $1 + 1 = 2$ and $2 + 1 = 3$.
5. The least witness is $m = 2$. The substitution $S_1$ gives $e$ the value $2$.
6. Under $S_1$, the conclusion of $C_1$ is $2 + 1 = 3$, which is true.
7. Under $S_1$, the conclusion of $C_2$ is $\neg(2 < 2)$, which is true.
8. So $S_1$ is a solving substitution for $C_1$ and $C_2$, and the process stops after one step.

## Remarks

The example shows the basic step: a false critical formula gives a witness, and the method moves the $\varepsilon$-term to the least witness.
The matrix $A$ has no $\varepsilon$-terms, so the value $2$ never has to change again.
With $t = 5$ in place of $2$, $C_1$ is true under $S_0$, since its premise $5 + 1 = 3$ is false, and the process stops at once.
If the step chose the witness $t = 2$ itself in every case, it would agree with the least witness here, but not in general, and then critical formulas like $C_2$ could stay false.

## Explanations

### L1 human

The term $e$ stands for "the smallest number that gives $3$ when we add $1$".
We first guess $0$ and check: $0 + 1$ is $1$, not $3$, so the guess is wrong.
We know that $2$ works, so we try $0$, $1$ and $2$ in order, and $2$ is the first that works.
We change the guess to $2$, and now every check passes.

### L2 human

To run one step, find a critical formula that is false under the current values.
Its premise names a number that has the property, so the least such number is found by a finite search below it.
Give the $\varepsilon$-term that value, and check all critical formulas again.
Here the search below $2$ took three tests, and after it both $C_1$ and $C_2$ held.
Watch out: fixing one formula is not the end of a step.
With [[nested terms|GHJSNQ4VQW]] a repair can make another critical formula false, so every formula must be checked again.
