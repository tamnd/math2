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

Consider the following proposal.
"Let $f \colon \mathbb{N} \to \mathbb{N}$ be the function with $f(n) = f(n + 1) + 1$ for each $n \in \mathbb{N}$."
It looks like a recursive definition, one of the [[kinds of definitions|B60DBNF77S]].
We show that it defines nothing.

1. A recursive definition computes $f(n + 1)$ from values at smaller arguments. This rule computes $f(n)$ from the larger argument $n + 1$, so the [[principle of recursive definition|BQ1D7T0EGD]] does not apply.
2. Suppose that a function $f \colon \mathbb{N} \to \mathbb{N}$ satisfies the rule. We show by induction on $k$ that $f(0) = f(k) + k$ for each $k \in \mathbb{N}$.
3. For $k = 0$ the claim is $f(0) = f(0)$.
4. If $f(0) = f(k) + k$, then the rule at $n = k$ gives $f(k) = f(k + 1) + 1$, so $f(0) = f(k + 1) + k + 1$.
5. Since $f(k) \geq 0$, step 2 gives $f(0) \geq k$ for each $k$. Take $k = f(0) + 1$: then $f(0) \geq f(0) + 1$, which is false.
6. So no function from $\mathbb{N}$ to the [[natural numbers|0MWKJ44V5A]] satisfies the rule.

Now change the codomain to $\mathbb{Z}$.

1. For each integer $c$, the function $f_c(n) = c - n$ satisfies the rule: $f_c(n + 1) + 1 = c - n - 1 + 1 = c - n = f_c(n)$.
2. Different values of $c$ give different functions, because $f_c(0) = c$.
3. So the rule has infinitely many solutions, and "the function with this rule" names none of them.

## Remarks

1. With codomain $\mathbb{N}$, existence fails. With codomain $\mathbb{Z}$, uniqueness fails. Either way, the proposal is not a definition.
2. A rule of the form "$f(n + 1)$ from $f(0), \ldots, f(n)$, plus a base value" always defines exactly one function. The direction of the recursion is what matters.
3. A rule can also refer to other arguments and still be a correct definition, if each chain of references ends. For example, $g(n) = g(\lfloor n/2 \rfloor) + 1$ for $n \geq 1$ with $g(0) = 0$ defines $g$, because $\lfloor n/2 \rfloor < n$.
4. For the rule $T(1) = 0$, $T(n) = 1 + T(n/2)$ for even $n$, and $T(n) = 1 + T(3n + 1)$ for odd $n > 1$, nobody knows whether each chain ends. The question is the [[Collatz conjecture|6PCQEXEX4N]].

## Explanations

### L1 human

A rule like "each value is one more than the next value" sounds like a definition, but it does not tell us where to start.
If the values must be whole numbers from $0$ up, the rule even makes trouble.
The first value would be at least $1$ more than the second, at least $2$ more than the third, and so on.
Then the first value would have to be bigger than every whole number, which is impossible.
A good step-by-step definition always starts at a fixed first value and moves forward.

### L2 human

Compare with the correct recursion $f(0) = 7$, $f(n + 1) = f(n) - 1$ on the integers.

1. The base value fixes $f(0) = 7$.
2. The rule computes each value from the previous one: $f(1) = 6$, $f(2) = 5$, and so on.
3. By induction, $f(n) = 7 - n$, and no other function satisfies the two rules.
4. This function also satisfies the upward rule $f(n) = f(n + 1) + 1$.

So the upward rule plus the base value $f(0) = 7$ defines a function on $\mathbb{Z}$, because it can be solved for $f(n + 1)$.
The trap is that an upward rule alone looks complete, but it fixes nothing until a base value is added and the rule is solved in the forward direction.
