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

A constructive proof of an [[existence statement|0JW2FHW7G3]] $\exists x \, P(x)$ names a specific object $a$, or gives a method that computes it, and then proves $P(a)$.
The object $a$ is called a witness.
The logical step from $P(a)$ to $\exists x \, P(x)$ is the rule of [[existential generalization|33ZNXRFVJJ]].
A proof that shows existence without naming a witness is a [[non-constructive existence proof|JZQVJ9XT63]].

## Motivation

An existence statement says only that some object has a property.
A proof that hands over the object gives more: the object can be checked, computed with and used in later work.
For an equation, a constructive proof gives a solution, and for a factorization problem it gives a factor.
Many existence proofs in school mathematics are of this kind, often without the name: "the number $x = 3$ satisfies $2x + 1 = 7$" proves that the equation has a solution.
The finding of the witness is often hard, but the final proof can be short, because it only has to check the witness.

## Notation

A constructive proof usually reads "Let $a = \ldots$; then $P(a)$ holds, because ...".
The search that found $a$ is scratch work, and it need not appear in the final proof.
When the statement has the form $\forall y \, \exists x \, P(x, y)$, the witness $x$ may depend on $y$, and the proof gives a formula or an algorithm for $x$ in terms of $y$.
In Lean, the tactic `use a` supplies the witness and leaves the goal `P a`; the term `⟨a, h⟩` with `h : P a` is a proof of `∃ x, P x`.

## Remarks

### Examples

1. [[There are n consecutive composite numbers|SJ5MYHND5D]]: the witnesses are $(n + 1)! + 2, \ldots, (n + 1)! + (n + 1)$.
2. [[Irrational a and b with a to the power b rational, by construction|H7X4FMAHC8]]: $a = \sqrt{2}$ and $b = \log_2 9$ give $a^b = 3$.
3. Between two rational numbers $p < q$ there is a rational number, for example $\frac{p + q}{2}$. It is rational, and $p < \frac{p + q}{2} < q$.
4. [[Euclid's theorem|0292EPPPT0]] on the infinitude of primes is constructive: for primes $p_1, \ldots, p_k$, any prime factor of $p_1 p_2 \cdots p_k + 1$ is a prime not in the list.
5. For integers $a$ and $b$, not both $0$, the extended Euclidean algorithm computes integers $x$ and $y$ with $ax + by = \gcd(a, b)$; see [[greatest common divisor|02WF878BH1]].

### Non-examples

1. [[The proof by cases that some irrational power is rational|7X8GT7Y5WY]]: it shows that one of two pairs works, without saying which one.
2. The [[pigeonhole principle|0HGVCWQGY3]] proof that among $13$ people two have a birthday in the same month. It shows that such a pair exists but does not name it; a list of the $13$ birthdays is needed to find it.
3. The proof of the [[intermediate value theorem|00KAFBR32E]] by the least upper bound property. It shows that a root exists but does not compute it; see [[a real root of x^5 - x - 1|2W5SMZWGYF]].

### Basic properties

1. A constructive proof of $\exists x \, P(x)$ has two parts: the witness $a$, and a proof of $P(a)$. A witness without the second part is not a proof.
2. A witness is seldom unique, and the proof may use any witness. A proof that $\exists x \, P(x)$ says nothing about uniqueness; that is a separate [[proof of uniqueness|GQHHNV79PA]].
3. In [[intuitionistic logic|Q11N8X99FK]], every proof of $\exists x \, P(x)$ can be turned into a witness and a proof of $P$ for it, and every proof of $A \lor B$ tells which of $A$ and $B$ holds. These are the existence property and the disjunction property.
4. A constructive witness may be far from the best one. The witnesses of example 1 for $n = 4$ are $122$ to $125$, while the first run of four consecutive composite numbers is $24, 25, 26, 27$.

### History

Luitzen Egbertus Jan Brouwer founded intuitionism in the first decade of the twentieth century and rejected existence proofs that give no construction.
Errett Bishop's book Foundations of Constructive Analysis of 1967 showed that a large part of analysis can be developed with constructive proofs only.
The philosophy behind these programmes is treated in [[constructivism|G958EQ8CWW]].

### Common errors

1. Naming a witness and not checking it. The check that $P(a)$ holds is the main part of the proof.
2. A witness that depends on a later variable. In $\forall \varepsilon > 0 \, \exists \delta > 0 \ldots$, the number $\delta$ may depend on $\varepsilon$, but in $\exists \delta > 0 \, \forall \varepsilon > 0 \ldots$ it may not; see [[quantifiers in mathematical writing|EGTZPA6QH3]].
3. Calling a proof constructive when one step splits on a case that cannot be decided, such as "$\sqrt{2}^{\sqrt{2}}$ is rational or irrational".

## Explanations

### L1 human

To show that a box contains a red ball, the simplest way is to take a red ball out of the box and show it.
That is a constructive proof.
"There is a whole number that is both even and a multiple of $3$" is proved by showing $6$, and checking that $6 = 2 \times 3$.
Another way would be to show that the box cannot be empty of red balls, without ever taking one out.
That is also a proof, but it does not tell where the ball is.

### L2 human

We prove: for every integer $n$, there is a multiple of $7$ that is greater than $n$.

1. Let $n$ be an integer. We construct a witness $m$ from $n$.
2. Let $m = 7(|n| + 1)$. Then $m$ is a multiple of $7$, since $|n| + 1$ is an integer.
3. Also $m = 7|n| + 7 > |n| \geq n$, because $7|n| \geq |n| \geq 0$ and $7 > 0$.
4. So $m$ is a multiple of $7$ and $m > n$.

The typical use: in a statement "for every $n$ there is $m$", the proof gives $m$ as a formula in $n$.

A trap: the witness $m = 7$ does not work, since it does not depend on $n$; for $n = 10$ it fails.
The witness $m = 7n$ fails too, for $n = 0$ and for negative $n$.

### L3 human

Under the Brouwer-Heyting-Kolmogorov interpretation, a proof of $\exists x \, P(x)$ is a pair of a witness $a$ and a proof of $P(a)$, and a proof of $\forall y \, \exists x \, P(x, y)$ is a method that sends $y$ to such a pair.
Through the Curry-Howard correspondence this becomes a dependent pair type, and in a proof assistant based on type theory a program that computes the witness can be extracted from the proof.
Kleene's realizability interpretation of 1945 makes the same idea precise for arithmetic.
Constructive mathematics as a whole, with its weaker logic and its own versions of analysis and algebra, is treated in the topic [[type theory and constructive mathematics|K6P3NSQEZ3]].
