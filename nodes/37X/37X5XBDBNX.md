---
tag: 37X5XBDBNX
kind: statement
role: theorem
name: Gödel's speed-up theorem
msc: ["03F20", "03F40"]
topics: [HXHHWY3328]
audience: research
about: [92SWXST1ZM, 4NBAX3VRQ7]
uses: [4NBAX3VRQ7, 4PZM5GJTR5, NB2BCZR40F, 3PRW76471J, KZSB5E471K, MPSCREYC3M, MFJXPAF0R0]
sources:
  - url: https://en.wikipedia.org/wiki/G%C3%B6del%27s_speed-up_theorem
    locator: lead section
history:
  first_stated: "1936"
  notes: "Gödel stated the speed-up for passing from arithmetic of order i to order i + 1, with proof length counted in steps, in the short note 'Über die Länge von Beweisen' (1936), without proof. Parikh (1973) proved a form for second-order over first-order arithmetic with addition and multiplication as relations and length counted in lines; Buss (1994) proved Gödel's claim for all orders with addition and multiplication as function symbols."
---

## Statement

Fix a Hilbert-style proof calculus for first-order logic whose formulas and proofs are strings over a finite alphabet.
For a theory $S$ and a sentence $\varphi$, let $\ell_{S}(\varphi)$ be the least number of symbols of an $S$-proof of $\varphi$, and $\ell_{S}(\varphi) = \infty$ if $S \nvdash \varphi$.

Let $T$ be a theory in the language $\set{0, S, +, \cdot}$ with these properties.

1. $T$ is [[consistent|VM8TQ70CVJ]].
2. The set of axioms of $T$ is decidable.
3. $T$ contains $\mathsf{PA}$.

Let $T' = T + \mathrm{Con}(T)$, where $\mathrm{Con}(T)$ is the [[consistency statement|4NBAX3VRQ7]] of $T$.
Then for every [[computable function|KZSB5E471K]] $f \colon \N \to \N$ there are infinitely many sentences $\psi$ such that $T \vdash \psi$ and
$$\ell_{T}(\psi) > f\bigl(\ell_{T'}(\psi)\bigr).$$
In words: some theorems of $T$ have proofs in $T + \mathrm{Con}(T)$ that are shorter than all their proofs in $T$ by more than any computable amount.
A proof is in [[proof of Gödel's speed-up theorem|GRBXQXWXEP]].

## Remarks

### Why each hypothesis is needed

1. Consistency. If $T$ is inconsistent, fix a $T$-proof of $0 = S0$. Then each sentence $\varphi$ has a $T$-proof of at most $C + c \abs{\varphi}$ symbols, for constants $C$, $c$ that depend only on the calculus and on $T$. Every proof of $\varphi$ contains $\varphi$, so $\abs{\varphi} \le \ell_{T'}(\varphi)$, and the conclusion fails for $f(k) = C + ck$.
2. Decidable axioms. Let $T = \mathrm{Th}(\N)$, the set of all sentences true in $\N$; it is consistent and contains $\mathsf{PA}$. Every theorem $\varphi$ is an axiom, so $\ell_{T}(\varphi)$ is at most a constant plus $\abs{\varphi}$, and no extension can speed it up by more than that. (For such $T$ there is also no $\Sigma_1$ provability predicate, so $\mathrm{Con}(T)$ is not defined in the usual way.)
3. $T \supseteq \mathsf{PA}$. The proof uses it only for formalized $\Sigma_1$-completeness and the [[derivability conditions|F6H4STF9RG]], which already hold for $T \supseteq \mathsf{I\Sigma}_1$. We do not discuss weaker base theories here.
4. Computability of $f$. For each $k$, only finitely many sentences have a $T'$-proof of at most $k$ symbols, so $g(k) = \max\set{\ell_{T}(\varphi) : T \vdash \varphi, \ \ell_{T'}(\varphi) \le k}$ is a finite number. Then $\ell_{T}(\psi) \le g(\ell_{T'}(\psi))$ for every theorem $\psi$ of $T$, so the conclusion fails for $f = g$. By the theorem, $g$ is not computable.

### Consequences

1. No computable function bounds the length of the shortest $T$-proof of a theorem of $T$ in terms of the length of its shortest $T'$-proof.
2. Some theorems of $T$ are short sentences with only very long proofs. In the proof, $\abs{\psi_n}$ grows linearly in $n$ while $\ell_{T}(\psi_n)$ grows faster than the given computable function $f$. The example on Wikipedia is a sentence that says "this sentence has no proof in $\mathsf{PA}$ of fewer than a googolplex symbols".
3. The extension $T'$ is not only stronger in its theorems, as the [[second incompleteness theorem|4PZM5GJTR5]] says; it is also stronger in the lengths of proofs of the old theorems.

### Converse

The converse "an unbounded speed-up needs new theorems" is false.
With the sentences $\psi_n$ of the proof, let $T'' = T \cup \set{\psi_n : n \in \N}$.
The set of axioms of $T''$ is decidable, and $T''$ has exactly the same theorems as $T$, because $T \vdash \psi_n$ for every $n$.
But $\ell_{T''}(\psi_n)$ is at most a constant plus $\abs{\psi_n}$, which grows linearly in $n$, while $\ell_{T}(\psi_n)$ grows faster than the given computable function.
So speed-up and strength are different measures of a theory.

### Generalizations

1. Higher order. Gödel's own claim was about passing from arithmetic of order $i$ to order $i + 1$, with the length of a proof counted as its number of steps (lines). Parikh (1973) proved such a speed-up of second-order over first-order arithmetic, for a version of $\mathsf{PA}$ in which addition and multiplication are ternary relations. Buss (1994) proved Gödel's claim for every order $i$, with addition and multiplication as function symbols.
2. Lines and symbols differ. A proof with few lines can contain very long formulas, so a lower bound on the number of lines is harder to get than a lower bound on the number of symbols. The argument of the proof here gives only the symbol version.
3. Natural statements. Harvey Friedman found explicit combinatorial statements, related to [[Kruskal's tree theorem|XVHKCX4F5Y]], that are provable in $\mathsf{PA}$ but whose shortest $\mathsf{PA}$-proofs are extremely long, while stronger systems give short proofs.
4. In complexity theory, [[Blum's speedup theorem|F53XQ3F2SN]] is the analogous result for programs: some computable functions have no fastest program.

## History

Gödel stated the speed-up for higher-order arithmetic in a short note of 1936, "Über die Länge von Beweisen", without a proof.
Parikh gave a proof for a relational version of arithmetic in 1973, and Buss proved Gödel's claim for the usual language in 1994.
The version for $T + \mathrm{Con}(T)$ with lengths counted in symbols, proved here, follows from the same self-referential idea as the incompleteness theorems.

## Explanations

### L1 human

A proof is a finite text, and we can measure its length by counting its symbols.
Gödel noticed that adding a true axiom can make some proofs enormously shorter.
He wrote a sentence that says "I have no proof shorter than a googolplex symbols".
In ordinary arithmetic, the sentence is provable, but only by a proof that is longer than a googolplex symbols.
If we add the axiom "arithmetic is consistent", then a proof of one page is enough.
So the extra axiom saves an amount of work that no computer program can bound in advance.

### L2 human

We follow the pattern of the proof for one value $n$, with $h(n)$ a large number.

1. The sentence $\psi_n$ says "no $T$-proof with code at most $h(n)$ proves $\psi_n$".
2. If such a short proof $p$ existed, then $T$ could check $p$ and prove $\neg \psi_n$, and $T$ would prove both $\psi_n$ and $\neg \psi_n$. So $\psi_n$ has no short $T$-proof.
3. So $\psi_n$ is true, and $T$ proves it by checking all codes up to $h(n)$, one by one. This proof is long.
4. In $T + \mathrm{Con}(T)$ the argument of step 2 is done once for all $n$, with "T is consistent" as an axiom. Then $\psi_n$ follows by putting $n$ into $\forall x \, \psi(x)$, and the proof has length about a constant times $n$.

The typical use of the theorem is to separate theories by the length of proofs, as in proof complexity.
A trap is to think that $T + \mathrm{Con}(T)$ proves new things only; it also proves old theorems much faster.

### L3 human

The theorem is the first result of the theory of the lengths of proofs, today a part of proof complexity and [[bounded arithmetic|RA380RWEC0]].
Its mechanism is the same as in the [[diagonal lemma|3PRW76471J]]: a sentence speaks about its own proofs, here with a bound on their size.
The bound turns an undecidable question into a decidable one, so $T$ can prove the sentence by exhaustive search, but only slowly.
Measuring length by lines instead of symbols changes the questions, and this is the setting of the results of Parikh and Buss.
The analogy with [[Blum's speedup theorem|F53XQ3F2SN]] is an instance of the general link between computability and provability: proofs are computations that certify a result.
