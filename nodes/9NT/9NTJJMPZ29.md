---
tag: 9NTJJMPZ29
kind: example
name: Excluded middle for the halting problem has no Dialectica witness
msc: ["03F10", "03D10"]
topics: [8XY7JYZKFW]
audience: grad
not_instance_of:
  - target: HZ17ES9PDY
    note: "No closed term of system T witnesses the Dialectica translation of excluded middle for the halting predicate, because such a term would decide the halting problem."
uses: [ZREF8MTYNW, A4WR995XZP, S9DK13K5PS, Z7TN2B35B0]
sources:
  - url: https://en.wikipedia.org/wiki/Dialectica_interpretation
    locator: Classical logic
  - url: https://en.wikipedia.org/wiki/Halting_problem
    locator: lead section
---

## Example

Let $P(n, k)$ be the quantifier-free formula $T(n, n, k)$, built from [[Kleene's T predicate|S9DK13K5PS]]: program $n$ on input $n$ halts with computation $k$.
Let $H = \forall n\, (\exists k\, P(n, k) \vee \neg \exists k\, P(n, k))$, an instance of excluded middle and so a theorem of PA.
We show that no closed terms of [[system T|A4WR995XZP]] witness its [[Dialectica interpretation|ZREF8MTYNW]].

1. The two sides interpret as $(\exists k\, P(n, k))^D = \exists k\, P(n, k)$ and $(\neg \exists k\, P(n, k))^D = \forall k'\, \neg P(n, k')$.
2. By the clause for $\vee$, the disjunction has witness $(z, k)$ and challenge $k'$, with matrix $(z = 0 \to P(n, k)) \wedge (z \ne 0 \to \neg P(n, k'))$.
3. By the clause for $\forall$, the witness becomes a pair of functions of $n$:
   $$H^D = \exists Z, K\, \forall n, k'\, \bigl( (Z n = 0 \to P(n, K n)) \wedge (Z n \ne 0 \to \neg P(n, k')) \bigr).$$
4. Suppose closed terms $Z$ and $K$ of T make this matrix provable in T.
   The theorems of T are true in the standard model, and by normalization $Z$ and $K$ denote total computable functions.
5. If $Z n = 0$, then $P(n, K n)$ is true, so program $n$ halts on input $n$.
6. If $Z n \ne 0$, then $\neg P(n, k')$ for every $k'$, so program $n$ does not halt on input $n$.
7. So $Z$ decides the [[halting problem|Z7TN2B35B0]], which is impossible, and no such terms exist.

## Remarks

The example shows that the interpretation cannot be applied to PA directly: the flag $z$ in the clause for $\vee$ forces every witness of a disjunction to say which side holds.
The same argument works for every undecidable set in place of the halting set.

For a decidable property the formula does have a witness.
With $P(n, k) = (k \cdot k = n)$, take $Z n = 0$ exactly when $n$ is a square, and $K n$ its square root; for $n = 12$ we get $Z 12 = 1$, and indeed $k \cdot k = 12$ has no solution.

A classical proof is saved by the negative translation, and the witness then becomes harmless.
HA proves $\forall n\, \neg (\neg \exists k\, P(n, k) \wedge \neg \neg \exists k\, P(n, k))$, which says that neither side can be refuted.
Its interpretation asks for $Y$ with $\neg (\neg P(n, Y n k) \wedge \neg \neg P(n, k))$ for all $n$ and $k$.
The term $Y n k = k$ wins: it hands the opponent's own number back, and it never says whether program $n$ halts.

## Explanations

### L1 human

Classical logic says that every program either stops or runs forever.
The Dialectica interpretation asks for a program that tells, for each program, which case holds.
No such program exists, and this is the undecidability of the halting problem.
So the interpretation rejects the classical statement as it stands, and it accepts only a form with negations in front.

### L2 human

We check what the witness of step 3 would have to do on two programs.
For a program $n_1$ that halts with computation $k_1$, the witness must give $Z n_1 = 0$ and a halting computation $K n_1$, for example $k_1$.
For a program $n_2$ that loops, the witness must give $Z n_2 \ne 0$, and then $\neg P(n_2, k')$ holds for every $k'$.
So $Z$ must separate the halting programs from the others, which no computable function does.

The typical use of the example is to show why the negative translation comes before the interpretation of a classical proof.
Watch out: the negatively translated formula has a witness, but that witness answers challenges and never names the halting case.
