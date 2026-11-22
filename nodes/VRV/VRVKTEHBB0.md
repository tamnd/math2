---
tag: VRVKTEHBB0
kind: example
name: Balanced strings of parentheses as an inductively defined set
msc: ["00A35", "68Q45"]
topics: [EEH2F76CYQ]
audience: ug1
instance_of: [AM4GQQMZ3C]
uses: [AM4GQQMZ3C, D9FCP61J44, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Dyck_language
    locator: Formal definition
  - url: https://en.wikipedia.org/wiki/Recursive_definition
    locator: Form of recursive definitions
---

## Example

Let $U$ be the set of finite [[strings|D9FCP61J44]] of the two symbols "(" and ")", and let $\varepsilon$ be the empty string.
We define the set $\mathcal{B} \subseteq U$ of balanced strings by an [[inductive definition|AM4GQQMZ3C]] with a base, two rules and an extremal clause.

- Base: $\varepsilon \in \mathcal{B}$.
- Rule 1: if $w \in \mathcal{B}$, then $(w) \in \mathcal{B}$.
- Rule 2: if $u \in \mathcal{B}$ and $v \in \mathcal{B}$, then $uv \in \mathcal{B}$.
- Extremal clause: $\mathcal{B}$ is the smallest subset of $U$ with the three properties above.

First we check that the string $(()())$ is in $\mathcal{B}$, by building it.

1. By the base, $\varepsilon \in \mathcal{B}$.
2. Rule 1 with $w = \varepsilon$ gives $() \in \mathcal{B}$.
3. Rule 2 with $u = v = ()$ gives $()() \in \mathcal{B}$.
4. Rule 1 with $w = ()()$ gives $(()()) \in \mathcal{B}$.

Next we prove a property of all members by induction on the rules.
For a string $s$, let $L(s)$ be the number of symbols "(" in $s$ and $R(s)$ the number of symbols ")".
We claim that $L(s) = R(s)$ for each $s \in \mathcal{B}$.

1. Let $C = \{s \in U : L(s) = R(s)\}$.
   We show that $C$ has the three properties of the base and the rules.
2. Base: $L(\varepsilon) = 0 = R(\varepsilon)$, so $\varepsilon \in C$.
3. Rule 1: let $w \in C$.
   Then $L((w)) = L(w) + 1$ and $R((w)) = R(w) + 1$, and these are equal because $L(w) = R(w)$.
   So $(w) \in C$.
4. Rule 2: let $u, v \in C$.
   The counts add under concatenation, so $L(uv) = L(u) + L(v) = R(u) + R(v) = R(uv)$, and $uv \in C$.
5. The set $\mathcal{B}$ is the smallest set with the three properties, so $\mathcal{B} \subseteq C$, which proves the claim.

Finally we show that the string $)($ is not in $\mathcal{B}$.
It has one symbol of each kind, so the claim above does not exclude it, and we need a second property.

1. Let $D$ be the set of strings that are empty or start with "(".
2. Base: $\varepsilon \in D$.
3. Rule 1: each string $(w)$ starts with "(", so it is in $D$.
4. Rule 2: let $u, v \in D$.
   If $u$ is not empty, then $uv$ starts with the first symbol of $u$, which is "(".
   If $u$ is empty, then $uv = v \in D$.
5. So $D$ has the three properties, and $\mathcal{B} \subseteq D$.
6. The string $)($ starts with ")", so it is not in $D$, and therefore it is not in $\mathcal{B}$.

## Remarks

The example shows the three jobs of an inductive definition.
To show that an object is in the set, build it by the rules.
To show that every member has a property, check the base and each rule.
To show that an object is not in the set, find a property that every member has and the object lacks; here "$L = R$" is not enough for $)($, and "empty or starts with (" is.

The set $\mathcal{B}$ is the set of [[Dyck words|0YTJ3RN3GE]].
A string is in $\mathcal{B}$ exactly when $L(s) = R(s)$ and every prefix of $s$ has at least as many symbols "(" as ")".
The direction from $\mathcal{B}$ to the prefix condition is one more induction on the rules, of the same form as above, and the other direction needs an induction on the length.

The rules matter one by one.
Without Rule 2, the smallest closed set is $\{\varepsilon, (), (()), ((())), \ldots\}$, and $()()$ is no longer a member.
The rules are also ambiguous: $()()()$ is $uv$ with $u = ()()$ and $v = ()$, and also with $u = ()$ and $v = ()()$.
Induction does not care, but a definition by recursion on these rules must give the same value for both ways of building.

## Explanations

### L1 human

Think of brackets in a calculation that are opened and closed correctly.
The empty string counts as correct.
If a string is correct, then putting it inside one more pair of brackets keeps it correct.
Two correct strings written one after the other are correct too.
Starting from nothing, these rules give $()$, then $()()$, then $(()())$.
Each rule adds as many opening brackets as closing ones, so every correct string has equal numbers of each.

### L2 human

Let us show by induction on the rules that each $s \in \mathcal{B}$ has even length.
Let $E$ be the set of strings of even length.
The empty string has length $0$, which is even, so $\varepsilon \in E$.
If $w$ has even length $2k$, then $(w)$ has length $2k + 2 = 2(k + 1)$, which is even.
If $u$ and $v$ have even lengths $2j$ and $2k$, then $uv$ has length $2j + 2k = 2(j + k)$, which is even.
So $E$ has the three properties, and $\mathcal{B} \subseteq E$.
Check: this also follows from $L(s) = R(s)$, because the length is $L(s) + R(s) = 2L(s)$.
The typical use of the method is a proof about all the strings, terms or trees that a grammar produces.
Watch out: a proof that only checks the two rules and forgets the base case proves nothing.
