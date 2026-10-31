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
        by: m2 v0.6.7 scope/1
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
      expressions:
        - key: e1
          kind: edition
          date: "1976"
          ids:
            doi: 10.1007/bfb0079990
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1976"
              ids:
                isbn:
                    - "9783540079965"
                    - "9783540379645"
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0079990
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
