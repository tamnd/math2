---
tag: 01XM7JEKHY
kind: concept
name: Constructive proof
aliases: [proof-by-construction, proof-by-example]
msc: ["00A35", "03F65"]
topics: [G9JFJGY4TQ, 958EF46EYJ]
audience: ug1
specializes: [0B94TKFQJX]
uses: [0JW2FHW7G3, 0B94TKFQJX, 33ZNXRFVJJ]
sources:
  - url: https://en.wikipedia.org/wiki/Constructive_proof
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Existential_generalization
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 3.3
same_as:
  wikidata: Q3044470
  wikipedia: Constructive proof
---

## Summary

To prove that something exists, the most convincing thing you can do is to show it and check it.
A constructive proof does exactly that: it names the object, or gives a recipe that produces it, and then proves that the object has the required property.

Here is a small one: there are five consecutive integers, none of them prime.
Take the five numbers $722, 723, 724, 725, 726$, which are $6! + 2$ to $6! + 6$ with $6! = 720$.
Each one has a divisor between $1$ and itself:
$$722 = 2 \cdot 361, \quad 723 = 3 \cdot 241, \quad 724 = 4 \cdot 181, \quad 725 = 5 \cdot 145, \quad 726 = 6 \cdot 121.$$
So all five are composite, and the statement is proved.

In general, a *constructive proof* of an [[existence statement|0JW2FHW7G3]] $\exists x \, P(x)$ names a specific object $a$, or gives a method that computes it, and then proves $P(a)$.
The object $a$ is called a *witness*.
The final logical step, from $P(a)$ to $\exists x \, P(x)$, is the rule of [[existential generalization|33ZNXRFVJJ]].
A proof that shows existence without naming a witness is a [[non-constructive existence proof|JZQVJ9XT63]].

## Motivation

An existence statement says only that some object has a property.
A proof that hands over the object gives more: you can check it, compute with it and use it in later work.
For an equation a constructive proof gives a solution, and for a factoring problem it gives a factor.
Many existence proofs in school mathematics are of this kind without the name: "the number $x = 3$ satisfies $2x + 1 = 7$" proves that the equation has a solution.

Finding the witness is often hard, but the final proof can still be short, because it only has to check the witness.
The search for the five numbers above, for example, is scratch work, and the proof is the list and the five factorizations.
In computing, a constructive proof is close to an algorithm, and proof assistants can extract a program from it.

## Notation

A constructive proof usually reads "Let $a = \dots$; then $P(a)$ holds, because ...".
When the statement has the form $\forall y \, \exists x \, P(x, y)$, the witness may depend on $y$, and the proof gives a formula or an algorithm for $x$ in terms of $y$.
In Lean, the tactic `use a` supplies the witness and leaves the goal `P a`.
The anonymous constructor `⟨a, h⟩`, with `h : P a`, is a proof of `∃ x, P x`, and so is `Exists.intro a h`.

## Remarks

### Why the method is valid

An existence statement $\exists x \, P(x)$ is true when at least one object of the domain satisfies $P$.
A constructive proof exhibits one such object, so the statement is true by the meaning of "there is".
Nothing else is needed, and in particular no use of the [[law of excluded middle|0RYYK8PG4S]].
So a constructive proof is accepted in every school of mathematics, classical or constructive, as long as its other steps are.

The proof has two parts, and both are required.
A witness without a proof that it works is only a guess.
A check of $P(a)$ without saying what $a$ is cannot be carried out.

### Witnesses that depend on a variable

Many existence claims sit inside a "for every", and then the witness is a formula.
For the general version of the summary, "for every $n \ge 1$ there are $n$ consecutive composite numbers", the witnesses are $(n + 1)! + 2, \dots, (n + 1)! + (n + 1)$, as [[the n consecutive composite numbers|SJ5MYHND5D]] shows.
Between two rational numbers $p < q$ there is always a rational number, and the midpoint $\frac{p + q}{2}$ is a witness that depends on $p$ and $q$.
For integers $a$ and $b$, not both $0$, the extended Euclidean algorithm computes integers $x$ and $y$ with $ax + by = \gcd(a, b)$; see [[greatest common divisor|02WF878BH1]].

[[Euclid's theorem|0292EPPPT0]] fits the same pattern.
Given primes $p_1, \dots, p_k$, every prime factor of $N = p_1 p_2 \cdots p_k + 1$ is a prime that is not in the list, because it divides $N$ while each $p_i$ leaves remainder $1$.
The witness is a prime factor of $N$, not $N$ itself, since $N$ need not be prime:
$$2 \cdot 3 \cdot 5 \cdot 7 \cdot 11 \cdot 13 + 1 = 30031 = 59 \cdot 509.$$

### When to choose it

Try to construct a witness first whenever the property is concrete enough to test.
A small search by hand or by computer often suggests a pattern, and the pattern becomes the formula of the proof.
[[Irrational a and b with a to the power b rational|H7X4FMAHC8]] is a case in point: the pair $a = \sqrt{2}$ and $b = \log_2 9$ works, because
$$\sqrt{2}^{\log_2 9} = 2^{\frac{1}{2} \log_2 9} = 2^{\log_2 3} = 3.$$
A witness need not be the best one.
The witnesses for $n = 4$ in the general recipe are $122$ to $125$, while the first run of four composite numbers is $24, 25, 26, 27$.
When no witness can be described, for example a root of a polynomial that has no formula in radicals, a non-constructive proof is the natural choice.

### What is not a constructive proof

[[The proof by cases that some irrational power is rational|7X8GT7Y5WY]] shows that one of two pairs works, but it does not say which one, so it names no witness.
The [[pigeonhole principle|0HGVCWQGY3]] proof that two of any $13$ people have birthdays in the same month shows that such a pair exists, but you need the list of birthdays to find it.
The proof of the [[intermediate value theorem|00KAFBR32E]] from the least upper bound property shows that a root exists but does not compute it; see [[a real root of x^5 - x - 1|2W5SMZWGYF]].

### Watch out

The first trap is to name a witness and not check it.
Saying "take $n = 40$" proves nothing about $n^2 + n + 41$ until you compute $40^2 + 40 + 41 = 1681 = 41^2$.

The second trap is a witness that depends on the wrong variable.
In $\forall \varepsilon > 0 \; \exists \delta > 0 \dots$ the number $\delta$ may depend on $\varepsilon$, but in $\exists \delta > 0 \; \forall \varepsilon > 0 \dots$ it may not; see [[quantifiers in mathematical writing|EGTZPA6QH3]].

The third trap is to call a proof constructive when one step splits on a case that nobody can decide, such as "$\sqrt{2}^{\sqrt{2}}$ is rational or irrational".

### Writing it up

Put the witness first, in a sentence of its own ("Let $a = \sqrt{2}$ and $b = \log_2 9$.").
Then check each required property in turn, each with its reason.
End with the existence statement in the words of the theorem.
Leave the search that found the witness out of the proof, or put it in a remark after the proof.

### History

Luitzen Egbertus Jan Brouwer founded intuitionism in the first decade of the twentieth century, and he rejected existence proofs that give no construction.
Errett Bishop's book Foundations of Constructive Analysis, of 1967, showed that a large part of analysis can be developed with constructive proofs only.
The philosophy behind these programs is treated in [[constructivism|G958EQ8CWW]].

### Try it

First, prove that some integer $n$ makes $n^2 + n + 41$ composite.
Take $n = 41$: then $41^2 + 41 + 41 = 41 \cdot 43 = 1763$, which is composite.

Second, prove that for every real $\varepsilon > 0$ there is a positive integer $n$ with $\frac{1}{n} < \varepsilon$.
Take $n = \lfloor 1/\varepsilon \rfloor + 1$; then $n > \frac{1}{\varepsilon}$, so $\frac{1}{n} < \varepsilon$.

## Explanations

### L1 human

To show that a box contains a red ball, the simplest way is to take a red ball out and hold it up.
That is a constructive proof.
"There is a whole number that is both even and a multiple of $3$" is proved by showing $6$ and checking that $6 = 2 \times 3$.
Another way would be to show that the box cannot be without a red ball, and never take one out.
That is also a proof, but it does not tell you where the ball is.

### L2 human

Let us prove that for every integer $n$ there is a multiple of $7$ that is greater than $n$.
The witness must depend on $n$, so we look for a formula.
Try $m = 7(|n| + 1)$.
It is a multiple of $7$, because $|n| + 1$ is an integer.
It is larger than $n$, because
$$m = 7|n| + 7 > |n| \ge n,$$
where the strict step uses $7|n| \ge |n|$ and $7 > 0$.
Check: for $n = -3$ we get $m = 28 > -3$, and for $n = 10$ we get $m = 77 > 10$.
The simpler guesses fail: $m = 7$ does not work for $n = 10$, and $m = 7n$ does not work for $n = 0$ or for negative $n$.
The problem shows the typical shape: in "for every $n$ there is $m$", the proof gives $m$ as a formula in $n$ and checks it for an arbitrary $n$.

### L3 human

Under the Brouwer-Heyting-Kolmogorov interpretation, a proof of $\exists x \, P(x)$ is a pair of a witness $a$ and a proof of $P(a)$, and a proof of $\forall y \, \exists x \, P(x, y)$ is a method that sends each $y$ to such a pair.
In [[intuitionistic logic|Q11N8X99FK]] this is more than a reading: intuitionistic arithmetic has the existence property, so a proof of a closed statement $\exists x \, P(x)$ yields a numeral $n$ and a proof of $P(n)$.
Through the Curry-Howard correspondence the pair becomes a dependent pair type, and a proof assistant based on type theory can extract a program that computes the witness.
Kleene's realizability interpretation of 1945 makes the same idea precise for arithmetic.
Constructive mathematics as a whole, with its weaker logic and its own analysis and algebra, is treated in the topic [[type theory and constructive mathematics|K6P3NSQEZ3]].
