---
tag: 96BRMR4P3N
kind: statement
role: theorem
name: Myhill–Nerode theorem
msc: [68Q45, 68Q70]
uses: [18WVBDCS38, 0G8VEZ3WTK, 0W95W33CMP, W65B6BKZRY]
about: [18WVBDCS38]
sources:
  - url: https://en.wikipedia.org/wiki/Myhill%E2%80%93Nerode_theorem
same_as:
  wikidata: Q422187
  wikipedia: Myhill–Nerode theorem
---

## Statement

Let $\Sigma$ be an alphabet and let $L \subseteq \Sigma^*$.
For $x, y \in \Sigma^*$, write $x \sim_L y$ when, for every $z \in \Sigma^*$, $xz \in L$ if and only if $yz \in L$.
Then $\sim_L$ is an [[equivalence relation|0G8VEZ3WTK]] on $\Sigma^*$, and:

1. $L$ is a [[regular language|18WVBDCS38]] if and only if $\sim_L$ has finitely many [[equivalence classes|0W95W33CMP]];
2. if $L$ is regular, the number of classes of $\sim_L$ is the least number of states of a [[DFA|W65B6BKZRY]] that accepts $L$;
3. a DFA that accepts $L$ with this least number of states is unique up to renaming of the states.

## Remarks

If a DFA $A$ accepts $L$, then two words that lead $A$ to the same state are equivalent, so $\sim_L$ has at most as many classes as $A$ has states.
Conversely, if there are finitely many classes, the classes themselves are the states of a DFA.
On the letter $a$, the class of $x$ goes to the class of $xa$.
The class of $\varepsilon$ is initial, and the classes inside $L$ are accepting.
This DFA is well defined because $x \sim_L y$ implies $xa \sim_L ya$.
Example: for $L = \set{a^n b^n : n \ge 0}$, the words $a^i$ for $i \ge 0$ lie in pairwise different classes, since $a^i b^i \in L$ but $a^j b^i \notin L$ for $j \ne i$; so $L$ is not regular.
The class of $x$ corresponds to the Brzozowski derivative $x^{-1} L = \set{z : xz \in L}$, since $x \sim_L y$ means $x^{-1} L = y^{-1} L$.

## Explanations

### L1 human

Two words are equivalent for a language when no continuation can tell them apart.
Adding the same ending to both gives two words that are both in the language or both outside it.
A finite machine reading a word has to remember at least which class the word is in.
The theorem says that this is also enough: a language is regular exactly when there are finitely many classes, and then the classes are the states of the smallest machine.

### L2 human

Unlike the [[pumping lemma|CBR9WAGZGZ]], this theorem characterizes regular languages, so it can prove both regularity and non-regularity.
It also gives the theoretical basis of [[DFA minimization|1WPX24AEAT]]: minimizing a DFA means merging states that lead to equivalent words.
The two-sided version of the same idea, the syntactic congruence, leads to the [[syntactic monoid|D47RMDH8MJ]] of a language.
