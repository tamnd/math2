---
tag: 7RFM1XPJQV
kind: example
name: A Skolem function for the halting formula is not a no-counterexample witness
msc: ["03F10", "03D10"]
topics: [8XY7JYZKFW]
audience: research
not_instance_of:
  - target: 4BCD1EM542
    note: "The no-counterexample interpretation asks for a functional of the counterexample function, not a Skolem function; here no computable Skolem function exists, but a computable functional does."
uses: [4BCD1EM542, S9DK13K5PS, Z7TN2B35B0, GCPQGMJYEV, HVHEKG9FA5]
sources:
  - url: https://en.wikipedia.org/wiki/Halting_problem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Herbrandization
    locator: Definition and examples
---

## Example

Let $T(e, x, y)$ be [[Kleene's T predicate|S9DK13K5PS]], and let $B = \forall x\, \exists y\, \forall z\, (T(x, x, y) \vee \neg T(x, x, z))$.
PA proves $B$: if program $x$ halts on input $x$, take $y$ a halting computation; otherwise every $y$ works.
A [[Skolem function|GCPQGMJYEV]] $h$ with $\forall x\, \forall z\, (T(x, x, h(x)) \vee \neg T(x, x, z))$ is a witness for $B$ that depends on $x$ alone.
We show that no such $h$ is computable, and we give the computable [[no-counterexample witness|4BCD1EM542]] instead.

1. Suppose $h$ is computable and satisfies the formula above.
2. If program $x$ halts on input $x$, take $z$ a halting computation. Then $T(x, x, h(x))$ must hold.
3. So program $x$ halts on input $x$ if and only if $T(x, x, h(x))$.
4. The right side is decidable for computable $h$, which decides the [[halting problem|Z7TN2B35B0]], a contradiction.
5. The n.c.i. of $B$ asks for $Y(x, f)$ with $T(x, x, Y) \vee \neg T(x, x, f(Y))$, for every $f$.
6. Let $Y(x, f) = f(0)$ if $T(x, x, f(0))$ holds, and $Y(x, f) = 0$ otherwise.
7. In the first case $T(x, x, Y)$ holds. In the second case $Y = 0$ and $\neg T(x, x, f(0))$ holds.

So the Skolem function is not computable, while the n.c.i. functional $Y$ is computable by one evaluation of $f$.

## Remarks

The Skolem function answers every test at once; the n.c.i. functional only answers the test that $f$ proposes.
This difference is the whole content of the interpretation.
The same formula shows that [[PA is not conservative over HA for this formula|HVHEKG9FA5]].
For $\Pi^0_2$ theorems, $\forall x\, \exists y\, \varphi$, there is no counterexample function, and the n.c.i. gives a witness that depends on $x$ alone.

## Explanations

### L1 human

The statement says: for each program, there is a number $y$ that settles whether the program halts.
No algorithm finds such a $y$ from the program alone, because that would solve the halting problem.
The no-counterexample interpretation asks less.
An opponent offers one number $f(0)$ and claims it is not a halting computation.
The algorithm checks this one claim, and either catches the opponent or answers $0$.

### L2 human

We run $Y$ on a program $x$ that halts with computation $c$.

1. For $f$ with $f(0) = c$: $T(x, x, c)$ holds, so $Y = c$, a real witness.
2. For $f$ with $f(0) = 5$, not a computation of $x$: $Y = 0$, and $\neg T(x, x, f(0))$ holds, so the test passes.

The typical use is to show why the n.c.i. takes the counterexample function as an input.
A trap is to call $Y$ a witness of $B$; it is correct only against the given $f$.
