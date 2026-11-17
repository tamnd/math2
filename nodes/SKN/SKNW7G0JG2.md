---
tag: SKNW7G0JG2
kind: example
name: Turing's completeness construction for a Π1 sentence
msc: ["03F40", "03F15"]
topics: [HXHHWY3328]
audience: research
instance_of: [F7Z4BV2KHD]
uses: [F7Z4BV2KHD, WHAP0K600D, F3Z30M606H, 4PZM5GJTR5, 4NBAX3VRQ7, 7SRG8BJRJV, 7CVJCQKY41]
sources:
  - url: https://en.wikipedia.org/wiki/Systems_of_Logic_Based_on_Ordinals
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Ordinal_logic
    locator: lead section
---

## Example

We use Turing's consistency progression over $\mathsf{PA}$, one of the [[Turing and Feferman progressions|F7Z4BV2KHD]].
By effective recursion there is a computable map that assigns to every number $a$ a $\Sigma_1$ formula $\mathrm{Ax}_a(x)$, the axiom formula of a theory $T_a$, with these clauses.

- $T_1 = \mathsf{PA}$.
- $T_{2^c} = T_c + \mathrm{Con}(T_c)$, where $\mathrm{Con}(T_c)$ is the [[consistency statement|4NBAX3VRQ7]] built from $\mathrm{Ax}_c$.
- $T_{3 \cdot 5^e} = \bigcup_n T_{\varphi_e(n)}$, where $\varphi_e$ is the partial computable function with index $e$.
- $T_a = \mathsf{PA}$ for every other number $a$.

The clauses apply to every number $a$, not only to notations in [[Kleene's O|WHAP0K600D]], and $\mathsf{PA}$ proves them for the formulas $\mathrm{Ax}_a$.
Let $\pi = \forall x \, R(x)$ be a $\Pi_1$ sentence with $R$ decidable, and let $o_n$ be the notation of the finite ordinal $n$ ($o_0 = 1$ and $o_{n+1} = 2^{o_n}$).
We build a notation $a$ such that $T_a \vdash \pi$, and such that $a \in \mathcal{O}$ with $\abs{a} = \omega + 1$ whenever $\pi$ is true.

1. By [[Kleene's recursion theorem|F3Z30M606H]] there is an index $e$ of a total computable function with $\varphi_e(n) = o_n$ if $R(0), \ldots, R(n)$ all hold, and $\varphi_e(n) = 2^{3 \cdot 5^e}$ otherwise. The recursion theorem is needed because the definition of $\varphi_e$ mentions its own index $e$.
2. Put $b = 3 \cdot 5^e$ and $a = 2^b$. By the clauses, $T_a = T_b + \mathrm{Con}(T_b)$.
3. Suppose $\pi$ is true. Then $\varphi_e(n) = o_n$ for all $n$, and $o_0 <_{\mathcal{O}} o_1 <_{\mathcal{O}} \cdots$. So $b \in \mathcal{O}$ with $\abs{b} = \omega$, and $a \in \mathcal{O}$ with $\abs{a} = \omega + 1$.
4. We now show $T_a \vdash \pi$, by an argument inside $T_a$. Assume $\neg \pi$. Then there is an $m$ with $\neg R(m)$.
5. For every $n \ge m$ we have $\varphi_e(n) = 2^b = a$, by the definition of step 1. $\mathsf{PA}$ verifies this from the explicit program with index $e$, so it holds inside $T_a$.
6. So the axioms of $T_a$ are among the axioms of $T_b$, by the clause for $b = 3 \cdot 5^e$. In particular $\mathrm{Con}(T_b)$ is an axiom of $T_b$, and so $\mathrm{Prov}_{T_b}(\ulcorner \mathrm{Con}(T_b) \urcorner)$.
7. The theory $T_b$ contains $\mathsf{PA}$, since $\varphi_e(0)$ is $1$ or $a$ and both stages contain $\mathsf{PA}$. The formalized [[second incompleteness theorem|4PZM5GJTR5]] for $T_b$, which $\mathsf{PA}$ proves, gives $\mathrm{Prov}_{T_b}(\ulcorner \mathrm{Con}(T_b) \urcorner) \to \neg \mathrm{Con}(T_b)$.
8. Steps 6 and 7 give $\neg \mathrm{Con}(T_b)$. But $\mathrm{Con}(T_b)$ is an axiom of $T_a$ (step 2), a contradiction.
9. So $T_a$ proves $\neg \pi \to (\mathrm{Con}(T_b) \wedge \neg \mathrm{Con}(T_b))$, and hence $T_a \vdash \pi$.
10. With step 3: if $\pi$ is true, then $a$ is a notation in $\mathcal{O}$ for $\omega + 1$, and the stage $T_a$ of the consistency progression proves $\pi$. This is Turing's completeness theorem for $\Pi_1$ sentences.

## Remarks

The proof in steps 4 to 9 does not use the truth of $\pi$, so $T_a \vdash \pi$ holds also when $\pi$ is false.
In that case the sequence $\varphi_e$ is not increasing, so $b \notin \mathcal{O}$, and $T_b$ contains its own consistency statement as an axiom, so $T_b$ and $T_a$ are inconsistent, by the second incompleteness theorem.
So the information "$\pi$ is true" is moved into the information "$b \in \mathcal{O}$", and the construction gives no new way to recognize true $\Pi_1$ sentences.
The example also shows the failure of invariance.
For each true $\Pi_1$ sentence there is a notation for $\omega + 1$ whose stage proves it, but a single stage $T_a$ has c.e. theorems and cannot prove all true $\Pi_1$ sentences, because the set of true $\Pi_1$ sentences is not c.e.
So different notations for $\omega + 1$ give stages with different theorems.
For $\Pi_2$ sentences no such construction exists: Feferman showed in 1962 that the consistency progression is not complete for true $\Pi_2$ sentences.

## Explanations

### L1 human

Take a statement that says "every number has a checkable property", for example "no even number above 2 fails to be a sum of two primes".
Turing wrote a clever label for an infinite ordinal, built from the statement itself.
If the statement is true, the label is a correct name for the ordinal "infinity plus one".
If the statement is false, the label is broken, and the theory at that label contradicts itself.
The theory at the label can prove the statement, by arguing "if the statement were false, my label would be broken, and I would be inconsistent, but I assume that I am consistent".
So the work of proving the statement is hidden in checking that the label is correct.

### L2 human

We follow the construction for the true sentence $\pi = \forall x \, (x + 0 = x)$.

1. Here $R(n)$ holds for all $n$, so $\varphi_e(n) = o_n$: the values are $1, 2, 4, 16, 65536, \ldots$.
2. So $b = 3 \cdot 5^e$ is a notation for $\omega$, and $T_b$ is the union of the finite stages of [[the consistency progression|7SRG8BJRJV]].
3. The stage $a = 2^b$ is $T_b + \mathrm{Con}(T_b)$, written with the axiom formula of $b$.
4. Inside $T_a$: if some $m$ had $m + 0 \ne m$, then $\varphi_e(n)$ would be $a$ for $n \ge m$, so $T_b$ would contain $\mathrm{Con}(T_b)$ and be inconsistent, against the axiom $\mathrm{Con}(T_b)$.

The typical use of the construction is to show that completeness results for progressions say little unless the notations are controlled.
A trap: the theory $T_b$ in step 2 has the same axioms as the union of the finite stages with the standard notation for $\omega$, but its axiom formula mentions $\pi$, and $\mathrm{Con}(T_b)$ in step 3 depends on that formula.
