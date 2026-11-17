---
tag: 0J0XBKG64S
kind: concept
name: Proof by contradiction
aliases: [reductio-ad-absurdum, indirect-proof]
msc: ["00A35", "97E50"]
topics: [G9JFJGY4TQ, 958EF46EYJ]
audience: school
specializes: [0B94TKFQJX]
uses: [0B94TKFQJX, 0XR7A7RSXB, 0NFAGWH84K, K930V33BSC]
sources:
  - url: https://en.wikipedia.org/wiki/Reductio_ad_absurdum
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Proof_by_contradiction
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 3.2
same_as:
  wikidata: Q14402006
  wikipedia: Reductio ad absurdum
---

## Summary

A proof by contradiction proves a [[proposition|0ZGC7ZESYN]] $P$ in two stages.
First it assumes the [[negation|0XR7A7RSXB]] $\neg P$.
Then it derives a contradiction from this assumption, that is, some statement $R$ together with its negation $\neg R$.
Since a true assumption cannot lead to a contradiction, $\neg P$ is false, and $P$ is true by the [[double negation law|0NFAGWH84K]].
For an implication "if $A$, then $B$", the method assumes $A$ and not $B$ together.
The method proves statements that give little to start from, such as "there is no ..." or "$x$ is irrational", and it is one of the oldest methods of proof.

## Motivation

Some statements are negative: "$\sqrt{2}$ is not a fraction", "there is no largest prime", "no integer solves this equation".
A direct proof of a negative statement has no object to compute with.
Assuming the opposite creates such an object: a fraction equal to $\sqrt{2}$, a largest prime, an integer solution.
The proof then studies this object until it finds an impossible property.
So the method turns "show that nothing has property $X$" into "study a thing with property $X$".

## Notation

A proof opens with "Suppose, for a contradiction, that ..." or "Assume the contrary."
It ends with "This is a contradiction." or with a symbol such as $\Rightarrow\!\Leftarrow$ or $\bot$, and then with one of the [[end of proof marks|ET9J6R9T5C]].
The Latin name is reductio ad absurdum, "reduction to the absurd", and the name "indirect proof" is also common.
In Lean, the Mathlib tactic `by_contra h` adds the hypothesis `h : ¬ P` and leaves the goal `False`.

Two forms must be told apart.
Proof of a negation: to prove $\neg P$, assume $P$ and derive a contradiction.
Proof by contradiction in the strict sense: to prove $P$, assume $\neg P$ and derive a contradiction, then remove the double negation.
Logicians call only the second form proof by contradiction, and the glossary entry [[classical reductio ad absurdum|TAQKQEGP19]] names it.
Many textbooks call both forms proof by contradiction.

## Remarks

### Examples

1. [[The logarithm of 3 to base 2 is irrational|8V5FDX9562]]: if $\log_2 3 = a/b$, then $2^a = 3^b$, an even number equal to an odd number.
2. [[There is no smallest positive rational number|35BR47HYGP]]: if $r$ were the smallest, then $r/2$ would be smaller.
3. The [[irrationality of the square root of 2|0DZGSDHD92]]: the classical [[proof by lowest terms|7GNMP4Q32W]] assumes $\sqrt{2} = a/b$ and finds that $a$ and $b$ are both even. A second classical proof uses [[infinite descent|0EFYCFHYFG]].
4. [[Cantor's theorem|0WTEMGYV2C]]: if a function $f$ from a set $S$ onto its power set existed, the set $\{x \in S : x \notin f(x)\}$ would be a value of $f$ and not a value of $f$.
5. The [[undecidability of the halting problem|Z7TN2B35B0]]: a program that decides halting would give a program that halts exactly when it does not halt.

### Non-examples

1. [[A direct proof in disguise as a proof by contradiction|K686ZGPR17]]: the assumed negation is never used, so removing it leaves a direct proof.
2. A [[proof by contrapositive|0BB5TPGQ1N]] of "if $A$, then $B$" assumes only not $B$ and proves not $A$. It reaches a specific conclusion, not an arbitrary contradiction.
3. A computation that shows $x^2 + 1 > 0$ for all real $x$, followed by "so $x^2 + 1 = 0$ has no real solution", is a direct proof of a negative statement. No assumption is made and later rejected.

### Basic properties

1. The method uses the law $\neg\neg P \Rightarrow P$, which is equivalent to the [[law of excluded middle|0RYYK8PG4S]] over intuitionistic logic. So it is valid in classical logic and not in [[intuitionistic logic|Q11N8X99FK]].
2. Proof of a negation needs no such law: deriving a contradiction from $P$ proves $\neg P$ in both logics.
3. The contradiction may be with any known fact, with a hypothesis, or with the assumption $\neg P$ itself.
4. A proof by contrapositive can always be written as a proof by contradiction: assume $A$ and not $B$, derive not $A$, and note the contradiction with $A$. The reverse rewriting is not always possible in a natural way.
5. From a contradiction every statement follows, by the principle of [[explosion|TTKZGJEEK7]]. So a proof by contradiction that runs too long may contain an error that went unnoticed.

### History

Greek geometers used indirect proofs, and [[Euclid's Elements|83WHDAV68J]] contains many of them.
The Latin name reductio ad absurdum comes from medieval and later logic.
In the early 20th century Luitzen Egbertus Jan Brouwer rejected the law of excluded middle for infinite collections, and with it proofs of existence by contradiction; this led to [[intuitionistic logic|Q11N8X99FK]], which Arend Heyting made formal in 1930.

### Common errors

1. Using the method when a direct proof exists. If the assumed negation is never used, the proof is a direct proof with extra words; see non-example 1.
2. Negating the statement wrongly. The negation of "every element of $S$ has property $X$" is "some element of $S$ does not have property $X$", not "no element of $S$ has property $X$".
3. Reaching a contradiction through an error in an unrelated step. A contradiction shows that something is wrong, but not which assumption is wrong. Each step other than the assumption must be checked.

## Explanations

### L1 human

Suppose someone says: "There is a largest whole number."
Take that number and add $1$.
The result is a whole number larger than the "largest" one, which is impossible.
So the claim was false: there is no largest whole number.
A proof by contradiction works like this.
To prove a statement, imagine that it is false, follow the consequences, and reach something impossible.
Then the statement cannot be false, so it is true.

### L2 human

We prove: there is no integer $n$ with $n^2 = 4n + 2$.

1. Suppose, for a contradiction, that $n$ is an integer with $n^2 = 4n + 2$.
2. The right side is $2(2n + 1)$, so $n^2$ is even.
3. By [[the contrapositive of the parity fact|MKNWSR8WRN]], $n$ is even. Write $n = 2k$.
4. Substitute: $4k^2 = 8k + 2$, so $2k^2 = 4k + 1$.
5. The left side $2k^2$ is even, and the right side $4k + 1$ is odd.
6. An integer cannot be both even and odd. This is a contradiction.
7. So the assumption in step 1 is false, and no integer $n$ satisfies $n^2 = 4n + 2$.

The typical use is a statement of non-existence: assume an object exists, and derive an impossible property of it.

A trap: the assumption in step 1 must be the exact negation of the claim.
Here the claim is "no integer $n$ has $n^2 = 4n + 2$", so the negation is "some integer $n$ has $n^2 = 4n + 2$".

### L3 human

In natural deduction, proof by contradiction is the classical rule: from a derivation of $\bot$ under the assumption $\neg P$, conclude $P$.
Adding this rule to intuitionistic logic gives exactly classical logic, so the rule marks the boundary between the two.
Many proofs by contradiction can be rewritten as constructive proofs, and proof mining extracts explicit bounds from such rewritten proofs.
The method takes the form of diagonal arguments in set theory and computability, as in [[Cantor's diagonal argument|0XCH8QVDCQ]], and of [[infinite descent|0EFYCFHYFG]] and the minimal counterexample method in number theory, which the topic [[induction and well-ordering as proof methods|EEH2F76CYQ]] treats.
When a proof by contradiction proves an existence statement, the proof is [[non-constructive|JZQVJ9XT63]].
