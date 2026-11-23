---
tag: NJ18EZ5JBC
kind: problem
name: Pigeonhole principles in bounded arithmetic
aliases: [delta0-php-problem, weak-pigeonhole-principle-problem]
msc: ["03F30", "03F20", "68Q15"]
topics: [RA380RWEC0]
audience: research
uses: [FYGWNXETVJ, GE43CSZTS9, 0HGVCWQGY3, A2CFPP8JMN, ZVD982MVST, 1Q046J0AW2]
about: [FYGWNXETVJ, 0HGVCWQGY3]
sources:
  - url: https://en.wikipedia.org/wiki/Pigeonhole_principle
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Bounded_arithmetic
    locator: Correspondence to propositional proof systems
history:
  posed_by: "J. B. Paris, A. J. Wilkie and A. R. Woods"
  notes: "J. B. Paris, A. J. Wilkie and A. R. Woods, Provability of the pigeonhole principle and the existence of infinitely many primes, Journal of Symbolic Logic 53 (1988), 1235-1244."
---

## Problem

Three pigeons cannot sit in two holes with one pigeon in each hole.
Let $\varphi(u, v)$ be a formula that says "pigeon $u$ sits in hole $v$".
The [[pigeonhole principle|0HGVCWQGY3]] for three pigeons and two holes says that the following two conditions cannot both hold:

$$\forall u < 3 \; \exists v < 2 \; \varphi(u, v) \qquad \text{and} \qquad \forall u < 3 \; \forall u' < 3 \; \forall v < 2 \; \big(u \ne u' \land \varphi(u, v) \to \neg \varphi(u', v)\big).$$

Every quantifier is bounded, so when $\varphi$ is a [[$\Delta_0$ formula|GE43CSZTS9]], the whole statement is $\Delta_0$ too.
Replace $3$ by $z + 1$ and $2$ by $z$, and you get one bounded statement for each $z$.

We write $\varphi : a \hookrightarrow b$ when the two conditions hold with $a$ pigeons and $b$ holes.
The $\Delta_0$ pigeonhole principle $\Delta_0\text{-}\mathrm{PHP}$ is the schema: for every $\Delta_0$ formula $\varphi$, possibly with parameters, and every $z$, not $\varphi : z + 1 \hookrightarrow z$.

**Problem 1 (open).** Does [[$\mathsf{I}\Delta_0$|FYGWNXETVJ]] prove $\Delta_0\text{-}\mathrm{PHP}$?

**Problem 2 (open).** Does $\mathsf{I}\Delta_0$ prove the weak pigeonhole principle for $\Delta_0$ formulas, that is, not $\varphi : z^2 \hookrightarrow z$ for every $z > 1$?

**Problem 3 (open).** Let $R$ be a new binary relation symbol.
Does $\mathsf{I}\Delta_0(R)$ prove the weak pigeonhole principle for $R$, with $2z$ or with $z^2$ pigeons and $z$ holes?

Problem 3 is a question of [[proof complexity|1Q046J0AW2]] in disguise, through the [[Paris-Wilkie translation|ZVD982MVST]].
A positive answer would give [[bounded-depth Frege|41QJ1WEMJ3]] proofs of polynomial size for the propositional weak pigeonhole formulas.

## Remarks

### Why the usual proof does not fit

For each fixed $z$, such as $z = 2$ above, $\mathsf{I}\Delta_0$ proves the statement by checking the finitely many cases.
The difficulty is the single schema for all $z$ at once.
The textbook proof inducts on $z$ with the statement "no injective map from $z + 1$ pigeons into $z$ holes exists".
That statement quantifies over all maps, and a map is a list of $z + 1$ holes.

So a map needs a code of about $z^{z + 1}$, which has about $(z + 1)\lvert z \rvert$ binary digits.
That is exponential in the length $\lvert z \rvert$ of the input.
By [[Parikh's theorem|YPQPC1WJMV]], $\mathsf{I}\Delta_0$ cannot prove that numbers of this size exist.
So the induction statement is not $\Delta_0$, and $\mathsf{I}\Delta_0$ has no induction for it.
A proof in $\mathsf{I}\Delta_0$ would need a different idea, and nobody has found one.

### What is known with a new symbol

For a new relation symbol $R$ and $z + 1$ pigeons, the answer is negative.
[[Ajtai's theorem|Q0ERK64J78]] shows that the [[pigeonhole formulas|RJ571F7FF0]] $\mathrm{PHP}^{n+1}_n$ have no bounded-depth Frege proofs of polynomial size.
By the Paris-Wilkie translation, $\mathsf{I}\Delta_0(R)$ does not prove the pigeonhole principle for $R$.
Later work made the lower bound exponential, and this extends the unprovability to the stronger theory $\mathsf{I}\Delta_0(R) + \Omega_1$.

The restriction to bounded depth matters.
[[Buss's theorem|VRX23FZV21]] gives Frege proofs of polynomial size of $\mathrm{PHP}^{n+1}_n$ when the depth may grow.
The weak pigeonhole formulas with $2n$ pigeons have bounded-depth Frege proofs of quasipolynomial size, by Paris, Wilkie and Woods.
Whether polynomial size suffices is open, and this is the propositional counterpart of Problem 3.

### What is known without a new symbol

Paris, Wilkie and Woods proved that $\mathsf{I}\Delta_0 + \Omega_1$ proves the weak pigeonhole principle for $\Delta_0$ formulas with $2z$ pigeons and $z$ holes.
A map of $z^2$ pigeons into $z$ holes restricts to a map of $2z$ pigeons into $z$ holes when $z \ge 2$, so the version with $z^2$ pigeons follows.
The axiom $\Omega_1$ (see [[the theory IΔ0 + Ω1|V8WD1F0NS2]]) is what their proof uses, so Problem 2 asks whether it can be removed.

Ajtai's theorem does not answer Problem 1.
A $\Delta_0$ formula of arithmetic is not a new symbol, and its Paris-Wilkie translation has no propositional variables, only the constants for true and false.
So the lower bounds of proof complexity give no information about it.

### Why the problems matter

Paris, Wilkie and Woods showed that $\mathsf{I}\Delta_0$ plus the weak pigeonhole principle for $\Delta_0$ formulas proves that there are infinitely many primes.
Whether $\mathsf{I}\Delta_0$ alone proves this is a question of Wilkie, and it is open as well.
So a positive answer to Problem 2 would bring much elementary number theory into $\mathsf{I}\Delta_0$.
The dual form of the weak principle, for polynomial-time functions, is the axiom of [[approximate counting|65K2S22DGZ]].

### Watch out

Do not read Ajtai's theorem as a solution of Problem 1.
It concerns a new symbol $R$, which a model can interpret as any relation at all.
Problem 1 concerns formulas of the language of arithmetic only, and these cannot be chosen freely in a model.

Do not try to fix the map $\varphi$ and induct on $z$ alone.
Each step of the textbook proof changes the map: it removes one pigeon and one hole and moves one pigeon.
After $k$ steps the map depends on the first $k$ choices, and one $\Delta_0$ formula with fixed parameters cannot describe all these maps.

### Try it

1. Write the pigeonhole principle for two pigeons and one hole, and say why logic alone proves it.
   Answer: the first condition says $\varphi(0, 0)$ and $\varphi(1, 0)$.
   The second condition with $u = 0$, $u' = 1$ and $v = 0$ says $\varphi(0, 0) \to \neg \varphi(1, 0)$, so the two conditions contradict each other.
2. How many binary digits does a list of the holes of $9$ pigeons need when there are $8$ holes?
   Answer: each hole is below $8$ and needs $3$ digits, so the list needs $9 \cdot 3 = 27$ digits.
3. Does $\mathsf{I}\Delta_0 + \Omega_1$ prove the weak principle for $\Delta_0$ formulas with $z^2$ pigeons?
   Answer: yes, because it proves the version with $2z$ pigeons, and $z^2 \ge 2z$ for $z \ge 2$.

## History

Paris, Wilkie and Woods posed the $\Delta_0$ pigeonhole problems in their 1988 paper, together with their results on the weak principle and the primes.
Ajtai proved the superpolynomial lower bound for $\mathrm{PHP}^{n+1}_n$ in bounded-depth Frege systems in 1988, and with it the unprovability for a new relation symbol.
Exponential lower bounds were proved by Krajíček, Pudlák and Woods, and independently by Pitassi, Beame and Impagliazzo.

## Explanations

### L1 human

If $4$ pigeons sit in $3$ holes, some hole has two pigeons.
The question is whether a very weak system of axioms for numbers can prove this fact for every number of pigeons.
In the weak system every "for all" and every "there is" must stop at a given bound.
The usual proof looks at all possible seatings at once, and there are far too many seatings for the weak system.
Nobody knows whether a cleverer proof exists.

### L2 human

We count the size of a seating for $z = 1000$ holes and $1001$ pigeons.
A hole number below $1000$ has at most $10$ binary digits, since $1000 < 2^{10} = 1024$.
A seating lists $1001$ hole numbers, so its code has about this many digits:

$$1001 \cdot 10 = 10010.$$

The input $z$ itself has only $10$ digits.
In general a seating has about $z \lvert z \rvert$ digits, which is exponential in $\lvert z \rvert$, and Parikh's theorem forbids such numbers in $\mathsf{I}\Delta_0$.

The typical use of the weak principle is as an extra axiom, for example to prove the infinitude of primes over $\mathsf{I}\Delta_0$.
Watch out: the principle for one fixed $z$ is easy, and only the uniform schema is hard.

### L3 human

The problems sit where weak arithmetic, counting and proof complexity meet.
For theories with a new symbol they become lower bound questions for bounded-depth Frege systems, and the switching lemma of circuit complexity gives the known answers.
For the language of arithmetic alone no such translation is available, and the problems are as hard as other basic questions about $\mathsf{I}\Delta_0$.

The weak pigeonhole principles also measure how much counting a theory can do.
Added as axioms to $\mathsf{PV}_1$ or $T^1_2$, they give Jeřábek's theories of [[approximate counting|65K2S22DGZ]], in which much probabilistic reasoning can be carried out.
Combinatorial principles of this kind also give the known relativized cases of the [[separation problem|PEJQDHHX8E]].
