---
records:
    - id: 6EVJGABVY4
      kind: monograph
      title: 'Complex Analysis: Proceedings of the Conference held at the University of Kentucky, May 18–22, 1976'
      creators:
        - name: James D. Buckholtz
          role: editor
        - name: Teddy J. Suffridge
          role: editor
      date: "1977"
      expressions:
        - key: e1
          kind: edition
          date: "1977"
          ids:
            doi: 10.1007/bfb0096815
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1977"
              ids:
                isbn:
                    - "9783540083436"
                    - "9783540373032"
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0096815
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: 6EVNCRZ118
      kind: preprint
      title: Quasi-copulas with a prescribed sub-track section
      creators:
        - name: Jiehua Xie
          role: author
        - name: Wei Zou
          role: author
      date: "2026-10-01"
      subjects:
        - system: arxiv
          code: math.PR
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-01"
          ids:
            arxiv: "2610.01247"
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.01247"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
---
