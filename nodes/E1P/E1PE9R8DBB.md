---
tag: E1PE9R8DBB
kind: concept
name: Mathematical rigor
aliases: [rigour, rigor, mathematical-rigor, rigorous-proof, mathematical-rigour]
msc: ["00A35"]
topics: [1BTHSHST4M]
audience: ug1
uses: [0B94TKFQJX, GD2JBXJV5Z, Y0HXCJRB9B]
sources:
  - url: https://en.wikipedia.org/wiki/Rigour
    locator: Mathematics
  - url: https://en.wikipedia.org/wiki/Mathematical_proof
    locator: Nature and purpose
  - url: https://en.wikipedia.org/wiki/Intermediate_value_theorem
    locator: History
  - url: https://en.wikipedia.org/wiki/Uniform_convergence
    locator: History
  - book: isbn:9781108439534
    locator: Introduction
---

## Summary

Rigor is the demand that every step of a [[proof|0B94TKFQJX]] has a reason that a competent reader can check.
It matters because a step that only looks right can be wrong, and a wrong step spreads into every result that uses it.

In his *Cours d'analyse* of 1821, Augustin-Louis Cauchy stated that a convergent series of continuous functions has a continuous sum.
The claim sounds right, and it is false as we now read it.
Take $u_1(x) = x$ and $u_k(x) = x^k - x^{k - 1}$ for $k \ge 2$, on the interval $[0, 1]$.
Each term is continuous, and the $n$-th partial sum is $s_n(x) = x^n$.
For $0 \le x < 1$ the partial sums tend to $0$, and at $x = 1$ they are all $1$, so the sum jumps at $x = 1$.
The step that failed was the exchange of two limits, which needs the extra hypothesis now called [[uniform convergence|08VZ57PT26]].

So we say that an argument is rigorous for a given reader when each step is an axiom, a definition, a hypothesis, an earlier result, or follows from earlier steps by a valid rule of inference.
Steps that the argument leaves out must be ones that this reader can fill in by routine work.
No step may rest only on a picture, on intuition, or on a claim that nobody has proved.

## Motivation

Many statements look true from a picture or from a few cases.
A continuous curve that starts below the horizontal axis and ends above it seems to cross the axis.
Yet on the rational numbers the function $g(x) = x^2 - 2$ is negative at $1$ and positive at $2$, and it has no rational zero, as [[the example on the intermediate value theorem|ARWPBPW0Y3]] shows.
So the crossing depends on a property of the real numbers that the picture does not show.

Rigor answers this problem in two ways.
A rigorous proof names each property that it uses, so the reader sees where each hypothesis enters and what fails without it.
It also lets one result serve as a safe step in later proofs, because each of its steps was checked.
The next question is who does the checking: a human reader, a community of experts over years, or a computer, as in [[computer-assisted proof|MC18C7BMFT]].

## Notation

There is no symbol for rigor.
American books spell the word "rigor" and British books spell it "rigour"; the adjective is "rigorous" in both.

Several words describe how much detail a proof gives.
A "sketch" or an "outline" gives the main steps and leaves gaps on purpose.
A "complete proof" claims that no gap remains for the intended reader.
A "formal proof" is a derivation in a formal system, in which each step follows a stated rule, and [[formal and informal proofs|8VZ77R4R8S]] compares the two kinds.
The words [[trivial, obvious and clearly|Y0HXCJRB9B]] claim that a step is routine, and they hide a gap when it is not.

## Remarks

### Finding the missing hypothesis

Why does Cauchy's claim fail for $s_n(x) = x^n$?
Convergence at each point lets the speed of convergence depend on the point.
Near $x = 1$ the convergence is slow: for each $n$, the point $x = (1/2)^{1/n}$ lies in $[0, 1)$ and gives
$$s_n(x) = \left( (1/2)^{1/n} \right)^n = \tfrac{1}{2},$$
while the limit at that point is $0$.
So no single $n$ makes $|s_n(x) - 0| < \tfrac{1}{2}$ for all $x$ in $[0, 1)$ at once.
Uniform convergence asks exactly for such an $n$ for each tolerance, and with it the claim becomes the [[uniform limit theorem|0X9XT05JVC]].

Check: for $n = 3$, $(1/2)^{1/3} \approx 0.794$ and $0.794^3 \approx 0.500$.

Historians still discuss what Cauchy meant by convergence, so the case is about the claim as later readers took it.
Its lesson does not depend on that question: a rigorous proof must name the hypothesis on which an exchange of limits rests.

### Two levels for one sum

Rigor depends on the reader, and a familiar identity shows how.
The pairing argument for $1 + 2 + \dots + n = n(n + 1)/2$ writes the sum forward and backward and adds the two rows:
$$2(1 + 2 + \dots + n) = \underbrace{(n + 1) + (n + 1) + \dots + (n + 1)}_{n \text{ terms}} = n(n + 1).$$
For a school reader this is a complete proof.
A reader who asks what the dots mean needs a definition of the sum by recursion and a proof by [[induction|0ASJVEFA9J]].
[[The sum at two levels of rigor|KQZNTQG6KM]] gives both proofs and says what each one takes as known.

### Where the picture hides an axiom

The [[intermediate value theorem|00KAFBR32E]] says that a continuous function on $[a, b]$ takes every value between $f(a)$ and $f(b)$.
The same statement fails on the rational numbers, since $x^2 - 2$ changes sign on $[1, 2]$ and $x^2 = 2$ has no rational solution.
So any proof must use a property that $\mathbb{R}$ has and $\mathbb{Q}$ lacks.
[[The supremum proof|P54346XMQQ]] uses the [[completeness axiom|0AXWET80YW]] at one named step, and [[the worked comparison|ARWPBPW0Y3]] checks every number.

In the same way, the proof that $\sqrt{2}$ is [[irrational|0DZGSDHD92]] is rigorous because each step uses the hypothesis $\sqrt{2} = a/b$, the definition of an even number, or arithmetic.

### What rigor depends on

Rigor is relative to the reader.
A paper for specialists leaves out steps that a text for first-year students must write, and both can be rigorous.

Rigor is relative to the period.
Eighteenth-century analysis accepted arguments with infinitely small quantities that the standard of the late 19th century rejected, as [[the history of proof and rigor|20F7K9RVT6]] tells.

Rigor is relative to the starting points.
A proof is rigorous with respect to the [[axioms|GD2JBXJV5Z]] and earlier results that it uses.

Rigor is not formality.
A rigorous informal proof can in principle be expanded into a formal derivation, but it is already rigorous when each gap is routine for its reader.
A program can check each step of [[a proof in the Lean proof assistant|QF0Q7B5Q73]], which is the strictest level we have.

### What fails the test

[[Euclid's first proposition|GQCW6RG3GB]] builds an equilateral triangle from two circles and takes a point where they meet.
No postulate of the *Elements* says that the circles meet, so by the modern standard that step has no reason.

The [[forty prime values of $n^2 + n + 41$|H75AB4EJT5]] for $n = 0$ to $39$ are not a proof that the value is always prime.
The checks cover forty cases and the claim covers all natural numbers, and $n = 40$ gives $40^2 + 40 + 41 = 1681 = 41^2$.

The sentence "a curve that goes from below the axis to above it must cross the axis" is not a rigorous step either.
It rests on a picture, and the property behind it, the completeness of $\mathbb{R}$, has no name in it.

### Watch out

A rigorous proof does not have to be long or full of symbols.
It gives each step that its reader needs and no more, so the pairing proof above is rigorous for a school reader in three lines.

A true conclusion does not make an argument rigorous.
Cauchy's claim is true for uniformly convergent series, yet his argument did not name that hypothesis, and the series $s_n(x) = x^n$ shows the gap.
In the same way, a correct theorem can have a faulty first proof.

A picture or a large computation of cases is not a proof of a general claim.
It can suggest a proof, and the proof must still name each property that it uses.

### History

Greek mathematics made deductive proof the standard, and [[Euclid's Elements|83WHDAV68J]] was the model of rigor for more than two thousand years.
Bernard Bolzano in 1817 and Cauchy in 1821 proved the intermediate value theorem, which earlier authors had taken as evident.
In 1826 Niels Henrik Abel pointed out that the series $\sin x - \tfrac{1}{2} \sin 2x + \tfrac{1}{3} \sin 3x - \dots$ is an exception to Cauchy's claim.
Philipp Ludwig von Seidel in 1847 located the failure in convergence that becomes arbitrarily slow, and later in the century uniform convergence became a standard notion in analysis.
In 1899 David Hilbert published a system of [[axioms for geometry|KM1FB8XZ2R]] that states the assumptions Euclid's proofs use without stating them.
In the 20th century rigor came to mean that a proof can in principle be written in a formal system such as set theory.

### Try it

First, the function $f_n(x) = x^n$ also converges on $[0, \tfrac{1}{2}]$.
Is the convergence uniform there?
Yes: for every $x$ in $[0, \tfrac{1}{2}]$ we have $x^n \le (1/2)^n$, and this bound tends to $0$ without depending on $x$.

Second, a student writes "$n^2$ is even, so $n$ is even, since squares keep parity".
Which step lacks a reason?
The phrase "squares keep parity" is the claim itself, so the step needs a real argument, such as the contrapositive proof in the L2 explanation below.

## Explanations

### L1 human

A rigorous argument is one in which each step has a reason that anyone can check.
The reason can be a rule we agreed on, a fact we proved before, or plain arithmetic.
Take the claim "the sum of two odd numbers is even".
The example $3 + 5 = 8$ is not a reason, because it is only one case.
A rigorous argument says that an odd number is one more than an even number, so the sum of two odd numbers is two more than the sum of two even numbers, and that is even.
Each part of the sentence can be checked, and it works for every pair of odd numbers.

### L2 human

We test a short proof by giving, for each step, the reason that justifies it.
The claim is that if $n$ is an integer and $n^2$ is even, then $n$ is even.

1. Suppose that $n$ is odd, since we prove the [[contrapositive|0BB5TPGQ1N]]: if $n$ is odd, then $n^2$ is odd.
2. Then $n = 2k + 1$ for some integer $k$, by the definition of an odd integer.
3. So $n^2 = 4k^2 + 4k + 1$, by expanding the square.
4. So $n^2 = 2(2k^2 + 2k) + 1$, by taking out the factor $2$ from the first two terms.
5. So $n^2$ is odd, because $2k^2 + 2k$ is an integer and $n^2$ has the form of the definition.
6. So if $n^2$ is even, then $n$ is even, because a statement and its contrapositive are equivalent.

Every step has a reason, so the proof is rigorous for a first-year reader.
The typical use of this test is to check your own proof before you hand it in.
Watch out for a step that you accept because it "looks right": if you cannot say its reason, you have found a gap.

### L3 human

Two notions of rigor live side by side.
The practical notion is social: a proof is rigorous when experts agree that each gap can be filled by routine work.
The ideal notion is formal: a proof is rigorous when it can be expanded into a derivation in a formal system, such as first-order logic with the axioms of set theory, so that a program can check each step.
Most mathematicians work with the practical notion and believe that it implies the ideal one, and [[formal and informal proofs|8VZ77R4R8S]] discusses that belief.

Both notions come under strain.
Very long proofs, such as the classification of finite simple groups, test the practical notion, and computer proofs test the idea that a human reads each step, as [[long proofs and surveyability|RM0S65BHWH]] explains.
In 1993 Arthur Jaffe and Frank Quinn asked how much speculation mathematics should allow before rigor arrives, and [[their debate with Thurston|K3M3TEX7SJ]] follows the replies.
Why a rigorous proof gives knowledge at all is a question for the [[philosophy of mathematics|NTJ5XW0PVD]].
