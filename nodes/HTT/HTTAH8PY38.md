---
tag: HTTAH8PY38
kind: example
name: The infinitude of primes and Goldbach's conjecture as sentences of arithmetic
msc: ["03F30", "03B10"]
topics: [QHCRN4JVG0]
audience: ug2
instance_of: [DKFGQTRYZE]
illustrates: [D8SD54M5PN]
uses: [329ZG1Z0G5, BD4PEHWBRX, DKFGQTRYZE, 71X7TB3F98]
sources:
  - url: https://en.wikipedia.org/wiki/Arithmetical_hierarchy
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Goldbach%27s_conjecture
    locator: lead section
  - book: isbn:9780521857840
---

## Example

Two famous statements of number theory, one proved and one open, become [[sentences|DKFGQTRYZE]] of the [[language of arithmetic|D8SD54M5PN]] $L_A$.
We use the formulas $\mathrm{Even}(x)$ and $\mathrm{Prime}(x)$ of [[divisibility, evenness and primality|BD4PEHWBRX]], which abbreviate $L_A$-formulas with one free variable $x$.

The sentence $\mathrm{Inf}$ says that there are infinitely many primes:
$$\mathrm{Inf} := \forall x\; \exists y\; (x < y \land \mathrm{Prime}(y)).$$
The sentence $\mathrm{GC}$ is Goldbach's conjecture, that every even number greater than $2$ is a sum of two primes:
$$\mathrm{GC} := \forall x\; \Bigl( \bigl(\overline{2} < x \land \mathrm{Even}(x)\bigr) \to \exists p \le x\; \exists q \le x\; \bigl(\mathrm{Prime}(p) \land \mathrm{Prime}(q) \land p + q = x\bigr) \Bigr).$$

We check that these are sentences and that they say what we want.

1. In $\mathrm{Inf}$, the variable $x$ is bound by $\forall x$ and $y$ by $\exists y$, and the variables inside $\mathrm{Prime}(y)$ are bound there.
   So $\mathrm{Inf}$ has no free variable.
2. A set of numbers is infinite exactly when it has an element above each number $x$.
   So $\mathfrak{N} \models \mathrm{Inf}$ says that the primes form an infinite set.
3. In $\mathrm{GC}$, the variables $x$, $p$ and $q$ are bound by the quantifiers in front of them, so $\mathrm{GC}$ is a sentence.
4. The bounds $p \le x$ and $q \le x$ lose no solution, because $p + q = x$ forces $p \le x$ and $q \le x$.
5. So $\mathfrak{N} \models \mathrm{GC}$ exactly when every even $n > 2$ is a sum of two primes.
6. At $x = 4$ the inner part holds with $p = q = 2$, and at $x = 10$ it holds with $p = 3$ and $q = 7$.

Euclid's theorem gives $\mathfrak{N} \models \mathrm{Inf}$.
Whether $\mathfrak{N} \models \mathrm{GC}$ is an open problem.

## Remarks

The shape of each sentence tells you what kind of evidence could settle it.
Inside $\mathrm{GC}$, everything after $\forall x$ uses only bounded quantifiers, so $\mathrm{GC}$ is a $\Pi_1$ sentence in the sense of [[the formula classes|GE43CSZTS9]].
If $\mathrm{GC}$ is false, then a finite search finds the counterexample, and $\neg \mathrm{GC}$ is a true $\Sigma_1$ sentence.
Then [[Robinson arithmetic|3K1AKGXF8A]] proves $\neg \mathrm{GC}$, by [[Σ1-completeness|69234Z1V00]].

The sentence $\mathrm{Inf}$ has the prefix $\forall x\, \exists y$ before a bounded formula, so it is a $\Pi_2$ sentence.
No single computation refutes it.
The twin prime conjecture $\forall x\, \exists y\, (x < y \land \mathrm{Prime}(y) \land \mathrm{Prime}(y + \overline{2}))$ has the same shape.

A small change of bound keeps the meaning of $\mathrm{GC}$.
If you replace $p \le x$ by $p < x$, nothing is lost, because the prime $q$ is at least $2$, so $p = x - q < x$.

## Explanations

### L1 human

"There are infinitely many primes" can be said with only "for all", "there is", plus, times and less than.
It becomes: "for every number $x$ there is a larger number $y$ that is prime".
Goldbach's conjecture becomes: "for every even $x$ larger than $2$ there are primes $p$ and $q$, at most $x$, with $p + q = x$".
For $x = 10$ we can take $p = 3$ and $q = 7$.

### L2 human

We check the inner part of $\mathrm{GC}$ at $x = 28$.
The hypothesis holds, since $2 < 28$ and $28 = 14 + 14$, so $\mathrm{Even}(\overline{28})$ is true.
Try $p = 5$, which leaves $q = 23$.
The number $23$ is prime, since none of $2$, $3$ and $4$ divides it and $5 \cdot 5 > 23$.
Both $5 \le 28$ and $23 \le 28$ hold, and
$$5 + 23 = 28.$$
So the inner part is true at $x = 28$.

Writing a statement in $L_A$ shows its logical form, and $\Pi_1$ statements such as $\mathrm{GC}$ are refuted by one computation when they are false.
Watch out: a check of many cases does not prove $\mathrm{GC}$.
A $\Pi_1$ sentence needs a proof for all $x$ at once.
