---
tag: 46AN6CZMRD
kind: definition
name: Lambek calculus
msc: ["03B47", "03B65", "68Q42"]
topics: [98QF5J4W16]
audience: research
defines: 5FAC9KX4H0
uses: [W72CA3R9MP, DAMGTSY6VV, 8R5ZPQ7893, BE9JQRJCTB, REKDJ8V504]
sources:
  - url: https://en.wikipedia.org/wiki/Categorial_grammar
    locator: Lambek calculus
  - url: https://en.wikipedia.org/wiki/Categorial_grammar
    locator: Relation to context-free grammars
  - url: https://plato.stanford.edu/entries/logic-substructural/
    locator: 2.3 The Lambek Calculus
    note: Restall, Substructural Logics, Stanford Encyclopedia of Philosophy, revision of 2024-08-15
  - doi: 10.1080/00029890.1958.11989160
    locator: pages 154-170
    note: Lambek, The Mathematics of Sentence Structure, American Mathematical Monthly 65 (1958)
  - doi: 10.1109/LICS.1993.287565
    locator: pages 429-433
    note: Pentus, Lambek grammars are context free, Proceedings of the Eighth Annual IEEE Symposium on Logic in Computer Science (1993)
  - doi: 10.1016/j.tcs.2006.03.018
    locator: pages 186-201
    note: Pentus, Lambek calculus is NP-complete, Theoretical Computer Science 357 (2006)
---

## Definition

Fix a set of atoms, called primitive types, for example $s$ (sentence), $n$ (noun) and $np$ (noun phrase).
The *types* are built from the atoms with the binary connectives $\cdot$, $\backslash$ and $/$.
A sequent of the *Lambek calculus* $\mathsf{L}$ is $\Gamma \Rightarrow A$, where $\Gamma$ is a nonempty finite list of types and $A$ is a type.
Below, $\Gamma$ is a nonempty list, $\Delta$ and $\Sigma$ are lists that may be empty, and $A$, $B$, $C$ are types.

1. Axiom: $A \Rightarrow A$.
2. Cut: from $\Gamma \Rightarrow A$ and $\Delta, A, \Sigma \Rightarrow C$ infer $\Delta, \Gamma, \Sigma \Rightarrow C$.
3. ${\cdot}\mathrm{L}$: from $\Delta, A, B, \Sigma \Rightarrow C$ infer $\Delta, A \cdot B, \Sigma \Rightarrow C$.
   ${\cdot}\mathrm{R}$: from $\Gamma \Rightarrow A$ and $\Gamma' \Rightarrow B$ infer $\Gamma, \Gamma' \Rightarrow A \cdot B$.
4. ${\backslash}\mathrm{L}$: from $\Gamma \Rightarrow A$ and $\Delta, B, \Sigma \Rightarrow C$ infer $\Delta, \Gamma, A \backslash B, \Sigma \Rightarrow C$.
   ${\backslash}\mathrm{R}$: from $A, \Gamma \Rightarrow B$ infer $\Gamma \Rightarrow A \backslash B$.
5. ${/}\mathrm{L}$: from $\Gamma \Rightarrow A$ and $\Delta, B, \Sigma \Rightarrow C$ infer $\Delta, B / A, \Gamma, \Sigma \Rightarrow C$.
   ${/}\mathrm{R}$: from $\Gamma, A \Rightarrow B$ infer $\Gamma \Rightarrow B / A$.

In ${\backslash}\mathrm{R}$ and ${/}\mathrm{R}$ the list $\Gamma$ must be nonempty; this is the only difference from the rules of the full Lambek calculus for these connectives.
A *Lambek grammar* over a finite alphabet $\Sigma_0$ is a finite set of pairs $(a, T)$ of a letter $a$ and a type $T$, the *lexicon*, together with a distinguished atom $s$.
It *accepts* a nonempty word $a_1 \dots a_n$ if there are types $T_1, \dots, T_n$ with $(a_i, T_i)$ in the lexicon and $T_1, \dots, T_n \Rightarrow s$ derivable in $\mathsf{L}$.

## Notation

Lambek's $A \backslash B$ takes its argument $A$ on the left, and $B / A$ takes its argument $A$ on the right.
In the notation of Steedman and others, the result is written first on both sides, so Lambek's $np \backslash s$ is written $s \backslash np$ there.

## Remarks

### Decidability and the count check

Every rule of $\mathsf{L}$ other than cut has premises of smaller size than its conclusion, and $\mathsf{L}$ has cut elimination by the method of the [[cut elimination for the full Lambek calculus|JSAH84Y9G2]].
So a cut-free search terminates, and derivability is decidable.
For an atom $p$, let $\#_p(p) = 1$, $\#_p(q) = 0$ for other atoms $q$, $\#_p(A \cdot B) = \#_p(A) + \#_p(B)$ and $\#_p(A \backslash B) = \#_p(B / A) = \#_p(B) - \#_p(A)$.
Claim: if $A_1, \dots, A_n \Rightarrow B$ is derivable, then $\#_p(A_1) + \dots + \#_p(A_n) = \#_p(B)$ for each atom $p$.

1. The axiom $A \Rightarrow A$ satisfies the equation.
2. For ${\backslash}\mathrm{L}$, the premises give $\#_p(\Gamma) = \#_p(A)$ and $\#_p(\Delta) + \#_p(B) + \#_p(\Sigma) = \#_p(C)$, where $\#_p$ of a list is the sum.
3. The conclusion has the sum $\#_p(\Delta) + \#_p(\Gamma) + \#_p(B) - \#_p(A) + \#_p(\Sigma) = \#_p(C)$, by step 2.
4. For ${\backslash}\mathrm{R}$, the premise gives $\#_p(A) + \#_p(\Gamma) = \#_p(B)$, so $\#_p(\Gamma) = \#_p(A \backslash B)$.
   The other rules are checked in the same way.

The count check proves non-derivability quickly: $np \Rightarrow s$ fails it.
It is only a necessary condition; see [[the non-example|GYJQE97XNA]].

### Pentus's theorems

1. The languages accepted by Lambek grammars are exactly the [[context-free languages|BE9JQRJCTB]] that do not contain the empty word.
   One direction builds a Lambek grammar from a [[context-free grammar|8R5ZPQ7893]] in Greibach normal form.
   Pentus proved the other direction in 1993.
2. The derivability problem of $\mathsf{L}$ is [[NP-complete|REKDJ8V504]].
   Pentus proved this in a paper of 2006.

This node states these results and cites them; it does not prove them.
Membership in NP has a short reason.
In a cut-free derivation each rule introduces one connective of the end sequent, and no rule copies a formula.
So a derivation of a sequent with $m$ connectives has $m$ rule applications and at most $m + 1$ axioms, and it is a certificate of polynomial size.

## Explanations

### L1 human

The Lambek calculus is a short list of rules for fitting types together.
A type such as $np / n$ means "give me a noun on the right, and I give a noun phrase".
The list of types must stay in order, like the words of a sentence.

### L2 human

We parse "the dog sleeps" with the lexicon: "the" has type $np / n$, "dog" has type $n$, "sleeps" has type $np \backslash s$.

1. $np \Rightarrow np$ and $s \Rightarrow s$ are axioms, and ${\backslash}\mathrm{L}$ with $\Gamma = np$ gives $np, np \backslash s \Rightarrow s$.
2. $n \Rightarrow n$ is an axiom.
3. ${/}\mathrm{L}$ with $\Gamma = n$ and the premise of step 1 gives $np / n, n, np \backslash s \Rightarrow s$.
4. So the grammar accepts "the dog sleeps".
5. The count check agrees: for $n$ the sum is $-1 + 1 + 0 = 0$, for $np$ it is $1 + 0 - 1 = 0$, and for $s$ it is $1$.

The typical use is to decide whether a string is a sentence of a Lambek grammar.
A trap: a word can have several types in the lexicon, and the grammar accepts the string if one choice of types works.
