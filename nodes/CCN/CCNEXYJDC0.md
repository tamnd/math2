---
tag: CCNEXYJDC0
kind: example
name: An upward recursion does not define a function
msc: ["00A35"]
topics: [BP0WAF23HB]
audience: ug1
not_instance_of:
  - target: B60DBNF77S
    note: the rule refers to a larger argument, so no recursive definition is given; no function to N and many functions to Z satisfy it
uses: [B60DBNF77S, BQ1D7T0EGD, 0MWKJ44V5A]
sources:
  - url: https://en.wikipedia.org/wiki/Recursive_definition
    locator: Form of recursive definitions
---

## Example

Consider the proposal "let $f \colon \mathbb{N} \to \mathbb{N}$ be the function with $f(n) = f(n + 1) + 1$ for each $n \in \mathbb{N}$".
It looks like a recursive definition, one of the [[kinds of definitions|B60DBNF77S]], but it defines nothing.
First we show that no function into the [[natural numbers|0MWKJ44V5A]] obeys the rule.

1. A recursive definition computes $f(n + 1)$ from values at smaller arguments.
   This rule computes $f(n)$ from the larger argument $n + 1$, so the [[principle of recursive definition|BQ1D7T0EGD]] does not apply.
2. Suppose that some $f \colon \mathbb{N} \to \mathbb{N}$ obeys the rule.
   We show by induction on $k$ that $f(0) = f(k) + k$ for every $k \in \mathbb{N}$.
3. For $k = 0$ the claim reads $f(0) = f(0)$.
4. Suppose $f(0) = f(k) + k$.
   The rule at $n = k$ gives $f(k) = f(k + 1) + 1$, so $f(0) = f(k + 1) + (k + 1)$.
5. Every value $f(k)$ is at least $0$, so step 2 gives $f(0) \ge k$ for every $k$.
   For $k = f(0) + 1$ this says $f(0) \ge f(0) + 1$, which is false.
6. So no function from $\mathbb{N}$ to $\mathbb{N}$ obeys the rule.

Now change the codomain to $\mathbb{Z}$, and the opposite failure appears.

1. For each integer $c$, the function $f_c(n) = c - n$ obeys the rule, because
   $$f_c(n + 1) + 1 = c - (n + 1) + 1 = c - n = f_c(n).$$
2. Different values of $c$ give different functions, since $f_c(0) = c$.
3. So the rule has infinitely many solutions, and "the function with this rule" names none of them.

## Remarks

With codomain $\mathbb{N}$ existence fails, and with codomain $\mathbb{Z}$ uniqueness fails.
Either way the proposal is not a definition.
A rule that gives a base value and computes $f(n + 1)$ from $f(0), \ldots, f(n)$ always defines exactly one function, so the direction of the recursion is what matters.

A rule may refer to other arguments and still be correct, as long as every chain of references ends.
For example, $g(0) = 0$ and $g(n) = g(\lfloor n/2 \rfloor) + 1$ for $n \ge 1$ define $g$, because $\lfloor n/2 \rfloor < n$:
$$g(6) = g(3) + 1 = g(1) + 2 = g(0) + 3 = 3.$$
For the rule $T(1) = 0$, $T(n) = 1 + T(n/2)$ for even $n$, and $T(n) = 1 + T(3n + 1)$ for odd $n > 1$, nobody knows whether every chain ends.
That question is the [[Collatz conjecture|6PCQEXEX4N]].

## Explanations

### L1 human

A rule like "each value is one more than the next value" sounds like a definition, but it does not say where to start.
If the values must be whole numbers from $0$ up, the rule even causes trouble.
The first value would be at least $1$ more than the second, at least $2$ more than the third, and so on.
Then the first value would have to be bigger than every whole number, which is impossible.
A good step-by-step definition starts at a fixed first value and moves forward.

### L2 human

Compare the forward recursion $f(0) = 7$, $f(n + 1) = f(n) - 1$ on the integers.
The base value fixes $f(0) = 7$, and the rule gives each value from the one before, so $f(1) = 6$ and $f(2) = 5$.
By induction $f(n) = 7 - n$, and no other function obeys the two rules.
This function also obeys the upward rule $f(n) = f(n + 1) + 1$.
So the upward rule together with the base value $f(0) = 7$ does define a function into $\mathbb{Z}$, because we can solve the rule for $f(n + 1)$ and run it forward.
Watch out: an upward rule alone looks complete, but it fixes nothing until we add a base value and turn it into a forward rule.
