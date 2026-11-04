---
tag: HRTKMX90SJ
kind: proof
name: Proof of the triangle inequality for real numbers
msc: [26A03]
proves: 03HF5PMY5T
uses: [00S7C68D51, 0QSPNASE50]
sources:
  - url: https://proofwiki.org/wiki/Triangle_Inequality/Real_Numbers
---

## Proof

1. Let $t$ be real. We show $-\abs{t} \le t \le \abs{t}$, with the [[absolute value|00S7C68D51]].
2. If $t \ge 0$, then $\abs{t} = t$ and $-\abs{t} = -t \le 0 \le t$. If $t < 0$, then $\abs{t} = -t > 0 > t$ and $-\abs{t} = t$.
3. Let $r \ge 0$ and let $s$ be real with $-r \le s \le r$. Then $\abs{s} \le r$. If $s \ge 0$, then $\abs{s} = s \le r$. If $s < 0$, then $\abs{s} = -s \le r$.
4. In the [[ordered field|0QSPNASE50]] $\R$, if $u \le v$ and $u' \le v'$, then $u + u' \le v + u' \le v + v'$, by adding $u'$ and then $v$.
5. Let $a$ and $b$ be real. By step 2, $-\abs{a} \le a \le \abs{a}$ and $-\abs{b} \le b \le \abs{b}$.
6. By step 4, $-(\abs{a} + \abs{b}) \le a + b \le \abs{a} + \abs{b}$.
7. Here $r = \abs{a} + \abs{b} \ge 0$. By step 3 with $s = a + b$, $\abs{a + b} \le \abs{a} + \abs{b}$.

## Idea

Each number lies between minus its absolute value and its absolute value. Adding two such bounds traps $a + b$ between $-(\abs{a} + \abs{b})$ and $\abs{a} + \abs{b}$.
