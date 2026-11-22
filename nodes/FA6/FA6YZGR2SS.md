---
tag: FA6YZGR2SS
kind: concept
name: Conditional statements
msc: ["97E40", "03B05"]
topics: [WMY13MXY3W]
audience: school
uses: [S9MHMRAX88, 12QQ51VK01]
sources:
  - url: https://en.wikipedia.org/wiki/Material_conditional
    locator: lead section
  - url: https://en.wikipedia.org/wiki/If_and_only_if
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Necessity_and_sufficiency
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.5
---

## Summary

Most theorems are promises with a condition: "if this holds, then that holds".
A calculus book says "if $f$ is differentiable at $a$, then $f$ is continuous at $a$", and the same book may say "$f$ is differentiable at $a$ only if $f$ is continuous at $a$".
The two sentences make the same promise, and learning to see that is learning to read conditionals.

A *conditional statement* is a [[statement|S9MHMRAX88]] of the form "if $P$, then $Q$", where $P$ and $Q$ are statements.
The statement $P$ is the *hypothesis*, and $Q$ is the *conclusion*.
In mathematics "if $P$, then $Q$" is false when $P$ is true and $Q$ is false, and it is true in the three other cases.
The same conditional has many English forms: "$P$ implies $Q$", "$Q$ if $P$", "$P$ only if $Q$", "$Q$ whenever $P$", "$P$ is sufficient for $Q$" and "$Q$ is necessary for $P$".
The *biconditional* "$P$ if and only if $Q$", often written "$P$ iff $Q$", means "if $P$ then $Q$, and if $Q$ then $P$".

## Motivation

In daily speech "if" also carries ideas of cause and of time, as in "if you drop the glass, it will break".
Mathematics keeps only the part that a proof can check: whenever the hypothesis is true, the conclusion is true.
This choice also settles the cases with a false hypothesis.
The theorem "for every integer $n$, if $4$ divides $n$, then $n$ is even" is true, so each of its instances must be true.
That includes $n = 6$, with a false hypothesis and a true conclusion, and $n = 7$, with both false.
So a conditional with a false hypothesis counts as true, and the only instance that could break the theorem is an $n$ that is divisible by $4$ and odd.

Conditionals return on nearly every later page.
A proof of a conditional assumes the hypothesis and reaches the conclusion, and [[negating mathematical statements|K930V33BSC]] shows that "not (if $P$, then $Q$)" is "$P$ and not $Q$".
The [[Wason selection task|7GYZJ2MGY9]] shows how easily people misread a conditional outside mathematics.

## Notation

The conditional "if $P$, then $Q$" is written $P \Rightarrow Q$, $P \to Q$ or, in older books, $P \supset Q$.
The biconditional is written $P \Leftrightarrow Q$, $P \leftrightarrow Q$ or $P \equiv Q$, and in words "iff".
The hypothesis is also called the antecedent or the premise, and the conclusion the consequent.
The arrow $\to$ also denotes functions, as in $f \colon \mathbb{R} \to \mathbb{R}$, and $\supset$ also means "is a superset of", so many authors prefer $\Rightarrow$ and $\Leftrightarrow$ between statements.
Watch out: an arrow joins statements, never numbers, so "$x = 2 \Rightarrow x^2 = 4$" is a conditional and not a step of a calculation.

## Remarks

### One promise, many sentences

[[The conditional "if $4$ divides $n$, then $n$ is even"|D77E2EA786]] can be said in seven ways, with "for every integer $n$" understood:

1. if $4$ divides $n$, then $n$ is even;
2. $4$ dividing $n$ implies that $n$ is even;
3. $n$ is even if $4$ divides $n$;
4. $4$ divides $n$ only if $n$ is even;
5. $n$ is even whenever $4$ divides $n$;
6. divisibility by $4$ is sufficient for evenness;
7. evenness is necessary for divisibility by $4$.

The hypothesis need not come first.
In forms 3 and 5 the conclusion comes first, and in form 4 "only if" stands before the conclusion.
The words "necessary" and "sufficient" have their own page, [[necessary and sufficient conditions|09BJQQB3VS]].

### Only if, and unless

"$P$ only if $Q$" means "if $P$, then $Q$": $P$ cannot happen without $Q$.
So "for a real number $x$, $x > 2$ only if $x > 1$" is true.
Turned around, "$x > 1$ only if $x > 2$" is false, because $x = 1.5$ satisfies $x > 1$ but not $x > 2$.
A safe habit is to rewrite every "only if" as "if ... then" before you use it.

"$P$ unless $Q$" means "if not $Q$, then $P$", which is the same as "$P$ or $Q$" with the inclusive or.
"A square matrix $A$ is invertible unless $\det A = 0$" says: if $\det A \ne 0$, then $A$ is invertible.
In speech "unless" often also suggests the reverse direction, but the mathematical reading does not claim it.
For matrices the reverse happens to be true as well, by a separate theorem.

### If and only if

A biconditional is two conditionals at once, so its proof has two parts, as [[the biconditional|0S6GMNJ62Y]] explains.
"An integer $n$ is even if and only if $n^2$ is even" is true.
If $n = 2k$, then $n^2 = 2(2k^2)$ is even.
If $n = 2k + 1$, then
$$n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$$
is odd, so an even $n^2$ forces an even $n$.
Other forms are "exactly when", "precisely when" and "is equivalent to".

The "if" of a definition is a special case.
In "an integer is even if it is divisible by $2$", the word "if" means "if and only if", as [[the "if" of a definition|FBCKHZPS3Y]] shows.
Outside definitions, "if" is one-way.

### Hidden quantifiers

Most conditionals in mathematics hide a "for every".
"If $x > 2$, then $x^2 > 4$" means "for every real $x$, if $x > 2$, then $x^2 > 4$", as [[the hidden quantifier in "if $x > 2$, then $x^2 > 4$"|FWXPGJBK97]] shows.
Some conditionals hide the word "if" as well.
"Every square is a rectangle" means: for every quadrilateral $Q$, if $Q$ is a square, then $Q$ is a rectangle.
So the form "every $A$ is a $B$" is always a conditional in disguise.

Some sentences look like conditionals and are not.
"Since $n$ is even, $n^2$ is even" claims that $n$ is even and gives a reason, while a conditional makes no claim about its hypothesis.
"If a check is wanted, put $n = 3$" has a command as its main clause, so it has no truth value.

### The rules you can use

"If $P$, then $Q$" is false exactly when $P$ is true and $Q$ is false; logic calls this the material conditional or [[implication|0NMG7W7Q11]].
A conditional with a false hypothesis is true, which is [[vacuous truth|0V4QXPGJQK]].
A conditional has the same truth value as its [[contrapositive|04T1CT7212]] "if not $Q$, then not $P$", and that is the basis of [[proof by contrapositive|0BB5TPGQ1N]].
The [[converse|09A3N7ZN5G]] "if $Q$, then $P$" and the [[inverse|VB7B8766D2]] "if not $P$, then not $Q$" can differ from it.
For example, the converse of "if $4$ divides $n$, then $n$ is even" fails for $n = 2$.
The biconditional is true exactly when $P$ and $Q$ have the same truth value.

### Watch out

The first error is to prove the converse instead of the statement.
To prove "if $P$, then $Q$", assume $P$ and reach $Q$, not the other way round.
The second error is to read "$P$ only if $Q$" as "if $Q$, then $P$".
The third error is to call a conditional with a false hypothesis false or meaningless.
"If $1 = 2$, then $5$ is even" is true, because its hypothesis is false.
The fourth error is to write "$x^2 = 4 \Rightarrow x = 2$" for real $x$.
That conditional is false, because $x = -2$ satisfies the hypothesis and not the conclusion.

### History

Philo the Dialectician, a Greek logician of about 300 BC, held that a conditional is false only when its antecedent is true and its consequent is false.
This is the [[Philonian conditional|V4HMDD1R0D]], and it is the conditional of modern mathematics.
Gottlob Frege took this conditional as a basic connective in his Begriffsschrift of 1879.
Paul Halmos wrote that he introduced the abbreviation "iff".

### Try it

First, rewrite "a function is continuous whenever it is differentiable" with "only if".
It is "a function is differentiable only if it is continuous".

Second, is "$n^2$ is odd only if $n$ is odd" true for every integer $n$?
Yes: it says "if $n^2$ is odd, then $n$ is odd", which is the contrapositive of "if $n$ is even, then $n^2$ is even".

## Explanations

### L1 human

A conditional is a promise: "if it rains, I will take an umbrella".
The promise is broken only when it rains and I do not take an umbrella.
If it does not rain, the promise is not broken, whatever I do.
In mathematics, "if a number ends in $0$, then it is even" works the same way.
For $20$ the promise is kept, because $20$ ends in $0$ and is even.
For $14$ the promise is not tested, because $14$ does not end in $0$, so it is not broken.
No number breaks the promise, so the statement is true.

### L2 human

Take the sentence "a function $f \colon \mathbb{R} \to \mathbb{R}$ is continuous whenever it is differentiable".
"$Q$ whenever $P$" means "if $P$, then $Q$", so the hypothesis is "$f$ is differentiable" and the conclusion is "$f$ is continuous".
The sentence speaks about every such $f$, so it is the theorem that [[differentiable functions are continuous|07ZMX4ANJS]].
In other forms: "$f$ is differentiable only if $f$ is continuous", "continuity is necessary for differentiability", and "differentiability is sufficient for continuity".

The contrapositive, "if $f$ is not continuous, then $f$ is not differentiable", is true because the theorem is true.
The converse, "if $f$ is continuous, then $f$ is differentiable", is false, since $|x|$ is continuous but not differentiable at $0$.
This analysis is the start of every proof of a conditional: the hypothesis says what you may assume, and the conclusion says what you must reach.
Watch out: "differentiable only if continuous" sounds to many readers like "continuous implies differentiable", which is the wrong direction.

### L3 human

The conditional of mathematics is the material conditional of classical logic.
It ignores relevance, so "if $2 + 2 = 4$, then $\pi$ is irrational" is true, although the parts have nothing to do with each other.
Such cases are the [[paradoxes of material implication|3T7ZJFC9QF]], and relevance logics and strict implication try to avoid them.
In practice a mathematical conditional almost always carries a universal quantifier, and "for all $x$, $P(x) \Rightarrow Q(x)$" says that $\{x : P(x)\}$ is a [[subset|0BJR9QR08E]] of $\{x : Q(x)\}$.

In a [[Boolean algebra|0XADJKM699]] the conditional $P \Rightarrow Q$ is $\neg P \lor Q$, and it equals the top element exactly when $P \le Q$.
The [[deduction theorem|9X08XK5RV2]] says that $Q$ follows from the assumption $P$ exactly when $P \Rightarrow Q$ can be proved, which is why "assume $P$, derive $Q$" proves a conditional.
In [[intuitionistic logic|Q11N8X99FK]] and in type theory, a proof of $P \Rightarrow Q$ is a method that turns each proof of $P$ into a proof of $Q$, so a conditional is a function type.
The proof methods for conditionals are in the topic [[proof methods|G9JFJGY4TQ]].
