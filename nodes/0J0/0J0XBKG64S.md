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

To show that something cannot happen, imagine that it does, and follow the consequences until they break a known fact.
This is the oldest trick in the proof book, and it is the natural tool for statements such as "there is no ..." or "$x$ is irrational".

Here is the classic case: $\sqrt{2}$ is not a rational number.
Suppose it were, and write $\sqrt{2} = a / b$ with positive integers $a$ and $b$ that have no common factor.
Squaring gives
$$a^2 = 2b^2,$$
so $a^2$ is even, and then $a$ is even by [[the lemma on even squares|MKNWSR8WRN]].
With $a = 2c$ we get $4c^2 = 2b^2$, so $b^2 = 2c^2$ and $b$ is even too.
Now $2$ is a common factor of $a$ and $b$, which contradicts the choice of $a$ and $b$, so $\sqrt{2}$ is irrational.

In general, a *proof by contradiction* of a [[proposition|0ZGC7ZESYN]] $P$ assumes the [[negation|0XR7A7RSXB]] $\neg P$ and derives a contradiction, some statement $R$ together with $\neg R$.
This shows $\neg\neg P$, and the [[double negation law|0NFAGWH84K]] then gives $P$.
A closely related form, the *proof of a negation* or *refutation*, proves $\neg P$ by assuming $P$ and deriving a contradiction.
The proof for $\sqrt{2}$ has this second form, since "irrational" means "not rational".

## Motivation

Negative statements give a direct proof nothing to compute with: "$\sqrt{2}$ is not a fraction", "there is no largest prime", "no integer solves this equation".
Assuming the opposite creates an object to study: a fraction equal to $\sqrt{2}$, a largest prime, an integer solution.
The proof then studies that object until it finds an impossible property.
So the method turns "show that nothing has property $X$" into "study a thing with property $X$".

The method runs through all of mathematics.
[[Cantor's theorem|0WTEMGYV2C]] shows that no function from a set $S$ onto its power set exists, because the set $\{x \in S : x \notin f(x)\}$ would be a value of $f$ and not a value of $f$.
The [[undecidability of the halting problem|Z7TN2B35B0]] shows that a program deciding halting would give a program that halts exactly when it does not halt.
In number theory it takes the forms of [[infinite descent|0EFYCFHYFG]] and the [[minimal counterexample|JGRCNPKNGG]].

## Notation

A proof opens with "Suppose, for a contradiction, that ..." or "Assume the contrary."
It ends with "This is a contradiction." or with a symbol such as $\Rightarrow\!\Leftarrow$ or $\bot$, followed by one of the [[end of proof marks|ET9J6R9T5C]].
The Latin name is *reductio ad absurdum*, "reduction to the absurd", and *indirect proof* is also common.
Logicians keep the name proof by contradiction for the form that proves $P$ from the absurdity of $\neg P$, which the glossary calls [[classical reductio ad absurdum|TAQKQEGP19]]; many textbooks use the name for both forms.
In Lean, the Mathlib tactic `by_contra h` adds the hypothesis `h : ¬P` and leaves the goal `False`, while `intro h` on a goal `¬P` gives `h : P` and the goal `False`, which is the refutation form.

## Remarks

### Why it works, and which logic it needs

Suppose an assumption $A$, together with known facts, leads to both $R$ and $\neg R$.
A true assumption cannot do that, so $A$ is false, that is, $\neg A$ holds.
This step is valid in every standard logic, because $\neg A$ means exactly "$A$ leads to absurdity".
So a refutation, which takes $A = P$ and concludes $\neg P$, is valid in [[intuitionistic logic|Q11N8X99FK]] as well as in classical logic.

The strict form takes $A = \neg P$, concludes $\neg\neg P$, and then removes the two negations to get $P$.
That last step is the double negation law, which is equivalent to the [[law of excluded middle|0RYYK8PG4S]] over intuitionistic logic.
So only the strict form needs classical logic.
Watch the difference in the two most famous examples: the irrationality of $\sqrt{2}$ and Cantor's theorem are refutations, and they are constructively valid.

### A proof that needs the strict form

Here is a positive statement proved by the strict form: for every function $f$ from the natural numbers to the natural numbers, there is an $n$ with $f(n) \le f(n + 1)$.
Suppose not, so $f(n) > f(n + 1)$ for every $n$.
Each step lowers the value by at least $1$, so by induction
$$f(n) \le f(0) - n \quad \text{for every } n.$$
At $n = f(0) + 1$ this gives $f(n) \le -1$, which is impossible for a natural number.
So there is an $n$ with $f(n) \le f(n + 1)$.

The proof shows that such an $n$ exists, but it never names one.
That is typical of the strict form when it proves an existence statement, and it makes the proof a [[non-constructive existence proof|JZQVJ9XT63]].

### Infinitely many primes

[[Euclid's theorem|0292EPPPT0]] says that there are infinitely many [[primes|0SN0MAEKYX]].
Suppose there were only finitely many, $p_1, \dots, p_n$, and put $N = p_1 p_2 \cdots p_n + 1$.
Then $N > 1$, so $N$ has a prime factor $q$.
Each $p_i$ divides $N - 1$, so if $q$ were some $p_i$, it would divide $N - (N - 1) = 1$, which is impossible.
So $q$ is a prime outside the list, and this contradicts the assumption.

Watch out: the proof does not show that $N$ is prime.
For the first six primes,
$$N = 2 \cdot 3 \cdot 5 \cdot 7 \cdot 11 \cdot 13 + 1 = 30031 = 59 \cdot 509.$$
Check: $59 \cdot 509 = 29500 + 531 = 30031$.
The argument only needs some prime factor of $N$, and $59$ and $509$ are both missing from the list.

### More examples

[[The logarithm of 3 to base 2 is irrational|8V5FDX9562]]: if $\log_2 3 = a / b$ with positive integers, then $2^a = 3^b$, an even number equal to an odd number.
[[There is no smallest positive rational number|35BR47HYGP]]: if $r$ were the smallest, then $r / 2$ would be a smaller one.
The irrationality of $\sqrt{2}$ also has a [[proof by lowest terms|7GNMP4Q32W]], written out in full, and a proof by [[infinite descent|0EFYCFHYFG]], which replaces the choice of lowest terms with an endless chain of smaller fractions.

### What is not a proof by contradiction

If the assumed negation is never used, the proof is [[a direct proof in disguise|K686ZGPR17]].
Delete the assumption, and if every step still stands, write the direct proof instead.

A [[proof by contrapositive|0BB5TPGQ1N]] of "if $A$, then $B$" assumes only $\neg B$ and reaches the specific statement $\neg A$.
It can be dressed as a contradiction, by assuming $A$ and $\neg B$ and noting the clash with $A$ at the end, but the dressing adds nothing.
A computation showing $x^2 + 1 \ge 1 > 0$ for all real $x$, and so that $x^2 + 1 = 0$ has no real root, is a direct proof of a negative statement, since nothing is assumed and later rejected.

### Watch out

The assumption must be the exact negation of the claim.
The negation of "every element of $S$ has property $X$" is "some element of $S$ lacks property $X$", not "no element of $S$ has property $X$"; the rules for [[negating mathematical statements|K930V33BSC]] give the right form.

A contradiction shows that something is wrong, but not which step is wrong.
If an unrelated step has an error, the proof may "contradict" a correct assumption.
From a contradiction every statement follows, by [[explosion|TTKZGJEEK7]], so a long proof by contradiction must have every other step checked with care.

### History

Greek geometers used indirect proofs, and [[Euclid's Elements|83WHDAV68J]] contains many of them.
Euclid's own proof about the primes is closer to a direct proof: given any finite list of primes, it produces a prime outside the list.
In the early 20th century Luitzen Egbertus Jan Brouwer rejected the law of excluded middle for infinite collections, and with it existence proofs by contradiction.
His view led to intuitionistic logic, which Arend Heyting made formal in 1930.

### Try it

First, prove that there is no largest even integer.
Suppose $m$ were the largest; then $m + 2$ is even and larger than $m$, a contradiction.

Second, decide which form proves "$\sqrt{3}$ is irrational", and finish the proof.
It is a refutation: assume $\sqrt{3} = a / b$ in lowest terms, so $a^2 = 3b^2$; then $3 \mid a$ by the [[proof by cases|0WCP0PVET6]] on remainders mod $3$, so $a = 3c$, $b^2 = 3c^2$, and $3 \mid b$ too, which contradicts lowest terms.

## Explanations

### L1 human

Suppose someone says: "There is a largest whole number."
Take that number and add $1$.
The result is a whole number larger than the "largest" one, which is impossible.
So the claim was false: there is no largest whole number.
A proof by contradiction works like this.
Imagine that the statement you want is false, follow the consequences, and reach something impossible.
Then the statement cannot be false.

### L2 human

Let us prove that no integer $n$ satisfies $n^2 = 4n + 2$.
Suppose, for a contradiction, that $n$ is such an integer.
The right side is $2(2n + 1)$, so $n^2$ is even, and then $n$ is even by [[the lemma on even squares|MKNWSR8WRN]].
Write $n = 2k$ and substitute:
$$4k^2 = 8k + 2, \qquad 2k^2 = 4k + 1.$$
The left side is even and the right side is odd, and no integer is both, so the assumption fails.
Check: the real roots of $n^2 - 4n - 2 = 0$ are $2 \pm \sqrt{6}$, and neither is an integer.
The problem shows the typical use, a statement of non-existence: assume an object exists, and find an impossible property of it.
Watch out: the assumption must be the exact negation, here "some integer $n$ has $n^2 = 4n + 2$".

### L3 human

In natural deduction, the strict form is the classical rule: from a derivation of $\bot$ under the assumption $\neg P$, conclude $P$.
Adding this rule to intuitionistic logic gives exactly classical logic, so the rule marks the border between the two.
The double negation translation of Gödel and Gentzen turns each classical proof into an intuitionistic proof of a translated statement, and for many statements about the natural numbers this recovers a constructive proof.
The method takes the form of diagonal arguments in set theory and computability, as in [[Cantor's diagonal argument|0XCH8QVDCQ]], and of descent and minimal counterexamples in number theory, which the topic [[induction and well-ordering as proof methods|EEH2F76CYQ]] treats.
