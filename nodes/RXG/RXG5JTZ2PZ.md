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

An epsilon-delta proof shows a statement of the form "for each $\varepsilon > 0$ there is $\delta > 0$ such that, for all $x$ with $0 < \lvert x - a \rvert < \delta$, we have $\lvert f(x) - L \rvert < \varepsilon$".
This is the [[epsilon-delta definition of a limit|0GBZDAFPX8]] $\lim_{x \to a} f(x) = L$, and the [[epsilon-delta definition of continuity|0W8YHHGCJG]] has the same form.
The proof has two parts with different directions.
In the scratch work we start from the goal $\lvert f(x) - L \rvert < \varepsilon$ and find a $\delta$, which may depend on $\varepsilon$ and $a$ but not on $x$.
In the written proof we go forward: we fix $\varepsilon$, define $\delta$, take an arbitrary $x$ with $0 < \lvert x - a \rvert < \delta$, and derive $\lvert f(x) - L \rvert < \varepsilon$.
The method matters because every rigorous proof about limits, continuity and convergence in analysis has this shape.

## Motivation

The phrase "$f(x)$ is close to $L$ when $x$ is close to $a$" is too vague for a proof.
The definition makes it exact with two numbers: the tolerance $\varepsilon$ for the output, and the tolerance $\delta$ for the input.
The statement has three [[quantifiers|EGTZPA6QH3]], $\forall \varepsilon \, \exists \delta \, \forall x$, and their order is the main difficulty for a student.
A proof must answer a challenge: for each tolerance $\varepsilon$ that an opponent names, we must name a $\delta$ that works for all $x$ at once.
The scratch work finds the answer, and the written proof shows that the answer works.
The scratch work goes backward from the goal, so it is not a proof, and the written proof must be a separate, forward argument.

## Notation

1. The letters $\varepsilon$ (epsilon) and $\delta$ (delta) are the standard names. Some books write $\epsilon$ for $\varepsilon$.
2. For sequences the same pattern uses an index $N$ instead of $\delta$: for each $\varepsilon > 0$ there is $N$ with $\lvert a_n - L \rvert < \varepsilon$ for all $n \ge N$. This is the [[epsilon-N definition of the limit of a sequence|09G6KHS6GY]].
3. The notation $\delta = \min(1, \varepsilon/5)$ means the smaller of the two numbers. Then $\delta \le 1$ and $\delta \le \varepsilon/5$ both hold.
4. Books differ on the condition $0 < \lvert x - a \rvert$. A limit excludes the point $a$ itself, and continuity at $a$ allows $x = a$.

## Remarks

### Examples

1. [[The limit of x^2 at 2 by epsilon and delta|FZ2S47KDE7]]: we factor $x^2 - 4 = (x - 2)(x + 2)$, bound $\lvert x + 2 \rvert$ by $5$ when $\lvert x - 2 \rvert < 1$, and take $\delta = \min(1, \varepsilon/5)$.
2. [[The limit of 1/x at 3 by epsilon and delta|9E4PCEXSJ3]]: we bound $\lvert x \rvert$ from below near $3$ and take $\delta = \min(1, 6\varepsilon)$.
3. A linear function: $\lim_{x \to 1} (3x + 2) = 5$. Since $\lvert (3x + 2) - 5 \rvert = 3 \lvert x - 1 \rvert$, the choice $\delta = \varepsilon/3$ works.
4. A sequence: $\lim_{n \to \infty} \frac{1}{n} = 0$. For $\varepsilon > 0$ take an integer $N > 1/\varepsilon$; then $n \ge N$ gives $\frac1n \le \frac1N < \varepsilon$, as in the page [[for each epsilon > 0, 1/n < epsilon|C4S1D9R7T0]].
5. A sum: if $f(x) \to L$ and $g(x) \to M$ as $x \to a$, then $f(x) + g(x) \to L + M$. We choose $\delta_1$ for $f$ with $\varepsilon/2$, $\delta_2$ for $g$ with $\varepsilon/2$, take $\delta = \min(\delta_1, \delta_2)$, and use the [[triangle inequality|03HF5PMY5T]].

### Non-examples

1. [[A delta that depends on x proves a false limit|R86WEZ07QE]]: a choice such as $\delta = \lvert x \rvert / 2$ or $\delta = \varepsilon / \lvert x + 2 \rvert$ uses $x$ before $x$ is chosen. With $\delta = \lvert x \rvert / 2$ one can "prove" the false limit $\lim_{x \to 0} 1 = 0$.
2. The scratch work alone, written as "$\lvert x^2 - 4 \rvert < \varepsilon$ so $\lvert x - 2 \rvert \lvert x + 2 \rvert < \varepsilon$ so $\lvert x - 2 \rvert < \varepsilon/5$", is not a proof. It goes from the goal to a condition, and its last step is not even an implication.
3. A table of values of $x^2$ for $x = 1.9, 1.99, 1.999$ suggests the limit $4$, but it does not prove it. It tests finitely many $x$ and no particular $\varepsilon$.

### Basic properties

1. If $\delta$ works for a given $\varepsilon$, then each smaller positive $\delta'$ also works, because the set of allowed $x$ becomes smaller.
2. If $\delta$ works for $\varepsilon$, then it works for each larger $\varepsilon'$. So it suffices to prove the statement for small $\varepsilon$, for example for $\varepsilon < 1$.
3. A minimum of finitely many positive numbers is positive. So a $\delta$ of the form $\min(\delta_1, \dots, \delta_k)$ meets all the restrictions $\delta \le \delta_i$ at once, and it is still positive.
4. The restriction $\delta \le 1$ is a common device: it keeps $x$ in a bounded interval around $a$, where the other factor of $\lvert f(x) - L \rvert$ has a bound $M$. Then $\delta = \min(1, \varepsilon/M)$ works.
5. The epsilon-delta and the sequential definitions of the limit are equivalent, as the page [[epsilon-delta and sequential definitions of continuity|A4C3JY380W]] shows for continuity.

### History

Bernard Bolzano in 1817 and Augustin-Louis Cauchy in 1821 described continuity and limits in terms of quantities that become small.
Karl Weierstrass and his school made the epsilon-delta form the standard definition in the second half of the 19th century.
Since then it has been the first rigorous definition that most students of analysis meet.

### Common errors

1. A student lets $\delta$ depend on $x$. The quantifier order $\forall \varepsilon \, \exists \delta \, \forall x$ requires that $\delta$ is fixed before $x$ is chosen.
2. A student hands in the scratch work as the proof. The written proof must start with "Let $\varepsilon > 0$", define $\delta$, and end with $\lvert f(x) - L \rvert < \varepsilon$.
3. A student uses a bound such as $\lvert x + 2 \rvert \le 5$ without the restriction $\delta \le 1$ that makes it true. Each bound in the proof needs its reason, and that reason must appear in the choice of $\delta$.

## Explanations

### L1 human

The statement "$x^2$ gets close to $4$ when $x$ gets close to $2$" needs a precise meaning.
Think of a game with two players.
The first player names a small tolerance, for example $0.1$.
The second player must answer with a distance, for example $0.02$, such that every $x$ within $0.02$ of $2$ gives $x^2$ within $0.1$ of $4$.
For $x = 2.01$ we get $x^2 = 4.0401$, which is within $0.1$ of $4$.
An epsilon-delta proof gives the second player a rule that wins the game for every tolerance.

### L2 human

We prove $\lim_{x \to 4} \sqrt{x} = 2$, where $\sqrt{x}$ is defined for $x \ge 0$.

1. Scratch work: we need $\lvert \sqrt{x} - 2 \rvert < \varepsilon$. We multiply and divide by $\sqrt{x} + 2$, which is at least $2$.
2. This gives $\lvert \sqrt{x} - 2 \rvert = \frac{\lvert x - 4 \rvert}{\sqrt{x} + 2} \le \frac{\lvert x - 4 \rvert}{2}$. So $\lvert x - 4 \rvert < 2\varepsilon$ suffices.
3. Proof: let $\varepsilon > 0$, and let $\delta = 2\varepsilon$. Then $\delta > 0$.
4. Let $x \ge 0$ with $0 < \lvert x - 4 \rvert < \delta$.
5. Since $(\sqrt{x} - 2)(\sqrt{x} + 2) = x - 4$ and $\sqrt{x} + 2 \ge 2 > 0$, we get $\lvert \sqrt{x} - 2 \rvert = \frac{\lvert x - 4 \rvert}{\sqrt{x} + 2}$.
6. So $\lvert \sqrt{x} - 2 \rvert \le \frac{\lvert x - 4 \rvert}{2} < \frac{\delta}{2} = \varepsilon$.
7. Since $\varepsilon > 0$ was arbitrary, $\lim_{x \to 4} \sqrt{x} = 2$.

The typical use of the pattern is to prove a limit from the definition when no limit law applies, and to prove the limit laws themselves.
A trap is the step "$\lvert x - 4 \rvert < 2\varepsilon$, hence $\lvert \sqrt{x} - 2 \rvert < \varepsilon$" without step 5: the reader must see the identity that connects the two quantities.

### L3 human

The statement $\forall \varepsilon > 0 \; \exists \delta > 0 \; \forall x$ asks for a function $\varepsilon \mapsto \delta(\varepsilon)$, a modulus of continuity at the point $a$.
When one $\delta$ works for all points $a$ of a set, the function is [[uniformly continuous|0M4JJT780X]], and the quantifier $\forall a$ moves to the right of $\exists \delta$.
In a metric space the pattern is the same with the distance in place of $\lvert x - a \rvert$.
In a topological space it becomes the statement that each neighbourhood of $L$ contains the image of a punctured neighbourhood of $a$.
Mathlib states limits with filters, and the epsilon-delta form is a theorem about the filters of neighbourhoods.
Estimates with several error terms combine the pattern with the triangle inequality, as in the [[epsilon over three argument|VXV7M0QDH6]].
The [[density argument|J2J35J3055]] uses that form to pass from a dense class to all functions.
Non-standard analysis replaces the quantifiers by infinitesimals, but the proofs there rest on the same estimates.
