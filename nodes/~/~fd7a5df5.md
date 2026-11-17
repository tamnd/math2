---
tag: ~fd7a5df5
kind: concept
name: Heuristics in mathematics
msc: ["00A35"]
topics: [X1NSTVGDNQ]
audience: ug1
uses: [0B94TKFQJX, 5V35SGEN1T]
sources:
  - url: https://en.wikipedia.org/wiki/Heuristic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/How_to_Solve_It
    locator: Heuristics dictionary
  - book: isbn:9780691164076
---

## Summary

A heuristic in mathematics is a rule of thumb for finding a solution or a proof.
It is a question or a suggestion, such as "try a special case" or "work backwards", that often leads to an idea but does not guarantee one.
Heuristic reasoning is the provisional reasoning that a heuristic produces: a guess, a plan or a partial argument that still needs a [[mathematical proof|0B94TKFQJX]].
A heuristic differs from an algorithm, which is a procedure that always ends with a correct answer, and from a proof, which shows that a statement is true.
Heuristics matter because most of the work of mathematics happens before the proof exists, and heuristics are the means by which that work is organized and taught.

## Motivation

A finished proof shows that a theorem is true, but it seldom shows how anyone found it.
A student who reads only finished proofs learns to check arguments, not to make them.
The question "how was this found?" has no complete answer, because there is no algorithm that finds proofs of all true statements.
There are still patterns that experienced solvers use again and again.
They look at examples, they solve easier problems first, they compare the problem with problems that they know, and they draw figures.
George Pólya collected such patterns in *How to Solve It* (1945) and called their study heuristic, after the Greek verb for "to find".
His aim was to make the patterns explicit, so that they can be taught and practised.

## Notation

Pólya writes "heuristic" for the study of the methods of discovery and "heuristic reasoning" for reasoning that is provisional and only plausible.
He uses the word "plausible" in a technical sense for reasoning that makes a conjecture more credible without proving it; the topic [[plausible reasoning and experimental mathematics|DME0TPC348]] treats it.
In computer science and operations research, a heuristic is an algorithm that runs fast but has no guarantee of an optimal or correct answer, as in the topic [[heuristics and metaheuristics|FQBS45218T]].
The two meanings share the idea of "useful but not guaranteed", but this page uses the first meaning.

## Remarks

### Examples

1. [[The sum of the first n cubes found by heuristics|~ce271fb0]]: small cases suggest the formula $\left(\frac{n(n+1)}{2}\right)^2$, and a proof by induction confirms it.
2. [[An estimate of 2 to the 100 by rounding|~c958f751]]: the heuristic $2^{10} \approx 10^3$ suggests $2^{100} \approx 10^{30}$, and an exact inequality then settles which number is larger.
3. The four phases of [[Pólya's four steps|~e58f9baf]]: a plan for the whole solution, with a list of questions for each phase.
4. Single heuristics: [[analogy|~02ce22ff]], [[specialization|~701d4f5c]], [[generalization|~478f3b5e]], [[working backwards|~4d7ce252]], [[auxiliary problems|~a5a06d23]] and [[auxiliary elements|~fbc26a8c]].
5. Lakatos's [[proofs and refutations|~deab029f]]: a heuristic for the growth of a whole theorem, by the analysis of counterexamples.

### Non-examples

1. [[The Euclidean algorithm is not a heuristic|~76a2b296]]: it always ends with the greatest common divisor, so it is an algorithm.
2. A proof by [[mathematical induction|0ASJVEFA9J]] is not heuristic reasoning. Each step of the proof is justified, and the conclusion is certain.
3. A table of values of $n^2 + n + 41$ for $n = 0, 1, \ldots, 39$, which are all prime, is evidence and not a heuristic rule. It suggests a conjecture, and the conjecture fails at $n = 40$, since $40^2 + 40 + 41 = 41^2$.

### Basic properties

1. A heuristic gives no guarantee. The same suggestion can solve one problem and mislead on another, so each heuristic page of this topic gives a case where it fails.
2. The result of heuristic reasoning must be checked by a proof or refuted by a [[counterexample|0ED72CTBNP]]. Until then it is a [[conjecture|WMEMMHZ3BH]] or a plan.
3. Heuristics act on the problem, not on the logic of the answer. They change the problem (special case, generalization, auxiliary problem), its representation (figure, notation) or the order of the work (working backwards).
4. Several heuristics often work together. A special case suggests a pattern, an analogy suggests a proof, and working backwards finds the first step.
5. Heuristics are separate from [[proof methods|G9JFJGY4TQ]]. A proof method fixes the logical form of the final argument, and a heuristic helps to find its content.

### History

Pappus of Alexandria described analysis and synthesis in Book 7 of his *Collection*, and Descartes and Leibniz planned a general art of discovery.
Pólya revived the subject for mathematics with *How to Solve It* (1945), *Mathematics and Plausible Reasoning* (1954) and *Mathematical Discovery* (two volumes, 1962 and 1965).
Imre Lakatos described a heuristic of proof analysis and counterexamples in *Proofs and Refutations* (1976).
Alan Schoenfeld's *Mathematical Problem Solving* (1985) studied how students and experts use heuristics, and found that knowing the names of heuristics is not enough to use them.

### Common errors

1. To treat a heuristic as a proof. "The pattern holds for $n \le 5$" is a reason to try a proof, not a proof.
2. To treat a list of heuristics as an algorithm. A list gives questions to ask, and the solver must still choose and adapt them.
3. To give up a heuristic after one failure, or to keep it after many. Part of the skill is to decide when to change the plan.

## Explanations

### L1 human

A heuristic is a good habit for finding answers, such as "try a small case first" or "draw a picture".
It often helps, but it can fail.
For example, to find $1 + 2 + \cdots + 100$, a small case helps: $1 + 2 + 3 + 4$ pairs into $(1 + 4) + (2 + 3) = 5 + 5$.
The same pairing for $1$ to $100$ gives $50$ pairs that each add to $101$, so the sum is $5050$.
The habit "try a small case" found the idea of pairing.
The pairing argument then shows that the answer is right.

### L2 human

We use heuristics to find and then prove the sum $S_n = \frac{1}{1 \cdot 2} + \frac{1}{2 \cdot 3} + \cdots + \frac{1}{n(n+1)}$.

1. Specialize. $S_1 = \frac{1}{2}$, $S_2 = \frac{1}{2} + \frac{1}{6} = \frac{2}{3}$, $S_3 = \frac{2}{3} + \frac{1}{12} = \frac{3}{4}$.
2. Find the pattern. The values $\frac{1}{2}, \frac{2}{3}, \frac{3}{4}$ suggest $S_n = \frac{n}{n+1}$.
3. Look for a reason. The guess says $1 - S_n = \frac{1}{n+1}$, which suggests the identity $\frac{1}{k(k+1)} = \frac{1}{k} - \frac{1}{k+1}$.
4. Check the identity: $\frac{1}{k} - \frac{1}{k+1} = \frac{(k+1) - k}{k(k+1)} = \frac{1}{k(k+1)}$.
5. Prove. The sum of $\frac{1}{k} - \frac{1}{k+1}$ for $k = 1, \ldots, n$ telescopes to $1 - \frac{1}{n+1} = \frac{n}{n+1}$.

The typical use: steps 1 to 3 are heuristic and find the answer and the idea, and steps 4 and 5 are the proof.

A trap: step 2 alone proves nothing, because many formulas agree with three values; only step 5 makes the formula certain.

### L3 human

Heuristics belong to the methodology of mathematics, which studies how results are found, as the page [[methodology of mathematics|3FJ3XMV9KD]] explains.
Since the set of provable statements of a rich enough theory is not decidable, no algorithm finds all proofs, and some form of heuristic search is unavoidable for humans and machines.
Automated theorem provers and proof assistants use heuristics in the same sense as Pólya: as guides that order a search without changing what counts as a proof.
Schoenfeld's analysis adds that heuristics are one of several resources of a solver, beside knowledge, control of the solving process and beliefs about mathematics.
The later pages of this topic treat single heuristics, Lakatos's [[proofs and refutations|~deab029f]], [[mathematical intuition|~7a3195db]] and the [[psychology of mathematical invention|~b7d7d194]].
The topic [[plausible reasoning and experimental mathematics|DME0TPC348]] continues with the weighing of evidence for conjectures.
