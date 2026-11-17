---
tag: KNQDDN6PT2
kind: concept
name: Many proofs of one theorem
aliases: [multiple-proofs-of-theorems, new-proofs-of-old-theorems]
msc: ["00A35"]
topics: [1BTHSHST4M]
audience: ug1
uses: [0B94TKFQJX, 84SZZBACP3]
sources:
  - url: https://en.wikipedia.org/wiki/Pythagorean_theorem
    locator: Other proofs of the theorem
  - url: https://en.wikipedia.org/wiki/Quadratic_reciprocity
    locator: History and alternative statements
  - url: https://en.wikipedia.org/wiki/Euclid%27s_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Prime_number_theorem
    locator: Elementary proofs
---

## Summary

Many theorems have more than one [[proof|0B94TKFQJX]], and mathematicians often prove a known theorem again by a different method.
Two proofs of one theorem are different when they use different main ideas, for example algebra in one and geometry in the other, and not only different wording.
A new proof adds no certainty to a theorem that is already accepted, but it can give new understanding, a more general result, a more [[elementary|84SZZBACP3]] route, or a method that solves other problems.
This practice matters because it shows that a proof is valued for what it explains and makes possible, and not only for the truth that it establishes.

## Motivation

Once a theorem has a correct proof, its truth is settled.
Yet the [[Pythagorean theorem|0VP3A1290K]] has hundreds of published proofs, and the law of [[quadratic reciprocity|085MJS6907]] has more than two hundred.
Gauss himself gave several proofs of quadratic reciprocity.
So mathematicians must see something in a proof beyond the fact that it is correct.
The cases below show what they look for.

## Notation

There is no special notation.
Writers speak of "a new proof", "a simpler proof", an "elementary proof" (one that avoids advanced methods such as complex analysis), and a "conceptual proof" (one that explains the result through a general structure).
A proof is "bijective" or "combinatorial" when it counts the same set in two ways, and "geometric" when it argues from a figure that is made precise.

## Remarks

### Reasons for a new proof

- New insight: a second proof can show why the theorem is true, when the first only shows that it is true.
- Generality: a proof that uses less of the hypotheses proves a stronger theorem.
- Elementary methods: a proof that avoids advanced tools makes the result available to more readers, and it shows that the tools were not needed.
- New methods: a proof can introduce a technique that later solves other problems.
- Verification: an independent proof of a long or computer-assisted result increases confidence in it, as in the four colour case.
- Teaching and beauty: a shorter or clearer proof is easier to teach, and some proofs are valued as [[elegant|STHWD1K9AN]]; the page [[proofs from the Book|A4RJYP79A7]] treats this ideal.

### Examples

- The Pythagorean theorem. Euclid proves it in Book I, Proposition 47, with areas of triangles and squares. Elisha Loomis collected 370 proofs in his book The Pythagorean Proposition (1940 edition). Other proofs use similar triangles, a [[rearrangement picture|T6WDA860PA]], or [[the dot product|J157D5FVP4]], and the last one extends to [[inner product spaces|794QRK467A]].
- Quadratic reciprocity. Gauss gave his first proof in 1796, published proofs in the Disquisitiones Arithmeticae of 1801, and found eight proofs in total, of which six were published. More than 240 proofs have been published. [[Gauss's lemma|037ACYXB5Z]] leads to [[a proof by counting lattice points|AAVMMKTYNX]], and other proofs use Gauss sums or algebraic number theory. Several of these methods later extended to higher reciprocity laws.
- The infinitude of primes. [[Euclid's theorem|0292EPPPT0]] has Euclid's proof from Elements IX.20 and [[the proof with $n! + 1$|TMXSM5BNVK]]. Euler showed that the sum of the reciprocals of the primes diverges, which gives more. Hillel Furstenberg gave a proof with topology, and Filip Saidak gave a short proof by construction.
- The [[prime number theorem|0EHBY5Y84N]]. Hadamard and de la Vallée Poussin proved it in 1896 with complex analysis. In the late 1940s Selberg and Erdős found elementary proofs, which showed that complex analysis was not necessary.

### Non-examples

- A proof that changes only the letters or the order of two independent steps is not a new proof. The condition that fails: the main idea is the same.
- A computer check of more cases of a theorem that is already proved is not a new proof. The condition that fails: the check covers finitely many cases, and the theorem is general.

### Basic properties

- Two proofs of one theorem can use different hypotheses, so they can generalize in different directions.
- A new proof can be longer than the old one, and still be valued, when it is more conceptual or more general.
- The count of proofs of a theorem depends on what counts as "different", so counts such as "370" are not exact measures.

### History

Loomis's collection of proofs of the Pythagorean theorem, in its 1940 edition, lists 370 proofs.
In the 19th century, Gauss's repeated proofs of quadratic reciprocity set an example of proving a theorem again for its methods.
In the 20th century, the search for elementary proofs, as for the prime number theorem, and for formal proofs, as for the [[four colour theorem|0M406JC8J1]], gave new reasons to reprove known results.

### Common errors

- To think that a second proof is needed because the first might be wrong. For accepted short proofs, the reason is usually insight or method, not doubt.
- To think that the shortest proof is always the best. A short proof can depend on a long theory, and it may explain less than a longer direct proof.
- To count two presentations of the same argument as two proofs.

## Explanations

### L1 human

We can show that $1 + 3 + 5 + 7 = 16 = 4^2$ in more than one way.
One way is to add the numbers.
Another way is to draw a $4 \times 4$ square of dots and split it into L-shapes of $1$, $3$, $5$ and $7$ dots.
The second way shows why the sum of the first odd numbers is always a square number.
Mathematicians look for new proofs of old facts for this reason: a new proof can show the reason behind the fact.

### L2 human

We give two proofs that there are infinitely many primes, and we compare them.

1. Euclid's proof. Let $p_1, \dots, p_k$ be any finite list of primes, and let $N = p_1 p_2 \cdots p_k + 1$.
2. Each $p_i$ divides $N - 1$, so $p_i$ does not divide $N$, because it would then divide $N - (N - 1) = 1$.
3. Since $N \ge 2$, it has a prime factor, and this prime is not in the list. So no finite list contains all primes.
4. A proof with Fermat numbers. Let $F_n = 2^{2^n} + 1$, so $F_0 = 3$, $F_1 = 5$, $F_2 = 17$.
5. By induction, $F_0 F_1 \cdots F_{n-1} = F_n - 2$; for $n = 2$, $3 \cdot 5 = 15 = 17 - 2$.
6. If a prime $p$ divides $F_m$ and $F_n$ with $m < n$, then $p$ divides $F_n - F_0 \cdots F_{n-1} = 2$. But $F_n$ is odd, so no such $p$ exists.
7. So the numbers $F_0, F_1, F_2, \dots$ are pairwise coprime, and their prime factors are all different. This gives infinitely many primes.

The first proof builds a number outside a finite list, and the second builds an infinite sequence of pairwise coprime numbers.
The second proof is longer, and it gives more: $F_0, \dots, F_n$ have $n + 1$ different prime factors, each at most $F_n$, so at least $n + 1$ primes are at most $2^{2^n} + 1$.
The typical use of a second proof is such an extra piece of information.
A trap is to think that $N$ in step 1 must be prime: for the first six primes, $N = 30031 = 59 \cdot 509$.

### L3 human

The value of a proof beyond correctness is a theme of the philosophy of mathematical practice.
Some authors distinguish proofs that convince from proofs that explain, and many new proofs are sought for their explanatory power.
In research, a "conceptual" reproof often comes with a generalization: Gauss sums led to reciprocity laws in cyclotomic fields, and class field theory gives a general framework in which quadratic reciprocity is a special case.

A second proof also matters for acceptance.
For results with very long or computer proofs, an independent proof or a formal proof is the strongest check; see [[acceptance of proofs|MJ3EHQJJHX]] and [[computer-assisted proof|MC18C7BMFT]].
The search for short, clear proofs leads to the ideal of [[proofs from the Book|A4RJYP79A7]], and the ranking of proofs by depth and elegance is treated on the page [[elegant and deep|STHWD1K9AN]].
