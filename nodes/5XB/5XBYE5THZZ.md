---
tag: 5XBYE5THZZ
kind: proof
name: Proof that g to the n equals 1 iff the order divides n
msc: [20A05]
proves: 0F5QC101Q7
uses: [G5S1M9, 0JPYSD5E0B, 00DRK90Z6K, 0CHQKZFK5S, 096PW7Q014]
sources:
  - url: https://proofwiki.org/wiki/Element_to_Power_of_Multiple_of_Order_is_Identity
---

## Proof

1. Let $G$ be a [[group|G5S1M9]] with identity $e$. Let $g \in G$ have finite [[order|0JPYSD5E0B]] $m$, so $m$ is the least positive integer with $g^m = e$.
2. For each integer $q$, the [[laws of exponents|00DRK90Z6K]] give $e^q = (g^0)^q = g^{0} = e$.
3. Let $n$ be an integer. Suppose first that $m$ [[divides|096PW7Q014]] $n$, and write $n = sm$ with $s \in \Z$.
4. Then $g^n = (g^m)^s = e^s = e$, by the laws of exponents and step 2.
5. Conversely, suppose that $g^n = e$. By the [[division algorithm|0CHQKZFK5S]], $n = qm + r$ with integers $q, r$ and $0 \leq r < m$.
6. By the laws of exponents, $g^n = g^{qm}g^r = (g^m)^q g^r = e^q g^r = g^r$.
7. So $g^r = e$. If $r > 0$, then $r$ is a positive integer smaller than $m$ with $g^r = e$. This contradicts the minimality of $m$.
8. Hence $r = 0$ and $n = qm$, so $m$ divides $n$.
9. So $g^n = e$ if and only if $m$ divides $n$.

## Idea

Dividing $n$ by $m$ splits $g^n$ into full cycles $g^m = e$ and a remainder $g^r$. The full cycles contribute nothing, so $g^n = g^r$. Since $m$ is the least positive exponent giving $e$, the remainder gives $e$ only when it is $0$.
