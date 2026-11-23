---
tag: MXRRV8J67S
kind: example
name: The no-counterexample interpretation of the drinker formula
msc: ["03F10", "03B10"]
topics: [8XY7JYZKFW]
audience: research
instance_of: [4BCD1EM542]
uses: [4BCD1EM542, 8BMQTZZEWB, VZ21F10WRS]
sources:
  - url: https://en.wikipedia.org/wiki/Drinker_paradox
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Herbrandization
    locator: Definition and examples
---

## Example

Let $P$ be a decidable property of natural numbers.
The [[drinker formula|8BMQTZZEWB]] $D = \exists x\, \forall y\, (P(x) \to P(y))$ is valid in classical logic.
Its [[no-counterexample interpretation|4BCD1EM542]] asks for a functional $X(f)$ with $P(X(f)) \to P(f(X(f)))$ for every $f : \mathbb{N} \to \mathbb{N}$.
We give one and check it.

1. Define $X(f) = 0$ if $P(f(0))$ holds, and $X(f) = f(0)$ otherwise.
2. In the case $P(f(0))$ we have $X = 0$, and $P(0) \to P(f(0))$ holds because its conclusion holds.
3. In the case $\neg P(f(0))$ we have $X = f(0)$, and $P(f(0)) \to P(f(f(0)))$ holds because its premise fails.
4. $P$ is decidable, so the two cases cover every $f$.

So $X$ satisfies the n.c.i. of $D$, with one test of $P$ and at most two evaluations of $f$.

## Remarks

The two candidates $0$ and $f(0)$ form a Herbrand disjunction, since $(P(0) \to P(f(0))) \vee (P(f(0)) \to P(f(f(0))))$ is a propositional tautology.
This is the shape that [[Herbrand's theorem|VZ21F10WRS]] gives for a valid formula of pure logic: finitely many terms in $f$ and a case distinction among them.

No computable functional of $P$ gives a witness of $D$ itself.
Suppose that $F$ computes a witness from $P$, and run it on the property $P$ that is true everywhere, with result $x_0$.
The computation reads finitely many values of $P$.
Now make $P$ false at one point that was not read and that differs from $x_0$.
Then $F$ still returns $x_0$, but now $P(x_0)$ holds and $\forall y\, P(y)$ fails, so $x_0$ is not a witness.

## Explanations

### L1 human

The drinker formula says that in a nonempty bar there is a person such that, if that person drinks, everyone drinks.
Its classical proof does not say who the person is.
The no-counterexample interpretation lets an opponent name, for each person $x$, someone $f(x)$ who might not drink.
Then the answer is easy: ask whether $f(0)$ drinks.
If yes, person $0$ passes this test, and if no, person $f(0)$ passes it, since that person does not drink.

### L2 human

We run $X$ with the property $P(n)$ that says that $n$ is even.
For $f(n) = n + 1$ we get $f(0) = 1$, which is odd, so $X = 1$.
The test is $P(1) \to P(2)$, which is true since $1$ is odd.
For $f(n) = 2n + 4$ we get $f(0) = 4$, which is even, so $X = 0$.
The test is $P(0) \to P(4)$, which is true since $4$ is even.

The typical use is to see the n.c.i. of a valid formula of pure logic as a finite case distinction.
Watch out: the answer $X$ is not a drinker for every test, since it passes only the test $f(X)$ that the opponent chose.
