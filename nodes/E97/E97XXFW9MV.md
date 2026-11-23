---
tag: E97XXFW9MV
kind: concept
name: Scratch work and the final proof
aliases: [scratch-work-and-final-proof, scratch-work, analysis-and-synthesis]
msc: ["00A35"]
topics: [STSM6PR7TX]
audience: ug1
uses: [8JQHJK94RZ, 0B94TKFQJX, FA6YZGR2SS]
sources:
  - book: isbn:9781108439534
    locator: Chapter 3
  - book: isbn:9780691164076
    locator: Part III
  - url: https://en.wikipedia.org/wiki/(%CE%B5,_%CE%B4)-definition_of_limit
    locator: lead section
---

## Summary

The order in which you find a proof is often the reverse of the order in which you should write it.
Scratch work is the private search, which may start from the goal and work backward; the final proof is the public text, which starts from what is known and goes forward.

Here is a search for $\delta$ next to the proof that comes out of it.
The claim is that $x^2 \to 1$ as $x \to 1$: for every $\varepsilon > 0$ there is $\delta > 0$ such that $0 < |x - 1| < \delta$ implies $|x^2 - 1| < \varepsilon$.
The scratch work starts from the goal.

> We want $|x^2 - 1| < \varepsilon$, and $|x^2 - 1| = |x - 1| \, |x + 1|$.
> The factor $|x - 1|$ is small, but $|x + 1|$ needs a bound.
> If we also ask $|x - 1| < 1$, then $0 < x < 2$, so $|x + 1| < 3$.
> Then $|x - 1| < \varepsilon / 3$ would finish, so try $\delta = \min(1, \varepsilon / 3)$.

The final proof starts from $\varepsilon$ and names $\delta$ at once.

> Let $\varepsilon > 0$, and let $\delta = \min(1, \varepsilon/3)$.
> Let $x$ be a real number with $0 < |x - 1| < \delta$.
> Since $|x - 1| < 1$, we have $0 < x < 2$, so $|x + 1| = x + 1 < 3$.
> Since also $0 < |x - 1| < \varepsilon / 3$, we get $|x^2 - 1| = |x - 1| \, |x + 1| < \frac{\varepsilon}{3} \cdot 3 = \varepsilon$.
> $\square$

The scratch work says "we want" and "would finish"; the proof says "let" and "so".
The method is to find the argument in the first style and to write it in the second, with every trace of the search removed.

## Motivation

Many proofs must name an object that the hypotheses do not give: the $\delta$ of a limit, the preimage of a point, the starting inequality of an estimate.
The natural way to find it is to start from what you want and ask what would make it true.
That search runs from the goal back to the givens.
A text in that order shows only that the goal implies something true, and this is not a proof of the goal, as the page on [[conditional statements|FA6YZGR2SS]] explains for the direction of an implication.

So you need two documents: the search, in any order, and the proof, in the order of logic.
The model case is the [[epsilon-delta proof|RXG5JTZ2PZ]], which you meet in every first course in analysis.
The same split returns for the preimages of [[surjectivity proofs|DD2P85Y8E9]] and for the witnesses of existence proofs.

## Notation

There is no special notation.
Velleman's "How to Prove It" sets the two parts apart with the labels "Scratch work" and "Proof", and many courses copy this.
On a homework sheet, a line or a box between the two parts tells the grader which part to check.

## Remarks

### The steps of the method

1. Write the goal and the givens on the scratch sheet.
2. Work backward from the goal: which simpler statement would imply it?
   Work forward from the givens: what do they imply?
3. Stop when the two chains meet, or when the backward chain names the object that the proof needs.
4. Mark each backward step that is not an equivalence, such as squaring or multiplying by a number of unknown sign.
5. Write the final proof forward: the hypotheses, the definition of each named object, each step with its reason, the conclusion.
6. Remove every trace of the search, such as "we want", "this would give" or "solving for $x$".
7. Check the final proof alone, without the scratch sheet.

### Three searches and their proofs

For [[the inequality x + 1/x ≥ 2|38RY69T8DQ]] with $x > 0$, the scratch work multiplies by $x$ and reduces the claim to $(x - 1)^2 \ge 0$.
Each step is an equivalence, so the final proof can start from the square and run the chain forward.

For [[the surjectivity of 3x − 7|13PJG9NT29]], the scratch work solves $3x - 7 = y$ and finds $x = \frac{y + 7}{3}$.
The final proof only names this $x$ and checks $f(x) = y$ in one line.

For an integer solution of $2x - 3y = 2$, the scratch work tries small values and finds $x = 4$, $y = 2$.
The final proof is one sentence: "Take $x = 4$ and $y = 2$; then $2x - 3y = 8 - 6 = 2$."
In all three cases the proof is shorter than the search, because a candidate is easier to check than to find.

### When the search is handed in

The common failure is to hand in the scratch work.
[[A backward text for the AM-GM inequality|80MA96BC4V]] starts from the claim and ends at a true fact, so it shows only that the claim implies something true.
[[A delta that depends on x|R86WEZ07QE]] is a second failure: the scratch work leaves $x$ inside $\delta$, but in the definition of a limit $\delta$ must be chosen before $x$.
A third failure is a "proof" of surjectivity that says "solving $3x - 7 = y$ gives $x = \frac{y + 7}{3}$, so $x$ exists".
The solving assumed that a solution exists, so it cannot prove existence.

### Reversible and one-way steps

A backward chain of equivalences, read forward, is a proof.
A backward chain with a one-way step is not.
Squaring is the usual culprit: from the false claim $-2 = 2$ squaring gives the true $4 = 4$, as the page on [[squaring both sides|FGS7ZJJYRK]] shows.
So mark each one-way step on the scratch sheet, and in the final proof check that it is used only in the forward direction.

A final proof can look unmotivated, since it may start with a line such as "$(x - 1)^2 \ge 0$" that comes from nowhere.
You may add one sentence of motivation outside the proof, such as "We compare with $(x - 1)^2$", as long as it is not a step.

### When the method does not apply

Some arguments are found and written in the same forward order, such as the expansion of $(a + b)^2$.
Then there is no separate scratch work.
The method also does not help when the backward search reaches no known fact.
Then you need another idea, such as a different strategy or a stronger claim.

### Watch out

The phrases of the search must not leak into the proof.
A student writes "We need $\frac{5}{n + 2} < \varepsilon$, which holds if $n > \frac{5}{\varepsilon}$" inside a proof that a sequence converges.
That sentence runs backward: it says what would be enough, not what is true.
The correct move is to choose $N > \frac{5}{\varepsilon}$ first and then derive $\frac{5}{n + 2} < \varepsilon$ for $n \ge N$.

### History

Pappus of Alexandria described two methods of the Greek geometers: analysis, which starts from what is sought and works backward, and synthesis, which turns the analysis around into a proof.
Pólya's "How to Solve It" (1945) brought the pair back as a heuristic, with dictionary entries on Pappus and on working backwards.
Velleman's "How to Prove It" uses the terms "scratch work" and "final proof" and asks students to keep them apart.
Solow's "How to Read and Do Proofs" organizes the search as a forward-backward method, in which forward steps from the hypotheses meet backward steps from the conclusion.

### Try it

Find $\delta$ for the claim that $3x + 1 \to 7$ as $x \to 2$, and write the final proof.
Scratch: $|3x + 1 - 7| = 3|x - 2|$, so $\delta = \varepsilon / 3$ works; the proof reads "Let $\varepsilon > 0$ and $\delta = \varepsilon/3$; if $0 < |x - 2| < \delta$, then $|3x + 1 - 7| = 3|x - 2| < \varepsilon$."

A student "proves" that every real $x$ with $x^2 = 9$ equals $3$ by the text "$x = 3$, so $x^2 = 9$"; what went wrong?
The text runs from the conclusion back to the hypothesis, which is scratch work in the wrong direction, and the claim is in fact false for $x = -3$.

## Explanations

### L1 human

A builder uses a scaffold to put up a wall, and then takes the scaffold away.
Scratch work is the scaffold of a proof.
To show that $x + \frac1x \ge 2$ for positive $x$, you can start from the claim and simplify it until you reach "a square is never negative".
That search is useful, but the proof tells the story in the other order: it starts with the square and ends with the claim.
For $x = 3$ the claim says $3 + \frac13 \ge 2$, and the square is $(3 - 1)^2 = 4$.
The reader sees the wall and does not need the scaffold.

### L2 human

We find and write a proof that $\frac{3n + 1}{n + 2} \to 3$ as $n \to \infty$.
In scratch work we simplify the error:
$$\frac{3n + 1}{n + 2} - 3 = \frac{3n + 1 - 3n - 6}{n + 2} = \frac{-5}{n + 2}.$$
So we need $\frac{5}{n + 2} < \varepsilon$, and this holds when $n > \frac{5}{\varepsilon}$.

Now the proof, in forward order.
Let $\varepsilon > 0$, and choose an integer $N > \frac{5}{\varepsilon}$, which exists by the [[Archimedean property|0A74SX55QP]].
Let $n \ge N$.
Then $n + 2 > N > \frac{5}{\varepsilon}$, so $\frac{5}{n + 2} < \varepsilon$.
By the computation above, $\left| \frac{3n + 1}{n + 2} - 3 \right| = \frac{5}{n + 2} < \varepsilon$, so the limit is $3$.

Check: for $\varepsilon = 0.1$ we may take $N = 51$, and then $\frac{5}{53} \approx 0.094 < 0.1$.
The computation of the error appears in both parts, but only the proof fixes $\varepsilon$ and $N$ before it uses them.

### L3 human

The pair of scratch work and final proof is the old pair of analysis and synthesis.
In [[natural deduction|6KT3BJZ7D1]] it matches the two ways to build a derivation: backward from the goal by introduction rules, and forward from the hypotheses by elimination rules.
Proof assistants make the split explicit, as in [[proof assistants and their design|YM6PRDE88V]]: the user works backward with tactics that change the goal, and the system records a forward proof term.

In analysis the scratch work is often a computation of how small the error terms must be, and the final proof fixes the constants at the start, as in the [[epsilon over three argument|VXV7M0QDH6]].
In algebra and combinatorics the scratch work is a table of examples, and the final proof may hide it completely.
The study of such searches belongs to [[heuristics of discovery|X1NSTVGDNQ]], and the forward and backward chains return as the givens and goals of [[proof strategies by logical form|872K5XB580]].
