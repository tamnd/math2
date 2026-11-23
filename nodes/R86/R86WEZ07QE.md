---
tag: R86WEZ07QE
kind: example
name: A delta that depends on x proves a false limit
msc: ["00A35", "26A03"]
topics: [MEKKHHQTKB]
audience: ug1
not_instance_of:
  - target: RXG5JTZ2PZ
    note: the number called delta is chosen after x and depends on x, so the quantifier order of the definition is broken
uses: [RXG5JTZ2PZ, 0GBZDAFPX8, EGTZPA6QH3]
sources:
  - url: https://en.wikipedia.org/wiki/(%CE%B5,_%CE%B4)-definition_of_limit
    locator: lead section
---

## Example

Let $f(x) = 1$ for every real $x$, so the true limit is $\lim_{x \to 0} f(x) = 1$.
Here is an argument that "proves" $\lim_{x \to 0} f(x) = 0$.

1. Let $\varepsilon > 0$, and let $\delta = \frac{\lvert x \rvert}{2}$.
2. Let $x$ satisfy $0 < \lvert x - 0 \rvert < \delta$, that is, $0 < \lvert x \rvert < \frac{\lvert x \rvert}{2}$.
3. No real $x$ satisfies this, because $\lvert x \rvert < \frac{\lvert x \rvert}{2}$ gives $\lvert x \rvert < 0$.
4. So the implication "$0 < \lvert x \rvert < \delta$ implies $\lvert f(x) - 0 \rvert < \varepsilon$" holds for every $x$, since its hypothesis is false.
5. So $\lim_{x \to 0} f(x) = 0$, the argument concludes.

The error is in step 1.
The [[epsilon-delta definition of a limit|0GBZDAFPX8]] has the [[quantifier|EGTZPA6QH3]] order $\forall \varepsilon > 0 \; \exists \delta > 0 \; \forall x$, so $\delta$ is chosen after $\varepsilon$ and before $x$.
It may depend on $\varepsilon$ and on the point $0$, but not on $x$.
The formula $\delta = \lvert x \rvert / 2$ uses a variable that is not yet chosen, so it does not define a number at all.
The argument is therefore not an instance of [[writing epsilon-delta proofs|RXG5JTZ2PZ]].

The definition also shows that the claim is false.
Take $\varepsilon = \frac12$.
For each $\delta > 0$, the point $x = \delta/2$ satisfies $0 < \lvert x \rvert < \delta$, and $\lvert f(x) - 0 \rvert = 1 \ge \frac12$.
So no $\delta$ works for this $\varepsilon$.

## Remarks

A milder form of the error appears in proofs that are otherwise sound.
For $\lim_{x \to 2} x^2 = 4$ the scratch work gives $\lvert x^2 - 4 \rvert = \lvert x - 2 \rvert \cdot \lvert x + 2 \rvert$, and a student writes $\delta = \varepsilon / \lvert x + 2 \rvert$.
That choice also depends on $x$, so it is not a $\delta$.
The correct proof removes $x$ with a bound: on $\lvert x - 2 \rvert < 1$ we have $\lvert x + 2 \rvert < 5$, and $\delta = \min(1, \varepsilon/5)$ works, as in [[the limit of x^2 at 2|FZ2S47KDE7]].

The extreme example shows that the quantifier order is not a formality.
With the order $\forall \varepsilon \, \forall x \, \exists \delta$, the trick of step 1 makes the hypothesis false for every $x$.
So that statement is true for every function and every claimed limit, and it means nothing.

## Explanations

### L1 human

In the game of the limit, the first player names a tolerance, then the second player names a distance, and only then is the point $x$ chosen.
The second player may not wait to see $x$.
The false argument cheats: it picks a distance that depends on $x$, and so small that no $x$ fits.
With this cheat the second player "wins" every game, even for the false claim that the constant $1$ tends to $0$.

### L2 human

We test the claim $\lim_{x \to 0} f(x) = 0$ for the constant $f(x) = 1$ against the correct quantifier order.

1. The claim needs, for $\varepsilon = \frac12$, a $\delta > 0$ such that $0 < \lvert x \rvert < \delta$ implies $\lvert 1 - 0 \rvert < \frac12$.
2. The conclusion $1 < \frac12$ is false for every $x$.
3. So the claim needs a $\delta$ such that no $x$ satisfies $0 < \lvert x \rvert < \delta$.
4. Each $\delta > 0$ has such points, for example $x = \delta/2$, so no $\delta$ exists, and the limit is not $0$.

Use this check when you review a written epsilon-delta proof.
Find the line where $\delta$ is defined, and make sure that only $\varepsilon$ and the fixed point appear in it.
Watch out for a hidden $x$, as in $\delta = \varepsilon / (x + 2)$, where $x$ is used before the line that introduces it.
