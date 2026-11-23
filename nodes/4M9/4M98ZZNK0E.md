---
tag: 4M98ZZNK0E
kind: concept
name: Checking a proof
aliases: [checking-a-proof]
msc: ["00A35"]
topics: [STSM6PR7TX]
audience: ug2
uses: [0B94TKFQJX, 40GCSM2G56, 0ED72CTBNP]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_proof
    locator: Nature and purpose
  - url: https://en.wikipedia.org/wiki/Peer_review
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Four_color_theorem
    locator: Early proof attempts
  - doi: 10.1080/00029890.1995.12004627
    locator: pages 600-608
  - book: isbn:9780691164076
    locator: Part III
---

## Summary

Checking a proof means deciding whether a written argument proves its stated result, and the sharpest tool for it is to run the argument on a case where the conclusion is false.
Here is a short argument that looks fine, which is a flawed example.

> Claim: if $f, g \colon \mathbb{R} \to \mathbb{R}$ are injective, then $f + g$ is injective.
> Suppose $f(x) + g(x) = f(y) + g(y)$.
> Since $f$ is injective, $f(x) = f(y)$, and since $g$ is injective, $g(x) = g(y)$.
> So $x = y$.

Run it on $f(x) = x$ and $g(x) = -x$, which are both injective, while $f + g$ is the zero function and is not injective.
With $x = 0$ and $y = 1$, the first line holds, since both sides are $0$.
The second line claims $f(0) = f(1)$, which is false.
So the argument breaks at the second line, and on reflection that line has no reason: injectivity turns $f(x) = f(y)$ into $x = y$, and says nothing about a sum.
The verdict is "wrong", with the line and the reason, and in this case the claim itself is false.

In general, a checker confirms that every step has a valid reason, that the cases cover everything, that every cited result is used within its hypotheses, and that the last line is the stated conclusion.
The result is a verdict, such as correct, correct with minor gaps, incomplete, or wrong, together with its reasons.

## Motivation

A proof can be wrong and still convince careful readers.
In 1879 Alfred Kempe published a proof of the [[four color theorem|0M406JC8J1]], and it stood until Percy Heawood found an error in 1890.
Errors of this kind are not slips of arithmetic.
Each line looks plausible, and the gap lies in a case or a dependence that the writer did not see.
A reader who reads for understanding, as in [[reading proofs|40GCSM2G56]], can miss such a gap.
Checking adds an adversarial attitude: the checker tries to break each step, and accepts the [[proof|0B94TKFQJX]] only when every attack fails.

## Remarks

### The method

Check the statement first: is it precise, with every variable quantified, and does the proof prove this statement rather than a special case, the [[converse|09A3N7ZN5G]] or a weaker form?
Then check the frame.
For a [[proof by contradiction|0J0XBKG64S]], is the assumed negation correct; for [[induction|0ASJVEFA9J]], are both the base case and the step there; for a [[proof by cases|0WCP0PVET6]], do the cases cover everything?

Check each step: write its reason, or note that it is missing, and redo each computation.
Check that each new object is defined before use and depends only on what is fixed at that point, since a $\delta$ that depends on $x$ is a typical fault, as in [[a delta that depends on x|R86WEZ07QE]].
Check that each cited result has its hypotheses satisfied where it is used.

Then mark where each hypothesis is used, and run the argument on a case where one hypothesis is dropped and the conclusion fails.
Some step must break there, and it must be a step that uses the dropped hypothesis.
Finish with the verdict and a list of problems, each tied to a line.

### Gaps and errors

A gap is a true step whose reason is missing.
A minor gap can be filled in a few lines by the intended reader, and a serious gap needs a new idea.
An error is a false step, and a [[counterexample|0ED72CTBNP]] to the step itself shows it.

A proof of a false statement contains at least one error.
A counterexample to the statement shows that an error exists, and running the argument on that counterexample finds where.
A correct proof of a different statement is also a failure: a proof that $a \mid b$ implies $a \mid bc$ does not prove that $a \mid bc$ implies $a \mid b$.
[[Fallacies and errors in proofs|T6QQ749DM5]] lists the common errors by type.

### Three checks in detail

[[Testing a boundedness argument on 1/x|YRZQ86RKYY]] checks a proof that a continuous function on $[0, 1]$ is bounded.
No line uses that the interval is closed, so the same argument would show that $1/x$ is bounded on $(0, 1]$, which is false, and the test finds the gap.

[[A student referee report on irrational numbers|DJ1RWAEHYD]] finds one minor gap and ends with the verdict "correct with a minor gap".
[[Testing the conclusion is not checking the proof|41W6CXZZZ6]] shows the opposite habit: a reader confirms a true statement on examples and accepts a circular argument for it.

### Writing a report

A short report has four parts.
It summarizes the claim and the method in a sentence or two, which shows that the checker understood the argument.
It gives the verdict.
It lists the problems, each with its line, its kind, such as gap, error or unclear notation, and a repair when one is known.
It adds comments on presentation, such as undefined symbols or missing words between formulas, as [[mathematical writing style|D5YPYTQ88G]] describes.
A good report criticizes the proof, not the writer, and gives a reason for each criticism.

### Facts about checking

The verdict "wrong" needs one failing step, but the verdict "correct" needs every step checked, so it costs far more work.
An argument that would apply word for word to a case where the conclusion fails cannot be correct.
A proof can be wrong while its statement is true, and then a repair may exist.
A [[structured proof|H2W8D7BMSW]], with numbered claims and sub-proofs, is easier to check, because each claim has its own short justification.
Lamport made this point in 1995 when he proposed the format.

### Watch out

Checking the statement on examples does not check the proof.
Examples can refute a statement, but they cannot confirm an argument.

Checking each computation but not the logic is not enough either, because a correct computation inside a wrong case split still gives a wrong proof.

A checker who accepts a step because it looks like a standard step has not checked it, and many hidden errors survive this way.
If a step is beyond the checker, the honest verdict is "I could not check step $k$", not "correct".
Long proofs are checked in parts, by several people, or with a [[proof assistant|YM6PRDE88V]].

### History

Alfred Kempe published his proof of the four color theorem in 1879, and Percy Heawood showed in 1890 that it contained an error.
Journals check papers by peer review, in which referees read a paper and report to the editor.
Pólya's stage of "looking back" in "How to Solve It" (1945) includes checking the result and the argument.

### Try it

Check this proof: "If $x^2 = 9$, then $x = 3$, because squaring $3$ gives $9$."
It proves the converse, and the test $x = -3$ shows that the claim itself is false.

A proof that every bounded sequence of real numbers converges never uses anything beyond boundedness.
Which test case exposes the gap?
The sequence $(-1)^n$ is bounded and does not converge.

## Explanations

### L1 human

Checking a proof is like checking a long calculation, but each step is a sentence, not a sum.
For each sentence, the checker asks: why is this true?
A good trick is to try the argument on a case where the answer is known to be wrong.
For example, an argument that "proves" that every number is even must break somewhere when we try it on $3$.
If it does not break on $3$, it cannot be a correct argument.

### L2 human

We check a short proof that if $a \mid b$ and $a \mid c$, then $a \mid (b + c)$, for integers $a$, $b$ and $c$.

> Write $b = ak$ and $c = al$.
> Then $b + c = a(k + l)$.
> So $a \mid (b + c)$.

The statement is precise, and the frame is a [[direct proof|0NTF6DMVAP]] that assumes both hypotheses.
The first line uses both hypotheses with the definition of divisibility, and the different letters $k$ and $l$ let the multipliers differ.
The second line is the distributive law, and $a = 3$, $b = 6$, $c = 9$ give $15 = 3 \cdot 5$.
The third line needs $k + l$ to be an integer, which the proof leaves out, so there is a minor gap.

Now drop the hypothesis $a \mid c$ and take $a = 3$, $b = 6$ and $c = 1$.
The first line fails, since $1 = 3l$ has no integer solution, so the proof uses that hypothesis where it must.
The verdict is: correct, with one minor gap in the third line.
Watch out: without a case where the conclusion fails, a checker does not know that each hypothesis does real work.

### L3 human

Checking is the human counterpart of proof verification in logic.
A formal proof can be checked by an algorithm, because each step must match a rule of inference, and a proof assistant runs such an algorithm.
An informal proof cannot be checked mechanically, so its acceptance rests on the social process of reading, refereeing and use, discussed under [[rigor and the acceptance of proofs|1BTHSHST4M]].

The test of a failing case has a precise form.
A sound argument that uses only the hypotheses $H_1, \dots, H_k$ proves its conclusion in every model of $H_1, \dots, H_k$.
So a model of those hypotheses in which the conclusion fails shows that the argument must use something more.
This is the idea of independence proofs, applied to a single argument instead of to a whole theory.
