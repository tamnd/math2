---
tag: F3NNR77WKP
kind: concept
name: Examples in mathematical practice
msc: ["00A35", "97E50"]
topics: [N4P3E53HM0]
audience: ug1
uses: [0B94TKFQJX, 0ED72CTBNP, WMEMMHZ3BH]
sources:
  - url: https://en.wikipedia.org/wiki/Counterexample
    locator: lead section
  - url: https://en.wikipedia.org/wiki/List_of_mathematical_examples
    locator: lead section
  - book: isbn:9781108439534
---

## Summary

An example is one particular object that you can write down and check against a definition, one condition at a time.
No list of examples proves a statement about all cases, but examples guide almost every step of mathematical work: they give a definition its content, suggest [[conjectures|WMEMMHZ3BH]], test them, and show the shape of a [[proof|0B94TKFQJX]].

An *example* of a notion is an object, described exactly enough that a reader can check each condition of the definition, that satisfies all the conditions.
A *non-example* is an object that fails the definition, and the most useful non-examples fail exactly one condition.
A [[counterexample|0ED72CTBNP]] is an object that makes a universal statement false.
Examples also differ in their role.
A *generic* example has no special features beyond the definition, an *extreme* example sits at the edge of what the definition allows, and a *boundary* example just satisfies or just fails one condition.
The *example space* of a person for a notion is the set of examples that the person can call to mind, together with the ways that the person knows to build new ones.

## Motivation

The definition "a group is a set with an associative operation, an identity element and inverses" is short, and it says almost nothing until you have seen some groups.
The integers with addition, the nonzero rational numbers with multiplication and the eight symmetries of a square fill it with content.
With them in mind, you can read a new claim about groups and test it at once.

Examples do the same work for conjectures.
A pattern in a table of cases suggests a statement, and the first thing that a mathematician does with the statement is to try it on more cases, chosen to be as different as possible.
One well-chosen object can destroy a claim that looked safe, and one well-chosen non-example can show why a definition has a condition that seemed fussy.
The idea returns in [[abstraction and generalization|976RZZCT1H]], where a notion is built from its examples, and in [[classification|9HQ3TADPA8]], which tries to list all examples of a notion.

## Notation

The words have no fixed technical sense, and authors use them in slightly different ways.
Here "generic" means "with no special property beyond the definition".
In algebraic geometry and in analysis, [[generic|3BHPBW4WJV]] also has a technical sense: a property is generic when it holds outside a small exceptional set.
"Counterexample" always refers to a statement, so an object is a counterexample to a claim, not to a definition.
"Non-example" always refers to a definition or a notion.

## Remarks

### Three kinds of test object

Suppose a claim is about all triangles.
The triangle with vertices $(0, 0)$, $(4, 0)$ and $(1, 3)$ is a fair test, because its side lengths
$$4, \qquad \sqrt{1 + 9} = \sqrt{10}, \qquad \sqrt{9 + 9} = \sqrt{18}$$
are all different, and no sum of two squares among $16$, $10$ and $18$ equals the third, so it has no right angle.
An equilateral triangle is a poor test, because its extra symmetry can make a false claim look true, as [[the special figure example|4KAG9W328V]] shows with altitudes and midpoints.

Extreme examples sit at the edge of a definition.
The trivial group $\{e\}$ is the smallest group, and many statements about groups have a true but degenerate case there.
Boundary examples sit just inside or just outside a class.
The function $f(x) = |x|$ is continuous on $\mathbb{R}$ but not differentiable at $0$, so it lies just outside the differentiable functions.

### One counterexample settles a claim

Take the claim "every group with $4$ elements is cyclic".
The group $\mathbb{Z}/4\mathbb{Z}$ agrees with it, since the element $1$ has order $4$.
The Klein four-group $\{e, a, b, c\}$, in which every element other than $e$ squares to $e$, has no element of order $4$, so it is not cyclic.
That single group refutes the claim, as [[the test of groups of order 4|6QWGVWWVGC]] works out.

The logic behind this is the negation of a universal statement.
The negation of "for every $x$, $P(x)$" is "for some $x$, not $P(x)$", so one object that fails $P$ is enough.
The same logic runs in reverse for existence.
To prove that a group which is not cyclic exists, it is enough to give the Klein four-group and check it.

### Agreeing cases prove nothing

The polynomial $n^2 + n + 41$ gives a prime for each $n = 0, 1, \dots, 39$.
At $n = 40$ the pattern breaks:
$$40^2 + 40 + 41 = 40 \cdot 41 + 41 = 41 \cdot 41 = 1681.$$
Check: $41^2 = 1600 + 80 + 1 = 1681$.
So forty agreeing cases did not make the statement true, as [[the forty prime values|H75AB4EJT5]] explain.

The cases can run much further than forty.
Pólya conjectured that for every $n \ge 2$, at least half of the numbers from $1$ to $n$ have an odd number of prime factors, counted with multiplicity.
The statement holds for every $n$ up to $906150256$, and the smallest counterexample is $n = 906150257$.
No amount of agreeing evidence replaces a proof, and no amount is too large to be overturned.

### Examples that shape a definition

Why is $1$ not a prime number?
The number $1$ has no positive divisors other than $1$ and itself, so the naive definition would admit it.
But then $6 = 2 \cdot 3 = 1 \cdot 2 \cdot 3$ would have two different factorizations into primes, and unique factorization would fail.
The example of $1$ is the reason for the condition $p > 1$, as [[the page on the prime 1|JSR7S5TZ9C]] explains.

A good non-example fails exactly one condition, because it then shows that this condition does not follow from the others.
The natural numbers $\{0, 1, 2, \dots\}$ with addition have an associative operation and an identity $0$, but $1$ has no inverse, since $1 + m \ge 1$ for every $m$.
So inverses are a real requirement of the group axioms and not a consequence of the other two.

### Watch out

The most common error is to test a claim only on special examples, such as an equilateral triangle, the identity matrix or the number $2$.
Take the claim "$x^2 \ge x$ for every real number $x$".
It holds for $x = 2$, $3$ and $10$, and it even holds for $x = 0$ and $x = 1$.
It fails for $x = \tfrac{1}{2}$:
$$\left(\tfrac{1}{2}\right)^2 = \tfrac{1}{4} < \tfrac{1}{2}.$$
The correct move is to look for test values in every region that the claim covers: negative, between $0$ and $1$, large.
A second error is to forget the extreme cases: the empty set, the trivial group, $n = 0$, the zero function.
Many false proofs fail exactly there.

### History

Imre Lakatos made counterexamples the main theme of [[Proofs and Refutations|79P9CTRN0V]], published as a book in 1976, which follows the history of [[Euler's polyhedron formula|09HT3P35YP]].
He called objects that violate a conjecture, and that some people then reject as not real instances, "monsters".
Books of counterexamples became a genre, for example Gelbaum and Olmsted's "Counterexamples in Analysis" (1964) and Steen and Seebach's "Counterexamples in Topology" (1970).
Anne Watson and John Mason studied the example spaces of learners in "Mathematics as a Constructive Activity: Learners Generating Examples" (2005).

### Try it

First, the claim is "if $n^2$ is divisible by $4$, then $n$ is divisible by $4$"; find a counterexample.
Take $n = 2$: then $n^2 = 4$ is divisible by $4$, but $2$ is not.

Second, give a non-example of a prime number other than $1$ that fails the definition in a different way.
The number $6$ is greater than $1$ but has the divisors $2$ and $3$, so it fails the condition on divisors.

Third, is the empty set a fair test for the claim "every set of real numbers has a smallest element"?
It is an extreme example, and it refutes the claim at once, because it has no elements at all.

## Explanations

### L1 human

An example is one concrete case of an idea.
The number $6$ is an example of an even number, and the number $7$ is a non-example.
Mathematicians use examples to understand a new word, to guess a rule, and to test the rule.
If somebody says "every number that ends in $3$ is prime", the example $33 = 3 \cdot 11$ shows at once that the rule is wrong.
But many examples that agree with a rule do not prove the rule, and for that a proof is needed.

### L2 human

Here is a typical use: is it true that $A^2 = B^2$ for two $2 \times 2$ matrices forces $A = B$ or $A = -B$?
For numbers it does, since $a^2 = b^2$ gives $(a - b)(a + b) = 0$.
The claim is universal, so one counterexample would refute it, and we may search in a simple family on purpose.
Take $B = I$, so that $B^2 = I$, and look for a diagonal matrix $A$ with $A^2 = I$:
$$A = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}, \qquad A^2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I.$$
Check: the diagonal entries of $A$ are $1$ and $-1$, so $A \ne I$ and $A \ne -I$.
So the claim is false for matrices, and the number argument broke because $(A - B)(A + B) = 0$ does not force a factor to be $0$.
This is the usual cycle: guess from examples, test on varied examples, then prove or refute.
Watch out for the opposite direction: to support a claim, special examples are the weakest evidence, because they have properties that the general case lacks.

### L3 human

A mature mathematician knows a few test objects for each notion.
For groups these include the cyclic groups, $S_3$, the quaternion group and $\mathrm{SL}_2(\mathbb{Z})$, and for topological spaces the Cantor set, the long line and the Sierpiński space.
They are chosen because each one fails some property that the others have, so together they separate the possible implications between properties.
In this sense a stock of examples and non-examples is a map of the logical relations between the conditions of a theory.

Examples also shape definitions, as Lakatos showed.
When a counterexample to a conjecture appears, mathematicians can change the conjecture, add a hypothesis, or change a definition so that the object is no longer an instance.
Each choice is a decision about which examples a notion should cover, as with the exclusion of $1$ from the primes.
Later sub-areas use these ideas again: the proof methods include the construction of examples and counterexamples, and [[classification|9HQ3TADPA8]] lists all examples of a notion up to equivalence.
