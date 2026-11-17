---
tag: W48XN2MEM9
kind: concept
name: Hypotheses and conclusion of a theorem
aliases: [hypothesis-of-a-theorem, conclusion-of-a-theorem, standing-assumption, sharp-hypothesis]
msc: ["00A35"]
topics: [N4P3E53HM0]
audience: ug1
uses: [0B94TKFQJX, KK5F0F03ZW]
sources:
  - url: https://en.wikipedia.org/wiki/Theorem
    locator: Informal account of theorems
  - url: https://en.wikipedia.org/wiki/Material_conditional
    locator: lead section
  - book: isbn:9781108439534
---

## Summary

Most [[theorems|KK5F0F03ZW]] have the form "if $H_1, H_2, \ldots, H_k$, then $C$".
The statements $H_1, \ldots, H_k$ are the hypotheses: the conditions that the theorem assumes.
The statement $C$ is the conclusion: the claim that the theorem makes when all the hypotheses hold.
The theorem asserts that $C$ is true in each case in which every hypothesis is true, and it asserts nothing about the other cases.
A standing assumption is a hypothesis that a text fixes once for a whole chapter or book, and then omits from each statement.
A hypothesis is needed when the statement becomes false without it, and it is sharp when no weaker condition of the same kind suffices.
To read a theorem is to find its hypotheses and its conclusion, and to apply it is to check each hypothesis in the case at hand.

## Motivation

[[Rolle's theorem|0194DY35BG]] says: if $f$ is continuous on $[a, b]$, differentiable on $(a, b)$, and $f(a) = f(b)$, then $f'(c) = 0$ for some $c$ in $(a, b)$.
The function $f(x) = |x|$ on $[-1, 1]$ is continuous and has $f(-1) = f(1)$.
But its derivative is $-1$ or $1$ at each point where it exists, so it is never $0$.
This does not contradict the theorem, because $|x|$ is not differentiable at $0$, so one hypothesis fails.
The example shows why a reader must find each hypothesis and check it, and why an author must state each hypothesis that the proof uses, as [[this example|YRC4NN8KDJ]] shows.

## Notation

Mathematical English marks hypotheses with "if", "let", "suppose", "assume" and "given", and it marks the conclusion with "then".
The statement "if $H$, then $C$" is written $H \Rightarrow C$ in symbols.
Many statements hide the conditional form.
"Every continuous function on $[a, b]$ is bounded" means "if $f$ is a continuous function on $[a, b]$, then $f$ is bounded".
The statement "let $G$ be a finite group and $H$ a subgroup; then $|H|$ divides $|G|$" has the hypotheses "$G$ is a finite group" and "$H$ is a subgroup of $G$".

## Remarks

### Examples

- The [[extreme value theorem|0WS1A8E2P9]] has the hypotheses "$f$ is continuous" and "the domain is a closed and bounded interval", and each one is needed, as [[this example|TK8AKSWV18]] shows.
- [[Rolle's theorem|0194DY35BG]] has three hypotheses, and each one is needed, as [[this example|YRC4NN8KDJ]] shows.
- [[Fermat's little theorem|0M25PRN3WQ]] has the hypotheses "$p$ is prime" and "$p$ does not divide $a$", and the conclusion $a^{p-1} \equiv 1 \pmod p$. The L2 explanation below tests both hypotheses.
- A sharp hypothesis: for each integer $n \geq 5$, we have $2^n > n^2$. The hypothesis $n \geq 5$ cannot be weakened to $n \geq 4$, because $2^4 = 16 = 4^2$.
- A standing assumption: many books on rings state once that "ring" means a commutative ring with an identity element. Each later theorem uses this hypothesis without stating it.

### Non-examples

- The "if" in a definition does not introduce a hypothesis. In "an integer $n$ is even if $n = 2k$ for some integer $k$", the "if" means "if and only if", as [[this example|1YJTRBDGC3]] shows.
- The induction hypothesis in a proof by induction is not a hypothesis of the theorem. It is an assumption made inside one step of the proof.
- The Riemann hypothesis is not a hypothesis of a theorem. It is an open conjecture, and the word "hypothesis" in its name means "a claim that is not yet proved".

### Basic properties

- Adding a hypothesis gives a weaker theorem, and dropping a hypothesis gives a stronger statement, which can be false.
- A theorem says nothing about a case in which a hypothesis fails. In such a case the conclusion can hold or fail. For example, $f(x) = x^2$ on $[-1, 2]$ has $f(-1) \neq f(2)$, but $f'(0) = 0$.
- If the conclusion fails in some case, then at least one hypothesis fails in that case. This is the contrapositive of the theorem.
- A correct proof uses each hypothesis that is needed. A hypothesis that a correct proof never uses can be dropped, and then the theorem becomes more general.
- To show that a hypothesis is needed, one finds an example that satisfies all the other hypotheses, but not the conclusion.

### Proof of the sharp example

For $n = 5$ we have $2^5 = 32 > 25 = 5^2$.
If $2^n > n^2$ for some $n \geq 5$, then $2^{n+1} = 2 \cdot 2^n > 2n^2$.
For $n \geq 3$ we have $n^2 - 2n - 1 = (n - 1)^2 - 2 \geq 2$, so $2n^2 = n^2 + n^2 > n^2 + 2n + 1 = (n + 1)^2$.
So $2^{n+1} > (n + 1)^2$, and [[mathematical induction|0ASJVEFA9J]] gives $2^n > n^2$ for each $n \geq 5$.

### History

The Greek word "hypothesis" means a thing placed under, that is, a supposition.
Proclus, in his commentary on Euclid, described the parts of a proposition: the enunciation, the setting out of the given data, the statement of what is required, the construction, the proof and the conclusion.
In this scheme the enunciation states the hypotheses and the conclusion in general terms, and the setting out applies the hypotheses to a named figure.

### Common errors

- To apply a theorem without a check of every hypothesis. The function $|x|$ and Rolle's theorem show the result.
- To use the converse: to conclude the hypotheses from the conclusion. A differentiable function $f$ with $f'(c) = 0$ need not satisfy $f(a) = f(b)$.
- To cite a theorem from a book with different standing assumptions. A result about rings with an identity element can fail for rings without one.

## Explanations

### L1 human

A theorem is like a guarantee with conditions: "if these things are true, then that thing is true".
The conditions are the hypotheses, and the promise is the conclusion.
For example: "if a whole number ends in $0$, then it is divisible by $5$".
The number $30$ meets the condition, so the promise applies, and $30$ is divisible by $5$.
The number $35$ does not end in $0$, so this theorem says nothing about it, although $35$ is also divisible by $5$.
Before we use a theorem, we must check that every condition holds.

### L2 human

We test the hypotheses of [[Fermat's little theorem|0M25PRN3WQ]]: if $p$ is a prime and $p$ does not divide the integer $a$, then $a^{p-1} \equiv 1 \pmod p$.

1. The hypotheses are "$p$ is prime" and "$p$ does not divide $a$". The conclusion is $a^{p-1} \equiv 1 \pmod p$.
2. A case with both hypotheses: $p = 5$ and $a = 2$. Then $2^4 = 16 = 3 \cdot 5 + 1$, so $2^4 \equiv 1 \pmod 5$, as the theorem says.
3. We drop "$p$ is prime" and keep the other hypothesis. With $p = 4$ and $a = 3$ we get $3^3 = 27 = 6 \cdot 4 + 3$, so $3^3 \equiv 3 \pmod 4$, not $1$.
4. So the hypothesis "$p$ is prime" is needed.
5. We drop "$p$ does not divide $a$" and keep "$p$ is prime". With $p = 3$ and $a = 3$ we get $3^2 = 9 \equiv 0 \pmod 3$, not $1$.
6. So the hypothesis "$p$ does not divide $a$" is needed too.

The typical use of this test is to understand a theorem: each hypothesis has a reason, and the failing examples show the reason.
A trap is to drop two hypotheses at once.
Then the failing example does not show which hypothesis is needed.

### L3 human

A theorem $H_1 \wedge \cdots \wedge H_k \Rightarrow C$ divides the cases into those that meet every hypothesis and the rest, and it speaks only about the first group.
The study of which hypotheses are needed leads to two kinds of new results.
Counterexamples show that a hypothesis cannot be dropped, and books such as "Counterexamples in Analysis" and "Counterexamples in Topology" collect them.
Generalizations replace a hypothesis by a weaker one, as when the [[law of cosines|060ZVZBV3E]] drops the right angle of the [[Pythagorean theorem|0VP3A1290K]].

Sharpness has a quantitative side.
A bound is sharp when some case attains it or comes as close as wished, and a hypothesis such as $n \geq 5$ is sharp when the statement fails for $n = 4$.
The search for the weakest hypotheses is a main source of new definitions and of new theories, as the page on [[abstraction and generalization|976RZZCT1H]] explains.
