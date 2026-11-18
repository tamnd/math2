---
tag: XFFNHDJR1M
kind: proof
name: Proof of the complexity of CTL* satisfiability and model checking
msc: ["03B44", "68Q17", "68Q60"]
topics: [CQM9SRN8PM]
audience: research
proves: XJ36V8QA0F
uses: [5MH8WSAWXT, RD9B213GJ5, TQWGW9X8VF, PXKKP038RG, JWC9CE07Q2]
methods: [12MQ2NJ29A, 0NTF6DMVAP]
sources:
  - book: isbn:9780262026499
    locator: Baier and Katoen, Principles of Model Checking, chapter 6
  - url: https://en.wikipedia.org/wiki/CTL*
    locator: section Decision problems
---

## Proof

We prove part 1 of [[the theorem|XJ36V8QA0F]] from [[the LTL complexity theorem|RD9B213GJ5]].
For part 2 we give the structure of the proofs of Emerson and Jutla and of Vardi and Stockmeyer, and we name the results cited without proof.

1. Model checking, the reduction. Let $\Phi$ be a [[CTL*|5MH8WSAWXT]] state formula. Call $E\varphi$ basic if $\varphi$ contains no path quantifier.
2. If $\Phi$ has a path quantifier, then it has a basic subformula $E\varphi$: take an occurrence of $E$ with no $E$ below it.
3. In a basic $E\varphi$, the path formula $\varphi$ is an LTL formula. So $s \models E\varphi$ if and only if $s$ fails the LTL formula $\neg\varphi$ on all paths.
4. Compute the set $Z$ of states that satisfy $E\varphi$. These are the states $s$ from which the product of $M$ with the Büchi automaton of $\varphi$ has an accepting run, and one search finds them all. Add a fresh atom $r$ with $L'(s) = L(s) \cup \set{r}$ for $s \in Z$.
5. Replace $E\varphi$ by $r$ in $\Phi$. By induction on formulas, the new formula has the same truth value at each state of the relabelled structure.
6. Repeat steps 2 to 5. Each round removes one quantifier, so there are at most $\lvert\Phi\rvert$ rounds.
7. Time. Round $k$ handles a formula $\varphi_k$, in time $\lvert M \rvert \cdot 2^{O(\lvert\varphi_k\rvert)}$, as in the LTL theorem. The sizes satisfy $\sum_k \lvert\varphi_k\rvert \le \lvert\Phi\rvert$, so the total is $\lvert M \rvert \cdot 2^{O(\lvert\Phi\rvert)}$.
8. Space. Each LTL step runs in polynomial space, and the labels of the fresh atoms take $O(\lvert M \rvert \cdot \lvert\Phi\rvert)$ bits. So CTL* model checking is in PSPACE.
9. Hardness. For an LTL formula $\varphi$, $M, s \models A\varphi$ in CTL* exactly when $s$ satisfies $\varphi$ in LTL. LTL model checking is PSPACE-hard, so CTL* model checking is PSPACE-hard. This proves part 1.
10. Satisfiability, tree models, cited. If $\Phi$ is satisfiable, it is satisfied at the root of a tree whose nodes have at most $\lvert\Phi\rvert$ children. This follows from unravelling, since CTL* is invariant under bisimulation, and from pruning to the witnessed successors.
11. Satisfiability, automaton, cited. For each $\Phi$ there is a Rabin [[tree automaton|TQWGW9X8VF]] that accepts exactly the tree models of step 10. It has $2^{2^{O(n)}}$ states and $2^{O(n)}$ pairs, where $n = \lvert\Phi\rvert$. Its construction goes through a deterministic Rabin word automaton for the path formulas.
12. Satisfiability, emptiness, cited. Emerson and Jutla show that emptiness of a Rabin tree automaton with $m$ states and $k$ pairs can be decided in time $(mk)^{O(k)}$.
13. Putting $m = 2^{2^{O(n)}}$ and $k = 2^{O(n)}$ into step 12 gives time $2^{2^{O(n)}}$. So satisfiability is in 2EXPTIME.
14. Lower bound, cited. Alternating Turing machines with space $2^{p(n)}$, for polynomials $p$, decide exactly the problems in 2EXPTIME. This is the Chandra, Kozen and Stockmeyer theorem.
15. Vardi and Stockmeyer build, from such a machine $T$ and an input $x$, a CTL* formula $\Phi_{T,x}$ of polynomial size. Its tree models encode accepting computation trees of $T$ on $x$.
16. The encoding uses $A$ for the universal choices of $T$ and $E$ for the existential ones. Path formulas with a binary counter compare corresponding tape cells of consecutive configurations.
17. So $\Phi_{T,x}$ is satisfiable if and only if $T$ accepts $x$, and satisfiability is 2EXPTIME-hard. This proves part 2.

## Idea

Model checking peels off one path quantifier at a time, and each layer is an LTL problem.
Satisfiability must also build the structure, which forces tree automata with an acceptance condition of exponential size, and one more exponential.

## Variants

1. For CTL, the same method of steps 10 to 13 gives Büchi tree automata of exponential size, and EXPTIME.
