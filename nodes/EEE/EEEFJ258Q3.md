---
tag: EEEFJ258Q3
kind: proof
name: Proof that first-order Łukasiewicz logic has no complete computably enumerable axiomatization
msc: ["03B52", "03D55"]
topics: [WZP584JQ06]
audience: research
proves: VAHH1505Z0
uses: [7CVJCQKY41, H5CW67CCST, TN9G24VABN, PPGD5KW8JC, Z7TN2B35B0, 758EYCN27B]
methods: [0J0XBKG64S]
sources:
  - url: https://plato.stanford.edu/archives/fall2016/entries/logic-fuzzy/
    locator: 4. Łukasiewicz, Gödel and product logic; 8. Complexity
  - url: https://en.wikipedia.org/wiki/Computably_enumerable_set
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Arithmetical_hierarchy
    locator: Properties; Relation to Turing machines
---

## Proof

We reduce the complement of the halting set to $\mathrm{Taut}$, so that a listing of $\mathrm{Taut}$ would decide the halting problem, and then we show that a proof system would give such a listing.
The theorem, that $\mathrm{Taut}$ is $\Pi^0_2$-complete, is due to Ragaz and is cited; the corollary is proved in full.
We identify each pair $(e, x) \in \mathbb{N}^2$ with one natural number by a computable bijection $\mathbb{N}^2 \to \mathbb{N}$.

### Part 1: a $\Pi^0_2$-complete set is not computably enumerable

Let $A \subseteq \mathbb{N}$ be $\Pi^0_2$-complete.
Let $H$ be the halting set from the [[undecidability of the halting problem|Z7TN2B35B0]], and let $\overline{H} = \mathbb{N}^2 \setminus H$.

1. For $(e, x) \in \mathbb{N}^2$ and $c \in \mathbb{N}$, let $R(e, x, c)$ say that the [[Turing machine|758EYCN27B]] $M_e$ halts on input $x$ within $c$ steps.
2. $R$ is a [[computable set|PPGD5KW8JC]]: simulate $M_e$ on $x$ for $c$ steps, and check whether it has halted.
3. By the definition of $H$, $(e, x) \in \overline{H}$ if and only if $\forall c \, \neg R(e, x, c)$, so $\overline{H}$ is in $\Pi^0_1$, and hence in $\Pi^0_2$.
4. $A$ is $\Pi^0_2$-complete, so there is a total computable $f$ with $z \in \overline{H} \iff f(z) \in A$, by the definition of [[many-one reducibility|H5CW67CCST]].
5. Assume, for contradiction, that $A$ is [[computably enumerable|TN9G24VABN]], so that some algorithm $\mathcal{A}$ halts exactly on the elements of $A$.
6. Let $\mathcal{B}$ be the algorithm that, on input $z$, computes $f(z)$ and then runs $\mathcal{A}$ on $f(z)$.
7. Then $\mathcal{B}$ halts on $z$ if and only if $f(z) \in A$, that is, by step 4, if and only if $z \in \overline{H}$.
8. The algorithm that runs $M_e$ on $x$ halts exactly on the pairs $(e, x) \in H$.
9. Let $\mathcal{D}$ run the algorithms of steps 8 and 6 on the same input $z$, one step of each in turn.
10. Each $z$ is in exactly one of $H$ and $\overline{H}$, so exactly one of the two algorithms halts, after finitely many steps.
11. Let $\mathcal{D}$ output $1$ if the algorithm of step 8 halts first, and $0$ if $\mathcal{B}$ does.
12. Then $\mathcal{D}$ halts on every input and outputs $1$ exactly on $H$, so $H$ is computable.
13. This contradicts the undecidability of the halting problem, so $A$ is not computably enumerable.

### Part 2: no complete computably enumerable axiomatization

Let $S$ be a proof system with a computably enumerable set of axioms and finitely many rules.
Each rule is a decidable relation between finitely many premises and one conclusion, as modus ponens and generalization are.
A proof in $S$ is a finite sequence of formulas, each an axiom or the conclusion of a rule from earlier members.

14. Fix an algorithm that lists the axioms of $S$ one by one.
15. For each $t \in \mathbb{N}$, take the finitely many sequences of formulas whose Gödel numbers are at most $t$.
16. Test each member of each sequence: is it among the first $t$ listed axioms, or the conclusion of a rule from earlier members?
17. Each test is a finite computation, because the rules are decidable and only $t$ axioms are listed.
18. If all members pass, output the last formula of the sequence, and then go on to $t + 1$.
19. Every output is a theorem of $S$, because the tested sequence is a proof.
20. Every theorem is output, because its proof is finite and uses finitely many axioms, so the test succeeds for all large $t$.
21. So the set of theorems of $S$ is computably enumerable.
22. If the theorems of $S$ were exactly the standard tautologies, then $\mathrm{Taut}$ would be computably enumerable, by step 21.
23. $\mathrm{Taut}$ is $\Pi^0_2$-complete by the theorem, so Part 1 gives a contradiction.
24. Hence no such $S$ exists, and $\mathrm{Taut}$ is not computably enumerable. $\blacksquare$

## Idea

The complement of the halting set is in $\Pi^0_2$, so it reduces to every $\Pi^0_2$-complete set.
If such a set were computably enumerable, the complement of the halting set would be computably enumerable too.
Then the halting set would be computable, which is false.
A computably enumerable axiomatization would make the tautologies computably enumerable, so no such axiomatization is complete.

## Variants

Part 1 uses only a reduction of $\overline{H}$, a $\Pi^0_1$ set, to $A$.
So the corollary needs only that $\mathrm{Taut}$ is $\Pi^0_1$-hard, which is weaker than the full theorem; Scarpellini's 1962 result came before the exact classification.
Part 1 can also start from the complement of the Turing jump $\emptyset'$, which is many-one complete for $\Pi^0_1$, in place of $\overline{H}$.
