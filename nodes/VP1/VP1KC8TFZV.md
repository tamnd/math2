---
tag: VP1KC8TFZV
kind: definition
name: Brzozowski derivative
msc: [68Q45]
defines: 4A2BAEWRPZ
uses: [5MFZ4VNY6D, 1P6EP01HZF, 4DMYF2PR4Q]
sources:
  - url: https://en.wikipedia.org/wiki/Brzozowski_derivative
---

## Definition

Let $\Sigma$ be an alphabet, let $L \subseteq \Sigma^*$ be a [[formal language|5MFZ4VNY6D]] and let $u \in \Sigma^*$ be a [[string|1P6EP01HZF]].
The *Brzozowski derivative* of $L$ with respect to $u$ is
$$u^{-1} L = \set{v \in \Sigma^* : uv \in L}.$$

For a [[regular expression|4DMYF2PR4Q]] $r$ and a letter $a \in \Sigma$, the derivative $a^{-1} r$ is the regular expression given by recursion on $r$:

1. $a^{-1} \emptyset = \emptyset$ and $a^{-1} \varepsilon = \emptyset$;
2. $a^{-1} a = \varepsilon$, and $a^{-1} b = \emptyset$ for a letter $b \ne a$;
3. $a^{-1}(r + s) = a^{-1} r + a^{-1} s$;
4. $a^{-1}(rs) = (a^{-1} r) s + \nu(r)\, a^{-1} s$, where $\nu(r) = \varepsilon$ if $\varepsilon \in L(r)$ and $\nu(r) = \emptyset$ otherwise;
5. $a^{-1}(r^*) = (a^{-1} r)\, r^*$.

For words, $\varepsilon^{-1} r = r$ and $(ua)^{-1} r = a^{-1}(u^{-1} r)$.

## Remarks

The two definitions agree: $L(u^{-1} r) = u^{-1} L(r)$ for every regular expression $r$ and word $u$.
Hence $w \in L(r)$ if and only if $\varepsilon \in L(w^{-1} r)$, and $\nu$ is computed by a simple recursion on $r$.
Example: for $r = (ab)^*$, rule 5 gives $a^{-1} r = (a^{-1}(ab))\, r$, and rule 4 with $\nu(a) = \emptyset$ gives $a^{-1}(ab) = \varepsilon b + \emptyset \emptyset$, so $L(a^{-1} r) = b (ab)^*$, the set of $v$ with $av \in (ab)^*$.
Non-example: $\set{v : vu \in L}$, where $u$ is removed from the end, is not the Brzozowski derivative; it is the right quotient of $L$ by $u$.
The derivative $u^{-1} L$ is also called the left quotient of $L$ by $u$.
