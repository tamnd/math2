---
tag: Y896GWYF8A
kind: concept
name: Problem posing
msc: ["00A35", "97D50"]
topics: [X1NSTVGDNQ]
audience: ug1
specializes: [6KCEWEP4WA]
uses: [6KCEWEP4WA, DYD57G2Y5Z, KT5SASGTQ5]
sources:
  - url: https://en.wikipedia.org/wiki/Marion_Walter
    locator: Education and career
  - url: https://en.wikipedia.org/wiki/How_to_Solve_It
    locator: Four phases
  - book: isbn:9780691164076
---

## Summary

Problem posing is the [[heuristic|6KCEWEP4WA]] of making new problems, from a situation, from a problem that you are solving, or from a problem that you have solved.
Its main tool is the question "what if not?": list the features of a problem, change one of them, and ask what the new problem is.

Here is posing at work.
A student has just found that a chessboard holds $204$ squares of all sizes, as in [[counting the squares on a chessboard|H817ES7NHH]].
The first new question that comes to mind is "what about a board with $9$ rows and $9$ columns?"
That question changes only a number, and the same method answers it at once, so it teaches nothing new.
The helping move is to write down the features of the problem and to change one that carries structure.
The features are an $8 \times 8$ board, figures that are squares, figures whose sides lie on grid lines, and a count as the answer.
"What if the figures are not squares?" gives a real question: how many rectangles does the board hold?

The student first tries to count rectangles by size, as for the squares, and finds $64$ sizes from $1 \times 1$ to $8 \times 8$, which is slow.
A new view solves the problem.
A rectangle is fixed by its two vertical sides and its two horizontal sides, and the board has $9$ vertical grid lines and $9$ horizontal grid lines.
So the count is
$$\binom{9}{2} \cdot \binom{9}{2} = 36 \cdot 36 = 1296.$$
Looking back, $1296 = 1^3 + 2^3 + \dots + 8^3$, and that coincidence poses the next question, worked out in [[counting the rectangles on a chessboard|Z0MD0682KC]].

Problem posing is advice, not an algorithm.
It produces questions, and many of them are trivial, too hard, or built on a wrong expectation about the form of the answer.

## Motivation

A textbook exercise comes with its question already chosen, but research and applications do not.
A mathematician must decide what to ask: which quantity to compute, which property to prove, and which case to treat first.
After a problem is solved, the same choice comes back, since the "looking back" phase of [[Pólya's four steps|DYD57G2Y5Z]] asks whether the result or the method can serve for another problem.
Problem posing makes that choice on purpose.
It also turns around the usual direction of teaching, in which students answer questions but rarely ask them.

## Notation

Brown and Walter call their method "what if not", and they start it with a list of the "attributes" of the problem.
They separate two phases: "accepting the given", in which you explore the problem as it is, and "challenging the given", in which you change its attributes.
A changed problem is a "variant" of the original.
Pólya's term "looking back" names the phase after a solution in which you test the result and ask what else it gives.

## Remarks

### The method of "what if not"

The method has five steps.

1. Choose a starting point: a theorem, a problem, a figure or a situation.
2. List its attributes: the objects, the conditions, the numbers and the question asked.
3. For each attribute, ask "what if not?" and name one or more alternatives.
4. For each alternative, pose a question about the new situation, and keep the questions that seem both interesting and within reach.
5. Try to answer them, compare the answers with the original, and pose again.

Writing the list of attributes is the step that matters most.
A student who waits for a new question to appear usually finds only the change of a number, as with the $9 \times 9$ board.
A written list shows features that the solution used without naming them, and those are the features worth changing.

### When it helps

Posing helps after a problem is solved, because a variant tests whether you understand the solution.
A variant that the same method solves shows the range of the method, and a variant that needs a new method shows its limits.

It helps when a problem is too hard, because an easier related problem can be posed by [[specialization|FTBJX4G51S]] or by dropping a condition, as in [[variation of the problem|KT5SASGTQ5]].

It helps when a situation comes without a question, as in modeling or in open tasks in a classroom.
It also helps when a theory is new, since the questions whose answers would organize the theory are the first ones to pose.

Two classical cases show what posing can produce.
"What if the figures on the sides are not squares?" applied to the [[Pythagorean theorem|0VP3A1290K]] gives a theorem for semicircles, equilateral triangles and every family of similar figures, as in [[similar figures on the sides of a right triangle|XNMYYT867E]].
"What if the exponent is not $2$?" applied to [[Pythagorean triples|0M7ARED5Q7]] gives the question of [[Fermat's Last Theorem|0Y5X3SDBCZ]], whether $x^n + y^n = z^n$ has a solution in positive integers for some $n \ge 3$, which took more than three centuries to answer.

### When it misleads

A posed question often carries a silent expectation about its answer, and the expectation can be false.
The sum $1 + 2 + \dots + n$ equals $\frac{n(n + 1)}{2}$, and the analogous question for $1 + \frac{1}{2} + \dots + \frac{1}{n}$ expects a formula of the same kind.
No such formula exists, as [[asking for a rational closed form of the harmonic numbers|ESH74VQRKG]] proves.

A changed attribute can also destroy the content.
"What if the triangle had four sides?" is not a question about triangles, and it gives no problem unless you also say what to ask about quadrilaterals.

Easy posing can hide hard answering.
"What if the rule is $3n - 1$ instead of $3n + 1$?" changes one sign in the [[Collatz conjecture|6PCQEXEX4N]], and the variant has a cycle that avoids $1$, since $5 \mapsto 14 \mapsto 7 \mapsto 20 \mapsto 10 \mapsto 5$.
Whether every starting value falls into a known cycle is then as open as the original question.

The converse and the generalization of a true statement may be false.
"If a quadrilateral is a square, its diagonals have equal length" is true, but a rectangle that is not a square shows that its converse is false.

### Related heuristics

[[Variation of the problem|KT5SASGTQ5]] changes a problem in order to solve it, and problem posing changes it in order to ask something new.
[[Generalization|8NJ0VN9Z97]] and [[specialization|FTBJX4G51S]] are two of the main moves of posing.
[[Analogy|7KDT0R1HF2]] poses a new problem as the analogue of a solved one, with the risk that the analogy fails, as in the harmonic numbers.
At the scale of a whole field, posing general questions gives rise to new theories, as described in [[abstraction and generalization|976RZZCT1H]].

### Watch out

Do not stop at variants that change one number, such as a $9 \times 9$ board instead of an $8 \times 8$ board.
A good variant changes the structure of the problem, the kind of figure, the operation or the condition.

Do not assume that the answer to a variant has the same form as the answer to the original.
The form of the old answer is a guess about the new one, not a promise.

Do not stop after the first new question either.
The method works best when you list many questions and then choose a few.

### History

Georg Cantor defended, among the theses of his doctoral examination in Berlin in 1867, the claim that in mathematics the art of asking a question is worth more than the art of solving it.
George Pólya's *How to Solve It* (1945) ends its four phases with "looking back", which asks what else a solution gives.
David Hilbert's list of $23$ problems, presented in 1900, is the best known case of posing as a contribution to research.
Stephen Brown and Marion Walter wrote *The Art of Problem Posing* (1983), which brought the "what if not" method to teachers.

### Try it

On a $3 \times 3$ board, how many squares and how many rectangles are there?
There are $9 + 4 + 1 = 14$ squares, and there are $\binom{4}{2}^2 = 36$ rectangles.

Pose the converse of "if a triangle is equilateral, then its three angles are equal", and decide whether it is true.
The converse says that a triangle with three equal angles is equilateral, and it is true, because equal angles lie opposite equal sides.

## Explanations

### L1 human

Most of the time in school, someone else gives us the question.
Problem posing means making up our own questions.
Take a fact that we know, for example that a square with side $3$ has area $9$.
Then change something and ask again.
What if it is a rectangle?
What if it is a triangle?
What if we want the perimeter instead?
Some of the new questions are easy, some are hard, and some lead to new mathematics.

### L2 human

We apply "what if not" to the fact that $1 + 2 + \dots + n = \frac{n(n + 1)}{2}$.
The attributes are that the terms are consecutive integers, that they start at $1$, that each term has exponent $1$, and that we add them.

1. "What if the exponent is not $1$?" poses the sum $1^2 + 2^2 + \dots + n^2$.
   Its value is $\frac{n(n + 1)(2n + 1)}{6}$, and for $n = 3$ this gives $14 = 1 + 4 + 9$.
2. "What if the terms are not consecutive integers?" poses the sum $1 + 3 + 5 + \dots + (2n - 1)$.
   Its value is $n^2$, and for $n = 4$ this gives $16 = 1 + 3 + 5 + 7$.
3. "What if we do not add?" poses the product $1 \cdot 2 \cdots n = n!$, which is not a polynomial in $n$, so the useful question becomes its size, which Stirling's formula answers.
4. "What if the terms are not integers?" poses $1 + \frac{1}{2} + \dots + \frac{1}{n}$, the harmonic number $H_n$, and here the expected kind of formula does not exist.

Write the attributes down before you change them, since a written list gives more and better questions than waiting for one.
Watch out: the form of the answer to the original problem is not a promise about the form of the answer to a variant.

### L3 human

In research, posing is often harder than solving.
A good question is hard enough to need new ideas and close enough to known methods to be within reach.
Hilbert's problems, the conjectures of Weil and the Langlands program shaped whole fields because they asked the right questions.
Lakatos described another source of questions: a counterexample to a theorem asks which hypothesis was missing, as in [[proofs and refutations|79P9CTRN0V]].
In teaching, posing tasks are used to test understanding, since a student who can pose a sensible variant knows which features of the solution matter.
