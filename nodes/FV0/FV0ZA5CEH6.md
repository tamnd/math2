---
tag: FV0ZA5CEH6
kind: example
name: The three-valued Post logic defines Łukasiewicz negation
msc: ["03B50"]
topics: [WZP584JQ06]
audience: research
instance_of: [YHYSGRE7JV]
illustrates: [8P3Y6T0RZS]
uses: [PHGRJ2D97H, 8P3Y6T0RZS]
sources:
  - url: https://en.wikipedia.org/wiki/Many-valued_logic
    locator: Post logics Pm
---

## Example

Take $m = 3$ in [[Post's logic|PHGRJ2D97H]], with the labels $0, 1, 2$ for the values $0, \tfrac12, 1$.
Negation is $\neg 0 = 2$, $\neg 1 = 0$ and $\neg 2 = 1$, and the shift $S = \neg\neg$ is $S0 = 1$, $S1 = 2$ and $S2 = 0$.
We build a term in $\neg$ and $\lor$ for the Łukasiewicz negation $f(x) = 2 - x$, which has the table $f(0) = 2$, $f(1) = 1$, $f(2) = 0$.
We follow [[the completeness proof|FR9JC8MNBJ]].

1. Put $M(x) = \max(x, Sx)$.
   Its table is $M(0) = 1$, $M(1) = 2$ and $M(2) = 2$.
2. Put $J_0(x) = S(M(x))$, the test for the value $0$.
   Its table is $J_0(0) = S(1) = 2$, $J_0(1) = S(2) = 0$ and $J_0(2) = S(2) = 0$.
3. Put $J_1(x) = J_0(S^2 x) = J_0(\neg x)$, the test for the value $1$.
   Its table is $J_1(0) = J_0(2) = 0$, $J_1(1) = J_0(0) = 2$ and $J_1(2) = J_0(1) = 0$.
4. The inputs with a nonzero output are $0$ and $1$.
   So we try $t(x) = \max(K_2(J_0 x), K_1(J_1 x))$, where $K_c(e) = S(\max(S^c e, J_0 e))$ lowers a test value to $c$.
5. Compute $K_2$ on the two test values.
   We get $K_2(2) = S(\max(1, 0)) = 2$ and $K_2(0) = S(\max(2, 2)) = 0$.
6. Compute $K_1$ on the two test values.
   We get $K_1(2) = S(\max(0, 0)) = 1$ and $K_1(0) = S(\max(1, 2)) = 0$.
7. Evaluate $t$ at the three inputs.
   At $x = 0$ the tests are $J_0 = 2$ and $J_1 = 0$, so $t(0) = \max(K_2(2), K_1(0)) = \max(2, 0) = 2$.
   At $x = 1$ the tests are $J_0 = 0$ and $J_1 = 2$, so $t(1) = \max(K_2(0), K_1(2)) = \max(0, 1) = 1$.
   At $x = 2$ both tests are $0$, so $t(2) = \max(K_2(0), K_1(0)) = 0$.

So $t$ gives $2, 1, 0$ at $0, 1, 2$, and $t = f$.

## Remarks

The example shows that Post's negation, which turns the values in a circle, can produce the order-reversing negation of Łukasiewicz.
The two negations are different functions, since Post's sends $1$ to $0$ and Łukasiewicz's fixes $1$.
Completeness says that each one is a term in the other connectives, and the steps above make this concrete for one direction.

The same recipe gives every other table.
For the constant $1$, use $K_1(J_0 x) \lor K_1(J_1 x) \lor K_1(J_2 x)$ with $J_2(x) = J_0(S x)$.
Exactly one test is $2$ at each input, so exactly one disjunct is $1$ and the others are $0$.
Łukasiewicz implication, a function of two variables, is built in the same way from tests in two variables.

The term is long, because the proof aims at existence, not at short formulas.

## Explanations

### L1 human

Post's "not" turns the three values around in a circle.
With "not" and "or" we build one formula that is high exactly at $0$, and one that is high exactly at the middle value.
Then we lower each formula to the output that we want and join them with "or".
The result reverses the three values, which is Łukasiewicz's "not".

### L2 human

The recipe has three steps.
First compute the shift $S$ and the tests $J_a$ as tables.
Then, for each input with a nonzero output, scale its test down to that output with $K_c$.
Finally, join the scaled tests with $\lor$ and check every input, as in step 7.
This is the typical use of the completeness proof: it turns an existence result into an explicit formula.
Watch out: $K_c$ gives the right answer only on the inputs $0$ and $m - 1$.
For example $K_1(1) = S(\max(2, 0)) = 0$, not $1$, so apply $K_c$ to tests and never to arbitrary values.
