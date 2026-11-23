---
tag: RXG5JTZ2PZ
kind: concept
name: Writing epsilon-delta proofs
aliases: [writing-epsilon-delta-proofs, epsilon-delta-proof]
msc: ["00A35", "26A03"]
topics: [MEKKHHQTKB, G9JFJGY4TQ]
audience: ug1
specializes: [0B94TKFQJX]
uses: [0GBZDAFPX8, 0W8YHHGCJG, 03HF5PMY5T, 0FFXKTKKQC, EGTZPA6QH3]
sources:
  - url: https://en.wikipedia.org/wiki/(%CE%B5,_%CE%B4)-definition_of_limit
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Limit_of_a_function
    locator: lead section
---

## Summary

An epsilon-delta proof is written in two passes.
First you work backward from the goal, on scratch paper, to find a $\delta$; then you write a forward proof that names that $\delta$ and checks that it works.

Here is the pattern on a real goal: $\lim_{x \to 3} x^2 = 9$.
On scratch paper, factor $\lvert x^2 - 9 \rvert = \lvert x - 3 \rvert \cdot \lvert x + 3 \rvert$.
If $\lvert x - 3 \rvert < 1$, then $2 < x < 4$, so $\lvert x + 3 \rvert < 7$, and the goal holds once also $\lvert x - 3 \rvert < \varepsilon/7$.
The written proof: let $\varepsilon > 0$, put $\delta = \min(1, \varepsilon/7)$, and take $x$ with $0 < \lvert x - 3 \rvert < \delta$.
Then $\lvert x + 3 \rvert < 7$ because $\delta \le 1$, and $\lvert x - 3 \rvert < \varepsilon/7$ because $\delta \le \varepsilon/7$, so
$$\lvert x^2 - 9 \rvert = \lvert x - 3 \rvert \cdot \lvert x + 3 \rvert < \frac{\varepsilon}{7} \cdot 7 = \varepsilon.$$

In general, the [[epsilon-delta definition of a limit|0GBZDAFPX8]] says that $\lim_{x \to a} f(x) = L$ when
$$\forall \varepsilon > 0 \ \exists \delta > 0 \ \forall x \ \big( 0 < \lvert x - a \rvert < \delta \implies \lvert f(x) - L \rvert < \varepsilon \big).$$
The [[definition of continuity|0W8YHHGCJG]] has the same shape with $L = f(a)$ and without the condition $0 < \lvert x - a \rvert$.

## Motivation

"$f(x)$ is close to $L$ when $x$ is close to $a$" is too vague to prove anything.
The definition makes it exact with two numbers, a tolerance $\varepsilon$ for the output and a tolerance $\delta$ for the input.
Its three [[quantifiers|EGTZPA6QH3]] come in a fixed order, and that order is the main difficulty.
Think of a challenge: an opponent names any $\varepsilon$, and you must answer with one $\delta$ that works for every $x$ at once.

The scratch work finds the answer and the written proof shows that it works.
They run in opposite directions, which is why they are separate: the scratch work starts from the goal, so it is not a proof.
Every rigorous argument about limits, continuity and convergence has this shape, and the [[epsilon over three argument|VXV7M0QDH6]] and the [[density argument|J2J35J3055]] later in the list build on it.

## Notation

The letters $\varepsilon$ (epsilon) and $\delta$ (delta) are standard, and some books write $\epsilon$.
For sequences an index $N$ takes the place of $\delta$, as in the [[epsilon-N definition of the limit of a sequence|09G6KHS6GY]].
The notation $\min(1, \varepsilon/7)$ means the smaller of the two numbers, so $\delta \le 1$ and $\delta \le \varepsilon/7$ both hold.
Books differ on the condition $0 < \lvert x - a \rvert$: a limit leaves out the point $a$ itself, while continuity at $a$ allows $x = a$.

## Remarks

### Why a minimum of two values

The scratch work usually produces two demands on $x$.
One keeps $x$ in a fixed interval around $a$, so that the other factor has a bound $M$; the other makes $\lvert x - a \rvert$ smaller than $\varepsilon/M$.
A minimum meets both demands, and it is still positive, because a minimum of finitely many positive numbers is positive.
The number $1$ is a choice: with $\lvert x - 3 \rvert < \tfrac12$ you get $\lvert x + 3 \rvert < 6.5$ and $\delta = \min(\tfrac12, \varepsilon/6.5)$.

Two monotonicity facts save work.
If $\delta$ works for $\varepsilon$, every smaller positive $\delta$ works too, since fewer $x$ are allowed.
If $\delta$ works for $\varepsilon$, it works for every larger $\varepsilon$, so you may assume $\varepsilon$ is small.

### More worked goals

For a line, no minimum is needed: $\lvert (3x + 2) - 5 \rvert = 3\lvert x - 1 \rvert$, so $\delta = \varepsilon/3$ proves $\lim_{x \to 1} (3x + 2) = 5$.
For [[the limit of x^2 at 2|FZ2S47KDE7]] the bound is $\lvert x + 2 \rvert < 5$ and $\delta = \min(1, \varepsilon/5)$.
For [[the limit of 1/x at 3|9E4PCEXSJ3]] the denominator needs a lower bound: on $2 < x < 4$, $3x > 6$, and $\delta = \min(1, 6\varepsilon)$.

For a sum of limits, choose $\delta_1$ for $f$ and $\delta_2$ for $g$, each with tolerance $\varepsilon/2$, and take $\delta = \min(\delta_1, \delta_2)$.
The [[triangle inequality|03HF5PMY5T]] then gives
$$\lvert f(x) + g(x) - (L + M) \rvert \le \lvert f(x) - L \rvert + \lvert g(x) - M \rvert < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.$$

### Watch out

The worst slip lets $\delta$ depend on $x$, as in $\delta = \varepsilon/\lvert x + 3 \rvert$.
The order $\forall \varepsilon \, \exists \delta \, \forall x$ fixes $\delta$ before $x$ is chosen, and [[a delta that depends on x|R86WEZ07QE]] can "prove" the false limit $\lim_{x \to 0} 1 = 0$.
The fix is to replace $x$ by a bound, which is exactly what the restriction $\delta \le 1$ does.

A second slip hands in the scratch work as the proof.
"$\lvert x^2 - 9 \rvert < \varepsilon$, so $\lvert x - 3 \rvert \lvert x + 3 \rvert < \varepsilon$, so $\lvert x - 3 \rvert < \varepsilon/7$" runs from the goal to a condition, and its last arrow is not even true.
A third slip uses the bound $\lvert x + 3 \rvert < 7$ but forgets the $1$ in the minimum that makes it true.
A table of values such as $2.9^2$, $2.99^2$ and $2.999^2$ suggests the limit but proves nothing.

### History

Bernard Bolzano in 1817 and Augustin-Louis Cauchy in 1821 described continuity and limits in terms of quantities that become small.
Karl Weierstrass and his students made the epsilon-delta form the standard definition in the second half of the 19th century.

### Try it

Prove $\lim_{x \to 1} (x^2 + x) = 2$.
Factor $x^2 + x - 2 = (x - 1)(x + 2)$; on $\lvert x - 1 \rvert < 1$ we have $0 < x < 2$, so $\lvert x + 2 \rvert < 4$, and $\delta = \min(1, \varepsilon/4)$ works.

Prove $\lim_{n \to \infty} \frac1n = 0$ with an $N$ in place of $\delta$.
Given $\varepsilon > 0$, take an integer $N > 1/\varepsilon$; then $n \ge N$ gives $\frac1n \le \frac1N < \varepsilon$.

## Explanations

### L1 human

"$x^2$ gets close to $9$ when $x$ gets close to $3$" needs an exact meaning, and a game gives it one.
The first player names a small tolerance, say $0.7$.
The second player answers with a distance, say $0.1$, so that every $x$ within $0.1$ of $3$ gives $x^2$ within $0.7$ of $9$.
For $x = 3.1$ we get $x^2 = 9.61$, which is within $0.7$ of $9$.
An epsilon-delta proof hands the second player a rule that wins for every tolerance.

### L2 human

We prove $\lim_{x \to 4} \sqrt{x} = 2$, for $x \ge 0$.

1. Scratch work: multiply and divide by $\sqrt{x} + 2$, which is at least $2$:
   $$\lvert \sqrt{x} - 2 \rvert = \frac{\lvert x - 4 \rvert}{\sqrt{x} + 2} \le \frac{\lvert x - 4 \rvert}{2}.$$
   So $\lvert x - 4 \rvert < 2\varepsilon$ is enough.
2. Proof: let $\varepsilon > 0$ and $\delta = 2\varepsilon > 0$, and let $x \ge 0$ with $0 < \lvert x - 4 \rvert < \delta$.
3. Since $(\sqrt{x} - 2)(\sqrt{x} + 2) = x - 4$ and $\sqrt{x} + 2 \ge 2$, the display of step 1 holds.
4. So $\lvert \sqrt{x} - 2 \rvert \le \lvert x - 4 \rvert / 2 < \delta/2 = \varepsilon$.

Here no minimum was needed, because the second factor had a bound on the whole domain.
Watch out: the reader must see the identity of step 3, which connects $\lvert \sqrt{x} - 2 \rvert$ to $\lvert x - 4 \rvert$.

### L3 human

The statement $\forall \varepsilon \, \exists \delta$ asks for a function $\varepsilon \mapsto \delta(\varepsilon)$, a modulus of continuity at $a$.
When one $\delta$ serves every point of a set, the function is [[uniformly continuous|0M4JJT780X]]: the quantifier over points moves to the right of $\exists \delta$.
For $x^2$ the scratch work gives $\delta = \min(1, \varepsilon/(2\lvert a \rvert + 1))$, which shrinks as $\lvert a \rvert$ grows, and indeed $x^2$ is not uniformly continuous on $\mathbb{R}$.
In metric spaces the same pattern uses a distance, in topological spaces it becomes a statement about neighborhoods, and Mathlib states limits with filters.
