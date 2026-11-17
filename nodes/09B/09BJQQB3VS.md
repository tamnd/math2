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

Let $p$ and $q$ be statements, and suppose that the [[material implication|0NMG7W7Q11]] $p \to q$ is true.
Then $p$ is a sufficient condition for $q$, and $q$ is a necessary condition for $p$.
The condition $p$ is necessary and sufficient for $q$ when $p \to q$ and $q \to p$ are both true, that is, when the [[biconditional|0S6GMNJ62Y]] $p \leftrightarrow q$ is true.
For conditions on a variable $x$ in a domain $D$, "$P(x)$ is sufficient for $Q(x)$" means $\forall x \in D\, (P(x) \to Q(x))$, with the [[universal quantifier|0GHS47PDAQ]] understood.
A theorem that gives a necessary and sufficient condition for a property is a characterization of that property.
The idea matters because a characterization replaces a property by an equivalent condition that is often easier to check.

## Motivation

Many problems ask whether an object has a property: whether a number is prime, whether a triangle has a right angle, or whether a function has a maximum at a point.
A sufficient condition gives a way to say "yes" in some cases.
A necessary condition gives a way to say "no" in some cases: if the necessary condition fails, the property fails.
A necessary and sufficient condition settles every case, because it says "yes" exactly when the answer is "yes".
For example, the rule of the digit sum decides divisibility by $3$ for every natural number.

The words "necessary" and "sufficient" are two readings of the one implication $p \to q$.
The reading "$p$ is sufficient for $q$" looks forward from $p$: whenever $p$ holds, $q$ holds.
The reading "$q$ is necessary for $p$" looks back from $p$: $p$ cannot hold without $q$.
The English forms of a conditional, such as "only if", are listed on the page [[conditional statements|FA6YZGR2SS]].

## Notation

There is no special symbol: "$p$ is sufficient for $q$" is written $p \to q$ or $p \Rightarrow q$.
"$p$ is necessary for $q$" is written $q \to p$, or $p \Leftarrow q$.
"$p$ is necessary and sufficient for $q$" is written $p \leftrightarrow q$ or $p \Leftrightarrow q$, and in words "$p$ if and only if $q$" or "$p$ iff $q$".
Several equivalent conditions are listed under the words "the following are equivalent", abbreviated TFAE.
In the proof of a characterization "the property holds if and only if $C$", the part labelled "necessity" proves that the property implies $C$, and the part labelled "sufficiency" proves that $C$ implies the property.

## Remarks

### Examples

1. [[Divisibility by 3 is characterized by the digit sum|RYJ4YKRWM2]]: a natural number is divisible by $3$ if and only if its digit sum is divisible by $3$.
2. [[A zero derivative is necessary but not sufficient for a local extremum|9ZJYHTGGW5]]: the condition $f'(c) = 0$ holds at each interior extremum of a differentiable $f$, and it also holds for $x^3$ at $0$, which has no extremum.
3. For an integer $n$, divisibility by $4$ is sufficient for "$n$ is even", but not necessary, because $2$ is even. See the [[English forms of this conditional|D77E2EA786]].
4. The [[converse of the Pythagorean theorem|EFF30FNVZ0]] completes a characterization: a triangle has a right angle at $C$ if and only if $a^2 + b^2 = c^2$.
5. Wilson's theorem and its [[converse|06WRV8HFDY]] characterize the primes: an integer $n > 1$ is prime if and only if $(n - 1)! \equiv -1 \pmod n$.
6. For an integer $n$, "$n^2$ is even" is necessary and sufficient for "$n$ is even". If $n = 2k$, then $n^2 = 2(2k^2)$; if $n = 2k + 1$, then $n^2 = 2(2k^2 + 2k) + 1$ is odd.

### Non-examples

1. [[Being odd is neither necessary nor sufficient for being prime|EB51VZGZ4G]]: the prime $2$ is even, and the odd number $9$ is not prime.
2. For a real number $x$, the condition $x > 1$ is not necessary and sufficient for $x^2 > 1$. It is sufficient, but $x = -2$ satisfies $x^2 > 1$ and not $x > 1$, so it is not necessary.
3. For $f \colon \mathbb{R} \to \mathbb{R}$, continuity at $a$ is not sufficient for differentiability at $a$. The function $|x|$ at $a = 0$ is continuous and not differentiable, although continuity is necessary, by the theorem that [[differentiable functions are continuous|07ZMX4ANJS]].

### Basic properties

1. "$p$ is sufficient for $q$" and "$q$ is necessary for $p$" are the same statement $p \to q$.
2. If $p$ is sufficient for $q$, then $\neg q$ is sufficient for $\neg p$. This is the law of the [[contrapositive|04T1CT7212]], and it is the reason why a failed necessary condition refutes the property.
3. A sufficient condition for a sufficient condition is sufficient: from $p \to q$ and $q \to r$ we get $p \to r$, by [[hypothetical syllogism|7MT8CPCEM4]].
4. If $q_1$ and $q_2$ are both necessary for $p$, then $q_1 \land q_2$ is necessary for $p$. If $p_1$ and $p_2$ are both sufficient for $q$, then $p_1 \lor p_2$ is sufficient for $q$.
5. The relation "is necessary and sufficient for" is symmetric: $p \leftrightarrow q$ and $q \leftrightarrow p$ are [[logically equivalent|0JMR2HM2N2]].
6. In terms of truth sets: $P$ is sufficient for $Q$ on $D$ exactly when $\{x \in D : P(x)\} \subseteq \{x \in D : Q(x)\}$. A necessary and sufficient condition has the same truth set as the property.

### History

Euclid's Elements gives the Pythagorean theorem as Proposition 47 of Book I and its converse as Proposition 48, so the two together form one of the oldest characterization theorems.
The abbreviation "iff" for "if and only if" is due to Paul Halmos.

### Common errors

1. A student treats a necessary condition as sufficient. For example, from $f'(c) = 0$ the student concludes that $f$ has an extremum at $c$, which fails for $f(x) = x^3$ at $c = 0$.
2. A student mixes up the two parts of the proof of a characterization. In "a triangle has a right angle at $C$ if and only if $a^2 + b^2 = c^2$", necessity proves that a right angle forces the equation, and sufficiency proves the converse.
3. A student proves one direction of a characterization twice, once directly and once by its contrapositive, as in [[two proofs of the same direction|K08FN2E081]]. The method of [[proving biconditionals|TFQ1845T84]] needs one proof of each direction.

## Explanations

### L1 human

A sufficient condition is enough to get a result: if it holds, the result holds.
A necessary condition is one that the result cannot do without: if it fails, the result fails.
Being a square is sufficient for being a rectangle, but not necessary, because a $1$ by $2$ rectangle is not a square.
Having four sides is necessary for being a rectangle, but not sufficient, because some four-sided shapes have no right angle.
Having four right angles is necessary and sufficient for a four-sided shape to be a rectangle: it is the definition.

### L2 human

We prove the characterization: for an integer $n$, $n$ is odd if and only if $8$ divides $n^2 - 1$.
The property is "$n$ is odd", and the condition is "$8 \mid n^2 - 1$".

1. Sufficiency: suppose $8$ divides $n^2 - 1$. Then $n^2 - 1$ is even, so $n^2$ is odd. If $n$ were even, $n^2$ would be even, so $n$ is odd.
2. Necessity: suppose $n$ is odd, $n = 2k + 1$. Then $n^2 - 1 = 4k^2 + 4k = 4k(k + 1)$.
3. One of $k$ and $k + 1$ is even, so $k(k + 1)$ is even, and $4k(k + 1)$ is divisible by $8$.
4. Steps 1 to 3 prove both directions, so "$8 \mid n^2 - 1$" is necessary and sufficient for "$n$ is odd".

The typical use of a characterization is to replace one condition by the other.
For example, it gives $n^2 \equiv 1 \pmod 8$ for every odd $n$, such as $7^2 = 49 = 6 \cdot 8 + 1$.
A trap is to prove only step 2 and to claim the characterization: step 2 shows that the condition is necessary, not that it is sufficient.

### L3 human

A characterization says that two predicates have the same truth set, and a long list of equivalent conditions (TFAE) says that many predicates have the same truth set.
Many central theorems have this form: a graph is planar if and only if it contains no subdivision of $K_5$ or $K_{3,3}$ (Kuratowski), and a subset of $\mathbb{R}^n$ is compact if and only if it is closed and bounded (Heine-Borel).
In optimization, the first-order condition $\nabla f(c) = 0$ is a necessary condition for an interior extremum, a second-order condition on the Hessian is a sufficient condition for a strict local extremum, and convexity makes the first-order condition sufficient.
The Karush-Kuhn-Tucker conditions follow the same pattern: necessary under a constraint qualification, and sufficient under convexity.
Order the predicates on $D$ by inclusion of their truth sets.
The sufficient conditions for $Q$ lie below $Q$, the necessary conditions lie above $Q$, and a characterization of $Q$ lies at $Q$ itself.
