---
tag: YP7KE8E6DC
kind: statement
role: theorem
name: Krajíček-Pudlák-Takeuti theorem
aliases: [kpt-witnessing-theorem, kpt-theorem]
msc: ["03F30", "68Q15"]
topics: [RA380RWEC0]
audience: research
uses: [A2CFPP8JMN, FMM44KFZQT, RH4R7GTTAX, VZ21F10WRS, TDQ7AXGM6P, P0A5DVRYDW, HM7DNQ2H5D]
about: [A2CFPP8JMN, PEJQDHHX8E, TDQ7AXGM6P]
proofs: [QFZA2723F9]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_arithmetic
    locator: Buss's witnessing theorem
  - url: https://en.wikipedia.org/wiki/Herbrand%27s_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Karp%E2%80%93Lipton_theorem
    locator: lead section
history:
  first_stated: "1991"
  notes: "J. Krajíček, P. Pudlák and G. Takeuti, Bounded arithmetic and the polynomial hierarchy, Annals of Pure and Applied Logic 52 (1991), 143-153."
---

## Statement

The KPT theorem turns a proof of a $\forall \exists \forall$ sentence in a weak theory into a fast guessing strategy that is right after a fixed number of corrections.
It also shows that if two neighboring theories of [[bounded arithmetic|A2CFPP8JMN]] are equal, then the [[polynomial hierarchy|TDQ7AXGM6P]] collapses.

We use Buss's theories $S^i_2$ and $T^i_2$, and we write $\square^p_{i+1} = \mathrm{FP}^{\Sigma^p_i}$ for the functions computable in polynomial time with an oracle for $\Sigma^p_i$.
For $i = 0$ we read $\mathsf{PV}_1$ in place of $T^0_2$, as in [[Cook's theory PV|FMM44KFZQT]], and $\square^p_1 = \mathrm{FP}$.

**Theorem.** Let $i \ge 0$.

1. (KPT witnessing.) Let $B(x, y, z)$ be a $\Sigma^b_{i+1}$ formula with the free variables shown, and assume $T^i_2 \vdash \forall x \, \exists y \, \forall z \, B(x, y, z)$.
   Then there are $k \ge 1$ and functions $f_1, \dots, f_k$, where $f_m$ has $m$ arguments and is $\Sigma^b_{i+1}$-definable in $T^i_2$, so that $f_m \in \square^p_{i+1}$.
   Moreover $T^i_2$ proves the disjunction below, with free variables $a, b_1, \dots, b_k$.

$$B(a, f_1(a), b_1) \lor B(a, f_2(a, b_1), b_2) \lor \cdots \lor B(a, f_k(a, b_1, \dots, b_{k-1}), b_k)$$

2. (Collapse.) If $T^i_2 = S^{i+1}_2$, then $\Sigma^p_{i+1} \subseteq \Pi^p_{i+1}/\mathrm{poly}$, and the polynomial hierarchy collapses.

## Remarks

### A game in two rounds

Read the disjunction as a game between a student and a teacher.
The student proposes $y_1 = f_1(a)$.
If $B(a, y_1, z)$ fails for some $z$, the teacher shows such a $z$ as $b_1$, and the student tries again with $y_2 = f_2(a, b_1)$.
The theorem says that the student wins within $k$ rounds against every teacher.

Here is a game where one round is not enough.
Let $R(a, w)$ say that $w \le a$ codes a satisfying assignment of the propositional formula coded by $a$, and let $B$ be the formula below.

$$B(a, y, z) := (y \ge 1 \land R(a, y - 1)) \lor (y = 0 \land \neg R(a, z))$$

So $y = 0$ claims "no assignment works", and $y = w + 1$ offers the assignment $w$.
Take $a$ to code $(x_1 \lor x_2) \land \neg x_1$.
The student opens with $y_1 = 0$.
The teacher refutes this with $b_1$, the assignment $x_1 = 0$, $x_2 = 1$.

$$(0 \lor 1) \land \neg 0 = 1 \land 1 = 1$$

Check: $b_1$ satisfies the formula, so $B(a, 0, b_1)$ is false.
In round two the student plays $y_2 = b_1 + 1$, and $B(a, b_1 + 1, z)$ is true for every $z$.
The student wins, having used the teacher's answer as its own.

### Why each hypothesis is needed

The theory must be $T^i_2$ and not $S^{i+1}_2$.
The theory $S^{i+1}_2$ proves a length-maximization principle that the [[proof|QFZA2723F9]] uses.
If part 1 held for $S^{i+1}_2$, the proof of part 2 would give $\Sigma^p_{i+1} \subseteq \Pi^p_{i+1}/\mathrm{poly}$ outright, for $i = 0$ the inclusion $\mathrm{NP} \subseteq \mathrm{coNP}/\mathrm{poly}$, which nobody expects.

The matrix $B$ must be $\Sigma^b_{i+1}$.
The proof needs $\neg B$ to be equivalent to a universal formula in a universal extension of $T^i_2$, so that its truth passes down to substructures.
For a matrix with one more bounded $\forall$ in front, this step breaks.

The student needs the teacher's answers.
In the game above, a one-round strategy would be a polynomial-time $f_1$ with $\forall z \, B(a, f_1(a), z)$.
It would decide satisfiability and find assignments, so $\mathrm{P} = \mathrm{NP}$.

### What it gives you

When $B$ does not mention $z$, the disjunction has one useful disjunct, and part 1 with $k = 1$ is [[Buss's witnessing theorem|RH4R7GTTAX]] for $T^i_2$.
So KPT witnessing extends witnessing by one quantifier, at the price of a few rounds of interaction.

Part 2 ties the [[separation problem|PEJQDHHX8E]] for bounded arithmetic to complexity theory.
If the polynomial hierarchy is infinite, then $T^i_2 \ne S^{i+1}_2$ for every $i$.
So a collapse of the hierarchy of theories would be a collapse of the polynomial hierarchy, through the advice class of [[P/poly|P0A5DVRYDW]] and the [[Karp-Lipton theorem|HM7DNQ2H5D]].

The theorem is also a tool for unprovability.
To show that $T^i_2$ does not prove a $\forall \exists \forall$ sentence, it is enough to show that no $\square^p_{i+1}$ student wins in a constant number of rounds.

### The converse

The conclusion of part 1 implies its hypothesis, by pure logic.
Assume that $\exists y \, \forall z \, B(a, y, z)$ fails, so every $y$ has a $z$ with $\neg B(a, y, z)$.
Choose $b_1$ with $\neg B(a, f_1(a), b_1)$, then $b_2$ with $\neg B(a, f_2(a, b_1), b_2)$, and so on up to $b_k$.
Every disjunct is then false, which contradicts the disjunction.
For part 2 no converse is known: a collapse of the polynomial hierarchy is not known to collapse the hierarchy of theories.

### Generalizations

The proof of part 1 is an application of [[Herbrand's theorem|VZ21F10WRS]], and it works for every universal theory and every matrix $B$ whose negation is universal.
In this form it is a bounded version of Kreisel's [[no-counterexample interpretation|4BCD1EM542]] for one alternation of quantifiers.
Later work of Buss and of Zambella sharpened the collapse in part 2 and showed that bounded arithmetic proves the collapse itself.
One consequence is that $S_2$ is finitely axiomatizable if and only if $S_2$ proves that the polynomial hierarchy collapses.

### Watch out

A winning strategy is not an algorithm for $y$.
Students sometimes read part 1 as "$y$ is computable in $\square^p_{i+1}$", but the last guess $f_k$ uses $b_1, \dots, b_{k-1}$, and the game above shows how much those answers help.

The number $k$ comes from the proof and is the same for every input $a$.
For the sentence "there is a largest number up to $a$", a student who only climbs to the teacher's last answer may need $a$ rounds.
That climbing strategy is not what the theorem promises, and here the good strategy is $f_1(a) = a$, with $k = 1$.

### Try it

1. Let $B(a, y, z) := y \le a \land (z \le a \to z \le y)$. Give a one-round strategy.
   Answer: $f_1(a) = a$, since every $z \le a$ satisfies $z \le a$.
2. In the satisfiability game, what happens when $a$ codes an unsatisfiable formula?
   Answer: the teacher has no refutation of $y_1 = 0$, since $\neg R(a, z)$ holds for every $z$, so the student wins in round one.
3. Write the disjunction for $k = 1$ and say what it means.
   Answer: it is $B(a, f_1(a), b_1)$ with $b_1$ free, so $f_1(a)$ is a witness for $y$ with no help at all.

## History

Krajíček, Pudlák and Takeuti proved the witnessing theorem and the collapse in a paper of 1991, *Bounded arithmetic and the polynomial hierarchy*.
Their paper introduced the student-teacher reading of the Herbrand disjunction.
Buss, in a paper of 1995, and Zambella, in a paper of 1996, sharpened the collapse and related it to the finite axiomatizability of $S_2$.

## Explanations

### L1 human

Suppose a theory proves: "for every $x$ there is a $y$ that beats every $z$".
A fast program may not be able to find such a $y$ on its own.
The theorem says that a fast program can find it if it may make a few wrong guesses.
After each wrong guess, a teacher shows a $z$ that refutes it, and the program learns from that.
The number of guesses is a fixed number, such as $2$, for all inputs $x$.
For example, to name a solution of a puzzle, the program first says "there is none"; if the teacher shows one, the program repeats it.

### L2 human

We prove the two-round disjunction for the satisfiability game in $\mathsf{PV}_1$ and see why one round would not do.
The formula $R(a, w)$ is decided by a polynomial-time algorithm, so it is an open formula of $\mathsf{PV}_1$, and so is $B$.
The theory proves $\forall a \, \exists y \, \forall z \, B(a, y, z)$ by cases: if some $w \le a$ has $R(a, w)$, take $y = w + 1$, and otherwise take $y = 0$.

The student functions are $f_1(a) = 0$ and $f_2(a, b_1) = b_1 + 1$.
Substitute them into the disjunction of part 1 with $k = 2$:

$$B(a, 0, b_1) \lor B(a, b_1 + 1, b_2).$$

The first disjunct is $\neg R(a, b_1)$, and the second is $R(a, b_1)$, since $b_1 + 1 \ge 1$.
So the disjunction is an instance of $\neg q \lor q$, and $\mathsf{PV}_1$ proves it.

A strategy with one round would need $\forall z \, B(a, f_1(a), z)$ for a polynomial-time $f_1$.
Then $f_1(a) = 0$ exactly when $a$ is unsatisfiable, and otherwise $f_1(a) - 1$ is an assignment.
That decides satisfiability in polynomial time, which would give $\mathrm{P} = \mathrm{NP}$.
The problem shows the typical use: count how many rounds a student needs, and read off what a proof would imply.

### L3 human

The theorem is a bounded form of Herbrand's theorem, read through the no-counterexample interpretation, for one alternation and a universal theory.
It is a standard tool for unprovability results in $\mathsf{PV}_1$ and $T^i_2$, often under a complexity assumption.

Part 2 shows that the question of [[separating the theories|PEJQDHHX8E]] is not independent of complexity theory.
A collapse $T^i_2 = S^{i+1}_2$ would put $\Sigma^p_{i+1}$ into $\Pi^p_{i+1}$ with polynomial-size advice, which most researchers consider unlikely.
So the hierarchy of theories is expected to be strict, but no separation is known.
