---
tag: STHWD1K9AN
kind: concept
name: Elegant and deep
aliases: [elegance-and-depth-in-mathematics, elegant-proof, deep-theorem, brute-force, abstract-nonsense, general-abstract-nonsense]
msc: ["00A35"]
topics: [Z2WNQ1DNTX]
audience: research
uses: [4M1FGQ0HNZ, 0B94TKFQJX, 84SZZBACP3, Q1RZT7DV0F]
sources:
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_jargon
    locator: Philosophy of mathematics
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_jargon
    locator: Proof techniques
  - url: https://en.wikipedia.org/wiki/Abstract_nonsense
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Elementary_proof
    locator: Prime number theorem
---

## Summary

Mathematicians judge [[proofs|0B94TKFQJX]] and results with a few informal words, and each word tells the reader what kind of argument to expect.
You meet them in sentences such as "this deep theorem has a short statement", "a brute force computation shows", or "by general abstract nonsense, the product is unique up to isomorphism".

A result is *deep* when every known proof needs ideas much more advanced than those needed to state it.
A proof is called `elegant` when it is short and shows why the result is true, often by one idea that replaces a computation.
A proof is by *brute force* when it checks as many cases as needed instead of finding a general principle; when it checks every case of a finite list, it is a proof by exhaustion.
*Abstract nonsense*, or *general abstract nonsense*, is a joking name for an argument of [[category theory|Q1RZT7DV0F]] that uses only general structure and none of the details of the problem.
These words belong to [[mathematical jargon|4M1FGQ0HNZ]]: they are judgments, not definitions, and no theorem depends on them.

## Motivation

Papers, referee reports and talks use these words as signposts.
"This is a deep theorem" warns you that the proof needs a large theory, so you should not expect to rebuild it in an afternoon.
"By abstract nonsense" tells you that the step follows from general facts, such as a universal property, and that you can supply it once you know those facts.
"A brute force computation shows" tells you that the step is a finite check with no idea behind it, so you may trust it or rerun it, but you will learn little by reading it.
A reader who knows this code can decide quickly which parts of a paper to read closely.
The study of mathematical beauty as a value belongs to [[mathematics and culture|FWE06TZ36P]].

## Notation

No symbol marks these judgments.
Common phrases are "a deep result", "an `elegant` argument", "a slick proof", "by brute force", "a direct computation", and "by general abstract nonsense".
The word `beautiful` is used with a meaning close to `elegant`.

Two of the words have two readings.
"Deep" can mean that the proof needs advanced tools, or that the result has far-reaching consequences.
"Abstract nonsense" is usually affectionate and means "a formal argument from general structure", but some speakers use it with a sneer, to mean "too abstract to be useful".
To tell the readings apart, look at what follows the word.
"Deep" followed by a remark about proofs is the first reading, and "deep" followed by a list of applications is the second.
"Abstract nonsense" followed by a complete argument is the affectionate reading.

## Remarks

### Deep: a short statement and a long proof

[[Fermat's last theorem|0Y5X3SDBCZ]] says that $x^n + y^n = z^n$ has no solution in positive integers when $n \ge 3$.
A school student can read the statement, but the proof by Wiles uses [[elliptic curves|427N6S6QQW]] and [[modular forms|GWKN5VG78A]].
That gap between the language of the statement and the tools of the proof is what "deep" measures.

Compare [[the equation 2^10 = 1024|FWDC5ZHAG9]].
Its proof is the computation $2^5 = 32$ and $32 \cdot 32 = 1024$, which uses only the multiplication that the statement already needs, so it is not deep.
The [[irrationality of the square root of 2|0DZGSDHD92]] is not deep either, since its proof uses only divisibility of integers.

Depth depends on the known proofs, so it can change.
The [[prime number theorem|0EHBY5Y84N]] was once the standard deep theorem, because every proof used complex analysis.
After [[elementary proofs|84SZZBACP3]] were found, it was no longer deep in that sense, though it kept its importance, which is the second reading of the word.

### Brute force

[[A brute force check of the values of n^2 + n + 41|6EHQD2M1PS]] computes forty values and tests each for primality.
It proves that $n^2 + n + 41$ is prime for $0 \le n \le 39$, and it gives no reason why.
At $n = 40$ the formula gives
$$40^2 + 40 + 41 = 41 \cdot 41 = 1681,$$
and that step is not brute force, since it uses the factor $41$ in the formula.

Brute force is a valid method: a check of every case of a finite list is a complete proof.
The [[four color theorem|0M406JC8J1]] was proved this way by Appel and Haken in 1976, with a computer check of a large finite set of configurations.
The word describes the method, not the quality of the result.

### Abstract nonsense

[[The uniqueness of a product is abstract nonsense|9NQD3BC9N0]].
A product of two objects in a category is unique up to a unique isomorphism, and the proof uses only the universal property, never elements or sets.
So one proof covers the Cartesian product of sets, the direct product of groups and the product of topological spaces at once.

Abstract nonsense is fully rigorous.
The phrase marks an argument from general structure, so the same argument holds in every category with that structure.
The [[Yoneda lemma|D6DF1ARPVD]] and the [[snake lemma|Q8AYGD93CW]] are standard tools of this kind.

### What makes a proof `elegant`

Take $1 + 2 + \dots + 100$.
Brute force adds the terms one by one, with $99$ additions.
The pairing argument writes the sum forwards and backwards, so each of the $100$ columns adds to $101$:
$$2S = 100 \cdot 101, \qquad S = 5050.$$
The same idea gives $1 + 2 + \dots + n = n(n + 1)/2$ for every $n$, and it shows why the formula holds.
Most readers call the second proof `elegant`: it is short, it explains, and it generalizes.
Two mathematicians can still disagree about a given proof, and the judgment never makes a proof more or less correct.

### Watch out

The first error is to read "abstract nonsense" as a criticism of the argument.
In most uses it is a joke about style, and the argument that follows is a complete proof.

The second error is to think that a deep result has a hard statement.
Depth compares the proof with the statement, and many deep results have short statements, as Fermat's last theorem shows.

The third error is to use these words in place of an argument.
"By brute force" must still say which cases are checked and how, and "this is `elegant`" proves nothing.
In the example of $n^2 + n + 41$, forty passing cases are evidence and not a proof for $n \ge 40$.

### History

Eilenberg and Mac Lane defined categories in their paper "General theory of natural equivalences" of 1945.
In a lecture of 1921, Hardy said that some theorems lie deep and others nearer the surface, and he doubted that the prime number theorem had an elementary proof.
Selberg and Erdős published elementary proofs of it in 1949.
Appel and Haken announced their computer-assisted proof of the four color theorem in 1976.

### Try it

First, is the statement "every positive integer is a sum of four squares" deep, given that its standard proofs use only integer arithmetic and a counting argument?
By the first reading it is not deep, since the tools are no more advanced than the statement, though the proof needs a clever idea.

Second, a proof checks the $2^{10} = 1024$ subsets of a $10$-element set one by one by computer.
Is it brute force, and is it a proof?
It is brute force, and it is a complete proof of the finite statement, provided the program is correct.

## Explanations

### L1 human

Mathematicians use some everyday words with special meanings.
A result is deep when its statement is simple but its proof needs a lot of advanced mathematics.
A proof is `elegant` when it is short and shows in a simple way why the result is true.
A proof is brute force when it checks many cases one by one.
"Abstract nonsense" is a joke name for proofs that use only very general ideas.
None of these words is a definition; they are opinions that most mathematicians share.

### L2 human

Here is how the words sort three proofs.
Fermat's last theorem has a statement about integers and a proof with elliptic curves and modular forms, so the theorem is deep.
The sum $1 + 2 + \dots + 100$ can be found by brute force with $99$ additions, or by the pairing argument:
$$S = \frac{100 \cdot 101}{2} = 5050,$$
and most readers call the pairing argument `elegant`.
The uniqueness of a product follows from its universal property alone, so its proof is abstract nonsense.
In practice these words appear in the introduction of a paper, to tell the reader what kind of proof follows, and they never replace the proof.

### L3 human

The word "deep" can be made more exact by measuring the gap between the language of a statement and the language of its known proofs.
For arithmetical statements logic gives one measure: the weakest formal system in which a proof exists, as in Friedman's conjecture about [[elementary function arithmetic|2JD80TE553]].

Abstract nonsense has an exact core: results such as the Yoneda lemma and the uniqueness of universal objects hold in every category, and the snake lemma holds in every abelian category.
Such arguments are short, so they are `elegant` in the sense of length, though readers new to the language often find them hard to follow.
Brute force has become a standard tool with computer-assisted proofs, such as those of the four color theorem and of the [[Kepler conjecture|AFMBQT06ZV]], and these proofs raise the question of what a proof must explain beyond being correct.
