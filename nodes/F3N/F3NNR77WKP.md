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

An example of a mathematical notion is one particular object that satisfies the definition of the notion, given so exactly that a reader can check each condition.
A non-example is an object that fails the definition, usually in exactly one condition.
Mathematicians sort examples by their role: a generic example has no special features beyond the definition, an extreme example lies at the edge of what the definition allows, and a boundary example just satisfies or just fails one condition.
A [[counterexample|0ED72CTBNP]] is an example that shows a universal statement to be false.
The example space of a person for a notion is the set of examples that the person can call to mind, together with the ways to build new ones.
Examples do not prove universal statements, but they guide almost each step of mathematical work: they make definitions clear, suggest [[conjectures|WMEMMHZ3BH]], test them, and show the shape of a [[proof|0B94TKFQJX]].

## Motivation

A definition such as "a group is a set with an associative operation, an identity and inverses" is short, but it says little until we see groups.
The integers with addition, the nonzero rationals with multiplication and the symmetries of a square fill the definition with content.
In the same way, a conjecture is formed from examples and is first tested on examples.
A single well-chosen example can refute a claim that seemed true, and a well-chosen non-example can show why a condition of a definition is there.
So a working mathematician keeps a stock of standard examples for each notion and uses it all the time.

## Notation

The words have no fixed technical sense, and authors use them in slightly different ways.
"Generic" in this page means "with no special property beyond the definition".
In algebraic geometry and in analysis, [[generic|3BHPBW4WJV]] also has a technical sense: a property is generic when it holds outside a small exceptional set.
"Counterexample" always refers to a statement: an object is a counterexample to a statement, not to a definition.
"Non-example" always refers to a definition or a notion.

## Remarks

### Examples

- Generic example. The triangle with vertices $(0, 0)$, $(4, 0)$ and $(1, 3)$ has no two equal sides and no right angle, so a claim about all triangles is tested fairly on it. [[This example|4KAG9W328V]] uses it.
- Extreme example. The trivial group $\{e\}$ is the smallest group. Many statements about groups have a degenerate but true case here, and some definitions exclude it on purpose.
- Boundary example. The function $f(x) = |x|$ is continuous on $\mathbb{R}$ but not differentiable at $0$. It sits just outside the class of differentiable functions.
- Test of a conjecture. The claim "each group of order $4$ is cyclic" is confirmed by $\mathbb{Z}/4\mathbb{Z}$ and refuted by the Klein four-group, as [[this example|6QWGVWWVGC]] shows.
- Guide for a definition. The wish that prime factorization be unique is the reason that $1$ is not a prime number, as [[this example|JSR7S5TZ9C]] shows.

### Non-examples

- A special figure used as if it were generic is not a fair test of a claim about all triangles. An equilateral triangle has extra symmetry, as [[this non-example|4KAG9W328V]] shows.
- A list of cases that agree with a statement is not a proof of the statement. The values of $n^2 + n + 41$ are prime for $n = 0$ to $39$, but $40^2 + 40 + 41 = 1681 = 41^2$.
- The number $1$ is a non-example of a [[prime number|01826KMG2H]]. It fails the condition "has exactly two positive divisors", because its only positive divisor is $1$.

### Basic properties

- One counterexample refutes a universal statement, because the negation of "for each $x$, $P(x)$" is "for some $x$, not $P(x)$".
- No number of examples proves a universal statement over an infinite set, because the examples cover only finitely many cases.
- An example proves an existential statement. To show that a group which is not cyclic exists, it suffices to give the Klein four-group and check it.
- A good non-example for a definition fails exactly one condition. Then it shows that this condition is not a consequence of the others.

### History

Imre Lakatos made the role of counterexamples a theme of his book "Proofs and Refutations" (1976), built on the history of [[Euler's polyhedron formula|09HT3P35YP]].
He called objects that violate a conjecture but are rejected as not "real" instances monsters.
Books of counterexamples became a genre, for example Gelbaum and Olmsted, "Counterexamples in Analysis" (1964), and Steen and Seebach, "Counterexamples in Topology" (1970).
Anne Watson and John Mason studied example spaces of learners in their book "Mathematics as a Constructive Activity: Learners Generating Examples" (2005).

### Common errors

- Students test a claim only on special examples, such as an equilateral triangle, the identity matrix or the number $2$. Special examples often have extra properties that hide the failure of the claim.
- Students take one confirming example as a proof of a universal statement. A confirming example only shows that the statement has a chance to be true.
- Students forget the extreme cases: the empty set, the trivial group, $n = 0$, the zero function. Many false proofs fail exactly there.

## Explanations

### L1 human

An example is one concrete case of an idea.
The number $6$ is an example of an even number, and the number $7$ is a non-example.
Mathematicians use examples to understand a new word, to guess a rule, and to test the rule.
If somebody says "each number that ends in $3$ is prime", the example $33 = 3 \cdot 11$ shows at once that the rule is wrong.
But many examples that agree with a rule do not prove the rule.
For that, a proof is necessary.

### L2 human

We use examples to decide whether the claim "if $a^2 = b^2$ for two $2 \times 2$ matrices, then $a = b$ or $a = -b$" is true.

1. The claim is universal, so one counterexample refutes it. We look for one in a simple family of matrices.
2. We take $b = I$, the identity matrix. Then $b^2 = I$, and we want a matrix $a$ with $a^2 = I$.
3. The matrix $a = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ gives $a^2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I$.
4. But $a \neq I$ and $a \neq -I$, because the diagonal entries of $a$ are $1$ and $-1$.
5. So $a$ is a counterexample, and the claim is false.

The typical use is this cycle: guess a statement from examples, test it on more varied examples, then prove it or refute it.
Here the search for a counterexample went to a special family on purpose, because the claim is universal and one failure is enough.
The trap is the opposite direction.
To show that a claim is true, special examples are the weakest evidence, because they have extra properties that the general case lacks.

### L3 human

Examples organize a large part of mathematical knowledge.
A mature mathematician knows for each notion a few test objects: for groups the cyclic groups, $S_3$, the quaternion group and $\mathrm{SL}_2(\mathbb{Z})$; for topological spaces the Cantor set, the long line and the Sierpiński space.
These objects are chosen because each one fails some property that the others have, so they separate the possible implications between properties.
In this sense a set of examples and non-examples is a map of the logical relations between the conditions of a theory.

Examples also shape definitions, as Lakatos showed.
When a counterexample to a conjecture appears, the community can change the conjecture, add a hypothesis, or change the definition so that the object is no longer an instance.
The choice between these options is a choice about which examples a notion should cover, as with the exclusion of $1$ from the prime numbers.
Later sub-areas use these ideas again: the methods of proof include the construction of examples and counterexamples, and the [[classification of objects|9HQ3TADPA8]] is the attempt to list all examples of a notion up to equivalence.
