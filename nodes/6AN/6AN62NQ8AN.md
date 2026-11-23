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

If a machine can list the axioms of a theory, then the theory also has a set of axioms that a machine can recognize, with exactly the same theorems.

Let $L$ be a countable signature whose symbols, logical symbols and variables are coded by natural numbers, so that each string has a [[Gödel number|MFJXPAF0R0]].
A set of strings is decidable when the set of their Gödel numbers is a [[computable set|PPGD5KW8JC]], and computably enumerable when that set is [[computably enumerable|TN9G24VABN]].
Let $T$ be a computably enumerable set of $L$-[[sentences|DKFGQTRYZE]].
Then there is a decidable set $A$ of $L$-sentences with the same theorems as $T$:
$$A \vdash \varphi \iff T \vdash \varphi \quad \text{for every } L\text{-formula } \varphi.$$
In addition, each sentence of $A$ is logically equivalent to a sentence of $T$, and each sentence of $T$ is logically equivalent to a sentence of $A$.

Equivalently, a [[theory|92SWXST1ZM]] $T$ is a [[recursively axiomatizable theory|3ANXZC3BEG]] if and only if its set of theorems $\operatorname{Thm}(T)$ is computably enumerable.
The [[proof by padding conjunctions|9NTNKT9W00]] gives the theorem.

## Remarks

### A small run of the idea

Suppose a machine prints the axioms of $T$ in the order $\sigma_0, \sigma_1, \sigma_2, \dots$, and short sentences may come out very late.
Then we cannot decide whether a given sentence will ever be printed.
Craig's trick replaces $\sigma_k$ by a conjunction of $k + 1$ copies of itself.
$$\sigma_0, \quad \sigma_1 \land \sigma_1, \quad \sigma_2 \land \sigma_2 \land \sigma_2, \quad \dots$$
Each new axiom says the same as the old one, and the $k$-th new axiom has more than $k$ symbols.
So a string with $\ell$ symbols can only be one of the first $\ell$ new axioms, and we decide membership by printing those $\ell$ and comparing.

### Why each hypothesis is needed

The hypothesis that $T$ is computably enumerable cannot be dropped.
True arithmetic $\mathrm{TA} = \operatorname{Th}(\mathbb{N}, 0, S, +, \cdot)$ has [[no decidable axiomatization|YSC90EM2M7]], so the conclusion fails for $T = \mathrm{TA}$, and $\mathrm{TA}$ is not computably enumerable.

The coding of $L$ by natural numbers gives a meaning to "decidable" and "computably enumerable".
For an uncountable signature there is no such coding.

The proof uses one property of the logic: from a sentence $\sigma$ we can compute longer and longer sentences that are equivalent to $\sigma$.
In first-order logic the conjunctions $\sigma \land \sigma \land \cdots \land \sigma$ do this.

### What it gives you

For a theory, three conditions are equivalent: it has a decidable set of axioms, it has a computably enumerable set of axioms, and its set of theorems is computably enumerable.
To get the third from the first, list all derivations.
To get the first from the third, apply the theorem to the set $\operatorname{Thm}(T)$ itself, which gives a decidable $A$ with $\operatorname{Thm}(A) = \operatorname{Thm}(T)$.

So the hypothesis "the axioms are computably enumerable" in [[Gödel's incompleteness theorems|X9WYNYE29C]] can be replaced by "the axioms form a decidable set", and conversely.
A theory whose theorems are not computably enumerable, such as $\mathrm{TA}$, has no decidable axiomatization.

### The use in philosophy of science

Split the vocabulary of a theory $T$ into an observational part $L_O$ and a theoretical part.
If $T$ is computably enumerable, so is the set of theorems of $T$ that use only $L_O$: list the theorems of $T$ and keep those in $L_O$.
Craig's theorem gives a decidable set $A_O$ of $L_O$-sentences with exactly these theorems.
So the observational consequences of $T$ can be axiomatized without theoretical terms.
Carl Hempel discussed this argument and raised objections to it: $A_O$ is an infinite list of axioms that is useless in practice, and dropping the theoretical terms can change how observations support each other.
Hilary Putnam argued that the argument assumes that prediction is the only aim of science.

### The converse

The direct converse is false: $T$ can have a decidable axiomatization without being computably enumerable itself.
Let $\sigma$ be the valid sentence $\forall x \, x = x$, and let $\sigma^{(n)}$ be the conjunction of $n + 1$ copies of $\sigma$.
For a set $B \subseteq \mathbb{N}$ that is not computably enumerable, let $T_B = \{ \sigma^{(n)} : n \in B \}$.
Every sentence of $T_B$ is valid, so $\operatorname{Thm}(T_B)$ is the set of valid sentences, and $A = \emptyset$ is a decidable axiomatization.
But $n \in B$ if and only if $\sigma^{(n)} \in T_B$, and $n \mapsto \sigma^{(n)}$ is computable, so $T_B$ is not computably enumerable.

### Generalizations

The number of copies of each axiom can be chosen as the number of steps that the enumeration needs to print it.
Then the set $A$ is even primitive recursive.
The same proof works for every logic with a computable syntax and a conjunction, for example propositional logic.

### Watch out

The new axioms are not simpler or more useful than the old ones.
They are the same sentences in a disguise that a machine can recognize, and the theorem gives no new information about which sentences $T$ proves.
In particular, a decidable set of axioms does not make the set of theorems decidable.

### Try it

First, the axioms of $T$ are printed as $\sigma_0 = \sigma_2 = \forall x \, x = x$ and $\sigma_1 = \forall x \forall y \, x = y$.
Is $\sigma_1$ itself in Craig's set $A$?
No: the first element of $A$ is $\sigma_0 \ne \sigma_1$, and every later element is a conjunction, while $\sigma_1$ begins with a quantifier.
Still $A \vdash \sigma_1$, since $\sigma_1 \land \sigma_1$ is in $A$.

Second, is the set of valid sentences of a countable signature recursively axiomatizable?
Yes, with the empty set of axioms, even though for some signatures the set is not decidable.

## History

William Craig published the theorem in 1953, in the paper "On axiomatizability within a system" in the Journal of Symbolic Logic.
It is a different result from the [[Craig interpolation theorem|E2CBFNAVZY]], which has the same author.
Hempel discussed the use of the theorem against theoretical terms, and Putnam criticized this use in a 1965 paper with the title "Craig's theorem".

## Explanations

### L1 human

Suppose a printer prints, one by one, the axioms of a theory, and there is no way to tell in advance whether a given sentence will ever be printed.
Craig's theorem says that we can swap these axioms for others that a computer can recognize, without changing what can be proved.
The trick is to repeat each axiom: the first printed axiom stays as it is, the second becomes "$\sigma$ and $\sigma$", the third becomes three copies, and so on.
A repeated sentence says the same thing as the original.
To check whether a sentence with 40 symbols is a new axiom, the computer only looks at the first 40 printed axioms, because later ones are longer.

### L2 human

We decide one string with the procedure of the proof.
Let the enumeration of $T$ begin with $\sigma_0 = \forall x \, x = x$, $\sigma_1 = \forall x \forall y \, x = y$ and $\sigma_2 = \forall x \, x = x$.
The new axioms are $\sigma_0$, then $(\sigma_1 \land \sigma_1)$, then $((\sigma_2 \land \sigma_2) \land \sigma_2)$, and so on.
Take $\tau = (\sigma_1 \land \sigma_1)$, and let $\ell$ be its number of symbols, which is larger than $2$.
The procedure computes the first $\ell$ new axioms and compares each with $\tau$.
It finds $\tau$ in position $1$, so $\tau \in A$.

The typical use is to pass between "computably enumerable axioms" and "decidable axioms" in theorems about incompleteness and undecidability.

### L3 human

The theorem says that a first-order theory has a decidable axiomatization exactly when its set of theorems is $\Sigma^0_1$.
The proof is an instance of padding, a method that complexity theory also uses: a problem becomes easier to decide when its instances are made longer.
The refinement with step counts shows that primitive recursive axiom sets already give all computably enumerable theories.
In the philosophy of science, the theorem gives a precise form to the question whether theoretical terms can be eliminated.
Another approach to that question is the Ramsey sentence of a theory, which replaces the theoretical terms by existentially quantified variables.
