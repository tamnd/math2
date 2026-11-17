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

Scratch work is the private search for a proof, and the final proof is the public text that presents it.
The scratch work may start from the goal, guess, test cases and work backward.
The final proof starts from the hypotheses and known facts and goes forward, each step an implication with a reason.
The method is to keep the two apart.
The writer finds the argument in scratch work, then writes the final proof in the forward order and leaves the search out of it.
It matters because the order in which an argument is found is often the reverse of the order in which it is valid.

## Motivation

Many proofs need an object or a constant that the hypotheses do not give.
Examples are the $\delta$ of a limit, the preimage of a point, and the first line of an inequality.
The natural way to find it is to start from what we want and ask what would make it true.
This search goes from the goal backward to the givens.
A text in that order shows "the goal implies something true", which is not a proof of the goal.
The page on [[conditional statements|FA6YZGR2SS]] explains this for the direction of an implication.
So the writer needs two documents: the search, in any order, and the proof, in the order of logic.
The model case is the [[epsilon-delta proof|RXG5JTZ2PZ]], where the scratch work finds $\delta$ from the goal $\lvert f(x) - L \rvert < \varepsilon$, and the proof starts with "Let $\varepsilon > 0$".

## Remarks

### When it applies

1. The proof must name an object: a $\delta$, an $N$, a preimage, a witness of an existence claim, or a constant in an estimate.
2. The proof of an inequality or an identity is found by transforming the goal.
3. The writer does not yet see the first line of the proof.

### The steps

1. Write the goal and the givens on the scratch sheet.
2. Work backward from the goal: ask which simpler statement would imply it. Work forward from the givens: ask what they imply.
3. Stop when the two chains meet, or when the backward chain names the object that the proof needs.
4. Mark each backward step that is not an equivalence. The final proof must not use such a step in the reverse direction.
5. Write the final proof forward: the hypotheses, the definition of each named object, each step with its reason, and the conclusion.
6. Remove from the final proof every trace of the search, such as "we want", "this would give" or "solving for $x$".
7. Check the final proof alone, without the scratch sheet.

### Examples

1. [[The limit of x^2 at 2 by epsilon and delta|FZ2S47KDE7]]: the scratch work bounds $\lvert x + 2 \rvert$ and finds $\delta = \min(1, \varepsilon/5)$. The final proof starts with $\varepsilon$ and defines $\delta$ at once.
2. [[The inequality x + 1/x ≥ 2 from scratch work to final proof|38RY69T8DQ]]: the scratch work reduces the claim to $(x - 1)^2 \ge 0$. The final proof starts there.
3. [[Finding a preimage in scratch work for the surjectivity of 3x − 7|13PJG9NT29]]: the scratch work solves $3x - 7 = y$, and the final proof only checks $f\left(\frac{y + 7}{3}\right) = y$.
4. An existence proof for an integer solution of $2x - 3y = 2$: the scratch work finds $x = 4$, $y = 2$ by trial. The proof is the single sentence "Take $x = 4$ and $y = 2$; then $2x - 3y = 8 - 6 = 2$."
5. A proof by [[mathematical induction|0ASJVEFA9J]] of a closed formula: the scratch work guesses $1 + 3 + \cdots + (2n - 1) = n^2$ from the cases $n = 1, 2, 3$. The proof then proves the formula by induction without the guess.

### Non-examples

1. [[Scratch work handed in as a proof of the two-number AM-GM inequality|80MA96BC4V]]: the text starts from the claim and ends at a true fact. So it shows only that the claim implies a true statement.
2. [[A delta that depends on x proves a false limit|R86WEZ07QE]]: the scratch work leaves the variable $x$ in $\delta$, and the "final proof" uses it. The final proof must name $\delta$ before $x$ is chosen.
3. A final proof that contains the sentence "solving $3x - 7 = y$ for $x$ gives $x = \frac{y+7}{3}$, so $x$ exists" is not separated from its scratch work. The solving assumes that a solution exists, so it does not prove existence.

### Basic properties

1. A backward chain of equivalences, read forward, is a proof. A backward chain with a one-way step is not, and the page [[squaring both sides does not prove an identity|FGS7ZJJYRK]] shows a failure.
2. The final proof is often shorter than the scratch work, because a candidate is easier to check than to find.
3. The final proof may look unmotivated. A writer can add one sentence of motivation outside the proof, such as "We will compare with $(x - 1)^2$", without making it a step.
4. The scratch work need not be correct. Only the final proof must be correct, and it must be checked alone.

### When it fails

The method does not apply when the search and the proof have the same order.
A direct calculation, such as the expansion of $(a + b)^2$, is found and written in the same forward order, and there is no separate scratch work.
The method also does not help when the backward search finds no known fact.
Then the writer needs another idea, such as a change of method or a stronger claim.

### Related methods

1. [[Writing proofs|8JQHJK94RZ]]: the general rules for the final proof.
2. [[Writing epsilon-delta proofs|RXG5JTZ2PZ]]: the model case of this method in analysis.
3. [[Proof strategies by logical form|872K5XB580]]: the scratch sheet of Velleman's method lists givens and goals, and each strategy changes them.
4. The forward-backward method of Solow organizes the search as forward steps from the hypotheses and backward steps from the conclusion, until the two chains meet.
5. [[Proving injectivity and surjectivity|DD2P85Y8E9]]: the preimage of a surjectivity proof is found in scratch work.

### History

Pappus of Alexandria described two methods: analysis, which starts from what is sought and works backward, and synthesis, which reverses the analysis into a proof.
Pólya's "How to Solve It" presents this pair as a heuristic, in the entries of its dictionary on working backwards and on Pappus.
Velleman's "How to Prove It" uses the terms "scratch work" and "final proof" and asks the student to keep them apart.

### Common errors

1. The student hands in the scratch work, which starts from the claim. The page [[fallacies and errors in proofs|T6QQ749DM5]] treats this error as the derivation of a true statement from the claim.
2. The student reverses a step that holds only one way, such as squaring or multiplying by a number of unknown sign.
3. The student keeps a variable of the scratch work in the final proof, such as $x$ in the $\delta$ of a limit. The order of the quantifiers forbids this.

## Explanations

### L1 human

A builder uses a scaffold to put up a wall, and then takes the scaffold away.
Scratch work is the scaffold of a proof.
To show that $x + \frac1x \ge 2$ for positive $x$, we may start from the claim and simplify it until we reach "a square is never negative".
That search is useful, but the proof tells the story in the other order: it starts with the square and ends with the claim.
For $x = 3$ the claim says $3 + \frac13 \ge 2$, and the square is $(3 - 1)^2 = 4$.
The reader of the proof sees the wall and does not need the scaffold.

### L2 human

We find and write a proof that $\lim_{n \to \infty} \frac{3n + 1}{n + 2} = 3$.

1. Scratch: we need $\left\lvert \frac{3n + 1}{n + 2} - 3 \right\rvert < \varepsilon$. We compute $\frac{3n + 1}{n + 2} - 3 = \frac{3n + 1 - 3n - 6}{n + 2} = \frac{-5}{n + 2}$.
2. Scratch: so we need $\frac{5}{n + 2} < \varepsilon$. This holds if $n > \frac{5}{\varepsilon}$, because then $n + 2 > \frac5\varepsilon$.
3. Proof: let $\varepsilon > 0$. Choose an integer $N > \frac{5}{\varepsilon}$, which exists by the [[Archimedean property|0A74SX55QP]].
4. Proof: let $n \ge N$. Then $n + 2 > n \ge N > \frac{5}{\varepsilon}$, so $\frac{5}{n + 2} < \varepsilon$.
5. Proof: since $\frac{3n + 1}{n + 2} - 3 = \frac{-5}{n + 2}$, we get $\left\lvert \frac{3n + 1}{n + 2} - 3 \right\rvert = \frac{5}{n + 2} < \varepsilon$.
6. Proof: so the limit is $3$, by the definition of the limit of a sequence.

The typical use is every proof that needs a constant, a bound or a witness.
A trap is to write the proof with "we need" and "this holds if".
These phrases belong to the scratch work, and they make the proof run backward.

### L3 human

The pair of scratch work and final proof is the old pair of analysis and synthesis.
In logic it reflects the two ways to build a derivation, as in [[natural deduction|6KT3BJZ7D1]].
One way goes backward from the goal by the introduction rules, and the other goes forward from the hypotheses by the elimination rules.
Proof assistants make the split explicit, as on the page [[proof assistants and their design|YM6PRDE88V]].
The user works backward with tactics that change the goal, and the system records a forward proof term.
In analysis the scratch work is often a calculation of how small the error terms must be.
The final proof fixes the constants at the start, as in the [[epsilon over three argument|VXV7M0QDH6]].
In algebra and combinatorics the scratch work is a computation of examples, and the final proof may hide it completely.
The study of such searches belongs to [[heuristics of discovery|X1NSTVGDNQ]].
