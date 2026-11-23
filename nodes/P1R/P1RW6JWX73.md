---
tag: P1RW6JWX73
kind: problem
name: Hilbert's program
msc: ["03A05", "03F25", "03F30"]
topics: [H8QZY0RZXZ]
audience: ug2
uses: [46JCQ6KDA4, 0QFT7Z76N5, 439M8B4DY2, VM8TQ70CVJ, N238J43XNE, X9WYNYE29C, 4PZM5GJTR5]
about: [EFFRJFW67Y]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert's_program
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Gentzen%27s_consistency_proof
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: lead section
  - book: isbn:9780521857840
same_as:
  wikidata: Q968548
  wikipedia: Hilbert's program
history:
  posed_by: "David Hilbert"
  first_stated: "1922"
---

## Problem

The statement "no whole number $x$ has $x \cdot x = 2$" can be checked one number at a time, and each check is a finite computation.
Suppose a proof of it uses real numbers, infinite sets or other tools whose meaning is less clear.
Hilbert's program asks for a guarantee that such proofs never give a false statement of this checkable kind, and it asks for the guarantee by the simplest reasoning possible.

The program has two parts.

1. Formalization: write all of classical mathematics as a [[formal system|439M8B4DY2]] $T$.
   The system has a finite alphabet, decidable sets of axioms and rules of inference, and so a decidable notion of proof.
2. Finitary consistency: prove, by finitary means only, that $T$ is [[consistent|VM8TQ70CVJ]].
   That is, no formula $\varphi$ has both $T \vdash \varphi$ and $T \vdash \neg \varphi$.

A proof is finitary when it reasons only about finite, concretely given objects, such as strings of symbols and natural numbers, by steps that can be checked in finitely many operations.
The program does not define "finitary" as a formal system.
Most logicians today identify finitary reasoning with primitive recursive arithmetic (PRA), the theory of [[primitive recursive functions|5NVA2JRHPV]] with quantifier-free induction.
Hilbert also hoped for a negation complete theory, one that decides each sentence, and for a decision procedure for first-order logic.

## Remarks

### Real and ideal statements

Hilbert divided the statements of mathematics into two kinds.
A real statement is a finitary statement, such as $2 + 3 = 5$, or a statement $\forall x\, \varphi(x)$ in which $\varphi$ is a decidable property of natural numbers.
An ideal statement is any other statement, for example a statement about all real numbers or about an arbitrary set.
Ideal statements have no direct finitary meaning.
Hilbert compared them to the ideal points of projective geometry: they are added to make the theory simple.
The aim of the program was to show that ideal statements are a safe tool: every real statement proved with their help is true.

### Why consistency is enough for real statements

The heart of the program is an argument that consistency makes ideal methods safe for real statements.
Let $T$ be a theory in the language of arithmetic that proves every true equation and inequation between closed numerical terms, as [[Robinson arithmetic|3K1AKGXF8A]] does.
Let $\forall x\, \varphi(x)$ be a real statement, with $\varphi$ quantifier-free.

1. Assume that $T$ is consistent and that $T \vdash \forall x\, \varphi(x)$.
2. Assume, for a contradiction, that $\forall x\, \varphi(x)$ is false in the natural numbers.
3. Then there is a number $n$ with $\varphi(n)$ false.
4. The formula $\neg \varphi(\underline{n})$ is a true quantifier-free sentence, where $\underline{n}$ is the numeral of $n$.
   So $T \vdash \neg \varphi(\underline{n})$ by the choice of $T$.
5. From $T \vdash \forall x\, \varphi(x)$, universal instantiation gives $T \vdash \varphi(\underline{n})$.
6. Steps 4 and 5 show that $T$ proves a formula and its negation, which contradicts step 1.
7. So $\forall x\, \varphi(x)$ is true.

### Consistency as conservativity

The argument of steps 1 to 7 is itself finitary.
So a finitary proof of $\operatorname{Con}(T)$ would give a finitary proof that each real theorem of $T$ is true.
In the language of [[conservative extensions|N238J43XNE]], the program asks that $T$ be conservative over finitary mathematics for real statements.
Steps 1 to 7 reduce this to consistency.

### The second incompleteness theorem

[[Gödel's second incompleteness theorem|4PZM5GJTR5]] of 1931 says the following.
Let $T$ be a consistent theory with a decidable set of axioms that contains a modest amount of arithmetic.
Then $T$ does not prove the arithmetic sentence $\operatorname{Con}(T)$ that expresses its consistency.

Each reasonable formalization of finitary reasoning, such as PRA, is contained in the theories that the program wanted to justify, for example [[Peano arithmetic|0QFT7Z76N5]] or ZFC.
So if finitary proofs are proofs in a subtheory $F$ of $T$, a finitary proof of $\operatorname{Con}(T)$ would be a proof of $\operatorname{Con}(T)$ in $T$, which the theorem forbids.
Hence there is no finitary consistency proof of arithmetic that can be formalized in arithmetic itself.
For this reason most logicians hold that the program cannot be carried out in its original form.
The conclusion depends on the claim that every finitary proof can be formalized inside $T$.

### Gentzen and ordinal analysis

Gerhard Gentzen proved the consistency of Peano arithmetic in 1936; see [[Gentzen's consistency proof|QPV0HNP22S]].
His proof uses finitary methods together with [[transfinite induction|0ZHQMQ2C1N]] up to the ordinal [[epsilon nought|KT50SMH3EC]], applied to quantifier-free properties.
Peano arithmetic does not prove this induction, so Gentzen's proof is not finitary in Hilbert's strict sense.
But it measures exactly what is needed beyond finitary reasoning.
This idea grew into [[ordinal analysis|C5E5TG8PGP]], a central part of [[proof theory|N4EDJNMTEF]].

### Reverse mathematics

A second partial realization comes from [[reverse mathematics|7SQS69T17R]].
The subsystem WKL$_0$ of [[second-order arithmetic|DC60FYCSPM]] proves many theorems of classical analysis and algebra, for example the Heine-Borel theorem for $[0, 1]$.
Harvey Friedman showed that WKL$_0$ is conservative over PRA for $\Pi^0_2$ sentences.
So every real statement proved in WKL$_0$ is also provable by finitary means, and the part of mathematics that WKL$_0$ covers is justified as Hilbert wanted.
Stephen Simpson described this result as a partial realization of Hilbert's program, in a paper of 1988.

### Status

As of 2026-11 the program in its original form is regarded as impossible, by the second incompleteness theorem.
Relativized forms of the program are active research.
They ask which theories are conservative over which weaker theories, and which ordinal measures the strength of a theory.
These questions are studied in [[proof interpretations and conservation results|8XY7JYZKFW]], [[ordinal analysis and ordinal notations|XTTKZTYDSD]] and [[reverse mathematics and subsystems of second-order arithmetic|BY8AAFN7C5]].

### Watch out

The program was not a claim that mathematics is a meaningless game.
Hilbert held that real statements have content, and he used the formal game to justify the ideal ones.

The first incompleteness theorem alone does not refute the program.
The main aim was consistency, and it is the second theorem that blocks a finitary consistency proof.

Gentzen's proof does not show that Peano arithmetic is "unsafe".
It shows that its consistency follows from a principle, induction up to $\varepsilon_0$, that most mathematicians accept without doubt.

### Try it

Is the statement "for every $x$, $x + 0 = x$" a real statement in Hilbert's sense?
Yes: it has the form $\forall x\, \varphi(x)$ with $\varphi$ quantifier-free, and each instance is a finite check.

Is "there is a prime number above $10^{100}$" a real statement of the form used in steps 1 to 7?
No: it is existential, and the argument of steps 1 to 7 does not apply to it.

## History

David Hilbert stated the program in lectures and papers of the early 1920s, with the paper "Neubegründung der Mathematik" of 1922 as an early statement.
His collaborators Paul Bernays and Wilhelm Ackermann, and also John von Neumann, worked on it during the 1920s.
In 1931 Gödel's incompleteness theorems showed that the program could not succeed as planned.
Hilbert and Bernays published the two volumes of *Grundlagen der Mathematik* in 1934 and 1939.
The second volume contains the first detailed proof of the second incompleteness theorem.

## Explanations

### L1 human

Hilbert wanted to put all of mathematics on a safe base.
His plan had two steps.
First, write every proof as a sequence of symbols that follows fixed rules, like moves in a game.
Second, show with simple, finite reasoning that the game can never produce a contradiction such as $0 = 1$.
If the game can never produce $0 = 1$, then a statement such as "$2 + 3 = 5$" proved in the game must be true.
Gödel showed that the second step is impossible in the strong form that Hilbert hoped for.

### L2 human

We run the argument "consistency gives the truth of real statements" on the opening statement.
Take $T$ to be [[Peano arithmetic|0QFT7Z76N5]] and the real statement $S$: for every natural number $x$, $x \cdot x \neq 2$.

1. The formula $x \cdot x \neq 2$ has no quantifiers, so $S$ has the form $\forall x\, \varphi(x)$ of a real statement.
2. $T$ proves $S$: for $x = 0$ and $x = 1$ the square is $0$ or $1$, and for $x \geq 2$ the square is at least $4$.
3. Suppose, for a contradiction, that $S$ were false.
   Then some number $n$ would satisfy $n \cdot n = 2$.
4. The sentence $\underline{n} \cdot \underline{n} = 2$ would then be a true closed equation, so $T$ would prove it.
5. Universal instantiation of $S$ at $\underline{n}$ gives $T \vdash \underline{n} \cdot \underline{n} \neq 2$.
6. Steps 4 and 5 would make $T$ inconsistent.
   So, if $T$ is consistent, $S$ has no counterexample, and $S$ is true.

Step 6 uses only the consistency of $T$, and not the truth of the axioms of $T$.
The typical use of this argument is to reduce trust in a strong theory to trust in its consistency, for statements that can be checked case by case.
Watch out: the argument fails for statements that are not real, such as an existential statement $\exists x\, \psi(x)$.
For example, $T + \neg \operatorname{Con}(T)$ is consistent when $T$ is consistent, by the second incompleteness theorem.
Yet it proves the false statement "there is a proof of $0 = 1$ in $T$".

### L3 human

In modern terms the program asks for a proof of $\operatorname{Con}(T)$ in PRA for a strong theory $T$.
By the argument above, such a proof would show in PRA that every $\Pi^0_1$ theorem of $T$ is true.
The second incompleteness theorem rules this out for every consistent $T$ that contains PRA, so the modern versions change the question.
One version replaces PRA by a stronger but still evident base, as Gentzen did with induction up to $\varepsilon_0$, and leads to ordinal analysis.
Another version fixes PRA and looks for strong theories that are still conservative over it, such as WKL$_0$.
It leads to reverse mathematics and to the conservation results of [[proof interpretations|8XY7JYZKFW]].
A third version goes back to Georg Kreisel's program of unwinding proofs.
It asks what a proof in $T$ gives computationally, for example a bound or an algorithm, and it is now called proof mining.
The [[foundations of mathematics|EFFRJFW67Y]] place the program among the other foundational programs, and the [[philosophy of mathematics|NTJ5XW0PVD]] treats [[formalism|46JCQ6KDA4]] as a view of mathematics.
