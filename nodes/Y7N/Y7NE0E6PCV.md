---
tag: Y7NE0E6PCV
kind: concept
name: Without loss of generality
aliases: [wlog, by-symmetry]
msc: ["00A35", "97E50"]
topics: [G9JFJGY4TQ, 958EF46EYJ]
audience: ug1
specializes: [0B94TKFQJX]
uses: [0WCP0PVET6, 0B94TKFQJX]
sources:
  - url: https://en.wikipedia.org/wiki/Without_loss_of_generality
    locator: lead section
---

## Summary

"Without loss of generality" is a promise that the cases you skip are copies of the case you prove.
A symmetry of the statement, such as exchanging two letters, turns each skipped case into the chosen one, so one argument covers all of them.

Here is a small one: for all real numbers $a$ and $b$,
$$\max(a, b) = \frac{a + b + |a - b|}{2}.$$
Exchanging $a$ and $b$ changes neither side, since $\max(b, a) = \max(a, b)$ and $|b - a| = |a - b|$.
So we may assume $a \le b$, because the case $b \le a$ becomes this one after the exchange.
Then $\max(a, b) = b$ and $|a - b| = b - a$, and the right side is $\tfrac{1}{2}(a + b + b - a) = b$.

In general, a proof *without loss of generality* (wlog) of a statement proves it only in a chosen case $C$, and it names a transformation of the variables with two properties.
The transformation keeps the statement, hypotheses and conclusion together, so that the statement holds for the old values exactly when it holds for the new ones.
And it moves every case outside $C$ into $C$.
Then the proof in $C$ proves the statement in every case.

## Motivation

Many statements treat their variables alike.
The identity above does not change when $a$ and $b$ are exchanged, so a [[proof by cases|0WCP0PVET6]] with the cases $a \le b$ and $b \le a$ would repeat the first case word for word, with the letters swapped.
"Without loss of generality, $a \le b$" records that the second case is the first one after a renaming, and it saves the repetition.

The same move appears far from algebra.
In geometry you often choose coordinates so that a point is at the origin or a circle has radius $1$, because the statement does not change under translation and scaling.
In number theory you assume $a \ge b \ge 0$ in a statement about the [[greatest common divisor|02WF878BH1]], since $\gcd(a, b) = \gcd(b, a) = \gcd(|a|, |b|)$.
Each of these is a wlog step, and each rests on a symmetry that someone must name.

## Notation

The phrase is written "without loss of generality", "wlog", "WLOG" or "w.l.o.g."; see [[mathematical abbreviations|4ZNYMYRRY3]] and [[a sentence with the abbreviations s.t., wlog and iff|K35RJ9YHC0]].
Other forms are "by symmetry, we may assume that ..." and "we may assume that ...".
In Lean, the Mathlib tactic `wlog h : a ≤ b` produces two goals.
The first is the reduction: prove the statement when `a ≤ b` fails, using the statement in the case `a ≤ b` as a hypothesis.
The second is the main case, with `h : a ≤ b` in the context.

## Remarks

### Why the reduction is valid

Write the statement as $S(a, b)$, to be proved for all real $a$ and $b$.
Suppose you know that $S(a, b)$ and $S(b, a)$ say the same thing, and that you have proved $S(a, b)$ whenever $a \le b$.
Take any pair with $b < a$.
Then the swapped pair $(b, a)$ has its first entry at most its second, so $S(b, a)$ holds by the proof, and $S(a, b)$ holds by the symmetry.
So the method is a proof by cases in which one case is proved directly and the other is reduced to it.
The reduction is part of the proof, even when it fits into the one sentence that names the symmetry.

### Naming the symmetry

The common symmetries are few, and a careful proof names the one it uses.
Exchanging two letters handles "wlog $a \le b$", as in [[the sum of the maximum and the minimum of two numbers|ZT2TCYNF2N]] and in [[a square root inequality by symmetry|8AR2JJMCPT]], where the exchange of $x$ and $y$ allows $x \ge y$.
Changing signs handles "wlog $x \ge 0$": for the triangle inequality $|x + y| \le |x| + |y|$, replacing $x$ and $y$ by $-x$ and $-y$ changes neither side and turns a negative sum $x + y$ into a positive one.
Relabeling points, rotating, translating and scaling handle the geometric cases.

The symmetry must keep the hypotheses as well as the conclusion.
In the square root example the hypotheses are $x \ge 0$ and $y \ge 0$, and the exchange keeps them; a symmetry of the conclusion alone would not be enough.

### When to choose it

Look for wlog whenever a case split produces two or more cases that differ only by a renaming.
Write the statement $S(a, b)$, write $S(b, a)$ by exchanging the letters everywhere, and compare.
If the two say the same thing, wlog is allowed, and it usually saves half the proof.
A wlog step also often does a second job: it removes absolute values or makes an expression such as $\sqrt{x - y}$ defined.

### When wlog fails

[[A wlog step for a statement that is not symmetric|YD1XSF3641]] assumes $|a| \ge |b|$ in the false claim $a^2 - b^2 \ge 0$.
Exchanging $a$ and $b$ turns $a^2 - b^2$ into its negative, so the case $|a| < |b|$ is not a copy of the chosen case, and there the claim fails at $a = 0$, $b = 1$.

In the same way, "for every real $x$, $x^2 + x \ge 0$; wlog $x \ge 0$" is wrong, because $x \mapsto -x$ changes $x^2 + x$ into $x^2 - x$.
The claim indeed fails at $x = -\tfrac{1}{2}$, where $x^2 + x = -\tfrac{1}{4}$.
And "wlog $n$ is even" in a statement about all integers is wrong unless some symmetry of the statement turns an odd $n$ into an even one.

### Watch out

Two wlog steps can clash.
After "wlog $a \le b$", the step "wlog $a \ge 0$, by changing all signs" is wrong, because changing the signs turns $a \le b$ into $-a \ge -b$.
For $a = -3$ and $b = 1$, the sign change gives $(3, -1)$ with $a > b$, and a second exchange gives $(-1, 3)$ with $a < 0$, so the two assumptions are never reached together.
Each later wlog step must use a symmetry that keeps the earlier assumptions.

The second trap is to leave the symmetry unnamed.
"Wlog $x \le y \le z$" in a statement about three numbers needs the statement to be unchanged under every permutation of $x$, $y$ and $z$, not just under one exchange.

### Writing it up

Name the symmetry and the case in one sentence: "Both sides are unchanged when $a$ and $b$ are exchanged, so we may assume $a \le b$."
Then prove the chosen case in full.
If the symmetry is less familiar, such as a change of sign or a permutation of three letters, check it on the page by writing out the transformed statement.

### History

John Harrison studied the formal content of wlog arguments in his paper "Without loss of generality" at the conference TPHOLs in 2009, and he implemented support for them in the HOL Light proof assistant.
Mathlib, the library of the Lean proof assistant, provides the tactic `wlog` for the same purpose.

### Try it

First, may you assume $x \le y$ when proving $x^2 + y^2 \ge 2xy$ for all real $x$ and $y$?
Yes: exchanging $x$ and $y$ changes neither $x^2 + y^2$ nor $2xy$, although the proof $(x - y)^2 \ge 0$ does not need the assumption.

Second, may you assume $x \le y$ when proving $x - y \le |x| + |y|$?
Not as it stands: the exchange gives $y - x \le |x| + |y|$, a different inequality, so the case $x > y$ needs its own argument.

## Explanations

### L1 human

Two friends compare their heights.
To say something about "the taller one and the shorter one", we can call the taller one Anna.
If Ben is in fact the taller one, we exchange the names, and nothing else changes.
So we lose nothing by assuming that Anna is the taller one.
That is what "without loss of generality" means: a choice that only fixes the names.

### L2 human

Let us prove that $x^2 + y^2 \ge 2|xy|$ for all real $x$ and $y$.
First the symmetry: replacing $x$ by $-x$, or $y$ by $-y$, changes neither $x^2 + y^2$ nor $|xy|$.
So we may assume $x \ge 0$ and $y \ge 0$, and then $|xy| = xy$.
Now complete the square:
$$x^2 + y^2 - 2xy = (x - y)^2 \ge 0.$$
So $x^2 + y^2 \ge 2xy = 2|xy|$ in the chosen case, and by the symmetry in every case.
Check: $x = 3$ and $y = -1$ give $10 \ge 6$.
The typical use is this: when absolute values or squares make the signs irrelevant, assume that all variables are at least $0$.
Watch out: the claim $x^2 + y^2 \ge -3xy$ does not allow this step, because replacing $x$ by $-x$ changes $-3xy$, and indeed it fails at $x = 1$, $y = -1$, where it says $2 \ge 3$.

### L3 human

In general, a group $G$ acts on the set of cases, the statement is invariant under the action, and a wlog step picks a representative in each orbit.
A proof on any set that meets every orbit proves the statement everywhere.
Normal forms in algebra are wlog steps of this kind: a statement about matrices that is invariant under conjugation can be proved for matrices in a normal form, such as the Jordan form over $\mathbb{C}$.
In formal proof the reduction that a book leaves to the reader must be proved, and this is the part that Harrison's work and the Lean `wlog` tactic make explicit.
Symmetry arguments sit next to invariants and extremal choices, which the topic [[counting, invariant and extremal arguments|GB14W4SYPK]] treats.
