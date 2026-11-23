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

Here are two proofs that there are infinitely many primes.
Euclid takes any finite list of primes and shows that their product plus one has a prime factor outside the list.
A second proof shows that the Fermat numbers $3, 5, 17, 257, \dots$ have no common factors, so each one brings at least one new prime.
Both proofs are correct, and the second even gives a bound: there are at least $n + 1$ primes up to $2^{2^n} + 1$.

Many theorems have more than one [[proof|0B94TKFQJX]], and mathematicians often prove a known theorem again by a new method.
Two proofs count as different when they rest on different main ideas, such as algebra in one and geometry in the other, and not just on different wording.
A new proof adds no certainty to a theorem that is already accepted.
What it can add is understanding, a more general result, a more [[elementary|84SZZBACP3]] route, or a method that solves other problems.

## Motivation

Once a theorem has a correct proof, its truth is settled.
Yet the [[Pythagorean theorem|0VP3A1290K]] has hundreds of published proofs, and the law of [[quadratic reciprocity|085MJS6907]] has more than two hundred.
Gauss himself kept returning to quadratic reciprocity and found eight proofs.
So mathematicians must see something in a proof beyond the fact that it is correct, and the cases below show what that is.

## Notation

There is no special notation, but a few phrases recur.
An elementary proof avoids advanced tools, such as complex analysis for a theorem about integers, and is not necessarily easy.
A conceptual proof explains the result through a general structure.
A bijective or combinatorial proof counts one set in two ways, and a geometric proof argues from a figure made precise.

## Remarks

### Why prove a theorem again

A second proof can show why a theorem is true, when the first only shows that it is true.
A proof that uses fewer of the hypotheses proves a stronger theorem, so a new proof can bring generality.
A proof that avoids advanced tools opens the result to more readers and shows that the tools were not needed.
A new proof can also introduce a technique that later solves other problems.
For long or computer-assisted results, an independent proof raises confidence, as the second proof of the four color theorem did in 1997.
Finally, a shorter or clearer proof is easier to teach, and the ideal of such proofs is the subject of [[proofs from the Book|A4RJYP79A7]].

### The Pythagorean theorem

Euclid proves the theorem as Proposition 47 of Book I, with areas of triangles and squares.
Elisha Loomis collected $370$ proofs in the 1940 edition of his book *The Pythagorean Proposition*.
Other proofs use similar triangles, the [[rearrangement picture|T6WDA860PA]], or [[the dot product|J157D5FVP4]].
The last of these is the one that generalizes: the same computation proves the theorem in every [[inner product space|794QRK467A]].

### Quadratic reciprocity

Gauss found his first proof in 1796 and published two proofs in the *Disquisitiones Arithmeticae* of 1801.
He found eight proofs in all, and six were published in his lifetime.
[[Gauss's lemma|037ACYXB5Z]] leads to [[a proof by counting lattice points|AAVMMKTYNX]], and other proofs use Gauss sums or algebraic number theory.
Several of these methods later extended to higher reciprocity laws, which one proof alone would not have suggested.

### The primes, twice

For the infinitude of primes, [[Euclid's theorem|0292EPPPT0]] has Euclid's proof from Book IX of the *Elements* and [[a variant with $n! + 1$|TMXSM5BNVK]].
Euler showed that the sum of the reciprocals of the primes diverges, which gives more than infinitely many primes.
Hillel Furstenberg published a proof with topology in 1955.

The [[prime number theorem|0EHBY5Y84N]] gives a sharper case.
Hadamard and de la Vallée Poussin proved it independently in 1896 with complex analysis.
In the late 1940s Selberg and Erdős found elementary proofs, which showed that complex analysis was not necessary, although the elementary proofs are longer.

### What is not a new proof

A proof that changes only the letters, or the order of two independent steps, is not a new proof, because the main idea is the same.
A computer check of more cases of a theorem that is already proved is not a new proof either, because it covers finitely many cases and the theorem is general.

### Watch out

Do not think that a second proof is sought because the first might be wrong.
For accepted short proofs the reason is almost always insight or method, not doubt.
Do not think that the shortest proof is always the best, since a short proof can rest on a long theory and explain less than a longer direct one.
And do not count two presentations of one argument as two proofs, which is also why counts such as "$370$ proofs" are not exact.

### Try it

First, does the proof by contradiction of Euclid's theorem differ from the direct proof that builds a new prime from a list?
No: both rest on the number $p_1 \cdots p_k + 1$, so they are two presentations of one proof.

Second, what does the Fermat number proof give that Euclid's does not?
It gives at least $n + 1$ primes up to $2^{2^n} + 1$, because $F_0, \dots, F_n$ are pairwise coprime and each is at most $F_n$.

## Explanations

### L1 human

You can show that $1 + 3 + 5 + 7 = 16 = 4^2$ in more than one way.
One way is to add the numbers.
Another way is to draw a $4 \times 4$ square of dots and split it into L-shapes of $1$, $3$, $5$ and $7$ dots.
The second way shows why the sum of the first odd numbers is always a square number.
Mathematicians look for new proofs of old facts for this reason: a new proof can show the reason behind the fact.

### L2 human

We give the two proofs of the Summary and compare them.
For Euclid's proof, let $p_1, \dots, p_k$ be any finite list of primes and put $N = p_1 \cdots p_k + 1$.
Each $p_i$ divides $N - 1$, so it cannot divide $N$, since it would then divide $N - (N - 1) = 1$.
As $N \ge 2$, it has a prime factor, and that prime is not in the list.

For the second proof, let $F_n = 2^{2^n} + 1$, so $F_0 = 3$, $F_1 = 5$ and $F_2 = 17$.
By induction on $n$,
$$F_0 F_1 \cdots F_{n-1} = F_n - 2,$$
and for $n = 2$ this reads $3 \cdot 5 = 15 = 17 - 2$.
If a prime $p$ divides $F_m$ and $F_n$ with $m < n$, then it divides $F_n - F_0 \cdots F_{n-1} = 2$, which is impossible because $F_n$ is odd.
So the Fermat numbers are pairwise coprime, their prime factors are all different, and there are infinitely many primes.

Euclid builds one number outside a finite list, while the second proof builds an infinite sequence of pairwise coprime numbers and so also counts primes.
The typical reason for a second proof is such extra information.
Watch out: $N$ in Euclid's proof need not be prime, since for the first six primes $N = 30031 = 59 \cdot 509$.

### L3 human

The value of a proof beyond correctness is a theme of the philosophy of mathematical practice.
Some authors separate proofs that convince from proofs that explain, and many new proofs are sought for the second reason.
In research a conceptual reproof often comes with a generalization: Gauss sums led to reciprocity laws in cyclotomic fields, and class field theory contains quadratic reciprocity as a special case.

A second proof also matters for acceptance.
For very long or computer-assisted results, an independent proof or a formal proof is the strongest check, as [[acceptance of proofs|MJ3EHQJJHX]] and [[computer-assisted proof|MC18C7BMFT]] explain.
The search for short, clear proofs leads to the ideal of [[proofs from the Book|A4RJYP79A7]], and the ranking of proofs by depth and by economy is treated in [[elegant and deep|STHWD1K9AN]].
