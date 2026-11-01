---
records:
    - id: 1ADMH800X0
      kind: preprint
      title: Strict-Saddle Landscapes and Multi-Rank Geometry in Low-Tubal-Rank Tensor Sensing
      creators:
        - name: Eugene Agyei-Kodie
          role: author
        - name: Longxiu Huang
          role: author
        - name: Shuang Li
          role: author
        - name: Xiao Liang
          role: author
      date: "2026-09-29"
      subjects:
        - system: arxiv
          code: cs.LG
        - system: arxiv
          code: math.OC
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-09-29"
          ids:
            arxiv: "2609.37865"
      scope:
        value: border
        rule: border-arxiv
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2609.37865"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to border
    - id: 1ADQEH35YE
      kind: monograph
      title: 'Algebraic K-Theory: Proceedings of the Conference Held at Northwestern University Evanston, January 12–16, 1976'
      creators:
        - name: Michael R. Stein
          role: editor
      date: "1976"
      msc:
        - code: 00Bxx
          from: zbmath_search
        - code: 14-06
          from: zbmath_search
        - code: 18-06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1976"
          ids:
            doi: 10.1007/bfb0079990
            zbl: "0328.00005"
            zbl_id: "3513710"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1976"
              ids:
                isbn:
                    - "9783540079965"
                    - "9783540379645"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0079990
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "3513710"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
