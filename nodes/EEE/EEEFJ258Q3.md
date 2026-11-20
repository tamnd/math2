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

This proof takes the theorem, that $\mathrm{Taut}$ is $\Pi^0_2$-complete, from the literature cited in the statement.
It proves the corollary in full.
Identify each pair $(e, x) \in \mathbb{N}^2$ with one natural number by a computable bijection $\mathbb{N}^2 \to \mathbb{N}$.

**Part 1: a $\Pi^0_2$-complete set is not computably enumerable.**
Let $A \subseteq \mathbb{N}$ be $\Pi^0_2$-complete.
Let $H$ be the halting set of the [[undecidability of the halting problem|Z7TN2B35B0]], and let $\overline{H} = \mathbb{N}^2 \setminus H$.

1. For $(e, x) \in \mathbb{N}^2$ and $c \in \mathbb{N}$, let $R(e, x, c)$ say that the [[Turing machine|758EYCN27B]] $M_e$ halts on input $x$ within $c$ steps.
2. $R$ is a [[computable set|PPGD5KW8JC]]: simulate $M_e$ on $x$ for $c$ steps, and check whether it has halted.
3. $(e, x) \in \overline{H}$ iff $\forall c \, \neg R(e, x, c)$, by the definition of $H$. So $\overline{H}$ is in $\Pi^0_1$.
4. Add a quantifier $\exists d$ on a variable $d$ that does not occur: $(e, x) \in \overline{H}$ iff $\forall c \, \exists d \, \neg R(e, x, c)$. So $\overline{H}$ is in $\Pi^0_2$.
5. $A$ is $\Pi^0_2$-complete, so there is a total computable $f$ with $z \in \overline{H} \iff f(z) \in A$. This is the definition of [[many-one reducibility|H5CW67CCST]].
6. Assume, for contradiction, that $A$ is [[computably enumerable|TN9G24VABN]]. Then some algorithm $\mathcal{A}$ halts exactly on the elements of $A$.
7. Let $\mathcal{B}$ be the algorithm that, on input $z$, computes $f(z)$ and then runs $\mathcal{A}$ on $f(z)$.
8. $\mathcal{B}$ halts on $z$ iff $f(z) \in A$, by step 6. By step 5, this holds iff $z \in \overline{H}$.
9. So $\overline{H}$ is computably enumerable.
10. $H$ is computably enumerable too: the algorithm that runs $M_e$ on $x$ halts exactly on the pairs $(e, x) \in H$.
11. Let $\mathcal{D}$ run the algorithms of steps 10 and 7 in turn, one step of each at a time, on the same input $z$.
12. Each $z$ is in exactly one of $H$ and $\overline{H}$. So exactly one of the two algorithms halts, after finitely many steps.
13. Let $\mathcal{D}$ output $1$ if the algorithm of step 10 halts, and $0$ if $\mathcal{B}$ halts.
14. Then $\mathcal{D}$ halts on every input and outputs $1$ exactly on $H$, so $H$ is computable.
15. This contradicts the undecidability of the halting problem. So $A$ is not computably enumerable.

**Part 2: no complete computably enumerable axiomatization.**
Let $S$ be a proof system with a computably enumerable set of axioms and finitely many rules.
Each rule is a decidable relation between finitely many premises and one conclusion, as modus ponens and generalization are.
A proof in $S$ is a finite sequence of formulas, each an axiom or the conclusion of a rule from earlier members.

16. Fix an algorithm that lists the axioms of $S$ one by one.
17. For each $t \in \mathbb{N}$, take the finitely many sequences of formulas whose Gödel numbers are at most $t$.
18. For each such sequence, test each member: is it among the first $t$ listed axioms, or the conclusion of a rule from earlier members?
19. Each test is a finite computation, because the rules are decidable and only $t$ axioms are listed.
20. If all members pass the test, output the last formula of the sequence. Then go to $t + 1$.
21. Every output is a theorem of $S$, because the tested sequence is a proof.
22. Every theorem is output: its proof is finite and uses finitely many axioms, so the test succeeds for all large $t$.
23. So the set of theorems of $S$ is computably enumerable.
24. Assume that the theorems of $S$ are exactly the standard tautologies. Then $\mathrm{Taut}$ is computably enumerable, by step 23.
25. $\mathrm{Taut}$ is $\Pi^0_2$-complete by the theorem, so Part 1 gives a contradiction.
26. Hence no such $S$ exists, and $\mathrm{Taut}$ is not computably enumerable. $\blacksquare$

## Idea

The complement of the halting set is in $\Pi^0_2$, so it reduces to every $\Pi^0_2$-complete set.
If such a set were computably enumerable, the complement of the halting set would be computably enumerable too.
Then the halting set would be computable, which is false.
A computably enumerable axiomatization would make the tautologies computably enumerable, so no such axiomatization is complete.

## Variants

1. The current SEP entry calls the set $\Sigma_2$-complete. Part 1 also works for a $\Sigma^0_2$-complete set, because step 3 puts $\overline{H}$ in $\Pi^0_1$, which is inside $\Sigma^0_2$.
2. Wikipedia states that the complement of the Turing jump $\emptyset'$ is many-one complete for $\Pi^0_1$. Part 1 can start from that set in place of $\overline{H}$.
