---
tag: NYPH63X6AN
kind: proof
name: Proof of unique readability by induction on length
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
proves: 3QPV4XW8MC
uses: [6D3WA7N2W4, HYJ10AF6RT, WDVVEYD6AT, 1P6EP01HZF]
methods: [0KMVFSHFGZ, 0WCP0PVET6]
sources:
  - book: isbn:9780122384523
    locator: Section 2.3
---

## Proof

We first show that no term or formula is a proper initial segment of another one, by strong induction on length, and then read off both parts of the [[statement|3QPV4XW8MC]].
A string $u$ is an *initial segment* of a string $w$ when $w = u v$ for some string $v$, and we write $|w|$ for the length of $w$.

1. Every [[term|6D3WA7N2W4]] and every [[formula|HYJ10AF6RT]] is a nonempty string.
   Each clause of the two definitions produces a nonempty string.
2. A term contains no $=$, no relation symbol, no connective and no quantifier.
   No clause for terms introduces these symbols, so this holds by induction on terms.
3. The first symbol of a term is a variable, a constant symbol or a function symbol, and it fixes the clause.
   A variable or a constant symbol alone is a term of length $1$, and the clause for $f(t_1, \dots, t_n)$ starts with $f$.
4. The first symbol of a formula is a term symbol, a relation symbol, $\neg$, a left bracket, $\forall$ or $\exists$, and these cases match the five forms of part 2 of the statement, with $\forall$ and $\exists$ together.
   Each clause for formulas starts with one of these symbols, the symbols are pairwise distinct, and by step 2 a formula $t_1 = t_2$ is the only kind that starts with a term symbol.
5. Prefix lemma for terms: if $s$ and $t$ are terms and $s$ is an initial segment of $t$, then $s = t$.
   We prove it by strong induction on $|t|$ in steps 6 to 8.
6. If $t$ is a variable or a constant symbol, then $|t| = 1$, and $s$ is nonempty by step 1, so $s = t$.
7. Let $t = f(t_1, \dots, t_n)$.
   Then $s$ also starts with $f$, so by step 3 it has the form $f(s_1, \dots, s_n)$ with the same $n = \operatorname{ar}(f)$.
   Both $t_1$ and $s_1$ start right after "$f($", so one of them is an initial segment of the other.
   The longer one is shorter than $t$, because $|t_1| < |t|$ and $|s_1| < |s| \le |t|$, so the induction hypothesis gives $s_1 = t_1$.
8. The next symbol is then a comma in both strings, or the closing bracket when $n = 1$.
   So $t_2$ and $s_2$ start at the same place, and the argument of step 7 gives $s_2 = t_2$; repeating it gives $s_i = t_i$ for every $i \le n$, and so $s = t$.
9. Part 1 of the statement follows.
   By step 3 the first symbol fixes the form, and if $f(t_1, \dots, t_n) = f(s_1, \dots, s_n)$, then steps 7 and 8 give $t_i = s_i$ for all $i$.
10. Prefix lemma for formulas: if $\psi$ and $\varphi$ are formulas and $\psi$ is an initial segment of $\varphi$, then $\psi = \varphi$.
    We prove it by strong induction on $|\varphi|$, with cases by the first symbol, which $\psi$ and $\varphi$ share, in steps 11 to 15.
11. If the first symbol is a term symbol, then by step 4 $\varphi$ is $t_1 = t_2$ and $\psi$ is $s_1 = s_2$.
    The terms $t_1$ and $s_1$ both start at the first place, so the prefix lemma for terms gives $s_1 = t_1$; then $=$ follows in both, and the same argument gives $s_2 = t_2$.
12. If the first symbol is a relation symbol $R$, then $\varphi = R(t_1, \dots, t_n)$ and $\psi = R(s_1, \dots, s_n)$ with $n = \operatorname{ar}(R)$.
    The argument of steps 7 and 8, with the prefix lemma for terms, gives $s_i = t_i$ for all $i$.
13. If the first symbol is $\neg$, then $\varphi = \neg \varphi'$ and $\psi = \neg \psi'$, and $\psi'$ is an initial segment of $\varphi'$.
    Since $|\varphi'| < |\varphi|$, the induction hypothesis gives $\psi' = \varphi'$.
14. If the first symbol is $\forall$ or $\exists$, then $\varphi = Q x \, \varphi'$ and $\psi = Q y \, \psi'$ with the same quantifier $Q$.
    The second symbol gives $x = y$, and the argument of step 13 gives $\psi' = \varphi'$.
15. If the first symbol is a left bracket, then $\varphi = (\varphi_1 \circ \varphi_2)$ and $\psi = (\psi_1 \ast \psi_2)$.
    The formulas $\varphi_1$ and $\psi_1$ start at the second place, so one is an initial segment of the other, and the longer one is shorter than $\varphi$, so the induction hypothesis gives $\psi_1 = \varphi_1$.
    The next symbol then gives $\ast = \circ$, the same argument gives $\psi_2 = \varphi_2$, and the closing bracket follows in both.
16. Part 2 of the statement follows.
    By step 4 the first symbol fixes the form, and two decompositions of one formula of the same form agree by the argument of steps 11 to 15, applied with $\psi = \varphi$.

This proves both parts of the statement.

## Idea

Read the string from left to right.
The first symbol tells which clause built it, so the only question is where the first argument ends.
The prefix lemma answers it: a term or formula can never be a proper initial segment of another one.
So two decompositions that start at the same place must end at the same place, and then the next part starts at the same place too.
For example, in $+(\cdot(x, y), S(0))$ the first argument must be $\cdot(x, y)$, since its proper initial segments $\cdot$, $\cdot($, $\cdot(x$ and so on are not terms.

## Variants

A bracket-counting proof works for the binary connectives.
Inside $(\varphi_1 \circ \varphi_2)$, every binary connective of $\varphi_1$ or $\varphi_2$ sits inside its own pair of brackets, so $\circ$ is the only binary connective at bracket depth $1$.
This finds the main connective directly, as in the worked formula on the statement.

A weight-counting proof works for prefix notation, as in Enderton.
Give each symbol of arity $n$ the weight $1 - n$, so a variable or constant weighs $1$ and a binary symbol weighs $-1$.
Then a string is a term exactly when its total weight is $1$ and each nonempty proper initial segment has weight at most $0$.
Check on $+ \, x \, y$: the initial segments $+$, $+x$ and $+xy$ weigh $-1$, $0$ and $1$.

The proof is also an algorithm: it reads a term or formula from left to right and returns its formation tree in linear time.
