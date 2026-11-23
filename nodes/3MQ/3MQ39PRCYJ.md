---
tag: 3MQ39PRCYJ
kind: statement
role: lemma
name: Arithmetical comprehension is equivalent to the existence of ranges of one-to-one functions
msc: ["03B30", "03F35"]
topics: [BY8AAFN7C5]
audience: grad
about: [NAASTN80QN]
uses: [DNXCKXZZ08, K9XG0Z2N9V]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Arithmetical comprehension ACA0
---

## Statement

To prove all of arithmetical comprehension, it is enough to know that the set of values of every one-to-one function exists.

**Lemma.** Over [[RCA0|DNXCKXZZ08]], the following are equivalent.

1. [[Arithmetical comprehension|K9XG0Z2N9V]].
2. $\Sigma^0_1$ comprehension: $\exists X\, \forall n\, (n \in X \leftrightarrow \varphi(n))$ for every $\Sigma^0_1$ formula $\varphi$ in which $X$ is not free.
3. For every one-to-one function $f \colon \mathbb{N} \to \mathbb{N}$, the range $\{ m : \exists i\, f(i) = m \}$ exists.

## Remarks

### Why the function is one-to-one

Statement 3 asks for less than the same statement for all functions, since a one-to-one function is a special function.
A weaker hypothesis is easier to reach in a reversal, so the lemma is stated in this form.
The one-to-one form is what the [[Bolzano-Weierstrass reversal|HV153Y95MQ]] needs: there the sum $\sum_i 2^{-f(i)-1}$ must have distinct terms, or a repeated value would carry into a higher binary digit and spoil the decoding.

The version for arbitrary functions is also equivalent, since it lies between statements 3 and 1.

### What it gives you

To show that a theorem implies $\mathsf{ACA}_0$ over $\mathsf{RCA}_0$, it suffices to take any one-to-one $f$, build an instance of the theorem from $f$, and compute the range of $f$ from a solution.
For example, a computable one-to-one $f$ can list the halting set, so the lemma turns "the theorem has a solution" into "the halting set exists", relative to any parameter.
The [[existence of Turing jumps|10NR4PGXHW]] is one more form of the same axiom, because the jump of $X$ is infinite and is the range of a one-to-one function computable from $X$, which lists its elements without repeats.

### The converse

The lemma is a cycle of implications, and [[its proof|EW0QB5XZS9]] goes from 1 to 3, from 3 to 2, and from 2 to 1.
The step from 1 to 3 holds at once, because the range is defined by an arithmetical formula.

### Generalizations

For every $k \ge 1$, $\mathsf{RCA}_0$ proves that $\Sigma^0_1$ comprehension implies $\Sigma^0_k$ comprehension, and the proof climbs one quantifier at a time.
The same pattern appears one level up.
Over $\mathsf{ACA}_0$, $\Pi^1_1$ comprehension is equivalent to the statement that for every sequence of trees $(T_k)_k$ on $\mathbb{N}$ the set $\{ k : T_k \text{ has a path} \}$ exists.

## History

The lemma is a standard tool of reverse mathematics from its beginning in the 1970s, and it appears in the basic chapter on $\mathsf{ACA}_0$ of Simpson's book *Subsystems of Second Order Arithmetic* (1999).

## Explanations

### L1 human

Arithmetical comprehension says that every set described with number quantifiers exists.
The lemma says that it is enough to ask for one kind of set: the set of values of a function that never repeats a value.
For example, if a function lists the programs that halt, one by one and without repeats, its set of values is the halting set.
All other arithmetical sets then follow, one quantifier at a time.

### L2 human

Suppose that a theorem $\tau$ gives, for every one-to-one $f$, an object from which the range of $f$ is $\Delta^0_1$-definable.
Then $\mathsf{RCA}_0 + \tau$ proves statement 3, and the lemma gives arithmetical comprehension.
In the reversal of [[König's lemma|3P2J5NWCM1]], the object is a path through a tree that guesses, for each $i$, a $j$ with $f(j) = i$ or the answer "none".
Watch out: the reversal must compute the range from the solution with $\Delta^0_1$ comprehension only.
If the decoding step itself uses a $\Sigma^0_1$ definition, the argument assumes what it wants to prove.
