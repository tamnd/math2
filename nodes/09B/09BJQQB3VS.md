---
tag: 09BJQQB3VS
kind: concept
name: Necessary and sufficient conditions
aliases: [necessary-condition, sufficient-condition]
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
uses: [0NMG7W7Q11, 0S6GMNJ62Y, 0GHS47PDAQ]
sources:
  - url: https://en.wikipedia.org/wiki/Necessity_and_sufficiency
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.5
same_as:
  wikidata: Q875267
  wikipedia: Necessity and sufficiency
---

## Summary

Being a square is enough to make a shape a rectangle, and having four sides is required for it.
So being a square is a sufficient condition for being a rectangle, and having four sides is a necessary condition.

Both words describe one implication.
Suppose that the [[material implication|0NMG7W7Q11]] $p \to q$ is true.
Then $p$ is a sufficient condition for $q$, and $q$ is a necessary condition for $p$.
The condition $p$ is necessary and sufficient for $q$ when $p \to q$ and $q \to p$ are both true, that is, when the [[biconditional|0S6GMNJ62Y]] $p \leftrightarrow q$ is true.
For conditions on a variable $x$ in a domain $D$, "$P(x)$ is sufficient for $Q(x)$" means $\forall x \in D\, (P(x) \to Q(x))$, with the [[universal quantifier|0GHS47PDAQ]] understood.

A theorem that gives a necessary and sufficient condition for a property is a characterization of that property, and it replaces the property by a condition that is often easier to check.

## Motivation

Many problems ask whether an object has a property: whether a number is prime, whether a triangle has a right angle, or whether a function has a maximum at a point.
A sufficient condition lets you say "yes" in some cases.
A necessary condition lets you say "no" in some cases, because if it fails, the property fails.
A necessary and sufficient condition settles every case, as the digit-sum rule does for divisibility by $3$.

The reading "$p$ is sufficient for $q$" looks forward from $p$: whenever $p$ holds, $q$ holds.
The reading "$q$ is necessary for $p$" looks back from $p$: $p$ cannot hold without $q$.
The English forms of a conditional, such as "only if", are listed in [[conditional statements|FA6YZGR2SS]].

## Notation

There is no special symbol.
"$p$ is sufficient for $q$" is written $p \to q$ or $p \Rightarrow q$, and "$p$ is necessary for $q$" is written $q \to p$ or $p \Leftarrow q$.
"$p$ is necessary and sufficient for $q$" is written $p \leftrightarrow q$ or $p \Leftrightarrow q$, and in words "$p$ if and only if $q$" or "$p$ iff $q$".
Several equivalent conditions are listed under the words "the following are equivalent", abbreviated TFAE.
In the proof of a characterization "the property holds if and only if $C$", the part called necessity proves that the property implies $C$, and the part called sufficiency proves that $C$ implies the property.

## Remarks

### The truth table behind the words

Let $p$ be "the shape is a square" and $q$ be "the shape is a rectangle", for a shape with four sides.

| $p$ | $q$ | $p \to q$ | $q \to p$ | $p \leftrightarrow q$ |
|---|---|---|---|---|
| T | T | T | T | T |
| T | F | F | T | F |
| F | T | T | F | F |
| F | F | T | T | T |

The row TF, a square that is not a rectangle, never occurs, so $p \to q$ is true and $p$ is sufficient.
The row FT, a $1$ by $2$ rectangle, does occur, so $q \to p$ is false and $p$ is not necessary for $q$.

### Worked examples

A natural number is divisible by $3$ if and only if its digit sum is, as in [[divisibility by 3 and the digit sum|RYJ4YKRWM2]].
The condition $f'(c) = 0$ is [[necessary but not sufficient for a local extremum|9ZJYHTGGW5]], since $x^3$ has $f'(0) = 0$ and no extremum at $0$.
[[Being odd is neither necessary nor sufficient for being prime|EB51VZGZ4G]]: $2$ is an even prime, and $9$ is odd and not prime.
The [[converse of the Pythagorean theorem|EFF30FNVZ0]] completes a characterization: a triangle has a right angle at $C$ if and only if $a^2 + b^2 = c^2$.
Wilson's theorem and its [[converse|06WRV8HFDY]] characterize the primes: an integer $n > 1$ is prime if and only if $(n - 1)! \equiv -1 \pmod n$.
For a real number $x$, the condition $x > 1$ is sufficient for $x^2 > 1$ but not necessary, as $x = -2$ shows.
Continuity at $a$ is necessary for differentiability at $a$, by the theorem that [[differentiable functions are continuous|07ZMX4ANJS]], but $|x|$ at $0$ shows that it is not sufficient.

### Rules for combining conditions

"$p$ is sufficient for $q$" and "$q$ is necessary for $p$" are the same statement $p \to q$.
If $p$ is sufficient for $q$, then $\neg q$ is sufficient for $\neg p$, by the law of the [[contrapositive|04T1CT7212]].
This is why a failed necessary condition refutes the property, and this step is valid in [[intuitionistic logic|Q11N8X99FK]] as well.
A sufficient condition for a sufficient condition is sufficient, by [[hypothetical syllogism|7MT8CPCEM4]].
If $q_1$ and $q_2$ are both necessary for $p$, then so is $q_1 \land q_2$, and if $p_1$ and $p_2$ are both sufficient for $q$, then so is $p_1 \lor p_2$.
In terms of truth sets, $P$ is sufficient for $Q$ on $D$ exactly when $\{x \in D : P(x)\} \subseteq \{x \in D : Q(x)\}$, and a characterization has the same truth set as the property.

### Watch out

Do not treat a necessary condition as sufficient: $f'(c) = 0$ does not give an extremum, as $x^3$ at $0$ shows.
Keep the two halves of a characterization apart.
In "a triangle has a right angle at $C$ if and only if $a^2 + b^2 = c^2$", necessity proves that a right angle forces the equation, and sufficiency proves the converse.
Do not prove one direction twice, once directly and once by its contrapositive, as in [[two proofs of the same direction|K08FN2E081]].
The method of [[proving biconditionals|TFQ1845T84]] needs one proof of each direction.

### History

Euclid's Elements gives the Pythagorean theorem as Proposition 47 of Book I and its converse as Proposition 48, so the two together form one of the oldest characterization theorems.
Paul Halmos is usually credited with the abbreviation "iff" for "if and only if".

### Try it

Is "$n^2$ is even" necessary and sufficient for "$n$ is even", for an integer $n$?
Yes: if $n = 2k$, then $n^2 = 2(2k^2)$, and if $n = 2k + 1$, then $n^2 = 2(2k^2 + 2k) + 1$ is odd.

## Explanations

### L1 human

A sufficient condition is enough to get a result: if it holds, the result holds.
A necessary condition is one that the result cannot do without: if it fails, the result fails.
Being a square is sufficient for being a rectangle, but not necessary, because a $1$ by $2$ rectangle is not a square.
Having four sides is necessary for being a rectangle, but not sufficient, because some four-sided shapes have no right angle.
Having four right angles is necessary and sufficient for a four-sided shape to be a rectangle.

### L2 human

We prove that for an integer $n$, $n$ is odd if and only if $8$ divides $n^2 - 1$.

1. Sufficiency: suppose $8$ divides $n^2 - 1$.
   Then $n^2 - 1$ is even, so $n^2$ is odd, and $n$ is odd, because the square of an even number is even.
2. Necessity: suppose $n$ is odd, $n = 2k + 1$.
   Then $n^2 - 1 = 4k^2 + 4k = 4k(k + 1)$.
3. One of $k$ and $k + 1$ is even, so $k(k + 1)$ is even, and $8$ divides $4k(k + 1)$.

A characterization lets you replace one condition by the other: it gives $n^2 \equiv 1 \pmod 8$ for every odd $n$, such as $7^2 = 49 = 6 \cdot 8 + 1$.
Step 2 alone shows only that the condition is necessary, so both directions are needed.

### L3 human

A characterization says that two predicates have the same truth set, and a TFAE list says that many predicates have the same truth set.
A graph is planar if and only if it contains no subdivision of $K_5$ or $K_{3,3}$ (Kuratowski), and a subset of $\mathbb{R}^n$ is compact if and only if it is closed and bounded (Heine-Borel).
In optimization, $\nabla f(c) = 0$ is necessary for an interior extremum, a second-order condition on the Hessian is sufficient for a strict local extremum, and convexity makes the first-order condition sufficient.
The Karush-Kuhn-Tucker conditions follow the same pattern: necessary under a constraint qualification, and sufficient under convexity.
Order the predicates on $D$ by inclusion of their truth sets.
The sufficient conditions for $Q$ lie below $Q$, the necessary conditions lie above $Q$, and a characterization of $Q$ lies at $Q$ itself.
