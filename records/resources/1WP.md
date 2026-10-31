---
records:
    - id: 1WP6RR4BEQ
      kind: monograph
      title: 'Number Theory: Proceedings of the 4th Matscience Conference held at Ootacamund, India, January 5–10, 1984'
      creators:
        - name: Krishnaswami Alladi
          role: editor
      date: "1982"
      expressions:
        - key: e1
          kind: edition
          date: "1982"
          ids:
            doi:
                - 10.1007/bfb0075746
                - 10.1007/bfb0097171
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1985"
              ids:
                isbn:
                    - "9783540152224"
                    - "9783540396420"
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1982"
              ids:
                isbn:
                    - "9783540115687"
                    - "9783540392798"
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
          native_id: 10.1007/bfb0075746
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0097171
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: 1WPPDSF0EJ
      kind: preprint
      title: Higher-Order Mean-Field Control Barrier Functions
      creators:
        - name: Levon Nurbekyan
          role: author
        - name: Samy Wu Fung
          role: author
      date: "2026-09-27"
      subjects:
        - system: arxiv
          code: math.OC
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-09-27"
          ids:
            arxiv: "2609.33852"
      scope:
        value: in
        rule: S2
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2609.33852"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to in
---
