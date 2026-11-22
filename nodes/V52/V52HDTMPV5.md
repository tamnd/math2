---
tag: V52HDTMPV5
kind: concept
name: Errors in induction proofs
aliases: [common-errors-in-induction, mistakes-in-proofs-by-induction]
msc: ["00A35", "97E50"]
topics: [EEH2F76CYQ]
audience: school
uses: [0ASJVEFA9J, 0KMVFSHFGZ]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Example of error in the induction step
  - url: https://en.wikipedia.org/wiki/All_horses_are_the_same_color
    locator: Explanation
  - book: isbn:9781108439534
    locator: Chapter 6
---

## Summary

An induction proof can look complete and still prove nothing, because one of its parts holds only on paper.
Here is a short example.
"Claim: $1 + 2 + \cdots + n = \tfrac{n(n+1)}{2} + 1$ for every $n \ge 1$. Step: if it holds for $n$, add $n + 1$ to both sides to get $\tfrac{(n+1)(n+2)}{2} + 1$."
The step is correct algebra, but the base case is false, since $1 \ne 2$, and so is the claim.

An *error in an induction proof* is a gap of this kind: a part of the proof that the principle of [[mathematical induction|0ASJVEFA9J]] needs and the argument does not establish.
A valid proof of "$P(n)$ for every $n \ge n_0$" proves $P(n_0)$, and proves the step for every $n \ge n_0$ using only the cases that the method allows.
The common errors are a missing or false base case, too few base cases in [[strong induction|0KMVFSHFGZ]], a step that assumes the result, a step that fails for some small $n$, a step that leaves the domain of the claim, an induction on the wrong variable, and a step that builds up instead of breaking down.

## Motivation

Induction proofs have a fixed shape, and the shape makes them look convincing.
A text with the words "base case", "induction hypothesis" and "induction step" can still prove nothing.
Famous false proofs, such as the [[proof that all horses are the same color|AJ2FDJJGTH]], hide one gap inside a step that looks correct.
Each error on the list can "prove" a false statement, so a reader who knows the list can check an induction proof in a few minutes.
The method is the same every time: find where each part of the principle is used, and test that part on the smallest case.

## Notation

We write $P(n)$ for the statement, $n_0$ for the first value, and "IH" for the induction hypothesis.
In ordinary induction the IH is $P(n)$ and the goal of the step is $P(n + 1)$.
In strong induction the IH is "$P(k)$ for all $n_0 \le k < n$" and the goal is $P(n)$.
Books use both forms, so a proof must say which form it uses, or the reader cannot check the range of the step.

## Remarks

### Errors in the base case

A missing base case leaves the step with nothing to start from.
The claim "$n^2 + n$ is odd" has a correct step, since $(n + 1)^2 + (n + 1) = (n^2 + n) + 2(n + 1)$ keeps the parity, but $0^2 + 0 = 0$ is even, and [[the step without a base case|TYDB4F6J2F]] proves nothing.

Too few base cases is the same error in strong induction.
A step that uses $P(n - 1)$ and $P(n - 2)$, or that splits $n$ into smaller parts, often works only from some $n_1$ on, and every value below $n_1$ must then be a base case.
The [[false proof that $2n = 0$|32AP5ZDMJJ]] writes $n = a + b$ with $a, b < n$, which is impossible for $n = 1$, so the false case $P(1)$ is never proved.

### Errors in the step

The step must prove $P(n + 1)$ from $P(n)$.
A step that starts from $P(n + 1)$ and derives something true assumes the result, and so does a step that uses "$P(k)$ for all $k$".

The step must also work for every $n \ge n_0$, including the smallest.
The [[horses argument|AJ2FDJJGTH]] has a step that works for $n \ge 2$ but fails from $1$ to $2$, where the two groups of one horse do not overlap, so the chain breaks at its first link.

The step must apply the IH only to objects that satisfy it.
In the false claim "if $\max(a, b) = n$ for natural numbers $a, b$, then $a = b$", the step passes from $a, b$ to $a - 1, b - 1$.
For $a = 0$, $b = 1$ and $n = 1$, the number $a - 1 = -1$ is not a natural number, so the IH does not cover it.

### Errors in the setup

An induction on the wrong variable fixes something that the step needs to change.
In the lattice path count $L(m, n) = L(m - 1, n) + L(m, n - 1)$, an induction on $n$ with $m$ fixed has no access to $L(m - 1, n)$.
The cure is to put "for all $m$" inside the claim, to use [[double induction|AABX4YPKRR]], to induct on $m + n$ as in [[counting lattice paths|HPB4XV5ACB]], or to [[strengthen the induction hypothesis|F94KJC2RXP]].

Building up is the error of [[induction on size|B2D8PTFNN1]].
The step must start from an arbitrary object of size $n + 1$ and break it down, and a step that adds to an object of size $n$ can miss objects.
The [[build-up argument for graphs|ECMJTM9A6C]] "proves" that every graph without isolated vertices is connected, and two disjoint edges on $4$ vertices refute it.

### Proofs that look wrong but are not

The [[proof that $F_n < 2^n$|3ZDPCTKC9M]] for the Fibonacci numbers uses two earlier cases and checks both base cases $n = 0$ and $n = 1$, so it has none of the errors.
A proof that starts at $n_0 = 4$ because the claim fails at $n = 3$ is also correct, as long as the step is proved for every $n \ge 4$; an example is $2^n \ge n^2$ for $n \ge 4$, an [[induction from an arbitrary base case|0GF6AJEBZ0]].
Finally, a step that uses $P(n)$ in a calculation that ends with $P(n + 1)$ does not assume the result, because $P(n)$ is the hypothesis that the method allows.

### How to check an induction proof

A false base case with a correct step still proves something: if $P(m)$ holds for some $m$, then $P(n)$ holds for every $n \ge m$.
A step that fails at one value $n_1$ breaks the chain there, and the proof gives only $P(n_0), \ldots, P(n_1)$.
So check the parts in this order.

1. Check the base cases by computation, and count them against the earlier cases that the step uses.
2. Find the smallest $n$ at which the step is used, and run the step there with the smallest objects.
3. At each use of the IH, check that the object is in the range of the IH.
4. Check that the step starts from an arbitrary object of the next size.

The errors are errors of the proof, not of the claim: a proof of the true claim $2^n \ge n^2$ for $n \ge 4$ without a base case is still wrong.

### History and Try it

The horses argument, the best known false induction, is credited to George Pólya.

First, what is wrong with "$n! > 2^n$ for $n \ge 1$: $(n + 1)! = (n + 1)\, n! > (n + 1) 2^n \ge 2^{n+1}$"?
The step is valid for $n \ge 1$, but the base case fails, since $1! = 1 < 2$; the claim holds from $n = 4$ on, where $24 > 16$, and fails at $n = 3$, where $6 < 8$.

Second, a student proves $P(n)$ for $n \ge 2$ with a step from $n - 1$ to $n$ that divides by $n - 2$; which value needs its own check?
The step is used at $n = 3$ first, where $n - 2 = 1$, so it is fine there, but if the step starts at $n = 2$ it divides by $0$, and $P(2)$ needs its own proof.

## Explanations

### L1 human

A proof by induction is like a row of dominoes.
The first domino must fall, and every domino must knock over the next one.
If the first domino never falls, nothing happens, however well the others are placed.
If one gap in the row is too wide, the dominoes stop there.
Most wrong induction proofs have exactly one of these faults: no first push, or one gap, often near the start of the row.

### L2 human

We find the error in a "proof" that $3^n = 1$ for every natural number $n$, by strong induction.
The argument checks $3^0 = 1$, then for $n \ge 1$ assumes $3^k = 1$ for all $k < n$ and writes
$$3^n = \frac{3^{n-1} \cdot 3^{n-1}}{3^{n-2}} = \frac{1 \cdot 1}{1} = 1.$$
Test the step at the smallest $n$ where it is used, $n = 1$.
There it needs $3^{n-2} = 3^{-1}$, and $-1$ is not a natural number, so the IH does not cover it.
So the step is valid only for $n \ge 2$, and $n = 1$ needs its own base case.
That base case is false, since $3^1 = 3 \ne 1$, so the claim fails at $n = 1$ and the proof is wrong.

The list of errors is a checklist: the base cases, the range of the step, and each use of the IH.
Watch out for a check of the step at a general large $n$ only, where every line of a wrong proof can be true.

### L3 human

Each error matches a hypothesis of the induction principle that the proof does not establish.
The principle asks for a set $S$ with $n_0 \in S$ and $n \in S \Rightarrow n + 1 \in S$ for every $n \ge n_0$; a missing base case drops the first condition, and a step that fails at $n_1$ drops the second at one point.
In strong induction there is no separate base case, but the step at the smallest values uses no earlier case, so those values are base cases in disguise.

In well-founded induction over any relation, the same errors appear as a step that fails at minimal elements, or a "smaller" object that is not smaller in the chosen order.
Proof assistants catch these errors mechanically: Lean's `induction` tactic produces one goal for each constructor, and Lean rejects a proof that leaves a goal open or uses a hypothesis that is not available.
Errors in proofs in general are the subject of [[fallacies and errors in proofs|T6QQ749DM5]].
