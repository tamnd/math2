---
tag: 6AN62NQ8AN
kind: statement
role: theorem
name: Craig's theorem on axiomatizability
msc: ["03B25", "03D25", "03A10"]
topics: [FBWW4J1XWG]
audience: grad
about: [3ANXZC3BEG, 92SWXST1ZM]
uses: [3ANXZC3BEG, 92SWXST1ZM, DKFGQTRYZE, TN9G24VABN, PPGD5KW8JC, MFJXPAF0R0]
sources:
  - url: https://en.wikipedia.org/wiki/Craig%27s_theorem
    locator: Recursive axiomatization
  - url: https://en.wikipedia.org/wiki/Craig%27s_theorem
    locator: Philosophical implications
history:
  first_stated: "William Craig, 1953"
  notes: "William Craig, On axiomatizability within a system, Journal of Symbolic Logic 18 (1953)."
---

## Statement

Let $L$ be a countable signature whose symbols, logical symbols and variables are coded by natural numbers, so that each string of symbols has a [[Gödel number|MFJXPAF0R0]].
A set of strings is decidable when the set of their Gödel numbers is a [[computable set|PPGD5KW8JC]], and computably enumerable when that set is [[computably enumerable|TN9G24VABN]].
Let $T$ be a computably enumerable set of $L$-[[sentences|DKFGQTRYZE]].
Then there is a decidable set $A$ of $L$-sentences with the same theorems as $T$:
$$A \vdash \varphi \iff T \vdash \varphi \quad \text{for every } L\text{-formula } \varphi.$$
In addition, each sentence of $A$ is logically equivalent to a sentence of $T$, and each sentence of $T$ is logically equivalent to a sentence of $A$.

Equivalent form: a [[theory|92SWXST1ZM]] $T$ is a [[recursively axiomatizable theory|3ANXZC3BEG]] if and only if the set $\operatorname{Thm}(T)$ of its theorems is computably enumerable.

## Remarks

### Why each hypothesis is needed

The hypothesis that $T$ is computably enumerable cannot be dropped.
True arithmetic $\mathrm{TA} = \operatorname{Th}(\N, 0, S, +, \cdot)$ is a set of sentences with no decidable axiomatization, by the example [[true arithmetic is not recursively axiomatizable|YSC90EM2M7]].
So the conclusion fails for $T = \mathrm{TA}$, and $\mathrm{TA}$ is not computably enumerable.

The hypothesis on the coding of $L$ is needed to give a meaning to "decidable" and "computably enumerable".
For an uncountable signature there is no coding of the strings by natural numbers.

The proof uses one property of the logic: from a sentence $\sigma$ we can compute longer and longer sentences that are equivalent to $\sigma$.
In first-order logic the conjunctions $\sigma \land \sigma \land \cdots \land \sigma$ do this.

### Consequences

1. Equivalent form. If $\operatorname{Thm}(T)$ is computably enumerable, apply the theorem to the set $\operatorname{Thm}(T)$. It gives a decidable $A$ with $\operatorname{Thm}(A) = \operatorname{Thm}(\operatorname{Thm}(T)) = \operatorname{Thm}(T)$. The other direction is property 3 of [[recursively axiomatizable theory|3ANXZC3BEG]].
2. For a theory, these three conditions are equivalent: it has a decidable set of axioms, it has a computably enumerable set of axioms, and its theorems form a computably enumerable set. So the hypothesis "the axioms are computably enumerable" in [[Gödel's incompleteness theorems|X9WYNYE29C]] can be replaced by "the axioms form a decidable set", and conversely.
3. A theory whose theorems are not computably enumerable has no decidable axiomatization. This applies to $\mathrm{TA}$.

The philosophical use concerns scientific theories.
Split the vocabulary of a theory $T$ into an observational part $L_O$ and a theoretical part.
If $T$ is computably enumerable, then so is the set of theorems of $T$ that use only $L_O$: list the theorems of $T$ and keep those in $L_O$.
Craig's theorem gives a decidable set $A_O$ of $L_O$-sentences with exactly these theorems.
So, as far as its consequences in the observational vocabulary go, the theory can be stated without theoretical terms.
Carl Hempel discussed this argument for eliminating theoretical terms and raised objections to it.
One objection is that $A_O$ is an infinite list of axioms that is unmanageable in practice.
Another is that the removal of theoretical terms can change the inductive relations between observation sentences.
Hilary Putnam argued that the use rests on the view that prediction is the only aim of science, and that theoretical terms are needed to speak about entities such as viruses or elementary particles.

### Converse

The direct converse is false.
If $A$ is decidable and $\operatorname{Thm}(A) = \operatorname{Thm}(T)$, then $\operatorname{Thm}(T)$ is computably enumerable, but $T$ itself need not be.
Let $\sigma$ be the valid sentence $\forall x \, x = x$, and write $\sigma^{(n)}$ for the conjunction of $n + 1$ copies of $\sigma$, as in the proof.
For a set $B \subseteq \N$ that is not computably enumerable, let $T_B = \set{\sigma^{(n)} : n \in B}$.
Each sentence of $T_B$ is derivable from the empty set, so $\operatorname{Thm}(T_B) = \operatorname{Thm}(\emptyset)$, and $A = \emptyset$ is a decidable axiomatization.
But $n \in B$ if and only if $\sigma^{(n)} \in T_B$, and $n \mapsto \sigma^{(n)}$ is computable, so $T_B$ is not computably enumerable.
The correct converse is property 3 of [[recursively axiomatizable theory|3ANXZC3BEG]]: a theory with a decidable axiomatization has computably enumerable theorems.

### Generalizations

The number of copies of each axiom can be chosen as the number of steps that the enumeration needs to produce it.
Then the set $A$ is even primitive recursive.
The same proof works for every logic with a computable syntax and a conjunction, for example for propositional logic.

## History

William Craig published the theorem in 1953, in the paper "On axiomatizability within a system" in the Journal of Symbolic Logic.
The theorem is different from the [[Craig interpolation theorem|E2CBFNAVZY]], which has the same author.
Hempel discussed the use of the theorem against theoretical terms in an essay on the work of Carnap, and Putnam criticized this use in a 1965 paper with the title "Craig's theorem".

## Explanations

### L1 human

Suppose a computer prints, one by one, the axioms of a theory, but there is no way to tell in advance whether a given sentence will ever be printed.
Craig's theorem says that we can replace these axioms by others that a computer can recognize, without changing what can be proved.
The trick is to repeat each axiom: the first axiom printed stays as it is, a second axiom $\sigma$ becomes "$\sigma$ and $\sigma$", a third becomes three copies, and so on.
The repeated sentence says the same thing as $\sigma$.
To check whether a sentence of length 40 is a new axiom, the computer only needs to look at the first 40 axioms printed, because later ones are longer.

### L2 human

We run the decision procedure of the proof on a small case.

1. Let the enumeration of $T$ begin with $\sigma_0 = \forall x \, x = x$, $\sigma_1 = \forall x \forall y \, x = y$ and $\sigma_2 = \forall x \, x = x$.
2. The new axioms are $\sigma_0^{(0)} = \sigma_0$, then $\sigma_1^{(1)} = (\sigma_1 \land \sigma_1)$, then $\sigma_2^{(2)} = ((\sigma_2 \land \sigma_2) \land \sigma_2)$.
3. Take the string $\tau = (\sigma_1 \land \sigma_1)$. Its length $|\tau|$ is a fixed number $\ell$, larger than $2$.
4. The procedure computes $\sigma_k^{(k)}$ for $k < \ell$ and compares each with $\tau$. It finds $\tau = \sigma_1^{(1)}$, so $\tau \in A$.
5. The string $\sigma_1$ is in $T$, but it is not in $A$. In $H$ the conjunction $\alpha \land \beta$ is spelled $\neg (\alpha \to \neg \beta)$, so $\sigma_k^{(k)}$ with $k \ge 1$ begins with $\neg$, while $\sigma_1$ begins with $\forall$. Also $\sigma_0^{(0)} = \sigma_0 \ne \sigma_1$.

The typical use is to pass between "computably enumerable axioms" and "decidable axioms" in statements about incompleteness and undecidability.
The trap is to think that the new axioms are simpler or more useful than the old ones: they are the same sentences in a disguise that a computer can recognize.

### L3 human

Craig's theorem says that a first-order theory has a decidable axiomatization exactly when its set of theorems is $\Sigma^0_1$.
The proof is an instance of padding, a method also used in complexity theory, where a problem is made easier to decide by making its instances longer.
The refinement with step counts shows that primitive recursive axiom sets give all computably enumerable theories.
So a result first proved for primitive recursive axiom sets extends to all computably enumerable ones.
In the philosophy of science, the theorem gives a precise form to the question whether theoretical terms can be eliminated.
Another method for this question is the Ramsey sentence of a theory, which replaces the theoretical terms by existentially quantified variables.
