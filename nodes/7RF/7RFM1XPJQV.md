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
PA proves $B$: if program $x$ halts on input $x$, take for $y$ a halting computation, and otherwise every $y$ works.
A [[Skolem function|GCPQGMJYEV]] for $B$ is a function $h$ with $\forall x\, \forall z\, (T(x, x, h(x)) \vee \neg T(x, x, z))$, a witness that depends on $x$ alone.
We show that no such $h$ is computable, and then we give a computable [[no-counterexample witness|4BCD1EM542]].

1. Suppose that $h$ is computable and satisfies the formula above.
2. If program $x$ halts on input $x$, take for $z$ a halting computation, so that $\neg T(x, x, z)$ fails and $T(x, x, h(x))$ must hold.
3. Hence program $x$ halts on input $x$ if and only if $T(x, x, h(x))$ holds.
4. For computable $h$ the right side is decidable, so it decides the [[halting problem|Z7TN2B35B0]], which is a contradiction.
5. The n.c.i. of $B$ asks for $Y(x, f)$ with $T(x, x, Y) \vee \neg T(x, x, f(Y))$, for every $f$.
6. Let $Y(x, f) = f(0)$ if $T(x, x, f(0))$ holds, and $Y(x, f) = 0$ otherwise.
7. In the first case $T(x, x, Y)$ holds, and in the second case $Y = 0$ and $\neg T(x, x, f(0))$ holds.

So no Skolem function is computable, while the n.c.i. functional $Y$ is computable with one evaluation of $f$.

## Remarks

The Skolem function must answer every test at once, while the n.c.i. functional only answers the test that $f$ proposes.
That difference is the whole content of the interpretation.

The same formula is a $\Pi^0_3$ sentence that [[PA proves and HA does not|HVHEKG9FA5]].
For a $\Pi^0_2$ theorem $\forall x\, \exists y\, \varphi$ there is no counterexample function, and the n.c.i. gives a witness that depends on $x$ alone.

## Explanations

### L1 human

The statement says that for each program there is a number $y$ that settles whether the program halts.
No algorithm finds such a $y$ from the program alone, because that would solve the halting problem.
The no-counterexample interpretation asks for less.
An opponent offers one number $f(0)$ and claims that it is not a halting computation.
The algorithm checks this one claim, and it either catches the opponent or answers $0$.

### L2 human

We run $Y$ on a program $x$ that halts with computation $c$.
For an $f$ with $f(0) = c$, the test $T(x, x, c)$ holds, so $Y = c$, which is a real witness.
For an $f$ with $f(0) = 5$, where $5$ is not a computation of $x$ on $x$, we get $Y = 0$, and $\neg T(x, x, f(0))$ holds, so the test passes.

The typical use is to show why the n.c.i. takes the counterexample function as an input.
Watch out: $Y$ is not a witness of $B$, since it is correct only against the given $f$.
