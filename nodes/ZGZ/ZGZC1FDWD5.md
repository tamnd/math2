---
tag: ZGZC1FDWD5
kind: proof
name: Proof of normalization for implicational natural deduction
msc: ["03F05"]
topics: [R10RMQCJQX]
audience: grad
proves: W33WAE1XTC
uses: [PAQ4ZX2TX1, V2Z855MFPC, A77FER1Q5H]
methods: [AABX4YPKRR, 12MQ2NJ29A, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_deduction
    locator: Proofs and type theory
---

## Proof

We prove parts 1 and 2 in full, and part 3 is cited.
We assume that discharge labels are distinct from the labels of open assumptions, renaming discharged labels when needed.
Renaming keeps a derivation a derivation.

**One reduction step.**
Let $R$ be a detour on $A \to B$, with $D_1$ the derivation of $B$ above it and $D_2$ the derivation of the minor premise $A$.
Let $D'$ be the result of the reduction step at $R$.

1. $D'$ is a derivation: each copy of $D_2$ ends with $A$, so it fits where the assumption $A$ labelled $u$ stood.
2. $D'$ has the same conclusion as the original derivation $D$, since the part ending with $B$ is replaced by a derivation of $B$.
3. The open assumptions of $D'$ are open assumptions of $D$. Copies of $D_2$ bring only open assumptions of $D_2$, and by the label convention no rule of $D_1$ discharges them.
4. The detours of $D'$ are of four kinds. The first kind are detours of $D$ outside $R$, $D_1$ and $D_2$, which stay as they are.
5. The second kind are detours of $D_1$, which stay as they are, and the third kind are copies of detours of $D_2$, one for each assumption labelled $u$.
6. The fourth kind are new detours. A copy of $D_2$ may end with ${\to}$I and stand where $A$ was the major premise of ${\to}$E. This new detour is on $A$.
7. Also $D_1$ may end with ${\to}$I and its conclusion $B$ may be the major premise of a ${\to}$E below $R$. This new detour is on $B$.
8. The degrees of $A$ and $B$ are less than the degree of $A \to B$, so every new detour has a smaller degree than $R$.

**Part 1, weak normalization.**
For a derivation $D$ with a detour, let $d$ be the largest degree of a detour of $D$, and $n$ the number of detours of degree $d$.
We prove part 1 by induction on the pair $(d, n)$ in the lexicographic order, which is a well-founded order on pairs of natural numbers.
A derivation without detours is normal, and there is nothing to prove.

9. Among the detours of degree $d$, choose one, $R$, whose minor premise derivation $D_2$ has the fewest formula occurrences.
10. Then $D_2$ contains no detour of degree $d$. Such a detour would have a minor premise derivation inside $D_2$, with fewer formula occurrences.
11. Reduce $D$ at $R$ and call the result $D'$. By steps 1 to 3, $D'$ is a derivation of the same conclusion from $\Gamma$.
12. By steps 4 and 5, the detours of $D'$ of degree $d$ are those of $D$ except $R$, together with copies of detours of $D_2$ of degree $d$.
13. By step 10, there are no such copies. By step 8, the new detours have degree less than $d$.
14. So $D'$ has exactly $n - 1$ detours of degree $d$, and none of larger degree.
15. If $n > 1$, the pair of $D'$ is $(d, n - 1)$. If $n = 1$, the largest degree of a detour of $D'$ is less than $d$, or $D'$ is normal.
16. In both cases the pair of $D'$ is smaller, or $D'$ is normal. The induction hypothesis turns $D'$ into a normal derivation by finitely many reduction steps.
17. Adding the step from $D$ to $D'$ proves part 1 for $D$.

**Part 2, the subformula property.**
We prove two claims at once, by induction on a normal derivation $D$ of $C$.
Claim (i): every formula of $D$ is a subformula of $C$ or of an open assumption of $D$.
Claim (ii): if the last rule of $D$ is not ${\to}$I, then $C$ is a subformula of an open assumption of $D$.

18. If $D$ is a single assumption $C$, then $C$ is open, and both claims hold.
19. Let $D$ end with ${\to}$I, from a derivation $D'$ of $B$ to $C = A \to B$, discharging assumptions $A$. Claim (ii) says nothing here.
20. $D'$ is normal, as a part of a normal derivation. By the induction hypothesis, each formula of $D'$ is a subformula of $B$ or of an open assumption of $D'$.
21. An open assumption of $D'$ is $A$ or an open assumption of $D$. Both $A$ and $B$ are subformulas of $C$, so claim (i) holds.
22. Let $D$ end with ${\to}$E, from a derivation $D'$ of $A \to C$ and a derivation $D''$ of $A$. Both are normal.
23. The last rule of $D'$ is not ${\to}$I, since otherwise $A \to C$ would be a detour of $D$.
24. By claim (ii) for $D'$, the formula $A \to C$ is a subformula of an open assumption of $D'$. Rule ${\to}$E discharges nothing, so this assumption is open in $D$.
25. So $C$ and $A$ are subformulas of an open assumption of $D$, and claim (ii) holds for $D$.
26. By claim (i) for $D'$, its formulas are subformulas of $A \to C$ or of open assumptions of $D$. By step 24, all are subformulas of open assumptions of $D$.
27. By claim (i) for $D''$, its formulas are subformulas of $A$ or of open assumptions of $D$. By step 25, the same holds.
28. The last formula $C$ is covered by step 25. So claim (i) holds for $D$.
29. Claim (i) for a normal derivation of $A$ from $\Gamma$ is part 2, since its open assumptions lie in $\Gamma$.

**Part 3, strong normalization.**
Part 3 is cited without proof.

30. Under the [[Curry-Howard correspondence|A77FER1Q5H]], a derivation is a simply typed lambda term, and a reduction step is a beta reduction step.
31. The [[strong normalization of the simply typed lambda calculus|V2Z855MFPC]] says that every beta reduction sequence of a typed term is finite. This gives part 3.

## Idea

Reducing a detour can create new detours, but only on the smaller formulas $A$ and $B$.
It can also copy old detours, and the choice in step 9 makes sure that no copied detour has the largest degree.
So the number of detours of the largest degree goes down by one at each step.
For part 2, a normal derivation is read from the bottom: below an elimination, everything comes from an assumption.

## Variants

Turing used the same strategy for the simply typed lambda calculus in an unpublished note.
The strategy bounds the number of steps by a tower of exponentials whose height grows with the largest degree $d$.
Strong normalization needs another method, such as Tait's computability predicates, because an arbitrary reduction order is allowed.
For the full intuitionistic system, the proof adds permutative reductions for $\vee$ and $\exists$, and the measure counts maximal segments instead of single formulas.
The [[cut-elimination theorem|AYRZ98Y0NW]] is the corresponding result for the sequent calculus, and its [[mix proof|8HV015W88G]] uses a similar double induction.
