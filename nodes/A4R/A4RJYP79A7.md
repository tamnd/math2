---
tag: A4RJYP79A7
kind: concept
name: Proofs from the Book
aliases: [book-proof, proof-from-the-book, proofs-from-the-book]
msc: ["00A35"]
topics: [1BTHSHST4M]
audience: ug2
uses: [0B94TKFQJX, STHWD1K9AN, ENY0GKRJS8, MD3MRG90W4, 0HGVCWQGY3]
sources:
  - url: https://en.wikipedia.org/wiki/Proofs_from_THE_BOOK
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Proofs_from_THE_BOOK
    locator: Content
  - url: https://en.wikipedia.org/wiki/Proofs_from_THE_BOOK
    locator: Outline
  - url: https://en.wikipedia.org/wiki/Paul_Erd%C5%91s
    locator: Personal life
---

## Summary

Choose any $6$ numbers from $1$ to $10$.
Then two of them have no common factor except $1$.
To see why, sort the numbers into the five boxes $\{1, 2\}$, $\{3, 4\}$, $\{5, 6\}$, $\{7, 8\}$ and $\{9, 10\}$.
Six numbers in five boxes put two numbers into one box, those two numbers are neighbors, and neighbors are coprime.
One idea, the boxes, does all the work, and once you have seen it you do not forget it.

A proof from the Book, or a Book proof, is a correct [[proof|0B94TKFQJX]] that mathematicians judge to be the best possible proof of its theorem.
Such a proof is short, turns on one clear idea, needs little background, and shows why the theorem holds.
The name comes from Paul Erdős, who liked to speak of an imagined book in which God keeps the perfect proof of every theorem.
The notion has no formal definition, and it rests on the shared judgment of mathematicians, which can change.

## Motivation

Many theorems have several correct proofs, as [[many proofs of one theorem|KNQDDN6PT2]] shows.
All of them establish the same fact, so correctness alone does not explain why mathematicians prefer some to others.
A proof that fits in a few lines and gives the reason for the result is remembered, taught and reused.
A proof that is correct but long, or that checks many cases, convinces the reader without showing why the result holds.
The idea of the Book names this preference, and it makes economy and clarity something that mathematicians can discuss; the wider topic is [[elegant and deep|STHWD1K9AN]].

## Notation

Erdős spoke of "The Book", and the collection of Martin Aigner and Günter Ziegler writes it in capitals, *Proofs from THE BOOK*.
We write "proof from the Book" or "Book proof".
Saying that a proof "is from the Book" is the usual way to praise it.

## Remarks

### Three Book proofs

[[Euclid's proof of the infinitude of primes|RB6G2NWW4J]] takes a finite list of primes and looks at a prime factor of their product plus one.
That prime cannot be in the list, and the only fact needed from outside is that every number above $1$ has a prime divisor.

[[Kelly's proof of the Sylvester-Gallai theorem|DBTXYQQCD0]] shows that a finite set of points in the plane, not all on one line, has a line through exactly two of them.
It picks a point and a line that are as close as possible, and shows that a line through three points would give a closer pair; this is the [[extremal principle|MD3MRG90W4]] at work.

The boxes of the Summary prove a general fact: among any $n + 1$ of the numbers $1, \dots, 2n$, two are coprime.
The [[pigeonhole principle|0HGVCWQGY3]] on the $n$ pairs $\{2i - 1, 2i\}$ gives two consecutive numbers, and any common divisor of consecutive numbers divides their difference $1$.
Picture proofs of identities, such as [[the sum of the first n odd numbers as a picture|EE2Y5SNFME]], are often counted as Book proofs too.

### What is not a Book proof

[[The case analysis of the four color theorem|8ZBH60TVBR]] is correct, but it rests on a computer check of hundreds of configurations.
It fails the tests of brevity and of explanation, though not the test of correctness.
A short argument with a gap is not a Book proof, because it is not a proof at all, and correctness comes first.
A proof that is short only because it quotes a much harder theorem does not count either.
For example, the infinitude of primes follows at once from the [[prime number theorem|0EHBY5Y84N]], but that proof hides all its work in the quoted theorem.

### What mathematicians look for

The criteria below describe what mathematicians usually praise in a proof, not rules that decide the question.

1. Correctness: each step holds, and the proof is complete.
2. Brevity: the proof is short compared with the background that it needs.
3. One idea: the proof turns on one construction or one choice, and the rest follows.
4. Little background: a reader with basic undergraduate mathematics can follow it.
5. Explanation: the proof shows why the result holds, which is one of the [[functions of proof|ENY0GKRJS8]].
6. Surprise: the idea is unexpected, and natural once seen.

The criteria can conflict.
A proof that uses a general theory can be short and clear for an expert and long for a beginner.
Aigner and Ziegler say in their preface that they have no definition of a Book proof, and their choices rest on judgment.

### Properties of the idea

A Book proof is first a proof, and shortness never replaces a complete argument.
The Book proof of a theorem can change, because a new idea can give a shorter or clearer proof long after the first one.
Many Book proofs use a standard device: an extremal choice, [[double counting|0F8YBHF2W3]], a bijection, the pigeonhole principle or an invariant.
A Book proof is often an [[elementary proof|84SZZBACP3]], but not always, and some chapters of Aigner and Ziegler need algebra, analysis or topology.

### History

Erdős used the image of the Book for many years in talks and conversation, and called a proof that he admired a proof from the Book.
He also liked to say, in paraphrase, that a mathematician need not believe in God but should believe in the Book.
Erdős died in 1996.
Martin Aigner and Günter Ziegler published *Proofs from THE BOOK* with Springer in 1998, with illustrations by Karl H. Hofmann, and dedicated it to Erdős, who had helped to plan it.
The book has five parts: number theory, geometry, analysis, combinatorics, and graph theory.
It received the Leroy P. Steele Prize for Mathematical Exposition of the American Mathematical Society in 2018.

### Watch out

Do not think that a Book proof needs no background: a proof can be short because the reader already knows the right ideas.
Do not prefer a short proof with a gap to a longer complete proof, since correctness comes before economy.
And do not think that each theorem has exactly one Book proof, or that the judgment is objective.
Mathematicians disagree, and Aigner and Ziegler give six proofs of the infinitude of primes in their first chapter.

### Try it

First, show that the bound $n + 1$ in the coprime problem is sharp.
The $n$ even numbers $2, 4, \dots, 2n$ share the divisor $2$, so $n$ numbers are not enough.

Second, is the proof of the infinitude of primes from the prime number theorem a Book proof?
No: it is correct and short on the page, but all of its work lies in a theorem much harder than the result.

## Explanations

### L1 human

Some proofs are long and hard, and some are so short and clear that people remember them for life.
The mathematician Paul Erdős joked that God has a book with the best proof of every theorem.
When he saw a very good proof, he said that it came from the Book.
The boxes of the Summary are a small example.
Six numbers chosen from $1$ to $10$ go into five boxes of neighbors, so one box gets two numbers, and two neighbors share no factor except $1$.

### L2 human

We prove: among any $n + 1$ numbers chosen from $1, 2, \dots, 2n$, two are coprime.
Form the $n$ pairs $\{1, 2\}, \{3, 4\}, \dots, \{2n - 1, 2n\}$, so that each number from $1$ to $2n$ lies in exactly one pair.
Place the $n + 1$ chosen numbers into these $n$ pairs.
By the pigeonhole principle some pair holds two chosen numbers, and they are $2i - 1$ and $2i$ for some $i$.
Let $d$ be a positive common divisor of the two; then $d$ divides their difference,
$$2i - (2i - 1) = 1,$$
so $d = 1$ and the two numbers are coprime.
The choice of the pairs is the whole idea, and the rest is a check.
That is what makes a proof feel like a Book proof.
Watch out: the proof is short, but finding the pairs is the hard part, and a first attempt usually tries cases.

### L3 human

The idea of the Book connects the practice of proof with the [[aesthetics of mathematics|AYDMRM3WA5]].
Philosophers ask whether the preference for such proofs is a matter of taste or a sign of explanation, and the functions of proof give one answer: a proof is valued when it explains, not only when it verifies.
A Book proof is short as an [[informal proof|8VZ77R4R8S]], while its formal version in a proof assistant can still be long, because it spells out the background.
At the other end are [[computer-assisted proofs|MC18C7BMFT]] and [[long proofs|RM0S65BHWH]], which verify without one visible idea.
The search for Book proofs also drives research, since a new short proof often links two fields: Hillel Furstenberg's proof of 1955 linked the primes with topology.
